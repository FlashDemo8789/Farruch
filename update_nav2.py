import glob, re

files = glob.glob("/Users/sf/aamirbeading.com/www.aamirbeading.com/*.html")
for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We want to insert the Team link right after the Runway link
    if 'data-page="team"' not in content:
        # Re-substitute
        new_content = re.sub(
            r'(<li><a href="runway\.html" data-page="runway">Runway</a></li>)',
            r'\1\n        <li><a href="team.html" data-page="team">Team</a></li>',
            content
        )
        if new_content != content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
