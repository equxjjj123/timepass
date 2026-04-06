from flask import Flask, render_template_string, request

app = Flask(__name__)

# ================= MOVIE DATABASE =================
movies = [

# ================= SCI-FI (20) =================
{"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
{"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
{"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7},
{"title": "Avatar", "genre": "Sci-Fi", "rating": 7.9},
{"title": "Tenet", "genre": "Sci-Fi", "rating": 7.5},
{"title": "Blade Runner 2049", "genre": "Sci-Fi", "rating": 8.0},
{"title": "Arrival", "genre": "Sci-Fi", "rating": 7.9},
{"title": "Gravity", "genre": "Sci-Fi", "rating": 7.7},
{"title": "Dune", "genre": "Sci-Fi", "rating": 8.0},

{"title": "Ex Machina", "genre": "Sci-Fi", "rating": 7.7},
{"title": "The Martian", "genre": "Sci-Fi", "rating": 8.0},
{"title": "Edge of Tomorrow", "genre": "Sci-Fi", "rating": 7.9},
{"title": "Minority Report", "genre": "Sci-Fi", "rating": 7.6},
{"title": "Oblivion", "genre": "Sci-Fi", "rating": 7.0},
{"title": "Looper", "genre": "Sci-Fi", "rating": 7.4},
{"title": "Elysium", "genre": "Sci-Fi", "rating": 6.6},
{"title": "Snowpiercer", "genre": "Sci-Fi", "rating": 7.1},
{"title": "Annihilation", "genre": "Sci-Fi", "rating": 6.8},
{"title": "Ready Player One", "genre": "Sci-Fi", "rating": 7.4},
{"title": "A Quiet Place", "genre": "Sci-Fi", "rating": 7.5},


# ================= ACTION (20) =================
{"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
{"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4},
{"title": "John Wick", "genre": "Action", "rating": 7.4},
{"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1},
{"title": "Gladiator", "genre": "Action", "rating": 8.5},
{"title": "Mission Impossible Fallout", "genre": "Action", "rating": 7.7},
{"title": "Casino Royale", "genre": "Action", "rating": 8.0},
{"title": "Skyfall", "genre": "Action", "rating": 7.8},
{"title": "Black Panther", "genre": "Action", "rating": 7.3},

{"title": "Die Hard", "genre": "Action", "rating": 8.2},
{"title": "The Avengers", "genre": "Action", "rating": 8.0},
{"title": "Thor Ragnarok", "genre": "Action", "rating": 7.9},
{"title": "Iron Man", "genre": "Action", "rating": 7.9},
{"title": "Captain America Civil War", "genre": "Action", "rating": 7.8},
{"title": "Batman Begins", "genre": "Action", "rating": 8.2},
{"title": "The Bourne Identity", "genre": "Action", "rating": 7.9},
{"title": "Rush Hour", "genre": "Action", "rating": 7.0},
{"title": "Lethal Weapon", "genre": "Action", "rating": 7.6},
{"title": "300", "genre": "Action", "rating": 7.6},
{"title": "Kill Bill Vol 1", "genre": "Action", "rating": 8.1},


# ================= ROMANCE (20) =================
{"title": "Titanic", "genre": "Romance", "rating": 7.9},
{"title": "The Notebook", "genre": "Romance", "rating": 7.8},
{"title": "La La Land", "genre": "Romance", "rating": 8.0},
{"title": "Pride and Prejudice", "genre": "Romance", "rating": 7.8},
{"title": "Before Sunrise", "genre": "Romance", "rating": 8.1},
{"title": "Me Before You", "genre": "Romance", "rating": 7.4},
{"title": "Notting Hill", "genre": "Romance", "rating": 7.2},
{"title": "A Walk to Remember", "genre": "Romance", "rating": 7.3},
{"title": "The Fault in Our Stars", "genre": "Romance", "rating": 7.7},

{"title": "500 Days of Summer", "genre": "Romance", "rating": 7.7},
{"title": "Her", "genre": "Romance", "rating": 8.0},
{"title": "The Vow", "genre": "Romance", "rating": 6.8},
{"title": "Love Actually", "genre": "Romance", "rating": 7.6},
{"title": "Pretty Woman", "genre": "Romance", "rating": 7.1},
{"title": "Dear John", "genre": "Romance", "rating": 6.3},
{"title": "PS I Love You", "genre": "Romance", "rating": 7.0},
{"title": "Before Sunset", "genre": "Romance", "rating": 8.1},
{"title": "Before Midnight", "genre": "Romance", "rating": 7.9},
{"title": "The Time Traveler's Wife", "genre": "Romance", "rating": 7.1},
{"title": "Blue Valentine", "genre": "Romance", "rating": 7.4},


# ================= COMEDY (20) =================
{"title": "3 Idiots", "genre": "Comedy", "rating": 8.4},
{"title": "Hera Pheri", "genre": "Comedy", "rating": 8.2},
{"title": "The Hangover", "genre": "Comedy", "rating": 7.7},
{"title": "Golmaal", "genre": "Comedy", "rating": 7.5},
{"title": "Dhamaal", "genre": "Comedy", "rating": 7.4},
{"title": "Andaz Apna Apna", "genre": "Comedy", "rating": 8.1},
{"title": "Welcome", "genre": "Comedy", "rating": 7.5},
{"title": "Bhool Bhulaiyaa", "genre": "Comedy", "rating": 7.4},
{"title": "Fukrey", "genre": "Comedy", "rating": 6.9},

{"title": "Munna Bhai MBBS", "genre": "Comedy", "rating": 8.1},
{"title": "Chup Chup Ke", "genre": "Comedy", "rating": 7.0},
{"title": "Housefull", "genre": "Comedy", "rating": 5.5},
{"title": "OMG Oh My God", "genre": "Comedy", "rating": 8.1},
{"title": "PK", "genre": "Comedy", "rating": 8.1},
{"title": "Ready", "genre": "Comedy", "rating": 4.9},
{"title": "No Entry", "genre": "Comedy", "rating": 6.6},
{"title": "De Dana Dan", "genre": "Comedy", "rating": 6.3},
{"title": "Jolly LLB", "genre": "Comedy", "rating": 7.5},
{"title": "Hungama", "genre": "Comedy", "rating": 7.6},
{"title": "Phir Hera Pheri", "genre": "Comedy", "rating": 7.2},


# ================= THRILLER (20) =================
{"title": "Shutter Island", "genre": "Thriller", "rating": 8.2},
{"title": "Se7en", "genre": "Thriller", "rating": 8.6},
{"title": "Gone Girl", "genre": "Thriller", "rating": 8.1},
{"title": "The Silence of the Lambs", "genre": "Thriller", "rating": 8.6},
{"title": "Prisoners", "genre": "Thriller", "rating": 8.1},
{"title": "Zodiac", "genre": "Thriller", "rating": 7.7},
{"title": "Fight Club", "genre": "Thriller", "rating": 8.8},
{"title": "The Girl with the Dragon Tattoo", "genre": "Thriller", "rating": 7.8},
{"title": "Nightcrawler", "genre": "Thriller", "rating": 7.9},

{"title": "The Prestige", "genre": "Thriller", "rating": 8.5},
{"title": "Memento", "genre": "Thriller", "rating": 8.4},
{"title": "Oldboy", "genre": "Thriller", "rating": 8.4},
{"title": "Black Swan", "genre": "Thriller", "rating": 8.0},
{"title": "Donnie Darko", "genre": "Thriller", "rating": 8.0},
{"title": "The Sixth Sense", "genre": "Thriller", "rating": 8.1},
{"title": "Enemy", "genre": "Thriller", "rating": 6.9},
{"title": "The Machinist", "genre": "Thriller", "rating": 7.7},
{"title": "Cape Fear", "genre": "Thriller", "rating": 7.3},
{"title": "The Others", "genre": "Thriller", "rating": 7.6},
{"title": "Insomnia", "genre": "Thriller", "rating": 7.2},

]
# ================= HOME PAGE =================
home_html = """
<!DOCTYPE html>
<html>
<head>
<title>Movie Recommender</title>
<style>
body {font-family: Arial; background: linear-gradient(135deg,#141e30,#243b55); color:white; text-align:center;}
.container {margin-top:80px;}
select,button {padding:10px; border-radius:8px; border:none; margin:10px;}
button {background:#ff6a00; color:white; cursor:pointer;}
button:hover {background:#ffb347;}
.footer {margin-top:50px; opacity:0.7;}
</style>
</head>
<body>
<div class="container">
<h1>🎬 Movie Recommender</h1>
<form action="/recommend" method="POST">
<select name="genre">
<option>Sci-Fi</option>
<option>Action</option>
<option>Romance</option>
<option>Comedy</option>
<option>Thriller</option>
</select><br>
<button type="submit">Get Recommendations</button>
</form>
<div class="footer">✨ Crafted beautifully by Kusum Sahu ✨</div>
</div>
</body>
</html>
"""

# ================= RECOMMENDATION PAGE =================
recommend_html = """
<!DOCTYPE html>
<html>
<head>
<title>Recommendations</title>
<style>
body {font-family: Arial; background:#0f2027; color:white; text-align:center;}
.movies {display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:15px; padding:20px;}
.card {
    background: white;
    color: black;
    padding: 15px;
    border-radius: 10px;
    cursor: pointer;
    transition: 0.3s;

    height: 120px;              /* ✅ fixed height */
    display: flex;
    flex-direction: column;
    justify-content: center;    /* center content vertically */
}
.card:hover {transform:scale(1.05);}
a {text-decoration:none; color:inherit;}
</style>
</head>
<body>
<h1>🎥 Recommended Movies</h1>
<div class="movies">
{% for m in movies %}
<a href="/movie/{{ m.title }}">
<div class="card">
<h3>{{ m.title }}</h3>
<p>⭐ Rating: {{ m.rating }}</p>
</div>
</a>
{% endfor %}
</div>
</body>
</html>
"""

# ================= MOVIE DETAIL PAGE =================
detail_html = """
<!DOCTYPE html>
<html>
<head>
<title>{{ movie.title }}</title>
<style>
body {font-family: Arial; background:#1c1c1c; color:white; text-align:center;}
.card {margin:100px auto; padding:30px; background:#333; width:300px; border-radius:15px;}
button {padding:10px; border:none; border-radius:8px; cursor:pointer;}
</style>
</head>
<body>
<div class="card">
<h1>{{ movie.title }}</h1>
<p>🎭 Genre: {{ movie.genre }}</p>
<p>⭐ Rating: {{ movie.rating }}</p>
<br>
<a href="/"><button>⬅ Back</button></a>
</div>
</body>
</html>
"""

# ================= ROUTES =================
@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    filtered = [m for m in movies if m['genre'] == genre]
    return render_template_string(recommend_html, movies=filtered)

@app.route('/movie/<title>')
def movie_detail(title):
    movie = next((m for m in movies if m['title'] == title), None)
    return render_template_string(detail_html, movie=movie)

# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)