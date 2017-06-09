import media
import fresh_tomatoes

#this is a list of movie instances in which
# I am passing the arguments title, storyline, poster image and trailer url.
guardians = media.Movies("Guardians of the Galaxy","Star-Lord (Chris Pratt) tries to find his true father.",
                         "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                         "https://www.youtube.com/watch?v=sMTntxvok1M")


suicide_squad = media.Movies('Suicide Squad', 'Dubbed Task Force X, the criminals '
                             'unite to battle a mysterious and powerful entity,',
                             'https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_%28film%29_Poster.png',
                             'https://www.youtube.com/watch?v=CmRih_VtVAs')

warcraft = media.Movies('Warcraft',' The film portrays the initial encounters '
                        'between the humans and the orcs',
                        'https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg',
                        'https://www.youtube.com/watch?v=RhFMIRuHAL4')

captain_america = media.Movies("Captain America civil war", "A very good movie",
                               "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                               "https://www.youtube.com/watch?v=uVdV-lxRPFo")


x_men = media.Movies("X-Men: Apocalypse", "Another very good movie",
                     "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg",
                     "https://www.youtube.com/watch?v=Jer8XjMrUB4")


justice = media.Movies("Justice League", "Bruce Wayne enlists the help of his new found ally, Diana Prince,"
                       "to face an even greater enemy.",
                       "https://upload.wikimedia.org/wikipedia/en/e/e5/Justice_League_film_logo.jpg",
                       "https://www.youtube.com/watch?v=fIHH5-HVS9o")


#This is a list that contain all the data for the movies.
movie_list = [guardians, suicide_squad, warcraft, captain_america, x_men, justice]
#I must call the fresh_tomatoes and pass the list movie_list
# as a result it will return a html file with the content ready to view.
fresh_tomatoes.open_movies_page(movie_list)
