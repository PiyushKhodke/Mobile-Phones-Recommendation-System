# 📱 Mobile Recommendation System (2026 Edition)

![Banner](https://images.unsplash.com/photo-1598327105666-5b89351cb31b?q=80&w=2000&auto=format&fit=crop)

A state-of-the-art mobile recommendation web application built with **React**, **Tailwind CSS**, and **Python Flask**. By leveraging an advanced machine learning algorithm based on numerical and categorical feature similarity, this system recommends the perfect 2025/2026 smartphones tailored precisely to your budget and hardware requirements.

---

## ✨ Key Features

- 🧠 **Advanced ML Recommendations:** Replaces basic text-similarity with a robust Feature Matrix utilizing `MinMaxScaler` and `cosine_similarity` to mathematically evaluate Price, RAM, Battery, Camera, and Brand.
- 📱 **Modern 2026 Dataset:** Powered by an up-to-date catalog of over 60 of the latest smartphones (e.g., iPhone 17 series, Galaxy S26 Ultra, Pixel 10).
- 🎨 **Premium UI/UX:** A stunning, dark-mode focused React frontend utilizing glassmorphism, dynamic gradients, and fluid micro-animations built with Tailwind CSS v4.
- ⚡ **Lightning Fast:** The dataset is loaded efficiently into memory at backend startup, resulting in near-instantaneous JSON REST API responses.

## 🛠️ Technology Stack

**Frontend:**
- React (via Vite)
- Tailwind CSS (v4)
- Axios

**Backend:**
- Python 3
- Flask & Flask-CORS
- Pandas
- Scikit-Learn (`MinMaxScaler`, `cosine_similarity`)
- NumPy

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed:
- [Node.js](https://nodejs.org/) (v18 or higher)
- [Python](https://www.python.org/) (v3.8 or higher)

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/Mobile-Recommendation-System.git
cd Mobile-Recommendation-System
```

### 2. Backend Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. *(Optional)* **Regenerate the 2026 Dataset:**
   If you want to modify or regenerate the latest smartphone dataset, run:
   ```bash
   python generate_2026_dataset.py
   ```
3. **Start the Flask Server:**
   ```bash
   python recommend.py
   ```
   *The backend will now be running on `http://127.0.0.1:5000`.*

### 3. Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```
2. **Install Node dependencies:**
   ```bash
   npm install
   ```
3. **Start the Vite development server:**
   ```bash
   npm run dev
   ```
   *The frontend will typically be accessible at `http://localhost:5173` or `http://localhost:5174`.*

---

## 🔌 API Documentation

### `POST /api/recommend`

Retrieves a list of up to 10 recommended smartphones based on user specifications.

**Request Body (JSON):**
```json
{
  "brand": "Samsung",
  "price": "140000",
  "ram": "12",
  "battery": "5000",
  "camera": "50",
  "ratings": "4.5",
  "processor": "Snapdragon"
}
```

**Response (JSON):**
```json
{
  "message": "Success",
  "recommendations": [
    {
      "Brand": "Samsung",
      "Model": "Galaxy S26 Ultra",
      "Prices": 139999.0,
      "Score": 0.998,
      "RAM": 16,
      "Battery": 5000,
      "Camera": 200.0,
      "Processor": "Snapdragon 8 Gen 5",
      "Ratings": 4.8
    }
  ]
}
```

## 🤝 Contributing

Contributions are always welcome! 
If you have ideas for adding more features, updating the dataset, or improving the ML model, feel free to fork this repository and submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
