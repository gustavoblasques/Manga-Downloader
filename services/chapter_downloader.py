import os
import requests
import re

def clean_name(name):
    if not name:
        return "Sem_Titulo"
    return re.sub(r'[\\/*?:"<>|]', '_', str(name)).strip()

def create_folder_download(manga_title, chapter_num, chapter_name, chapter_links):
    safe_manga_title = clean_name(manga_title)
    safe_chapter_name = clean_name(chapter_name)
    base_folder = "Mangás"
    manga_path = os.path.join(base_folder, safe_manga_title)
    chapter_path = os.path.join(manga_path, f"{chapter_num} - {safe_chapter_name}")
    
    os.makedirs(chapter_path, exist_ok=True)
    
    print(f"Baixando para: {chapter_path}")
    
    for counter, link in enumerate(chapter_links, start=1):
        r = requests.get(link)
        
        extension = os.path.splitext(link)[1] 
        if not extension:
            extension = ".jpg"
            
        file_name = f"{counter:03d}{extension}" 
        file_path = os.path.join(chapter_path, file_name)
        
        with open(file_path, mode="wb") as f:
            f.write(r.content)

    print(f"Download concluído: {len(chapter_links)} páginas.")