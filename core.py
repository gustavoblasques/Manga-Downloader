import input_handler
from services.mangadex_api import buscar_id_por_titulo, manga_info, get_chapter_link, get_chapter_feed
from services.chapter_downloader import create_folder_download
from services.log_manager import load_log, check_log, register_download_log
import sys



def main():
    while True:
        lista_busca = []
        log = load_log()
        try:
            welcome_option = input_handler.escolha_usuario_inicio()
            if welcome_option == 1:
                titulo = input_handler.encontrar_nome_manga()
                ids_manga = buscar_id_por_titulo(titulo)
                for id in ids_manga:
                    lista_busca.append(manga_info(id))
                manga_final = manga_select(lista_busca)
                print(f"Você escolheu {manga_final.title}")

                chapter_feed = get_chapter_feed(manga_final.manga_id)
                input_chapters = input_handler.choose_chapters()
                capitulos = []
                if input_chapters is None:
                    for cap in chapter_feed:
                        if manga_final.manga_id not in log or cap.chapter_id not in log[manga_final.manga_id]:
                            get_chapter_link(cap.chapter_id)
                            create_folder_download(manga_final.title,cap.number,cap.title,link)
                            register_download_log(manga_final.manga_id, cap.chapter_id)
                        else:
                            print(f"Capítulos {cap.chapter_id} já baixados. Pulando...")
                else:
                    try:
                        for i in input_chapters:
                            capitulos.append(chapter_feed[i - 1])

                        for cap in capitulos:
                            if manga_final.manga_id not in log or cap.chapter_id not in log[manga_final.manga_id]:
                                print(cap.chapter_id)
                                link = get_chapter_link(cap.chapter_id)
                                create_folder_download(manga_final.title,cap.number,cap.title,link)
                                register_download_log(manga_final.manga_id, cap.chapter_id)
                            else:
                                print(f"Capítulo(s) {cap.chapter_id} já baixado(s). Pulando...")
                    except IndexError:
                        print(f"Capítulos não encontrados. Certifique-se que os capítulos estão disponíveis.")

            elif welcome_option == 2:
                choose_lang = input_handler.manga_language
            elif welcome_option == 3:
                print("Encerrando o programa.")
                sys.exit()
        except ValueError:
            print("Digite apenas números.")

def manga_select(lista_busca):
    print("Os mangás encontrados foram:")

    for index, manga in enumerate(lista_busca):
        print(f"[{index + 1}] - {manga.title} - Autor: {manga.author}")
    escolha = int(input("Qual deseja baixar? \n"))
    manga_selecionado = lista_busca[escolha - 1]

    return manga_selecionado



if __name__ == "__main__":
    check_log()
    main()








