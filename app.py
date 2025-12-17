from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("OMDB_API_KEY")  # Read API key from environment variable

@app.route("/", methods=["GET", "POST"])
def home():
    movie_data = None
    if request.method == "POST":
        movie_name = request.form["movie"]
        url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}&plot=full"
        response = requests.get(url)
        movie_data = response.json()
    return render_template("index.html", movie=movie_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
