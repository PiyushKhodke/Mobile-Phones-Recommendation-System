from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import traceback

app = Flask(__name__)
CORS(app)

# Load the dataset globally
try:
    global_df = pd.read_csv("smartphones_2026.csv")
    global_df['Prices'] = global_df['Prices'].astype(float)
    global_df['Camera'] = global_df['Camera'].astype(float)
    global_df['Battery'] = global_df['Battery'].astype(int)
    global_df['RAM'] = global_df['RAM'].astype(int)
    global_df['Ratings'] = global_df['Ratings'].astype(float)
except Exception as e:
    print("Error loading CSV:", e)
    global_df = pd.DataFrame()

def get_input_data(req_data):
    brand = req_data.get('brand', '')
    price = req_data.get('price')
    camera = req_data.get('camera')
    battery = req_data.get('battery')
    processor = req_data.get('processor', '')
    ram = req_data.get('ram')
    ratings = req_data.get('ratings')

    df = global_df.copy()

    if brand:
        df = df.loc[df['Brand'].str.contains(brand, case=False, na=False)]
    if price is not None and price != '':
        df = df.loc[df['Prices'] <= float(price)]
    if ratings is not None and ratings != '':
        df = df.loc[df['Ratings'] >= float(ratings)]
    if ram is not None and ram != '':
        df = df.loc[df['RAM'] >= int(ram)]
    if battery is not None and battery != '':
        df = df.loc[df['Battery'] >= int(battery)]
    if camera is not None and camera != '':
        df = df.loc[df['Camera'] >= float(camera)]
    if processor:
        df = df.loc[df["Processor"].str.contains(processor, case=False, na=False)]
    
    return df

def get_recommended_phones(df, input_data):
    if input_data.empty:
        return pd.DataFrame()
        
    features = ['Prices', 'RAM', 'Battery', 'Camera', 'Ratings']
    df_features = df[features].copy()
    
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df_features)
    
    brand_dummies = pd.get_dummies(df['Brand'])
    # Give brand matching a strong weight
    brand_weighted = brand_dummies.values * 2.0
    
    # Combined feature matrix for all phones
    final_matrix = np.hstack((df_scaled, brand_weighted))
    
    # We use the best match (first one in filtered list) as the reference for recommendations
    reference_phone = input_data.iloc[0:1]
    
    input_scaled = scaler.transform(reference_phone[features])
    
    input_brand = reference_phone['Brand'].iloc[0]
    input_brand_vec = np.zeros((1, brand_dummies.shape[1]))
    if input_brand in brand_dummies.columns:
        idx = brand_dummies.columns.get_loc(input_brand)
        input_brand_vec[0, idx] = 2.0
        
    final_input_matrix = np.hstack((input_scaled, input_brand_vec))
    
    # Calculate similarity score against all phones in the dataset
    sim_scores = cosine_similarity(final_input_matrix, final_matrix)[0]
    
    res_df = df.copy()
    res_df['Score'] = sim_scores
    # Sort by similarity score, and then by ratings as a tie-breaker
    res_df = res_df.sort_values(by=['Score', 'Ratings'], ascending=[False, False])
    
    return res_df[['Brand', 'Model', 'Prices', 'Score', 'Processor', 'RAM', 'Battery', 'Camera', 'Ratings']]

@app.route('/api/recommend', methods=['POST'])
def recommend():
    try:
        req_data = request.json
        if not req_data:
            return jsonify({"error": "No JSON data provided"}), 400
            
        input_data = get_input_data(req_data)

        if input_data.empty:
            return jsonify({"message": "No exact phones matched your criteria. Try loosening the constraints.", "recommendations": []}), 200

        recommended_phones = get_recommended_phones(global_df, input_data)
        
        # Take top 10 recommendations
        top_recs = recommended_phones.head(10).to_dict(orient='records')
        
        return jsonify({
            "message": "Success",
            "recommendations": top_recs
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
