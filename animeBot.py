from mal import Anime
from mal import AnimeSearch

def animeInf(animeTit):
    animesearch = AnimeSearch(animeTit)
    anime = animesearch.results[0]
    animeId = Anime(anime.mal_id)
    short = animeId.synopsis.split(".", 2)
    info = f"**Anime title**: {anime.title}\n**Anime score**: {anime.score}\n**Anime synoposis**: {short[0]}. {short[1]}.\n{animeId.image_url}"
    return info

