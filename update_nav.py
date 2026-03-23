import glob, os

files = glob.glob("/Users/sf/aamirbeading.com/www.aamirbeading.com/*.html")
target = "<li><a href=\"runway.html\" data-page=\"runway\">Runway</a></li>"
replacement = target + "\n        <li><a href=\"team.html\" data-page=\"team\">Team</a></li>"

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "<li><a href=\"team.html\"" not in content and target in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
