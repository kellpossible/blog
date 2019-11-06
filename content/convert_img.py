import os, csv

matches = []

pattern = r"[!]\[(.*)\]\(/(.*)\)"
replacement = "{{ img(path="{2}", caption="{1}") }}"

for root, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename.endswith(".md"):
            matches.append(os.path.join(root, filename))

    
