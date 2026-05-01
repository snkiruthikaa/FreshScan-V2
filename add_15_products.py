# add_15_products.py
import sqlite3
from datetime import datetime, timedelta

DB_PATH = "freshscan.db"

# Only 15 products - all with proper dates
products = [
    # Dairy & Eggs
    ("Organic Milk", "MILK-001", "Dairy & Eggs", "2024-04-01", "2024-04-20", "Keep refrigerated at 4°C"),
    ("Fresh Eggs", "EGG-001", "Dairy & Eggs", "2024-04-01", "2024-05-01", "Refrigerate at 4°C"),
    ("Greek Yogurt", "YOG-001", "Dairy & Eggs", "2024-04-01", "2024-04-25", "Keep refrigerated"),
    ("Amul Butter", "BUTTER-001", "Dairy & Eggs", "2024-04-01", "2024-06-01", "Keep refrigerated"),
    
    # Bakery & Bread
    ("Wheat Bread", "BREAD-001", "Bakery & Bread", "2024-04-01", "2024-04-10", "Store in cool dry place"),
    ("Britannia Cake", "CAKE-001", "Bakery & Bread", "2024-04-01", "2024-05-01", "Store in airtight container"),
    
    # Fresh Fruits
    ("Apple", "APPLE-001", "Fresh Fruits", "2024-04-01", "2024-04-20", "Store in refrigerator"),
    ("Banana", "BANANA-001", "Fresh Fruits", "2024-04-01", "2024-04-12", "Store at room temperature"),
    
    # Fresh Vegetables
    ("Tomato", "TOMATO-001", "Fresh Vegetables", "2024-04-01", "2024-04-15", "Store in cool place"),
    ("Onion", "ONION-001", "Fresh Vegetables", "2024-04-01", "2024-04-30", "Store in dry place"),
    
    # Meat & Seafood
    ("Chicken Breast", "CHICKEN-001", "Meat & Seafood", "2024-04-01", "2024-04-08", "Keep frozen or refrigerated"),
    
    # Beverages
    ("Coca Cola", "COKE-001", "Beverages - Cold", "2024-04-01", "2024-10-01", "Store in cool place"),
    ("Tata Tea", "TEA-001", "Beverages - Hot", "2024-04-01", "2025-04-01", "Store in airtight container"),
    
    # Snacks
    ("Lays Chips", "LAYS-001", "Snacks & Chips", "2024-04-01", "2024-07-01", "Store in cool dry place"),
    
    # Cooking Essentials
    ("Fortune Oil", "OIL-001", "Cooking Essentials", "2024-04-01", "2025-04-01", "Store in cool dark place")
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

added = 0
skipped = 0

print("📦 Adding 15 products to database...")
print("="*50)

for product in products:
    name, batch, category, mfg, expiry, storage = product
    
    # Check if batch already exists
    cursor.execute("SELECT id FROM products WHERE batch_id = ?", (batch,))
    if cursor.fetchone():
        print(f"⚠️ Skipped: {name} (Batch {batch} already exists)")
        skipped += 1
        continue
    
    # Add product
    cursor.execute('''
        INSERT INTO products (product_name, batch_id, category, mfg_date, expiry_date, storage_instructions)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, batch, category, mfg, expiry, storage))
    
    added += 1
    print(f"✅ Added: {name} | {batch} | Expires: {expiry}")

conn.commit()
conn.close()

print("="*50)
print(f"✅ Successfully added {added} products")
print(f"⚠️ Skipped: {skipped} duplicates")
print("="*50)
print("\n🔧 Next steps:")
print("1. Restart your Flask app")
print("2. Go to Admin Panel and click 'Generate All QR'")
print("3. Check if QR codes are generated in static/qr_codes/ folder")