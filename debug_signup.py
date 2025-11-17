# # debug_signup.py
# import requests
# import json

# SUPABASE_URL = 'https://mhfxrhnmdhmmdlfvxjgt.supabase.co'
# SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1oZnhyaG5tZGhtbWRsZnZ4amd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjMyNjM1NzUsImV4cCI6MjA3ODgzOTU3NX0.g7RYA1lthHTEYF8QFLGMQVfgIIb1MnsHONYPIbNsEsE'

# def debug_signup():
#     print("🔧 DEBUG SIGNUP TEST - DIRECT API")
#     print("=" * 50)
    
#     # Test with different emails
#     test_emails = [
#         "testuser123@example.com",
#         "adan@gmail.com", 
#         "user@test.com",
#         "simple@email.com"
#     ]
    
#     for email in test_emails:
#         print(f"\n🧪 Testing: {email}")
        
#         test_data = {
#             "email": email,
#             "password": "password123"
#         }
        
#         headers = {
#             "Authorization": f"Bearer {SUPABASE_KEY}",
#             "Content-Type": "application/json",
#             "apikey": SUPABASE_KEY
#         }
        
#         try:
#             # Try signup
#             url = f"{SUPABASE_URL}/auth/v1/signup"
#             response = requests.post(url, json=test_data, headers=headers)
            
#             print(f"📤 Status: {response.status_code}")
            
#             if response.status_code == 200:
#                 user_data = response.json()
#                 print(f"✅ SUCCESS - User ID: {user_data['user']['id']}")
                
#                 # Try to delete test user (cleanup)
#                 try:
#                     delete_url = f"{SUPABASE_URL}/auth/v1/admin/users/{user_data['user']['id']}"
#                     delete_headers = {
#                         "Authorization": f"Bearer {SUPABASE_KEY}",
#                         "apikey": SUPABASE_KEY
#                     }
#                     delete_response = requests.delete(delete_url, headers=delete_headers)
#                     if delete_response.status_code == 200:
#                         print("✅ Cleanup: User deleted")
#                 except:
#                     print("⚠️ Could not cleanup user")
                    
#             else:
#                 error_data = response.json()
#                 print(f"❌ FAILED: {error_data.get('msg', error_data)}")
                
#         except Exception as e:
#             print(f"❌ ERROR: {e}")

# if __name__ == '__main__':
#     debug_signup()



# check_css_location.py
import os

def find_css_file():
    print("🔍 FINDING CSS FILE LOCATION...")
    
    # Check different possible locations
    locations = [
        'custom.css',                    # Root folder
        'static/css/custom.css',         # Correct static path
        '../static/css/custom.css',      # Relative path
        'static/custom.css',             # Wrong static path
        'css/custom.css',                # CSS folder only
    ]
    
    for location in locations:
        exists = os.path.exists(location)
        print(f"📁 {location}: {'✅ EXISTS' if exists else '❌ NOT FOUND'}")
        
        if exists:
            full_path = os.path.abspath(location)
            print(f"   📍 Full path: {full_path}")
    
    # Check if file is in root (same as app.py)
    root_files = [f for f in os.listdir('.') if f.endswith('.css')]
    print(f"\n🎨 CSS files in root folder: {root_files}")
    
    # Check static folder structure
    if os.path.exists('static'):
        static_contents = []
        for root, dirs, files in os.walk('static'):
            for file in files:
                static_contents.append(os.path.join(root, file))
        print(f"\n📁 Static folder contents: {static_contents}")

if __name__ == '__main__':
    find_css_file()