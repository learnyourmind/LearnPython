import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story', 
	'A Story of a Boy and his toys that came to life', 
	'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 
	'https://www.youtube.com/watch?v=c3986gGp3Qs')

#print(toy_story.trailer_url)

Avatar = media.Movie('Avatar', 
                     'A story of a marine in other world',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg', 
                     'https://www.youtube.com/watch?v=a0CDJZu4M5I')
#print(Avatar.storyline)
#Avatar.show_trailer()

movies = [toy_story, Avatar]
fresh_tomatoes.open_movies_page(movies)