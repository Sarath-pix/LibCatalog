from flask import Flask, jsonify

app = Flask(__name__)

BOOKS = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien"},
    {"id": 2, "title": "Ponniyin Selvan", "author": "Kalki Krishnamurthy"},
    {"id": 3, "title": "The Alchemist", "author": "Paulo Coelho"},
]

@app.route("/")
def home():
    return jsonify(
        message="Library Catalog CI/CD is working!",
        books_count=len(BOOKS),
        endpoints=["/books", "/health"],
    )

@app.route("/books")
def books():
    return jsonify(BOOKS)

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)