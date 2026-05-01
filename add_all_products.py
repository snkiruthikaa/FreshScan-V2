# add_all_products.py
import sqlite3
from datetime import datetime, timedelta

DB_PATH = "freshscan.db"

# Get today's date for calculations
today = datetime.now().date()

# Define products with different expiry statuses
products = [
    # ========== EXPIRED PRODUCTS (Past dates) ==========
    # Dairy & Eggs - Expired
    ("Amul Gold Milk ", "MILK-EXP-001", "Dairy & Eggs", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     "Keep refrigerated - EXPIRED, do not consume"),
    
    ("Mother Dairy Curd ", "CURD-EXP-002", "Dairy & Eggs", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     "Expired - discard immediately"),
    
    ("Paneer", "PANEER-EXP-003", "Dairy & Eggs", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     "Expired - do not use"),
    
    # Bakery - Expired
    ("Brown Bread ", "BREAD-EXP-004", "Bakery & Bread", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=4)).strftime('%Y-%m-%d'), 
     "Expired bread - discard"),
    
    ("Fruit Cake ", "CAKE-EXP-005", "Bakery & Bread", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     "Expired cake"),
    
    # Meat - Expired
    ("Chicken Breast", "CHICKEN-EXP-006", "Meat & Seafood", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     "Expired chicken - unsafe to eat"),
    
    # Fruits - Expired
    ("Rotten Apple", "APPLE-EXP-007", "Fresh Fruits", 
     (today - timedelta(days=14)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=7)).strftime('%Y-%m-%d'), 
     "Apple expired - rotten"),
    
    # ========== NEAR EXPIRY PRODUCTS (0-7 days left) ==========
    # Dairy - Near Expiry
    ("Fresh Milk (Near Expiry)", "MILK-NEAR-008", "Dairy & Eggs", 
     (today - timedelta(days=18)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=2)).strftime('%Y-%m-%d'), 
     "Expires in 2 days! Consume soon"),
    
    ("Yogurt (Near Expiry)", "YOG-NEAR-009", "Dairy & Eggs", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=3)).strftime('%Y-%m-%d'), 
     "Expires in 3 days"),
    
    ("Cheese Slice (Near Expiry)", "CHEESE-NEAR-010", "Dairy & Eggs", 
     (today - timedelta(days=25)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=5)).strftime('%Y-%m-%d'), 
     "Expires in 5 days"),
    
    # Bakery - Near Expiry
    ("Whole Wheat Bread", "BREAD-NEAR-011", "Bakery & Bread", 
     (today - timedelta(days=4)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=1)).strftime('%Y-%m-%d'), 
     "Expires tomorrow!"),
    
    ("Croissant (Near Expiry)", "CROISSANT-NEAR-012", "Bakery & Bread", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=2)).strftime('%Y-%m-%d'), 
     "Expires in 2 days"),
    
    ("Pav Bhaji Bread", "PAV-NEAR-013", "Bakery & Bread", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=3)).strftime('%Y-%m-%d'), 
     "Expires in 3 days"),
    
    # Meat - Near Expiry
    ("Mutton Curry Cut", "MUTTON-NEAR-014", "Meat & Seafood", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=4)).strftime('%Y-%m-%d'), 
     "Use within 4 days"),
    
    ("Fish Fillet (Near Expiry)", "FISH-NEAR-015", "Meat & Seafood", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=1)).strftime('%Y-%m-%d'), 
     "Expires tomorrow - cook immediately"),
    
    # Fruits - Near Expiry
    ("Banana (Near Expiry)", "BANANA-NEAR-016", "Fresh Fruits", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=2)).strftime('%Y-%m-%d'), 
     "Expires in 2 days - eat now"),
    
    ("Strawberry (Near Expiry)", "STRAWBERRY-NEAR-017", "Fresh Fruits", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=3)).strftime('%Y-%m-%d'), 
     "Expires in 3 days"),
    
    # Vegetables - Near Expiry
    ("Spinach (Near Expiry)", "SPINACH-NEAR-018", "Fresh Vegetables", 
     (today - timedelta(days=4)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=1)).strftime('%Y-%m-%d'), 
     "Expires tomorrow!"),
    
    ("Tomato (Near Expiry)", "TOMATO-NEAR-019", "Fresh Vegetables", 
     (today - timedelta(days=6)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=4)).strftime('%Y-%m-%d'), 
     "Use within 4 days"),
    
    # ========== SAFE PRODUCTS (More than 7 days left) ==========
    # Dairy - Safe
    ("Organic Milk", "MILK-SAFE-020", "Dairy & Eggs", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=20)).strftime('%Y-%m-%d'), 
     "Fresh - 20 days remaining"),
    
    ("Greek Yogurt", "YOG-SAFE-021", "Dairy & Eggs", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=25)).strftime('%Y-%m-%d'), 
     "25 days remaining"),
    
    ("Fresh Eggs (Dozen)", "EGG-SAFE-022", "Dairy & Eggs", 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=30)).strftime('%Y-%m-%d'), 
     "30 days remaining"),
    
    ("Amul Butter", "BUTTER-SAFE-023", "Dairy & Eggs", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=60)).strftime('%Y-%m-%d'), 
     "60 days remaining"),
    
    ("Cheddar Cheese Block", "CHEESE-SAFE-024", "Dairy & Eggs", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining"),
    
    ("Ghee", "GHEE-SAFE-025", "Dairy & Eggs", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=300)).strftime('%Y-%m-%d'), 
     "Long shelf life - 300 days remaining"),
    
    # Bakery - Safe
    ("Premium White Bread", "BREAD-SAFE-026", "Bakery & Bread", 
     (today - timedelta(days=1)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=12)).strftime('%Y-%m-%d'), 
     "12 days remaining"),
    
    ("Butter Croissant Pack", "CROISSANT-SAFE-027", "Bakery & Bread", 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=10)).strftime('%Y-%m-%d'), 
     "10 days remaining"),
    
    # Fresh Fruits - Safe
    ("Red Apple", "APPLE-SAFE-028", "Fresh Fruits", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=15)).strftime('%Y-%m-%d'), 
     "15 days remaining"),
    
    ("Orange", "ORANGE-SAFE-029", "Fresh Fruits", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=18)).strftime('%Y-%m-%d'), 
     "18 days remaining"),
    
    ("Pomegranate", "POMEGRANATE-SAFE-030", "Fresh Fruits", 
     (today - timedelta(days=4)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=20)).strftime('%Y-%m-%d'), 
     "20 days remaining"),
    
    ("Watermelon", "WATERMELON-SAFE-031", "Fresh Fruits", 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=14)).strftime('%Y-%m-%d'), 
     "14 days remaining"),
    
    # Fresh Vegetables - Safe
    ("Potato - 5kg", "POTATO-SAFE-032", "Fresh Vegetables", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=30)).strftime('%Y-%m-%d'), 
     "30 days remaining"),
    
    ("Onion - 5kg", "ONION-SAFE-033", "Fresh Vegetables", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=25)).strftime('%Y-%m-%d'), 
     "25 days remaining"),
    
    ("Carrot", "CARROT-SAFE-034", "Fresh Vegetables", 
     (today - timedelta(days=4)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=12)).strftime('%Y-%m-%d'), 
     "12 days remaining"),
    
    ("Broccoli", "BROCCOLI-SAFE-035", "Fresh Vegetables", 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=10)).strftime('%Y-%m-%d'), 
     "10 days remaining"),
    
    # Meat & Seafood - Safe (Frozen)
    ("Frozen Chicken Wings", "CHICKEN-SAFE-036", "Meat & Seafood", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining - frozen"),
    
    ("Frozen Fish Fingers", "FISH-SAFE-037", "Meat & Seafood", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining - frozen"),
    
    ("Prawns (Frozen)", "PRAWNS-SAFE-038", "Meat & Seafood", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=150)).strftime('%Y-%m-%d'), 
     "150 days remaining - frozen"),
    
    # Beverages - Cold
    ("Coca Cola Can", "COKE-SAFE-039", "Beverages - Cold", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "6 months remaining"),
    
    ("Sprite Bottle", "SPRITE-SAFE-040", "Beverages - Cold", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "6 months remaining"),
    
    ("Real Orange Juice", "JUICE-SAFE-041", "Beverages - Cold", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=60)).strftime('%Y-%m-%d'), 
     "60 days remaining"),
    
    # Beverages - Hot
    ("Tata Tea Gold", "TEA-SAFE-042", "Beverages - Hot", 
     (today - timedelta(days=60)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=300)).strftime('%Y-%m-%d'), 
     "300 days remaining"),
    
    ("Nescafe Classic", "COFFEE-SAFE-043", "Beverages - Hot", 
     (today - timedelta(days=45)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=365)).strftime('%Y-%m-%d'), 
     "1 year remaining"),
    
    # Snacks & Chips
    ("Lays Classic", "LAYS-SAFE-044", "Snacks & Chips", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining"),
    
    ("Kurkure Masala", "KURKURE-SAFE-045", "Snacks & Chips", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=100)).strftime('%Y-%m-%d'), 
     "100 days remaining"),
    
    # Cooking Essentials
    ("Fortune Sunflower Oil", "OIL-SAFE-046", "Cooking Essentials", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=365)).strftime('%Y-%m-%d'), 
     "1 year remaining"),
    
    ("Tata Salt", "SALT-SAFE-047", "Cooking Essentials", 
     (today - timedelta(days=60)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=730)).strftime('%Y-%m-%d'), 
     "2 years remaining"),
    
    ("MDH Masala Pack", "MASALA-SAFE-048", "Cooking Essentials", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    # Ready to Eat
    ("Maggi Noodles", "MAGGI-SAFE-049", "Ready to Eat", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=150)).strftime('%Y-%m-%d'), 
     "150 days remaining"),
    
    ("MTR Dal Makhani", "MTR-SAFE-050", "Ready to Eat", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining"),
]

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

