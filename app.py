from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "a117f74e"  # Your OMDb API key

@app.route("/", methods=["GET", "POST"])
def home():
    movie_data = None

    if request.method == "POST":
        movie_name = request.form["movie"]

        url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}&plot=full"
        response = requests.get(url)
        movie_data = response.json()

        print(movie_data)  # Optional: for debugging in terminal

    return render_template("index.html", movie=movie_data)

if __name__ == "__main__":
    app.run(debug=True)



