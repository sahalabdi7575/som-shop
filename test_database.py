# # test_database.py
# from supabase import create_client
# import os

# SUPABASE_URL = 'https://mhfxrhnmdhmmdlfvxjgt.supabase.co'
# SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1oZnhyaG5tZGhtbWRsZnZ4amd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjMyNjM1NzUsImV4cCI6MjA3ODgzOTU3NX0.g7RYA1lthHTEYF8QFLGMQVfgIIb1MnsHONYPIbNsEsE'

# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# def test_products_table():
#     print("🧪 Testing Products Table...")
#     try:
#         # Test reading from products table
#         response = supabase.table('products').select('*').execute()
#         print(f"✅ Products table exists: {len(response.data)} products found")
        
#         # Test inserting into products table
#         test_product = {
#             'name': 'Test Product',
#             'slug': 'test-product-123',
#             'description': 'This is a test product',
#             'price': 10.00,
#             'stock': 5,
#             'category': 'Test',
#             'image_url': '/static/images/placeholder.jpg'
#         }
        
#         insert_response = supabase.table('products').insert(test_product).execute()
#         if insert_response.data:
#             print("✅ INSERT test: SUCCESS - Product added to database")
            
#             # Delete test product
#             product_id = insert_response.data[0]['id']
#             delete_response = supabase.table('products').delete().eq('id', product_id).execute()
#             print("✅ DELETE test: SUCCESS - Test product cleaned up")
#         else:
#             print("❌ INSERT test: FAILED - Could not add product")
            
#     except Exception as e:
#         print(f"❌ Database test FAILED: {e}")

# def test_admin_user():
#     print("\n🧪 Testing Admin User...")
#     try:
#         # Check if admin user exists
#         response = supabase.table('users').select('*').eq('email', 'daymaro94@gmail.com').execute()
#         if response.data:
#             print(f"✅ Admin user exists: {response.data[0]['email']}")
#         else:
#             print("❌ Admin user NOT found in database")
#     except Exception as e:
#         print(f"❌ Admin user test FAILED: {e}")

# if __name__ == '__main__':
#     print("🔍 DATABASE DIAGNOSTIC TOOL")
#     print("=" * 50)
#     test_products_table()
#     test_admin_user()