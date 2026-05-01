# add_90_products.py
import sqlite3
from datetime import datetime, timedelta

DB_PATH = "freshscan.db"

# Get today's date for calculations
today = datetime.now().date()

# Products to add - NO FRUITS, NO VEGETABLES, NO STATUS TEXT IN NAMES
products = []

# ============================================================
# 1. DAIRY & EGGS (15 products)
# ============================================================

# EXPIRED DAIRY
products.extend([
    ("Amul Gold Milk", "MILK-EXP-001", "Dairy & Eggs", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     "EXPIRED - Do not consume"),
    
    ("Mother Dairy Curd", "CURD-EXP-002", "Dairy & Eggs", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     "EXPIRED - Discard"),
    
    ("Paneer Fresh", "PANEER-EXP-003", "Dairy & Eggs", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     "EXPIRED - Do not use"),
])

# NEAR EXPIRY DAIRY
products.extend([
    ("Fresh Milk", "MILK-NEAR-004", "Dairy & Eggs", 
     (today - timedelta(days=18)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=2)).strftime('%Y-%m-%d'), 
     "Expires in 2 days! Consume soon"),
    
    ("Greek Yogurt", "YOG-NEAR-005", "Dairy & Eggs", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=3)).strftime('%Y-%m-%d'), 
     "Expires in 3 days"),
    
    ("Cheese Slice", "CHEESE-NEAR-006", "Dairy & Eggs", 
     (today - timedelta(days=25)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=5)).strftime('%Y-%m-%d'), 
     "Expires in 5 days"),
    
    ("Butter", "BUTTER-NEAR-007", "Dairy & Eggs", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=6)).strftime('%Y-%m-%d'), 
     "Use within 6 days"),
])

# SAFE DAIRY
products.extend([
    ("Organic Fresh Milk", "MILK-SAFE-008", "Dairy & Eggs", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=20)).strftime('%Y-%m-%d'), 
     "Fresh - 20 days remaining"),
    
    ("Premium Greek Yogurt", "YOG-SAFE-009", "Dairy & Eggs", 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=25)).strftime('%Y-%m-%d'), 
     "25 days remaining"),
    
    ("Organic Eggs (12 pcs)", "EGG-SAFE-010", "Dairy & Eggs", 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=30)).strftime('%Y-%m-%d'), 
     "30 days remaining"),
    
    ("Amul Butter (500g)", "BUTTER-SAFE-011", "Dairy & Eggs", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=60)).strftime('%Y-%m-%d'), 
     "60 days remaining"),
    
    ("Cheddar Cheese Block", "CHEESE-SAFE-012", "Dairy & Eggs", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining"),
    
    ("Amul Ghee (1L)", "GHEE-SAFE-013", "Dairy & Eggs", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=300)).strftime('%Y-%m-%d'), 
     "Long shelf life - 300 days"),
    
    ("Protein Buttermilk", "BUTTERMILK-SAFE-014", "Dairy & Eggs", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=40)).strftime('%Y-%m-%d'), 
     "40 days remaining"),
    
    ("Mozzarella Cheese", "MOZZARELLA-SAFE-015", "Dairy & Eggs", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=50)).strftime('%Y-%m-%d'), 
     "50 days remaining"),
])

# ============================================================
# 2. BAKERY & BREAD (12 products)
# ============================================================

# EXPIRED BAKERY
products.extend([
    ("Brown Bread", "BREAD-EXP-016", "Bakery & Bread", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=4)).strftime('%Y-%m-%d'), 
     "EXPIRED - Discard"),
    
    ("Fruit Cake", "CAKE-EXP-017", "Bakery & Bread", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     "EXPIRED"),
])

# NEAR EXPIRY BAKERY
products.extend([
    ("Whole Wheat Bread", "BREAD-NEAR-018", "Bakery & Bread", 
     (today - timedelta(days=4)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=1)).strftime('%Y-%m-%d'), 
     "Expires tomorrow!"),
    
    ("Butter Croissant", "CROISSANT-NEAR-019", "Bakery & Bread", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=2)).strftime('%Y-%m-%d'), 
     "Expires in 2 days"),
    
    ("Pav Bhaji Bread Pack", "PAV-NEAR-020", "Bakery & Bread", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=3)).strftime('%Y-%m-%d'), 
     "Expires in 3 days"),
    
    ("Garlic Bread Loaf", "GARLIC-NEAR-021", "Bakery & Bread", 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=4)).strftime('%Y-%m-%d'), 
     "Expires in 4 days"),
])

