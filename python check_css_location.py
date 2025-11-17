# # check_css_location.py
# import os

# def find_css_file():
#     print("🔍 FINDING CSS FILE LOCATION...")
    
#     # Check different possible locations
#     locations = [
#         'custom.css',                    # Root folder
#         'static/css/custom.css',         # Correct static path
#         '../static/css/custom.css',      # Relative path
#         'static/custom.css',             # Wrong static path
#         'css/custom.css',                # CSS folder only
#     ]
    
#     for location in locations:
#         exists = os.path.exists(location)
#         print(f"📁 {location}: {'✅ EXISTS' if exists else '❌ NOT FOUND'}")
        
#         if exists:
#             full_path = os.path.abspath(location)
#             print(f"   📍 Full path: {full_path}")
    
#     # Check if file is in root (same as app.py)
#     root_files = [f for f in os.listdir('.') if f.endswith('.css')]
#     print(f"\n🎨 CSS files in root folder: {root_files}")
    
#     # Check static folder structure
#     if os.path.exists('static'):
#         static_contents = []
#         for root, dirs, files in os.walk('static'):
#             for file in files:
#                 static_contents.append(os.path.join(root, file))
#         print(f"\n📁 Static folder contents: {static_contents}")
# if __name__ == '__main__':
#     find_css_file()