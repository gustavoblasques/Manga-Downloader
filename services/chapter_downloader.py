import os
import requests

def create_folder_download(manga_title, chapter_num, chapter_name, chapter_links):
    # 1. Limpeza básica de nomes (evita caracteres proibidos pelo Windows/Linux)
    safe_manga_title = "".join([c if c.isalnum() else "_" for c in manga_title])
    
    # 2. Caminho estruturado: Mangás / Título / Num - Nome
    base_folder = "Mangás"
    manga_path = os.path.join(base_folder, safe_manga_title)
    chapter_path = os.path.join(manga_path, f"{chapter_num} - {chapter_name}")
    
    os.makedirs(chapter_path, exist_ok=True)
    
    print(f"Baixando para: {chapter_path}")
    
    for counter, link in enumerate(chapter_links, start=1):
        r = requests.get(link)
        
        # Identifica a extensão (assume que a url termina em .jpg, .png, etc)
        # Se o link não tiver a extensão, você pode forçar .jpg (comum no Mangadex)
        extension = os.path.splitext(link)[1] 
        if not extension:
            extension = ".jpg"
            
        file_name = f"{counter:03d}{extension}" # Ex: 001.jpg, 002.jpg
        file_path = os.path.join(chapter_path, file_name)
        
        with open(file_path, mode="wb") as f:
            f.write(r.content)

    print(f"Download concluído: {len(chapter_links)} páginas.")