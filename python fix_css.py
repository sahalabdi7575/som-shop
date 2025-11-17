# # fix_css.py
# import os
# import shutil

# def fix_css():
#     print("🛠️ FIXING CSS LOCATION...")
    
#     # Check if CSS exists in root
#     if os.path.exists('custom.css'):
#         print("✅ Found custom.css in root folder")
        
#         # Create static/css directories if they don't exist
#         os.makedirs('static/css', exist_ok=True)
#         print("✅ Created static/css folder")
        
#         # Copy CSS to correct location
#         shutil.copy2('custom.css', 'static/css/custom.css')
#         print("✅ Copied custom.css to static/css/custom.css")
        
#         # Verify the copy worked
#         if os.path.exists('static/css/custom.css'):
#             print("✅ Verification: CSS file successfully moved!")
            
#             # Show new location
#             new_path = os.path.abspath('static/css/custom.css')
#             print(f"📍 CSS is now at: {new_path}")
#             return True
#         else:
#             print("❌ Failed to move CSS file")
#             return False
#     else:
#         print("❌ custom.css not found in root folder")
#         return False

# if __name__ == '__main__':
#     success = fix_css()
#     if success:
#         print("\n🎉 CSS LOCATION FIXED SUCCESSFULLY!")
#         print("🔄 Please RESTART your Flask app and test the website!")
#     else:
#         print("\n❌ Could not fix CSS location.")