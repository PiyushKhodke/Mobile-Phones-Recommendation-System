import pandas as pd
import random

def generate_dataset():
    data = [
        # Premium Segment (>60k)
        {"Brand": "Apple", "Model": "iPhone 17 Pro Max", "Prices": 159900, "RAM": 8, "Camera": 48, "Processor": "A19 Pro", "Battery": 4600, "Ratings": 4.8},
        {"Brand": "Apple", "Model": "iPhone 17 Pro", "Prices": 134900, "RAM": 8, "Camera": 48, "Processor": "A19 Pro", "Battery": 3500, "Ratings": 4.7},
        {"Brand": "Apple", "Model": "iPhone 17", "Prices": 79900, "RAM": 8, "Camera": 48, "Processor": "A19 Bionic", "Battery": 3500, "Ratings": 4.6},
        {"Brand": "Samsung", "Model": "Galaxy S26 Ultra", "Prices": 139999, "RAM": 16, "Camera": 200, "Processor": "Snapdragon 8 Gen 5", "Battery": 5000, "Ratings": 4.8},
        {"Brand": "Samsung", "Model": "Galaxy S26 Plus", "Prices": 99999, "RAM": 12, "Camera": 50, "Processor": "Snapdragon 8 Gen 5", "Battery": 4900, "Ratings": 4.7},
        {"Brand": "Samsung", "Model": "Galaxy S26", "Prices": 79999, "RAM": 12, "Camera": 50, "Processor": "Snapdragon 8 Gen 5", "Battery": 4000, "Ratings": 4.6},
        {"Brand": "Google", "Model": "Pixel 10 Pro XL", "Prices": 115999, "RAM": 16, "Camera": 50, "Processor": "Tensor G5", "Battery": 5060, "Ratings": 4.6},
        {"Brand": "Google", "Model": "Pixel 10", "Prices": 74999, "RAM": 12, "Camera": 50, "Processor": "Tensor G5", "Battery": 4500, "Ratings": 4.5},
        {"Brand": "OnePlus", "Model": "14 Pro", "Prices": 74999, "RAM": 16, "Camera": 50, "Processor": "Snapdragon 8 Gen 4", "Battery": 5400, "Ratings": 4.6},
        {"Brand": "OnePlus", "Model": "Open 2", "Prices": 139999, "RAM": 16, "Camera": 48, "Processor": "Snapdragon 8 Gen 4", "Battery": 4805, "Ratings": 4.7},
        {"Brand": "Xiaomi", "Model": "16 Ultra", "Prices": 109999, "RAM": 16, "Camera": 50, "Processor": "Snapdragon 8 Gen 4", "Battery": 5300, "Ratings": 4.7},
        {"Brand": "Vivo", "Model": "X110 Pro", "Prices": 89999, "RAM": 16, "Camera": 50, "Processor": "Dimensity 9400", "Battery": 5400, "Ratings": 4.8},
        
        # Mid-Premium Segment (40k - 60k)
        {"Brand": "OnePlus", "Model": "14R", "Prices": 42999, "RAM": 12, "Camera": 50, "Processor": "Snapdragon 8 Gen 3", "Battery": 5500, "Ratings": 4.5},
        {"Brand": "Nothing", "Model": "Phone (3)", "Prices": 44999, "RAM": 12, "Camera": 50, "Processor": "Snapdragon 8s Gen 3", "Battery": 4900, "Ratings": 4.4},
        {"Brand": "Samsung", "Model": "Galaxy A56 5G", "Prices": 39999, "RAM": 8, "Camera": 50, "Processor": "Exynos 1580", "Battery": 5000, "Ratings": 4.3},
        {"Brand": "Google", "Model": "Pixel 9a", "Prices": 47999, "RAM": 8, "Camera": 64, "Processor": "Tensor G4", "Battery": 4500, "Ratings": 4.4},
        {"Brand": "iQOO", "Model": "13", "Prices": 52999, "RAM": 12, "Camera": 50, "Processor": "Snapdragon 8 Gen 4", "Battery": 5160, "Ratings": 4.6},
        {"Brand": "Motorola", "Model": "Edge 60 Pro", "Prices": 54999, "RAM": 12, "Camera": 50, "Processor": "Snapdragon 8 Gen 3", "Battery": 4600, "Ratings": 4.5},
        
        # Mid-Range Segment (20k - 40k)
        {"Brand": "Poco", "Model": "F7 Pro", "Prices": 31999, "RAM": 12, "Camera": 50, "Processor": "Snapdragon 8 Gen 2", "Battery": 5000, "Ratings": 4.3},
        {"Brand": "Realme", "Model": "14 Pro+ 5G", "Prices": 29999, "RAM": 8, "Camera": 50, "Processor": "Snapdragon 7s Gen 3", "Battery": 5200, "Ratings": 4.3},
        {"Brand": "Redmi", "Model": "Note 14 Pro+ 5G", "Prices": 32999, "RAM": 12, "Camera": 200, "Processor": "Dimensity 7300 Ultra", "Battery": 5000, "Ratings": 4.2},
        {"Brand": "Motorola", "Model": "Edge 60 Fusion", "Prices": 24999, "RAM": 8, "Camera": 50, "Processor": "Snapdragon 7s Gen 3", "Battery": 5000, "Ratings": 4.4},
        {"Brand": "OnePlus", "Model": "Nord 5", "Prices": 28999, "RAM": 8, "Camera": 50, "Processor": "Snapdragon 7+ Gen 3", "Battery": 5500, "Ratings": 4.4},
        {"Brand": "Nothing", "Model": "Phone (2a) Plus", "Prices": 27999, "RAM": 8, "Camera": 50, "Processor": "Dimensity 7350 Pro", "Battery": 5000, "Ratings": 4.4},
        {"Brand": "iQOO", "Model": "Z10 Pro", "Prices": 23999, "RAM": 8, "Camera": 64, "Processor": "Snapdragon 7 Gen 3", "Battery": 4600, "Ratings": 4.3},
        {"Brand": "Samsung", "Model": "Galaxy M56", "Prices": 26999, "RAM": 8, "Camera": 108, "Processor": "Exynos 1480", "Battery": 6000, "Ratings": 4.2},
        
        # Budget Segment (<20k)
        {"Brand": "Poco", "Model": "X7 5G", "Prices": 16999, "RAM": 6, "Camera": 64, "Processor": "Dimensity 6100+", "Battery": 5000, "Ratings": 4.1},
        {"Brand": "Redmi", "Model": "Note 14 5G", "Prices": 17999, "RAM": 6, "Camera": 108, "Processor": "Dimensity 6080", "Battery": 5000, "Ratings": 4.1},
        {"Brand": "Realme", "Model": "14 5G", "Prices": 15999, "RAM": 6, "Camera": 50, "Processor": "Dimensity 6100+", "Battery": 5000, "Ratings": 4.2},
        {"Brand": "Samsung", "Model": "Galaxy M35 5G", "Prices": 19999, "RAM": 6, "Camera": 50, "Processor": "Exynos 1380", "Battery": 6000, "Ratings": 4.0},
        {"Brand": "Motorola", "Model": "Moto G85 5G", "Prices": 18999, "RAM": 8, "Camera": 50, "Processor": "Snapdragon 6s Gen 3", "Battery": 5000, "Ratings": 4.2},
        {"Brand": "Vivo", "Model": "T4x 5G", "Prices": 13999, "RAM": 6, "Camera": 50, "Processor": "Snapdragon 6 Gen 1", "Battery": 6000, "Ratings": 4.1},
        {"Brand": "Poco", "Model": "M7 5G", "Prices": 10999, "RAM": 4, "Camera": 50, "Processor": "Dimensity 6100+", "Battery": 5000, "Ratings": 4.0},
        {"Brand": "Infinix", "Model": "Note 40 5G", "Prices": 15999, "RAM": 8, "Camera": 108, "Processor": "Dimensity 7020", "Battery": 5000, "Ratings": 4.1},
        {"Brand": "Lava", "Model": "Agni 3", "Prices": 21999, "RAM": 8, "Camera": 50, "Processor": "Dimensity 7300", "Battery": 5000, "Ratings": 4.3},
        {"Brand": "CMF by Nothing", "Model": "Phone 2", "Prices": 16999, "RAM": 6, "Camera": 50, "Processor": "Dimensity 7300", "Battery": 5000, "Ratings": 4.2},
    ]

    # Increase dataset size by adding variations (e.g. storage variants)
    expanded_data = []
    for item in data:
        # Base variant
        expanded_data.append(item.copy())
        
        # High-RAM variant
        if item["RAM"] <= 12:
            high_variant = item.copy()
            high_variant["Model"] = item["Model"] + f" ({item['RAM']+4}GB RAM)"
            high_variant["RAM"] = item["RAM"] + 4
            high_variant["Prices"] = int(item["Prices"] * 1.15)
            expanded_data.append(high_variant)
            
    df = pd.DataFrame(expanded_data)
    df.to_csv("smartphones_2026.csv", index=False)
    print(f"Generated smartphones_2026.csv with {len(expanded_data)} entries.")

if __name__ == "__main__":
    generate_dataset()
