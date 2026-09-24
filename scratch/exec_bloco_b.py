import os

root_dir = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER"
replaced_files = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    if ".git" in dirpath:
        continue
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        # Check text files
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if "gmail.com" in content.lower() or "contato@colmeiastudiosacademy.com.br" in content.lower():
                new_content = content.replace("contato@colmeiastudiosacademy.com.br", "contato@colmeiastudiosacademy.com.br")
                new_content = new_content.replace("contato@colmeiastudiosacademy.com.br", "contato@colmeiastudiosacademy.com.br")
                new_content = new_content.replace("contato@colmeiastudiosacademy.com.br", "contato@colmeiastudiosacademy.com.br")
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                replaced_files.append(filepath)
        except Exception as e:
            pass

print(f"Replaced in {len(replaced_files)} files:")
for fp in replaced_files:
    print(fp)
