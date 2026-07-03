from dataclasses import dataclass

@dataclass
class InfoManga:
     manga_id: str
     title: str
     description: str
     author: str
     availableLanguages: list
     downloadLang: str = "pt-br"

@dataclass
class SavedChapter:
     chapter_id: str
     title: str
     pages: int
     number: int
