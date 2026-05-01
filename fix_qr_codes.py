# fix_qr_codes.py
import sqlite3
import qrcode
import os

DB_PATH = "freshscan.db"
QR_FOLDER = "static/qr_codes"

# YOUR NGROK URL - COPY PASTED FROM ABOVE
NGROK_URL = "https://mouldier-quintin-folksily.ngrok-free.dev"

os.makedirs(QR_FOLDER, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT id, product_name FROM products")
products = cursor.fetchall()

print(f"📊 Generating QR codes for {len(products)} products...")
print("="*50)
print(f"🔗 Using URL: {NGROK_URL}")
print("="*50)

for product in products:
    product_id = product[0]
    product_name = product[1]
    
    url = f"{NGROK_URL}/product/{product_id}"
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{QR_FOLDER}/product_{product_id}.png")
    
    print(f"✅ QR for {product_name} → {url}")

conn.close()
print("="*50)
print(f"✅ Generated {len(products)} QR codes in {QR_FOLDER}/")
print("\n📱 Now scan any QR code with your phone camera!")