from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from datetime import datetime, timedelta
import database
import qr_generator
import config
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'freshscan-secret-key-2024'

# Initialize components
try:
    db = database.db
    print("✅ Database module loaded successfully")
except Exception as e:
    print(f"❌ Error loading database: {e}")
    db = None

try:
    qr = qr_generator.qr_gen
    print("✅ QR generator loaded successfully")
except Exception as e:
    print(f"❌ Error loading QR generator: {e}")
    qr = None

# ========================
# HELPER FUNCTIONS
# ========================

def is_first_time():
    """Check if this is first time setup (no products in database)"""
    if not db:
        return True
    try:
        conn, cursor = db.get_connection()
        cursor.execute('SELECT COUNT(*) FROM products')
        count = cursor.fetchone()[0]
        return count == 0
    except:
        return True

def get_first_product_id():
    """Get the first product ID from database, or create a sample if none exists"""
    if not db:
        return 1
    
    try:
        conn, cursor = db.get_connection()
        cursor.execute('SELECT id FROM products LIMIT 1')
        result = cursor.fetchone()
        
        if result:
            return result[0]
        else:
            # Create a sample product if no products exist
            sample_product = (
                "Sample Product", "SAMPLE-001", "General",
                datetime.now().strftime('%Y-%m-%d'),
                (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
                "Store in cool dry place"
            )
            product_id = db.add_product(sample_product)
            
            # Generate QR code for sample product
            if qr and product_id:
                qr.generate_qr(product_id, "Sample Product", "SAMPLE-001")
            
            return product_id if product_id else 1
    except Exception as e:
        print(f"Error getting first product: {e}")
        return 1

# ========================
# MAIN HOME ROUTE
# ========================

@app.route('/')
def home():
    """Beautiful homepage"""
    if not db:
        return redirect(url_for('setup'))
    
    try:
        conn, cursor = db.get_connection()
        cursor.execute('SELECT COUNT(*) FROM products')
        count = cursor.fetchone()[0]
        
        return render_template('homepage.html', 
                             config=config.Config,
                             products_count=count)
    except:
        return render_template('homepage.html', 
                             config=config.Config,
                             products_count=0)

# ========================
# LANDING PAGE
# ========================

@app.route('/landing')
def landing():
    """Landing page with options to go to admin or scan QR"""
    return render_template('landing.html', config=config.Config)

# ========================
# SETUP ROUTE
# ========================

@app.route('/setup')
def setup():
    """Initial setup page - first time users"""
    sample_product_id = get_first_product_id()
    return render_template('setup.html', 
                         config=config.Config,
                         sample_product_id=sample_product_id)

# ========================
# USER FACING ROUTES (QR SCANNING)
# ========================

@app.route('/product/<int:product_id>')
def show_product(product_id):
    """Main route - displays product expiry info when QR is scanned"""
    if not db:
        return "Database not initialized", 500
    
    try:
        product = db.get_product(product_id)
        
        if not product:
            return render_template('error.html', 
                                 message=f"Product ID {product_id} not found",
                                 error_code="404")
        
        # Unpack product data
        (prod_id, product_name, batch_id, category, 
         mfg_date, expiry_date, storage_instructions, added_date) = product
        
        # Calculate status
        status_info = db.calculate_status(expiry_date)
        
        # Format dates
        try:
            mfg_display = datetime.strptime(mfg_date, '%Y-%m-%d').strftime('%d %b %Y')
        except:
            mfg_display = mfg_date
        
        try:
            expiry_display = datetime.strptime(expiry_date, '%Y-%m-%d').strftime('%d %b %Y')
        except:
            expiry_display = expiry_date
        
        # Get category icon
        try:
            conn, cursor = db.get_connection()
            cursor.execute('SELECT icon FROM categories WHERE name = ?', (category,))
            result = cursor.fetchone()
            category_icon = result[0] if result else "📦"
        except:
            category_icon = "📦"
        
        return render_template('product.html',
                             product_id=product_id,
                             product_name=product_name,
                             batch_id=batch_id,
                             category=category,
                             category_icon=category_icon,
                             mfg_date=mfg_display,
                             expiry_date=expiry_display,
                             storage_instructions=storage_instructions,
                             remaining_days=status_info['remaining_days'],
                             status=status_info['status'],
                             color=status_info['color'],
                             icon=status_info['icon'],
                             brand_name=config.Config.BRAND_NAME,
                             tagline=config.Config.TAGLINE)
    except Exception as e:
        return render_template('error.html',
                             message=f"Error loading product: {str(e)}",
                             error_code="500")

# ========================
# ADMIN ROUTES WITH CRUD & SEARCH & PAGINATION
# ========================

@app.route('/admin')
def admin_dashboard():
    """Admin dashboard with batch search and pagination"""
    if not db:
        return "Database not initialized", 500
    
    try:
        # Get pagination parameters
        page = request.args.get('page', 1, type=int)
        per_page = 15  # Number of products per page
        
        # Get search parameter (only batch ID)
        search_batch = request.args.get('search_batch', '')
        
        # Get all products
        all_products = db.get_all_products()
        
        # Filter products based on batch search
        filtered_products = []
        if search_batch:
            for product in all_products:
                if search_batch.lower() in product[2].lower():
                    filtered_products.append(product)
        else:
            filtered_products = all_products
        
        # Calculate pagination
        total_products = len(filtered_products)
        total_pages = (total_products + per_page - 1) // per_page if total_products > 0 else 1
        
        # Ensure page is within range
        if page < 1:
            page = 1
        if page > total_pages and total_pages > 0:
            page = total_pages
        
        # Get products for current page
        start_idx = (page - 1) * per_page
        end_idx = min(start_idx + per_page, total_products)
        page_products = filtered_products[start_idx:end_idx]
        
        # Calculate status for each product on current page
        products_with_status = []
        for product in page_products:
            status_info = db.calculate_status(product[5])
            products_with_status.append({
                'id': product[0],
                'name': product[1],
                'batch': product[2],
                'category': product[3],
                'mfg_date': product[4],
                'expiry_date': product[5],
                'storage': product[6],
                'added_date': product[7],
                'icon': product[8] if len(product) > 8 else "📦",
                'status_info': status_info
            })
        
        stats = db.get_stats()
        
        return render_template('admin.html',
                             products=products_with_status,
                             stats=stats,
                             search_batch=search_batch,
                             page=page,
                             total_pages=total_pages,
                             total_products=total_products,
                             per_page=per_page,
                             config=config.Config)
    except Exception as e:
        return render_template('error.html',
                             message=f"Error loading admin panel: {str(e)}",
                             error_code="500")

@app.route('/admin/add', methods=['GET', 'POST'])
def add_product():
    """Add new product"""
    if not db:
        return "Database not initialized", 500
    
    try:
        if request.method == 'POST':
            # Get form data
            product_name = request.form['product_name']
            batch_id = request.form['batch_id']
            category = request.form['category']
            mfg_date = request.form['mfg_date']
            expiry_date = request.form['expiry_date']
            storage = request.form.get('storage_instructions', '')
            
            # Add to database
            product_id = db.add_product((
                product_name, batch_id, category, 
                mfg_date, expiry_date, storage
            ))
            
            if product_id:
                # Generate QR code
                if qr:
                    qr.generate_qr(product_id, product_name, batch_id)
                return jsonify({'success': True, 'product_id': product_id})
            else:
                return jsonify({'success': False, 'error': 'Batch ID already exists'})
        
        # Get categories for dropdown
        conn, cursor = db.get_connection()
        cursor.execute('SELECT name, icon FROM categories')
        categories = cursor.fetchall()
        
        # Default dates for demo
        today = datetime.now().strftime('%Y-%m-%d')
        next_week = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        
        return render_template('add_product.html',
                             categories=categories,
                             today=today,
                             next_week=next_week)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/admin/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    """Edit existing product"""
    if not db:
        return "Database not initialized", 500
    
    try:
        if request.method == 'POST':
            # Get form data
            product_name = request.form['product_name']
            batch_id = request.form['batch_id']
            category = request.form['category']
            mfg_date = request.form['mfg_date']
            expiry_date = request.form['expiry_date']
            storage = request.form.get('storage_instructions', '')
            
            # Update in database
            conn, cursor = db.get_connection()
            cursor.execute('''
                UPDATE products 
                SET product_name=?, batch_id=?, category=?, 
                    mfg_date=?, expiry_date=?, storage_instructions=?
                WHERE id=?
            ''', (product_name, batch_id, category, mfg_date, expiry_date, storage, product_id))
            conn.commit()
            
            # Regenerate QR code with new info
            if qr:
                qr.generate_qr(product_id, product_name, batch_id)
            
            return jsonify({'success': True, 'message': 'Product updated successfully'})
        
        # GET request - show edit form
        product = db.get_product(product_id)
        if not product:
            return "Product not found", 404
        
        # Get categories for dropdown
        conn, cursor = db.get_connection()
        cursor.execute('SELECT name, icon FROM categories')
        categories = cursor.fetchall()
        
        return render_template('edit_product.html',
                             product=product,
                             categories=categories)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/admin/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    """Delete product"""
    if not db:
        return jsonify({'success': False, 'error': 'Database not initialized'}), 500
    
    try:
        conn, cursor = db.get_connection()
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        
        # Delete QR code file if exists
        qr_path = f'static/qr_codes/product_{product_id}.png'
        if os.path.exists(qr_path):
            os.remove(qr_path)
        
        return jsonify({'success': True, 'message': 'Product deleted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/admin/generate-all-qr')
def generate_all_qr():
    """Generate QR codes for all products"""
    if not qr:
        return "QR generator not initialized", 500
    
    try:
        qr.generate_batch_qr_codes()
        return redirect(url_for('admin_dashboard'))
    except Exception as e:
        return render_template('error.html',
                             message=f"Error generating QR codes: {str(e)}",
                             error_code="500")

@app.route('/admin/export-csv')
def export_csv():
    """Export all products to CSV file"""
    if not db:
        return "Database not initialized", 500
    
    try:
        import csv
        import io
        from flask import make_response
        
        products = db.get_all_products()
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(['ID', 'Product Name', 'Batch ID', 'Category', 
                        'Manufacturing Date', 'Expiry Date', 'Storage Instructions', 
                        'Added Date', 'Status', 'Days Remaining'])
        
        for product in products:
            status_info = db.calculate_status(product[5])
            writer.writerow([
                product[0], product[1], product[2], product[3],
                product[4], product[5], product[6], product[7],
                status_info['status'], status_info['remaining_days']
            ])
        
        response = make_response(output.getvalue())
        response.headers['Content-Disposition'] = 'attachment; filename=freshscan_products.csv'
        response.headers['Content-type'] = 'text/csv'
        return response
        
    except Exception as e:
        return render_template('error.html',
                             message=f"Error exporting CSV: {str(e)}",
                             error_code="500")

# ========================
# CLOUD SUPPORT (QR Works Anywhere)
# ========================

@app.route('/set-public-url', methods=['POST'])
def set_public_url():
    """Set public URL for QR codes (for ngrok/cloud deployment)"""
    try:
        public_url = request.json.get('public_url', '')
        if public_url:
            config.Config.BASE_URL = public_url
            if qr:
                qr.base_url = public_url
            return jsonify({'success': True, 'url': public_url})
        return jsonify({'success': False, 'error': 'No URL provided'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get-public-url')
def get_public_url():
    """Get current public URL"""
    return jsonify({'public_url': config.Config.BASE_URL})

# ========================
# DEMO & TESTING ROUTES
# ========================

@app.route('/demo')
def demo():
    """Demo page for presentation"""
    return render_template('demo.html')

@app.route('/test/qr/<int:product_id>')
def test_qr(product_id):
    """Test QR code functionality"""
    if not db:
        return "Database not initialized", 500
    
    try:
        product = db.get_product(product_id)
        if not product:
            return f"Product {product_id} not found", 404
        
        qr_url = f"{config.Config.BASE_URL}/product/{product_id}"
        
        return f"""
        <h1>QR Test - Product {product_id}</h1>
        <p><strong>Name:</strong> {product[1]}</p>
        <p><strong>Batch:</strong> {product[2]}</p>
        <p><strong>QR URL:</strong> <a href="{qr_url}" target="_blank">{qr_url}</a></p>
        <img src="/static/qr_codes/product_{product_id}.png" width="300">
        <p><a href="/admin">← Admin</a> | <a href="/product/{product_id}">View Product →</a></p>
        """
    except Exception as e:
        return f"Error: {str(e)}", 500

# ========================
# ERROR HANDLERS
# ========================

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html',
                         message="The page you're looking for doesn't exist.",
                         error_code="404"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html',
                         message="Something went wrong on our end.",
                         error_code="500"), 500

# ========================
# APPLICATION STARTUP
# ========================

def setup_directories():
    """Ensure all required directories exist"""
    directories = ['static/qr_codes', 'static/images', 'templates']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

if __name__ == '__main__':
    setup_directories()
    
    print("=" * 50)
    print(f"🚀 {config.Config.BRAND_NAME} v{config.Config.VERSION}")
    print(f"📱 Server starting at: {config.Config.BASE_URL}")
    print("=" * 50)
    print("\n📊 Access Points:")
    print(f"🔗 Home/Landing: {config.Config.BASE_URL}/")
    print(f"🔗 Setup Guide: {config.Config.BASE_URL}/setup")
    print(f"🔗 Admin Panel: {config.Config.BASE_URL}/admin")
    print(f"🔗 Demo: {config.Config.BASE_URL}/demo")
    print(f"🔗 Sample Product: {config.Config.BASE_URL}/product/1")
    print("\n📱 **QR SCANNING:**")
    print("1. Go to /admin and generate QR codes")
    print("2. Print QR codes or show on screen")
    print("3. Scan QR with phone camera - works on any WiFi!")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=config.Config.PORT, debug=True)