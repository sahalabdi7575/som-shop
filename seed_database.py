# #!/usr/bin/env python3
# """
# Database Seeding Script for SomaliShop E-commerce
# Run this script to populate your Supabase database with sample data
# """

# import os
# import sys
# from supabase import create_client
# from dotenv import load_dotenv
# import uuid
# from datetime import datetime, timedelta

# # Add the parent directory to Python path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # Load environment variables
# load_dotenv()

# def get_supabase_client():
#     """Initialize Supabase client"""
#     supabase_url = ('https://mhfxrhnmdhmmdlfvxjgt.supabase.co')
#     supabase_key =('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1oZnhyaG5tZGhtbWRsZnZ4amd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjMyNjM1NzUsImV4cCI6MjA3ODgzOTU3NX0.g7RYA1lthHTEYF8QFLGMQVfgIIb1MnsHONYPIbNsEsE')
    
#     if not supabase_url or not supabase_key:
#         print("Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
#         sys.exit(1)
    
#     return create_client(supabase_url, supabase_key)

# def seed_products(supabase):
#     """Seed products table with sample data"""
#     print("Seeding products...")
    
#     products = [
#         {
#             'id': str(uuid.uuid4()),
#             'name': 'Somali Cotton T-Shirt',
#             'slug': 'somali-cotton-t-shirt',
#             'description': 'High quality 100% cotton T-shirt featuring traditional Somali patterns. Comfortable, breathable, and perfect for everyday wear. Available in multiple sizes.',
#             'price': 12.00,
#             'image_url': '/static/images/placeholder.jpg',
#             'stock': 50,
#             'category': 'Clothing',
#             'created_at': datetime.utcnow().isoformat()
#         },
#         {
#             'id': str(uuid.uuid4()),
#             'name': 'Traditional Somali Coffee Set',
#             'slug': 'traditional-somali-coffee-set',
#             'description': 'Authentic Somali coffee set including ceramic jebena (coffee pot) and four matching cups. Perfect for traditional Somali coffee ceremonies and making authentic bun.',
#             'price': 45.00,
#             'image_url': '/static/images/placeholder.jpg',
#             'stock': 15,
#             'category': 'Home & Kitchen',
#             'created_at': datetime.utcnow().isoformat()
#         },
#         {
#             'id': str(uuid.uuid4()),
#             'name': 'Handwoven Basket (Large)',
#             'slug': 'handwoven-basket-large',
#             'description': 'Beautifully handwoven traditional Somali basket made from natural materials. Large size perfect for storage, decoration, or as a unique gift. Each piece is unique and crafted by skilled artisans.',
#             'price': 25.00,
#             'image_url': '/static/images/placeholder.jpg',
#             'stock': 20,
#             'category': 'Handicrafts',
#             'created_at': datetime.utcnow().isoformat()
#         },
#         {
#             'id': str(uuid.uuid4()),
#             'name': 'Organic Frankincense Pack',
#             'slug': 'organic-frankincense-pack',
#             'description': 'Premium grade organic frankincense (lubaan) sourced directly from Somalia. Known for its rich aroma and traditional uses. Perfect for meditation, relaxation, and cultural ceremonies.',
#             'price': 15.00,
#             'image_url': '/static/images/placeholder.jpg',
#             'stock': 100,
#             'category': 'Wellness',
#             'created_at': datetime.utcnow().isoformat()
#         },
#         {
#             'id': str(uuid.uuid4()),
#             'name': 'Leather Wallet',
#             'slug': 'leather-wallet',
#             'description': 'Durable genuine leather wallet with multiple card slots and cash compartment. Features traditional Somali craftsmanship and modern design elements.',
#             'price': 20.00,
#             'image_url': '/static/images/placeholder.jpg',
#             'stock': 30,
#             'category': 'Accessories',
#             'created_at': datetime.utcnow().isoformat()
#         },
#         {
#             'id': str(uuid.uuid4()),
#             'name': 'Somali Spice Collection',
#             'slug': 'somali-spice-collection',
#             'description': 'Curated collection of authentic Somali spices including xawaash, cumin, coriander, and cardamom. Perfect for creating traditional Somali dishes at home.',
#             'price': 18.00,
#             'image_url': '/static/images/placeholder.jpg',
#             'stock': 40,
#             'category': 'Food & Spices',
#             'created_at': datetime.utcnow().isoformat()
#         }
#     ]
    
