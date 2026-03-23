import glob, re

files = glob.glob("/Users/sf/aamirbeading.com/www.aamirbeading.com/collection-*.html")
for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # regex to find the main collection image
    # Note: <img src="images/..." alt="..." class="collection-image">
    match = re.search(r'<img src="(images/[^"]+)" alt="[^"]*" class="collection-image"', content)
    if match:
        img_path = match.group(1)
        # replace banner03.jpg with the specific image
        new_content = re.sub(r"url\('images/banner03\.jpg'\)", f"url('{img_path}')", content)
        new_content = re.sub(r"rgba\(10,10,10,0\.4\), rgba\(10,10,10,0\.8\)", "rgba(5,5,5,0.7), rgba(5,5,5,0.9)", new_content) # darken slightly for legibility
        
        with open(f, "w") as file:
            file.write(new_content)
        print(f"Updated {f} to use {img_path}")
    else:
        print(f"Match not found in {f}")

