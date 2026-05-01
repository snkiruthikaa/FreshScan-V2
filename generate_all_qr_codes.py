# generate_all_qr_codes.py
import sqlite3
import qrcode
import os

DB_PATH = "freshscan.db"
QR_FOLDER = "static/qr_codes"

# 🔴 IMPORTANT: Change this to YOUR ngrok URL
NGROK_URL = "https://YOUR_NGROK_URL.ngrok-free.dev"  # ← REPLACE THIS!

def generate_qr_for_all_products():
    """Generate QR codes for every product using ngrok URL"""
    
    # Create QR folder if not exists
    os.makedirs(QR_FOLDER, exist_ok=True)
    
    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get all products
    cursor.execute("SELECT id, product_name, batch_id FROM products")
    products = cursor.fetchall()
    
    print(f"📊 Found {len(products)} products in database")
    print(f"🔗 Using URL: {NGROK_URL}")
    print("="*50)
    
    generated = 0
    failed = 0
    
    for product in products:
        product_id = product[0]
        product_name = product[1]
        
        # Create URL using ngrok (NOT localhost!)
        url = f"{NGROK_URL}/product/{product_id}"
        
        try:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4
            )
            qr.add_data(url)
            qr.make(fit=True)
            
            # Create image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save QR code
            qr_path = os.path.join(QR_FOLDER, f"product_{product_id}.png")
            img.save(qr_path)
            
            generated += 1
            print(f"✅ QR for {product_name} → {url}")
            
        except Exception as e:
            failed += 1
            print(f"❌ Failed for {product_name}: {e}")
    
    conn.close()
    
    print("="*50)
    print(f"📊 SUMMARY:")
    print(f"   ✅ QR Codes Generated: {generated}")
    print(f"   🔗 URL used: {NGROK_URL}")
    print("="*50)

if __name__ == "__main__":
    print("="*50)
    print("🔲 GENERATING QR CODES WITH NGORK URL")
    print("="*50)
    
    # Show warning
    if "YOUR_NGROK_URL" in NGROK_URL:
        print("⚠️ WARNING: You haven't updated the NGROK_URL!")
        print("   Please edit this file and add your actual ngrok URL.")
        print("   Example: NGROK_URL = 'https://abc123.ngrok-free.dev'")
        print("\n❌ QR codes will NOT work until you update the URL!")
    else:
        generate_qr_for_all_products()