#     for product in products:
#         try:
#             response = supabase.table('products').insert(product).execute()
#             if response.data:
#                 print(f"✓ Added: {product['name']}")
#             else:
#                 print(f"✗ Failed to add: {product['name']}")
#         except Exception as e:
#             print(f"✗ Error adding {product['name']}: {e}")
    
#     print("Product seeding completed!")

# def seed_sample_orders(supabase):
#     """Seed sample orders for demonstration"""
#     print("Seeding sample orders...")
    
#     # Create a test user profile (user should exist in Auth first)
#     test_user_id = str(uuid.uuid4())
#     user_data = {
#         'id': test_user_id,
#         'email': 'test@example.com',
#         'full_name': 'Test Customer',
#         'created_at': datetime.utcnow().isoformat()
#     }
    
#     try:
#         supabase.table('users').insert(user_data).execute()
#         print("✓ Added test user")
#     except Exception as e:
#         print(f"Note: Test user might already exist: {e}")
    
#     # Get some products to create orders
#     products_response = supabase.table('products').select('id, price').limit(3).execute()
#     if not products_response.data:
#         print("No products found to create sample orders")
#         return
    
#     # Create sample order
#     order_id = str(uuid.uuid4())
#     order_data = {
#         'id': order_id,
#         'user_id': test_user_id,
#         'total_amount': 57.00,
#         'status': 'completed',
#         'payment_status': 'paid',
#         'customer_phone': '+252612345678',
#         'merchant_number_used': '+2520907251291',
#         'created_at': (datetime.utcnow() - timedelta(days=5)).isoformat()
#     }
    
#     try:
#         supabase.table('orders').insert(order_data).execute()
#         print("✓ Added sample order")
        
#         # Add order items
#         order_items = []
#         for i, product in enumerate(products_response.data[:2]):
#             order_items.append({
#                 'id': str(uuid.uuid4()),
#                 'order_id': order_id,
#                 'product_id': product['id'],
#                 'quantity': i + 1,
#                 'price': product['price'],
#                 'created_at': (datetime.utcnow() - timedelta(days=5)).isoformat()
#             })
        
#         for item in order_items:
#             supabase.table('order_items').insert(item).execute()
        
#         print("✓ Added sample order items")
        
#     except Exception as e:
#         print(f"Error creating sample order: {e}")

# def check_existing_data(supabase):
#     """Check if data already exists"""
#     print("Checking existing data...")
    
#     products_response = supabase.table('products').select('id').execute()
#     if products_response.data:
#         print(f"Found {len(products_response.data)} existing products")
#         return True
    
#     return False

# def main():
#     """Main seeding function"""
#     print("=== SomaliShop Database Seeding ===")
    
#     supabase = get_supabase_client()
    
#     # Check if data already exists
#     if check_existing_data(supabase):
#         response = input("Data already exists. Do you want to reseed? (y/N): ")
#         if response.lower() != 'y':
#             print("Seeding cancelled.")
#             return
    
#     try:
#         # Seed products
#         seed_products(supabase)
        
#         # Seed sample orders
#         seed_sample_orders(supabase)
        
#         print("\n=== Seeding Completed Successfully ===")
#         print("Sample data has been added to your database.")
#         print("You can now access the admin panel with:")
#         print("Email: daymaro94@gmail.com")
#         print("Password: 12345678")
        
#     except Exception as e:
#         print(f"Seeding failed: {e}")
#         sys.exit(1)

# if __name__ == '__main__':
#     main()