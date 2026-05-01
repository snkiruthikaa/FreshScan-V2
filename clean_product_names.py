# clean_product_names.py
import sqlite3

DB_PATH = "freshscan.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get all products
cursor.execute("SELECT id, product_name FROM products")
products = cursor.fetchall()

updated = 0
print("=" * 50)
print("🧹 CLEANING PRODUCT NAMES")
print("=" * 50)

for product in products:
    product_id = product[0]
    old_name = product[1]
    
    # Remove all status indicators from names
    new_name = old_name
    new_name = new_name.replace(" (Expired)", "")
    new_name = new_name.replace("(Expired)", "")
    new_name = new_name.replace(" (Near Expiry)", "")
    new_name = new_name.replace("(Near Expiry)", "")
    new_name = new_name.replace(" (EXPIRED)", "")
    new_name = new_name.replace("(EXPIRED)", "")
    new_name = new_name.strip()
    
    if new_name != old_name:
        cursor.execute("UPDATE products SET product_name = ? WHERE id = ?", (new_name, product_id))
        print(f"✅ Cleaned: {old_name} → {new_name}")
        updated += 1

conn.commit()
conn.close()

print("=" * 50)
print(f"✅ Updated {updated} product names")
print("=" * 50)
print("\n🚀 Now restart your Flask app and check Admin Panel!")