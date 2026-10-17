import os
import re

folder = 'video'

for file in os.listdir(folder):
    if not file.endswith('.mp4'):
        continue

    # # ke baad number nikalo jaise #3 -> 3
    match_num = re.search(r'#(\d+)', file)
    # Title nikalo __ se pehle wala
    match_title = re.search(r'^(.*?)__Sigma', file)

    if not match_num:
        continue

    num = int(match_num.group(1))

    if match_title:
        title = match_title.group(1) # Basic_Structure_of_an_HTML_Website
        title = title.replace('__', ' ').strip()
        # Clean title: _ ko space me badal de, extra underscore hata de
        title = re.sub(r'_+', ' ', title).strip()
    else:
        title = f"Tutorial"

    # Naya naam: 01_Basic Structure of an HTML Website.mp4
    new_name = f"{num:02d}_{title}.mp4"
    
    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, new_name)

    if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")

print("Done! Clean ho gaya")