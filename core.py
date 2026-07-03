import input_handler
from services.mangadex_api import buscar_id_por_titulo, manga_info, get_chapter_link, get_chapter_feed
from services.chapter_downloader import create_folder_download

titulo = input_handler.encontrar_nome_manga()
lista_busca = []


def manga_select(lista_busca):
    print("Os mangás encontrados foram:")

    for index, manga in enumerate(lista_busca):
        print(f"[{index + 1}] - {manga.title} - Autor: {manga.author}")
    escolha = int(input("Qual deseja baixar? \n"))
    manga_selecionado = lista_busca[escolha - 1]

    return manga_selecionado
 
ids_manga = buscar_id_por_titulo(titulo)

for id in ids_manga:
    lista_busca.append(manga_info(id))

manga_final = manga_select(lista_busca)
print(f"Você escolheu {manga_final.title}")

chapter_feed = get_chapter_feed(manga_final.manga_id)


input_chapters = input_handler.choose_chapters()
capitulos = []
for i in input_chapters:
    capitulos.append(chapter_feed[i - 1])


for cap in capitulos:
    print(cap.chapter_id)
    link = get_chapter_link(cap.chapter_id)
    print(f"Link do capítulo {cap.number}: {link}")
    create_folder_download(manga_final.title,cap.number,cap.title,link)
    break