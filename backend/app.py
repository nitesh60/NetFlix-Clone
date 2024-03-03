# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/movies')
def get_movies():
    # Implement logic to fetch movies from a database or API
    movies = [
        {"title": "One Piece", "genre": "Anime", "rating": 9.5,"image": 'http://127.0.0.1:5000/static/img/One Piece.jpg', "description": "Description of Movie 1" },
        {"title": "Naruto", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Dragon Ball Z", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Dragon Ball Z.jpg', "description": "Description of Movie 1"},
        {"title": "Death Note", "genre": "Anime", "rating": 9.5,"image": 'http://127.0.0.1:5000/static/img/DN.jpg', "description": "Description of Movie 1" },
        {"title": "Baki Hanma", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/BH.jpg', "description": "Description of Movie 1"},
        {"title": "Jujutsu Kaisen", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/JK.jpg', "description": "Description of Movie 1"},
        {"title": "Bleach", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/BL.jpg', "description": "Description of Movie 1"},
        {"title": "One Punch Man", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Hunter × Hunter", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "One Piece", "genre": "Anime", "rating": 9.5,"image": 'http://127.0.0.1:5000/static/img/One Piece.jpg', "description": "Description of Movie 1" },
        {"title": "Naruto", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Dragon Ball Z", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Dragon Ball Z.jpg', "description": "Description of Movie 1"},
        {"title": "Death Note", "genre": "Anime", "rating": 9.5,"image": 'http://127.0.0.1:5000/static/img/One Piece.jpg', "description": "Description of Movie 1" },
        {"title": "Baki Hanma", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Jujutsu Kaisen", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Bleach", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "One Punch Man", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Hunter × Hunter", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "One Piece", "genre": "Anime", "rating": 9.5,"image": 'http://127.0.0.1:5000/static/img/One Piece.jpg', "description": "Description of Movie 1" },
        {"title": "Naruto", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Dragon Ball Z", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Dragon Ball Z.jpg', "description": "Description of Movie 1"},
        {"title": "Death Note", "genre": "Anime", "rating": 9.5,"image": 'http://127.0.0.1:5000/static/img/One Piece.jpg', "description": "Description of Movie 1" },
        {"title": "Baki Hanma", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Jujutsu Kaisen", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Bleach", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "One Punch Man", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Hunter × Hunter", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "One Piece", "genre": "Anime", "rating": 9.5,"image": 'http://127.0.0.1:5000/static/img/One Piece.jpg', "description": "Description of Movie 1" },
        {"title": "Naruto", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Dragon Ball Z", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Dragon Ball Z.jpg', "description": "Description of Movie 1"},
        {"title": "Death Note", "genre": "Anime", "rating": 9.5,"image": 'http://127.0.0.1:5000/static/img/One Piece.jpg', "description": "Description of Movie 1" },
        {"title": "Baki Hanma", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Jujutsu Kaisen", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Bleach", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "One Punch Man", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},
        {"title": "Hunter × Hunter", "genre": "Anime", "rating": 8.9,"image": 'http://127.0.0.1:5000/static/img/Naruto.jpg', "description": "Description of Movie 1"},

    ]
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)