# SAFE BAKERY
products.extend([
    ("Premium White Bread", "BREAD-SAFE-022", "Bakery & Bread", 
     (today - timedelta(days=1)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=12)).strftime('%Y-%m-%d'), 
     "12 days remaining"),
    
    ("Butter Croissant Pack", "CROISSANT-SAFE-023", "Bakery & Bread", 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=10)).strftime('%Y-%m-%d'), 
     "10 days remaining"),
    
    ("Multigrain Bread", "MULTIGRAIN-SAFE-024", "Bakery & Bread", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=15)).strftime('%Y-%m-%d'), 
     "15 days remaining"),
    
    ("Chocolate Chip Cookies", "COOKIE-SAFE-025", "Bakery & Bread", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=60)).strftime('%Y-%m-%d'), 
     "60 days remaining"),
    
    ("Marie Biscuits Pack", "MARIE-SAFE-026", "Bakery & Bread", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining"),
    
    ("Oreo Biscuits", "OREO-SAFE-027", "Bakery & Bread", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
])

# ============================================================
# 3. MEAT & SEAFOOD (12 products)
# ============================================================

# EXPIRED MEAT
products.extend([
    ("Chicken Breast", "CHICKEN-EXP-028", "Meat & Seafood", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=2)).strftime('%Y-%m-%d'), 
     "EXPIRED - Unsafe to eat"),
])

# NEAR EXPIRY MEAT
products.extend([
    ("Mutton Curry Cut", "MUTTON-NEAR-029", "Meat & Seafood", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=4)).strftime('%Y-%m-%d'), 
     "Use within 4 days"),
    
    ("Fish Fillet", "FISH-NEAR-030", "Meat & Seafood", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=1)).strftime('%Y-%m-%d'), 
     "Expires tomorrow - cook immediately"),
    
    ("Pork Chops", "PORK-NEAR-031", "Meat & Seafood", 
     (today - timedelta(days=4)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=3)).strftime('%Y-%m-%d'), 
     "Use within 3 days"),
])

# SAFE MEAT (Frozen)
products.extend([
    ("Frozen Chicken Wings", "CHICKEN-SAFE-032", "Meat & Seafood", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining - Keep frozen"),
    
    ("Frozen Fish Fingers", "FISH-SAFE-033", "Meat & Seafood", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining - Keep frozen"),
    
    ("Frozen Prawns", "PRAWNS-SAFE-034", "Meat & Seafood", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=150)).strftime('%Y-%m-%d'), 
     "150 days remaining - Keep frozen"),
    
    ("Frozen Chicken Nuggets", "NUGGETS-SAFE-035", "Meat & Seafood", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Frozen Sausages", "SAUSAGE-SAFE-036", "Meat & Seafood", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining"),
    
    ("Frozen Chicken Breast Fillet", "CHICKENFILLET-SAFE-037", "Meat & Seafood", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining"),
    
    ("Frozen Shrimp Large", "SHRIMP-SAFE-038", "Meat & Seafood", 
     (today - timedelta(days=18)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=150)).strftime('%Y-%m-%d'), 
     "150 days remaining"),
])

# ============================================================
# 4. FROZEN FOODS (8 products)
# ============================================================

products.extend([
    ("Vanilla Ice Cream", "ICECREAM-SAFE-039", "Frozen Foods", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining - Keep frozen"),
    
    ("Chocolate Ice Cream", "ICECREAM-CHOC-040", "Frozen Foods", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=200)).strftime('%Y-%m-%d'), 
     "200 days remaining"),
    
    ("Frozen Paratha (10 pcs)", "PARATHA-SAFE-041", "Frozen Foods", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining"),
    
    ("Frozen Mixed Vegetables", "MIXVEG-SAFE-042", "Frozen Foods", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Frozen Pizza Margherita", "PIZZA-SAFE-043", "Frozen Foods", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining"),
    
    ("Frozen French Fries", "FRIES-SAFE-044", "Frozen Foods", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Frozen Spring Rolls", "SPRINGROLL-SAFE-045", "Frozen Foods", 
     (today - timedelta(days=6)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=150)).strftime('%Y-%m-%d'), 
     "150 days remaining"),
    
    ("Frozen Momos", "MOMO-SAFE-046", "Frozen Foods", 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining"),
])

# ============================================================
# 5. BEVERAGES - COLD (10 products)
# ============================================================

