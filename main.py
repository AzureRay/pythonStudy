import movie, fresh_tomatoes

lv_de_shui = movie.Movie("Mr.Donkey", "https://img3.doubanio.com/view/photo/photo/public/p2393044761.jpg", "https://www.youtube.com/watch?v=y7eENwyLvBE")
your_names = movie.Movie("Your Names", "https://img1.doubanio.com/view/photo/photo/public/p2395733377.jpg", "https://www.youtube.com/watch?v=8cNKoNBwKhw")
qi_yue = movie.Movie("Qiyue and Ansheng","https://img3.doubanio.com/view/photo/photo/public/p2378140502.jpg","https://www.youtube.com/watch?v=V5VGZ6N2x8w")
zootopia = movie.Movie("Zootopia","https://img1.doubanio.com/view/photo/photo/public/p2315672647.jpg","https://www.youtube.com/watch?v=7jknyqafCVM")

movie_list = [lv_de_shui, your_names, qi_yue, zootopia]
fresh_tomatoes.open_movies_page(movie_list)


