import media
import fresh_tomatoes

mummy = media.Movie("Mummy", "Mummy comes to live killing people", "https://m.media-amazon.com/images/M/MV5BODg1NTIxMzEtM2NmMi00MDQ2LWE5YjYtZTgxYmNhZTQxYWIzXkEyXkFqcGdeQXVyNDYzODU1ODM@._V1_SY1000_CR0,0,631,1000_AL_.jpg", "https://www.youtube.com/watch?v=IjHgzkQM2Sg")
avengers = media.Movie("Avengers", "Heroes collaborates to save the Earth", "https://images-na.ssl-images-amazon.com/images/I/719S7I-%2ByBL._SL1023_.jpg", "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
meg = media.Movie("Meg", "A giant shark killing people", "data:image/jpeg;base64,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", "https://www.youtube.com/watch?v=rUjIo-7nHfw")
mask = media.Movie("Mask", "Wearing a mask gives super powers", "http://img.moviepostershop.com/the-mask-movie-poster-1994-1020201915.jpg", "https://www.youtube.com/watch?v=DkJs6Y1QJrE")
sound_of_music = media.Movie("Sound of Music", "Singing happy songs and dancing", "https://i.pinimg.com/originals/44/b0/02/44b002473db208d6006a42fd3ff6cede.jpg", "https://www.youtube.com/watch?v=TRPEpJHI9zg")
pokemon = media.Movie("Pokemon the Movie", "Weirdly mutated monsters trying to kill each other", "https://www.artinsights.com/wp-content/uploads/2016/08/Pokemon-poster.jpeg", "https://www.youtube.com/watch?v=r12w4iRBLp4")

movies = [mummy, avengers, meg, mask, sound_of_music, pokemon]
fresh_tomatoes.open_movies_page(movies)
