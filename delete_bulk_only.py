# delete_bulk_only.py
import sqlite3

DB_PATH = "freshscan.db"

# These are the batch ID prefixes from the bulk products
bulk_prefixes = [
    "AMUL-MILK", "MOTHER-CURD", "NESTLE-YOG", "BRIT-CHEESE", "EGGOZ-EGG",
    "BRIT-BREAD", "MODERN-BREAD", "PARLE-BISCUIT", "SUNF-MARIE", "OREO-BISCUIT",
    "APPLE-WASH", "BANANA-ELA", "ORANGE-NAG", "MANGO-ALPH", "GRAPES-BLK",
    "TOMATO-033", "ONION-034", "POTATO-035", "SPINACH-036", "CARROT-037",
    "CHICKEN-BRST", "MUTTON-CURRY", "PRAWNS-046", "ICECREAM-MD", "PARATHA-FROZ",
    "COKE-058", "PEPSI-059", "TATA-TEA", "BRU-COFFEE", "LAYS-072", "KURKURE-073",
    "DAIRYMILK-079", "KITKAT-080", "KELLOG-CORN", "MAGGI-099", "BARILLA-104"
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for prefix in bulk_prefixes:
    cursor.execute("DELETE FROM products WHERE batch_id LIKE ?", (f"{prefix}%",))

conn.commit()
deleted = cursor.rowcount
conn.close()

print(f"✅ Deleted {deleted} bulk products")
print("✅ Your original products are still there!")