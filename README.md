# 🍎 FreshScan - Digital Food Expiry Tracker

**Scan Safe, Eat Fresh** - A QR-based digital food expiry tracking system for quick commerce platforms.

---

## 📱 About the Project

FreshScan solves the problem of expired product delivery by providing a digital expiry tracking system using QR codes. When customers receive products, they can scan the QR code to instantly check if the product is safe, near expiry, or expired.

**Target Platforms:** Zepto, Swiggy Instamart, Blinkit, BigBasket

---

## ✨ Features

- ✅ Complete CRUD Operations (Add, Edit, Delete Products)
- ✅ QR Code Generation for each product/batch
- ✅ Real-time Expiry Calculation (Safe/Near Expiry/Expired)
- ✅ Mobile-Friendly - No app needed, works with phone camera
- ✅ Admin Dashboard with Pagination (15 products per page)
- ✅ Search by Batch ID
- ✅ Filter by Status (Safe/Near Expiry/Expired)
- ✅ CSV Export for Reporting
- ✅ Print QR Labels
- ✅ Color-coded Status (🟢 Green / 🟡 Yellow / 🔴 Red)
- ✅ Works on any WiFi (ngrok integration)

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | Python Flask |
| Database | SQLite with sqlite3 |
| QR Generation | qrcode + Pillow |
| Frontend | HTML5, CSS3, JavaScript |
| Tunneling | ngrok (for mobile scanning) |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone repository
git clone https://github.com/snkiruthikaa/FreshScan-V2.git
cd FreshScan-V2

# Install dependencies
pip install -r requirements.txt

# Initialize database
python database.py

# Run the application
python app.py
