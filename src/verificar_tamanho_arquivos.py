import os

root_dir = r"f:\PROJETOS\ARTEFATO"
large_files = []
total_size = 0
file_count = 0

for root, dirs, files in os.walk(root_dir):
    # Ignorar .git se existir
    if ".git" in dirs:
        dirs.remove(".git")
    for f in files:
        file_path = os.path.join(root, f)
        try:
            sz = os.path.getsize(file_path)
            total_size += sz
            file_count += 1
            if sz > 25 * 1024 * 1024: # > 25 MB
                rel_path = os.path.relpath(file_path, root_dir)
                large_files.append((rel_path, sz / (1024 * 1024)))
        except Exception as e:
            pass

print(f"Total de arquivos: {file_count}")
print(f"Tamanho total: {total_size / (1024 * 1024):.2f} MB")
print("\nArquivos maiores que 25MB:")
for p, s in large_files:
    print(f"  {p} ({s:.2f} MB)")
