from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'imdb.db'

def query_db(query, args=(), one=False):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_actor', methods=['GET'])
def search_actor():
    actor_name = request.args.get('actor')
    print(f"Searching for actor: {actor_name}")  # Debugging
    query = """
        SELECT Actor.Name, Movie.Title
        FROM Actor
        JOIN Casting ON Actor.ActorId = Casting.ActorId
        JOIN Movie ON Movie.MovieID = Casting.MovieID
        WHERE Actor.Name LIKE ?
    """
    actors = query_db(query, ('%' + actor_name + '%',))
    print(f"Query results: {actors}")  # Debugging
    results = {}
    for actor, movie in actors:
        if actor not in results:
            results[actor] = []
        results[actor].append(movie)
    print(f"Formatted results: {results}")  # Debugging
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
