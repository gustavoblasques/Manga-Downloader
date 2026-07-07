import json
import os

log_file = "Download_Log.json"

def check_log():
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            json.dump({}, f)

def load_log():
    check_log()
    with open(log_file, "r") as f:
        return json.load(f)

def register_download_log(manga_id, chapter_id):
    log = load_log()

    if manga_id not in log:
        log[manga_id] = []

    if chapter_id not in log[manga_id]:
        log[manga_id].append(chapter_id)

    with open(log_file, 'w') as f:
        json.dump(log, f, indent=4)
        print(f"Capítulo {chapter_id} adicionado ao log.")