added = 0
skipped = 0

print("=" * 60)
print("📦 FRESHSCAN - ADDING 50+ PRODUCTS")
print("=" * 60)
print("\n📊 Products by status:")
print("   🔴 EXPIRED - 7 products")
print("   🟡 NEAR EXPIRY - 12 products")
print("   🟢 SAFE - 31+ products")
print("   📦 TOTAL - 50+ products")
print("\n" + "=" * 60)
print("⏳ Adding products to database...\n")

for product in products:
    name, batch, category, mfg, expiry, storage = product
    
    # Check if batch already exists
    cursor.execute("SELECT id FROM products WHERE batch_id = ?", (batch,))
    if cursor.fetchone():
        print(f"⚠️ Skipped: {name} (Batch: {batch})")
        skipped += 1
        continue
    
    # Add product
    cursor.execute('''
        INSERT INTO products (product_name, batch_id, category, mfg_date, expiry_date, storage_instructions)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, batch, category, mfg, expiry, storage))
    
    added += 1
    
    # Determine status for display
    expiry_date = datetime.strptime(expiry, '%Y-%m-%d').date()
    days_left = (expiry_date - today).days
    
    if days_left < 0:
        status_icon = "🔴"
        status_text = "EXPIRED"
    elif days_left <= 7:
        status_icon = "🟡"
        status_text = "NEAR EXPIRY"
    else:
        status_icon = "🟢"
        status_text = "SAFE"
    
    print(f"{status_icon} Added: {name[:30]:30} | {batch:20} | {status_text}")

conn.commit()
conn.close()

print("\n" + "=" * 60)
print("📊 SUMMARY")
print("=" * 60)
print(f"   ✅ Successfully added: {added} products")
print(f"   ⏭️  Skipped (duplicates): {skipped} products")
print(f"   📦 Total in database: {added}")
print("\n📊 Status Distribution:")
print("   🔴 EXPIRED: Products with past expiry dates")
print("   🟡 NEAR EXPIRY: Products expiring within 7 days")
print("   🟢 SAFE: Products with more than 7 days remaining")
print("=" * 60)
print("\n🚀 NEXT STEPS:")
print("   1. Run: python fix_qr_codes.py")
print("   2. Restart Flask: python app.py")
print("   3. Go to Admin Panel: /admin")
print("   4. Click 'Generate All QR' if needed")
print("=" * 60)