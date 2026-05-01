# add_sample_products.py
import sqlite3
from datetime import datetime, timedelta
import random

# Database path
DB_PATH = "freshscan.db"

# Define products for each category
products_data = {
    "Dairy & Eggs": [
        ("Amul Gold Milk", "AMUL-MILK-001", 7, 3),
        ("Mother Dairy Curd", "MOTHER-CURD-002", 10, 3),
        ("Nestlé Yogurt", "NESTLE-YOG-003", 21, 5),
        ("Amul Butter", "AMUL-BUTTER-004", 90, 10),
        ("Britannia Cheese", "BRIT-CHEESE-005", 60, 15),
        ("Eggoz Nutrition Eggs", "EGGOZ-EGG-006", 30, 5),
        ("Amul Paneer", "AMUL-PANEER-007", 15, 5),
        ("Mother Dairy Dahi", "MOTHER-DAHI-008", 10, 3),
        ("Nandini Curd", "NANDINI-CURD-009", 10, 3),
        ("Verka Milk", "VERKA-MILK-010", 7, 3),
        ("Gowardhan Ghee", "GOWARDHAN-GHEE-011", 365, 30),
        ("Amul Cheese Slice", "AMUL-CHEESE-012", 90, 10),
    ],
    "Bakery & Bread": [
        ("Britannia Bread", "BRIT-BREAD-013", 7, 2),
        ("Modern Bread", "MODERN-BREAD-014", 7, 2),
        ("Britannia Cake", "BRIT-CAKE-015", 30, 7),
        ("Parle Biscuits", "PARLE-BISCUIT-016", 180, 15),
        ("Sunfeast Marie", "SUNF-MARIE-017", 180, 15),
        ("Britannia Rusk", "BRIT-RUSK-018", 90, 10),
        ("The Baker's Dozen Croissant", "BAKER-CROISSANT-019", 14, 3),
        ("Oreo Biscuits", "OREO-BISCUIT-020", 365, 30),
        ("Hide & Seek Biscuits", "HIDE-SEEK-021", 180, 15),
        ("Good Day Biscuits", "GOODDAY-022", 180, 15),
    ],
    "Fresh Fruits": [
        ("Apple - Washington", "APPLE-WASH-023", 30, 7),
        ("Banana - Elaichi", "BANANA-ELA-024", 10, 3),
        ("Orange - Nagpur", "ORANGE-NAG-025", 21, 5),
        ("Mango - Alphonso", "MANGO-ALPH-026", 14, 4),
        ("Grapes - Black", "GRAPES-BLK-027", 10, 3),
        ("Pomegranate", "POMEGRANATE-028", 21, 5),
        ("Watermelon", "WATERMELON-029", 14, 4),
        ("Kiwi", "KIWI-030", 21, 5),
        ("Strawberry", "STRAWBERRY-031", 7, 2),
        ("Papaya", "PAPAYA-032", 10, 3),
    ],
    "Fresh Vegetables": [
        ("Tomato", "TOMATO-033", 10, 3),
        ("Onion", "ONION-034", 30, 7),
        ("Potato", "POTATO-035", 30, 7),
        ("Spinach", "SPINACH-036", 5, 2),
        ("Carrot", "CARROT-037", 21, 5),
        ("Broccoli", "BROCCOLI-038", 10, 3),
        ("Capsicum", "CAPSICUM-039", 10, 3),
        ("Cabbage", "CABBAGE-040", 14, 4),
        ("Cauliflower", "CAULIFLOWER-041", 10, 3),
        ("Brinjal", "BRINJAL-042", 10, 3),
    ],
    "Meat & Seafood": [
        ("Chicken Breast", "CHICKEN-BRST-043", 7, 2),
        ("Chicken Curry Cut", "CHICKEN-CURRY-044", 7, 2),
        ("Mutton Curry Cut", "MUTTON-CURRY-045", 7, 2),
        ("Prawns", "PRAWNS-046", 7, 2),
        ("Fish - Rohu", "FISH-ROHU-047", 7, 2),
        ("Eggs - Hen", "EGGS-HEN-048", 30, 5),
        ("Sausages", "SAUSAGES-049", 45, 10),
        ("Chicken Nuggets", "NUGGETS-050", 90, 15),
    ],
    "Frozen Foods": [
        ("Mother Dairy Ice Cream", "ICECREAM-MD-051", 180, 30),
        ("Vadilal Ice Cream", "ICECREAM-VAD-052", 180, 30),
        ("Frozen Paratha", "PARATHA-FROZ-053", 90, 15),
        ("Frozen Peas", "PEAS-FROZ-054", 180, 30),
        ("Frozen Corn", "CORN-FROZ-055", 180, 30),
        ("Frozen Pizza", "PIZZA-FROZ-056", 120, 20),
        ("Frozen Fries", "FRIES-FROZ-057", 180, 30),
    ],
    "Beverages - Cold": [
        ("Coca Cola", "COKE-058", 180, 30),
        ("Pepsi", "PEPSI-059", 180, 30),
        ("Sprite", "SPRITE-060", 180, 30),
        ("Real Fruit Juice", "REAL-JUICE-061", 90, 15),
        ("Tropicana Juice", "TROPICANA-062", 90, 15),
        ("Paper Boat Drink", "PAPERBOAT-063", 120, 20),
        ("Thums Up", "THUMSUP-064", 180, 30),
        ("Frooti", "FROOTI-065", 120, 20),
    ],
    "Beverages - Hot": [
        ("Tata Tea", "TATA-TEA-066", 365, 30),
        ("Red Label Tea", "REDLABEL-067", 365, 30),
        ("Bru Coffee", "BRU-COFFEE-068", 365, 30),
        ("Nescafe", "NESCAFE-069", 365, 30),
        ("Green Tea", "GREENTEA-070", 365, 30),
        ("Masala Chai", "MASALA-CHAI-071", 365, 30),
    ],
    "Snacks & Chips": [
        ("Lays Chips", "LAYS-072", 180, 30),
        ("Kurkure", "KURKURE-073", 180, 30),
        ("Pringles", "PRINGLES-074", 180, 30),
        ("Haldiram's Namkeen", "HALDIRAM-075", 180, 30),
        ("Doritos", "DORITOS-076", 180, 30),
        ("Cheetos", "CHEETOS-077", 180, 30),
        ("Bingo Chips", "BINGO-078", 180, 30),
    ],
    "Chocolates & Candy": [
        ("Dairy Milk", "DAIRYMILK-079", 365, 30),
        ("KitKat", "KITKAT-080", 365, 30),
        ("Munch", "MUNCH-081", 365, 30),
        ("5 Star", "5STAR-082", 365, 30),
        ("Perk", "PERK-083", 365, 30),
        ("Cadbury Gems", "GEMS-084", 365, 30),
        ("Eclairs", "ECLAIRS-085", 365, 30),
    ],
    "Breakfast Cereals": [
        ("Kellogg's Cornflakes", "KELLOG-CORN-086", 365, 30),
        ("Kellogg's Chocos", "KELLOG-CHOCOS-087", 365, 30),
        ("Quaker Oats", "QUAKER-OATS-088", 365, 30),
        ("Muesli", "MUESLI-089", 365, 30),
        ("Upma Mix", "UPMA-MIX-090", 180, 30),
        ("Poha", "POHA-091", 180, 30),
    ],
    "Cooking Essentials": [
        ("Fortune Oil", "FORTUNE-OIL-092", 365, 30),
        ("Saffola Oil", "SAFFOLA-OIL-093", 365, 30),
        ("Tata Salt", "TATA-SALT-094", 730, 60),
        ("MDH Masala", "MDH-MASALA-095", 365, 30),
        ("Everest Masala", "EVEREST-096", 365, 30),
        ("Aashirvaad Atta", "AASHIRVAAD-097", 180, 30),
        ("Daawat Rice", "DAAWAT-RICE-098", 365, 30),
    ],
    "Ready to Eat": [
        ("Maggi Noodles", "MAGGI-099", 180, 30),
        ("Top Ramen", "TOPRAMEN-100", 180, 30),
        ("MTR Ready Meal", "MTR-MEAL-101", 180, 30),
        ("Haldiram's Chole", "HALDIRAM-CHOLE-102", 180, 30),
        ("Knorr Soup", "KNORR-SOUP-103", 180, 30),
    ],
    "Pasta & Noodles": [
        ("Barilla Pasta", "BARILLA-104", 365, 30),
        ("Maggi Pasta", "MAGGI-PASTA-105", 180, 30),
        ("Yippee Noodles", "YIPPEE-106", 180, 30),
        ("Wai Wai Noodles", "WAIWAI-107", 180, 30),
    ],
    "Sauces & Condiments": [
        ("Maggi Ketchup", "MAGGI-KETCHUP-108", 365, 30),
        ("Kissan Ketchup", "KISSAN-109", 365, 30),
        ("Heinz Mayo", "HEINZ-MAYO-110", 180, 30),
        ("Ching's Sauce", "CHINGS-111", 365, 30),
        ("Schezwan Chutney", "SCHZ-CHUTNEY-112", 365, 30),
    ],
    "Canned & Packaged": [
        ("Tuna Canned", "TUNA-CAN-113", 730, 60),
        ("Baked Beans", "BEANS-CAN-114", 730, 60),
        ("Corn Canned", "CORN-CAN-115", 730, 60),
        ("Mushroom Canned", "MUSH-CAN-116", 730, 60),
    ],
    "Health & Nutrition": [
        ("Protein Bar", "PROTEIN-BAR-117", 180, 30),
        ("Boost", "BOOST-118", 365, 30),
        ("Horlicks", "HORLICKS-119", 365, 30),
        ("Complan", "COMPLAN-120", 365, 30),
        ("Protinex", "PROTINEX-121", 365, 30),
    ],
    "Baby Food": [
        ("Cerelac", "CERELAC-122", 365, 30),
        ("Nestlé Lactogen", "LACTOGEN-123", 365, 30),
        ("Baby Puree", "BABY-PUREE-124", 180, 30),
        ("Farex", "FAREX-125", 365, 30),
    ],
    "Organic & Health Foods": [
        ("Organic Rice", "ORGANIC-RICE-126", 365, 30),
        ("Quinoa", "QUINOA-127", 365, 30),
        ("Millets", "MILLETS-128", 365, 30),
        ("Organic Honey", "ORGANIC-HONEY-129", 730, 60),
        ("Chia Seeds", "CHIA-SEEDS-130", 365, 30),
    ],
    "Sweets & Desserts": [
        ("Gulab Jamun Mix", "GULABJAMUN-131", 180, 30),
        ("Rasgulla", "RASGULLA-132", 60, 15),
        ("Soan Papdi", "SOANPAPDI-133", 180, 30),
        ("Kaju Katli", "KAJUKATLI-134", 180, 30),
        ("Mysore Pak", "MYSOREPAK-135", 180, 30),
    ],
    "Pickles & Preserves": [
        ("Mango Pickle", "MANGO-PICKLE-136", 365, 30),
        ("Mixed Pickle", "MIXED-PICKLE-137", 365, 30),
        ("Lemon Pickle", "LEMON-PICKLE-138", 365, 30),
        ("Kissan Jam", "KISSAN-JAM-139", 365, 30),
        ("Honey", "HONEY-140", 730, 60),
    ],
    "Spreads & Dips": [
        ("Peanut Butter", "PENUT-BUTTER-141", 365, 30),
        ("Nutella", "NUTELLA-142", 365, 30),
        ("Hummus", "HUMMUS-143", 60, 15),
        ("Cream Cheese", "CREAM-CHEESE-144", 90, 15),
        ("Chocolate Spread", "CHOC-SPREAD-145", 365, 30),
    ],
    "Indian Grocery": [
        ("Basmati Rice", "BASMATI-146", 365, 30),
        ("Toor Dal", "TOOR-DAL-147", 365, 30),
        ("Chana Dal", "CHANA-DAL-148", 365, 30),
        ("Besan", "BESAN-149", 365, 30),
        ("Poha", "POHA-150", 180, 30),
        ("Idli Mix", "IDLI-MIX-151", 180, 30),
        ("Dosa Mix", "DOSA-MIX-152", 180, 30),
    ],
    "International Cuisine": [
        ("Pizza Base", "PIZZA-BASE-153", 90, 15),
        ("Pasta Sauce", "PASTA-SAUCE-154", 365, 30),
        ("Taco Kit", "TACO-KIT-155", 180, 30),
        ("Sushi Nori", "SUSHI-NORI-156", 365, 30),
        ("Kimchi", "KIMCHI-157", 90, 15),
    ]
}

