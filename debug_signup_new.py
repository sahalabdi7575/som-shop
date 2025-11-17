# debug_signup_new.py
import requests
import random
import string

SUPABASE_URL = 'https://mhfxrhnmdhmmdlfvxjgt.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1oZnhyaG5tZGhtbWRsZnZ4amd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjMyNjM1NzUsImV4cCI6MjA3ODgzOTU3NX0.g7RYA1lthHTEYF8QFLGMQVfgIIb1MnsHONYPIbNsEsE'

def generate_random_email():
    """Generate random email for testing"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test{random_string}@example.com"

def debug_signup_new():
    print("🔧 DEBUG SIGNUP TEST - NEW EMAILS")
    print("=" * 50)
    
    # Generate 3 random emails
    test_emails = [generate_random_email() for _ in range(3)]
    
    for email in test_emails:
        print(f"\n🧪 Testing NEW email: {email}")
        
        test_data = {
            "email": email,
            "password": "password123"
        }
        
        headers = {
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "apikey": SUPABASE_KEY
        }
        
        try:
            # Try signup
            url = f"{SUPABASE_URL}/auth/v1/signup"
            response = requests.post(url, json=test_data, headers=headers)
            
            print(f"📤 Status: {response.status_code}")
            
            if response.status_code == 200:
                user_data = response.json()
                print(f"✅ SUCCESS - User ID: {user_data['user']['id']}")
                print("🎉 SIGNUP IS WORKING! The problem was duplicate emails.")
                return True
            else:
                error_data = response.json()
                print(f"❌ FAILED: {error_data.get('msg', error_data)}")
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
    
    return False

if __name__ == '__main__':
    success = debug_signup_new()
    if success:
        print("\n🎯 SOLUTION: Use NEW email addresses that haven't been registered before!")
    else:
        print("\n🔧 The issue might be in your Supabase Auth configuration.")