products.extend([
    ("Coca Cola (2L)", "COKE-SAFE-047", "Beverages - Cold", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "6 months remaining"),
    
    ("Sprite (2L)", "SPRITE-SAFE-048", "Beverages - Cold", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "6 months remaining"),
    
    ("Pepsi (2L)", "PEPSI-SAFE-049", "Beverages - Cold", 
     (today - timedelta(days=25)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "6 months remaining"),
    
    ("Real Orange Juice (1L)", "JUICE-SAFE-050", "Beverages - Cold", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=60)).strftime('%Y-%m-%d'), 
     "60 days remaining"),
    
    ("Tropicana Apple Juice", "TROPICANA-SAFE-051", "Beverages - Cold", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=60)).strftime('%Y-%m-%d'), 
     "60 days remaining"),
    
    ("Paper Boat Mango Drink", "PAPERBOAT-SAFE-052", "Beverages - Cold", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining"),
    
    ("Thums Up (750ml)", "THUMSUP-SAFE-053", "Beverages - Cold", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Maaza Mango Drink", "MAAZA-SAFE-054", "Beverages - Cold", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=150)).strftime('%Y-%m-%d'), 
     "150 days remaining"),
    
    ("Appy Fizz", "APPY-SAFE-055", "Beverages - Cold", 
     (today - timedelta(days=18)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining"),
    
    ("Bournvita", "BOURNVITA-EXP-056", "Beverages - Cold", 
     (today - timedelta(days=60)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     "EXPIRED"),
])

# ============================================================
# 6. BEVERAGES - HOT (8 products)
# ============================================================

products.extend([
    ("Tata Tea Gold (250g)", "TEA-SAFE-057", "Beverages - Hot", 
     (today - timedelta(days=60)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=300)).strftime('%Y-%m-%d'), 
     "300 days remaining - Keep dry"),
    
    ("Nescafe Classic (50g)", "COFFEE-SAFE-058", "Beverages - Hot", 
     (today - timedelta(days=45)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=365)).strftime('%Y-%m-%d'), 
     "1 year remaining"),
    
    ("Red Label Tea", "REDLABEL-SAFE-059", "Beverages - Hot", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=365)).strftime('%Y-%m-%d'), 
     "1 year remaining"),
    
    ("Green Tea Tulsi", "GREENTEA-SAFE-060", "Beverages - Hot", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=365)).strftime('%Y-%m-%d'), 
     "1 year remaining"),
    
    ("Bru Instant Coffee", "BRU-SAFE-061", "Beverages - Hot", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=300)).strftime('%Y-%m-%d'), 
     "300 days remaining"),
    
    ("Lemon Tea Pack", "LEMONTEA-SAFE-062", "Beverages - Hot", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Masala Chai Premium", "MASALACHAI-SAFE-063", "Beverages - Hot", 
     (today - timedelta(days=25)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=240)).strftime('%Y-%m-%d'), 
     "240 days remaining"),
    
    ("Coffee", "COFFEE-EXP-064", "Beverages - Hot", 
     (today - timedelta(days=50)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     "EXPIRED"),
])

# ============================================================
# 7. SNACKS & CHIPS (10 products)
# ============================================================

products.extend([
    ("Lays Classic (52g)", "LAYS-SAFE-065", "Snacks & Chips", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining"),
    
    ("Kurkure Masala", "KURKURE-SAFE-066", "Snacks & Chips", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=100)).strftime('%Y-%m-%d'), 
     "100 days remaining"),
    
    ("Pringles Original", "PRINGLES-SAFE-067", "Snacks & Chips", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=150)).strftime('%Y-%m-%d'), 
     "150 days remaining"),
    
    ("Doritos Nachos", "DORITOS-SAFE-068", "Snacks & Chips", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining"),
    
    ("Cheetos Masala", "CHEETOS-SAFE-069", "Snacks & Chips", 
     (today - timedelta(days=6)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=100)).strftime('%Y-%m-%d'), 
     "100 days remaining"),
    
    ("Bingo Tangy Chips", "BINGO-SAFE-070", "Snacks & Chips", 
     (today - timedelta(days=18)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=90)).strftime('%Y-%m-%d'), 
     "90 days remaining"),
    
    ("Haldiram's Aloo Bhujia", "HALDIRAM-SAFE-071", "Snacks & Chips", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Nacho Cheese Dip", "NACHODIP-SAFE-072", "Snacks & Chips", 
     (today - timedelta(days=5)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=120)).strftime('%Y-%m-%d'), 
     "120 days remaining"),
    
    ("Microwave Popcorn", "POPCORN-NEAR-073", "Snacks & Chips", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=7)).strftime('%Y-%m-%d'), 
     "Expires in 7 days"),
    
    ("Potato Chips", "CHIPS-EXP-074", "Snacks & Chips", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=3)).strftime('%Y-%m-%d'), 
     "EXPIRED"),
])

# ============================================================
# 8. CHOCOLATES & CANDY (8 products)
# ============================================================