def add_sample_products():
    """Add all sample products to database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    today = datetime.now().date()
    added_count = 0
    skipped_count = 0
    
    for category, products in products_data.items():
        for product in products:
            name, batch_prefix, shelf_life_days, buffer_days = product
            
            # Generate random manufacturing date (between 1 and 60 days ago)
            days_ago = random.randint(1, 60)
            mfg_date = today - timedelta(days=days_ago)
            
            # Expiry date = manufacturing date + shelf life days
            expiry_date = mfg_date + timedelta(days=shelf_life_days)
            
            # Check if batch ID already exists
            cursor.execute("SELECT id FROM products WHERE batch_id = ?", (batch_prefix,))
            if cursor.fetchone():
                skipped_count += 1
                continue
            
            # Insert product
            cursor.execute('''
                INSERT INTO products (product_name, batch_id, category, mfg_date, expiry_date, storage_instructions)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, batch_prefix, category, mfg_date, expiry_date, "Store as per instructions on package"))
            
            added_count += 1
            print(f"✅ Added: {name} | Batch: {batch_prefix} | Category: {category} | Expires in {shelf_life_days} days")
    
    conn.commit()
    conn.close()
    
    print("\n" + "="*60)
    print(f"📊 SUMMARY:")
    print(f"   ✅ Added: {added_count} products")
    print(f"   ⏭️ Skipped (duplicate): {skipped_count} products")
    print(f"   📦 Total categories: {len(products_data)}")
    print("="*60)
    return added_count

if __name__ == "__main__":
    print("="*60)
    print("🍎 FRESHSCAN - ADDING 150+ REAL PRODUCTS")
    print("="*60)
    print("\n📋 Categories being added:")
    for cat in products_data.keys():
        print(f"   - {cat} ({len(products_data[cat])} products)")
    
    print("\n⏳ Adding products to database...\n")
    add_sample_products()
    print("\n✅ Done! You can now view all products in the admin panel.")