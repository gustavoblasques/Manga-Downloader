import requests 
from models import InfoManga, SavedChapter


base_url = "https://api.mangadex.org"
languages = InfoManga.downloadLang

def buscar_id_por_titulo(titulo):
    r = requests.get(
        f"{base_url}/manga",
        params={"title": titulo}
    )
    return([manga["id"] for manga in r.json()["data"]])

def manga_info(id):
        manga_expandido = requests.get(
                f"{base_url}/manga/{id}?includes[]=author&includes[]=artist"
            )
        result = manga_expandido.json()
        attr = result["data"]["attributes"]
        relationships = result["data"]["relationships"]

        title_dic = attr.get('title', {})
        title_main = list(title_dic.values())[0]

        description_dic = attr.get("description")
        description_main = list(description_dic.values())[0] if description_dic else "Sem Descrição."

        relationships_dic = relationships[0]
        relationships_attr = relationships_dic.get('attributes')
        author_name = relationships_attr.get('name')

        available_lang = attr.get("availableTranslatedLanguages")

        return  InfoManga(
                    manga_id= id,
                     title= title_main,
                     description= description_main,
                     author= author_name,
                     availableLanguages=available_lang
        )
##REVISAR
def get_chapter_feed(manga_id):
    chapter_feed = requests.get(f"{base_url}/manga/{manga_id}/feed",
                     params={"translatedLanguage[]": languages} )
    chapter_list = []
    chapters_result = chapter_feed.json()
    for data in chapters_result["data"]:
        attr = data["attributes"]
        chapter = SavedChapter(
            chapter_id = data["id"],
            title = attr.get("title"),
            pages = attr.get("pages"),
            number = attr.get("chapter")
        )
        chapter_list.append(chapter)
    chapter_list.sort(key=lambda x: float(x.number) if x.number is not None else 0)
    return chapter_list

def get_chapter_link(chapter_id):
    baseurl = "https://api.mangadex.org/at-home/server/"
    get_metadata = requests.get(f"{baseurl}/{chapter_id}")
    chapter_baseurl = get_metadata.json()["baseUrl"]
    chapter_hash = get_metadata.json()["chapter"]["hash"]
    chapter_data_list = get_metadata.json()["chapter"]["data"]
    chapter_link = []
    for data in chapter_data_list:
         chapter_link.append(f"{chapter_baseurl}/data/{chapter_hash}/{data}")
    return chapter_link
