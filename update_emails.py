import glob, os

files = glob.glob("/Users/sf/aamirbeading.com/www.aamirbeading.com/*.html")
for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "@farruch.com" in content:
        content = content.replace("@farruch.com", "@farruch.co")
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")