products.extend([
    ("Dairy Milk Silk", "DAIRYMILK-SAFE-075", "Chocolates & Candy", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("KitKat Chocolate", "KITKAT-SAFE-076", "Chocolates & Candy", 
     (today - timedelta(days=15)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=200)).strftime('%Y-%m-%d'), 
     "200 days remaining"),
    
    ("Munch Chocolate", "MUNCH-SAFE-077", "Chocolates & Candy", 
     (today - timedelta(days=10)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("5 Star Chocolate", "FIVESTAR-SAFE-078", "Chocolates & Candy", 
     (today - timedelta(days=25)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Cadbury Gems", "GEMS-SAFE-079", "Chocolates & Candy", 
     (today - timedelta(days=12)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=240)).strftime('%Y-%m-%d'), 
     "240 days remaining"),
    
    ("Eclairs Candy", "ECLAIRS-SAFE-080", "Chocolates & Candy", 
     (today - timedelta(days=8)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=300)).strftime('%Y-%m-%d'), 
     "300 days remaining"),
    
    ("Chocolate Bar", "CHOC-NEAR-081", "Chocolates & Candy", 
     (today - timedelta(days=60)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=5)).strftime('%Y-%m-%d'), 
     "Expires in 5 days"),
    
    ("Candy Pack", "CANDY-EXP-082", "Chocolates & Candy", 
     (today - timedelta(days=90)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     "EXPIRED"),
])

# ============================================================
# 9. COOKING ESSENTIALS (8 products)
# ============================================================

products.extend([
    ("Fortune Sunflower Oil", "OIL-SAFE-083", "Cooking Essentials", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=365)).strftime('%Y-%m-%d'), 
     "1 year remaining"),
    
    ("Tata Salt (1kg)", "SALT-SAFE-084", "Cooking Essentials", 
     (today - timedelta(days=60)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=730)).strftime('%Y-%m-%d'), 
     "2 years remaining"),
    
    ("MDH Masala Pack", "MASALA-SAFE-085", "Cooking Essentials", 
     (today - timedelta(days=20)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Everest Garam Masala", "EVEREST-SAFE-086", "Cooking Essentials", 
     (today - timedelta(days=25)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=240)).strftime('%Y-%m-%d'), 
     "240 days remaining"),
    
    ("Aashirvaad Atta (5kg)", "ATTA-SAFE-087", "Cooking Essentials", 
     (today - timedelta(days=45)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=180)).strftime('%Y-%m-%d'), 
     "180 days remaining"),
    
    ("Daawat Basmati Rice", "RICE-SAFE-088", "Cooking Essentials", 
     (today - timedelta(days=60)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=365)).strftime('%Y-%m-%d'), 
     "1 year remaining"),
    
    ("Sugar (1kg)", "SUGAR-SAFE-089", "Cooking Essentials", 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     (today + timedelta(days=730)).strftime('%Y-%m-%d'), 
     "2 years remaining"),
    
    ("Spice Pack", "SPICE-EXP-090", "Cooking Essentials", 
     (today - timedelta(days=90)).strftime('%Y-%m-%d'), 
     (today - timedelta(days=30)).strftime('%Y-%m-%d'), 
     "EXPIRED"),
])

# ============================================================
# ADD TO DATABASE
# ============================================================

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

added = 0
skipped = 0

print("=" * 60)
print("📦 FRESHSCAN - ADDING 90+ PRODUCTS")
print("=" * 60)
print("\n📂 Categories included:")
print("   ✅ Dairy & Eggs")
print("   ✅ Bakery & Bread")
print("   ✅ Meat & Seafood")
print("   ✅ Frozen Foods")
print("   ✅ Beverages - Cold")
print("   ✅ Beverages - Hot")
print("   ✅ Snacks & Chips")
print("   ✅ Chocolates & Candy")
print("   ✅ Cooking Essentials")
print("\n" + "=" * 60)
print("⏳ Adding products to database...\n")

for product in products:
    name, batch, category, mfg, expiry, storage = product
    
    # Check if batch already exists
    cursor.execute("SELECT id FROM products WHERE batch_id = ?", (batch,))
    if cursor.fetchone():
        print(f"⚠️ Skipped: {name[:35]} (Batch: {batch})")
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
    elif days_left <= 7:
        status_icon = "🟡"
    else:
        status_icon = "🟢"
    
    print(f"{status_icon} Added: {name[:35]} | {batch}")

conn.commit()
conn.close()

print("\n" + "=" * 60)
print("📊 SUMMARY")
print("=" * 60)
print(f"   ✅ Successfully added: {added} products")
print(f"   ⏭️  Skipped (duplicates): {skipped} products")
print("=" * 60)
print("\n🚀 NEXT STEPS:")
print("   1. Run: python fix_qr_codes.py")
print("   2. Restart Flask: python app.py")
print("   3. Go to Admin Panel: /admin")
print("=" * 60)