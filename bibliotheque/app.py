import sys, os
from flask import Flask , render_template, jsonify
from markupsafe import escape

app = Flask(__name__)

#route for home page
@app.route("/")
def index():
    return "Welcome to my App"

@app.route("/votre_nom/<name>")
def MyCustomName(name):
    return render_template('name.html', name=name)

@app.route('/api/books', methods = ['GET'])
def GetBook():
    book=[
        {
            'id':1,
            'titre' : 'un titre',
        },
        {
            'id':2,
            'titre': 'un autre titre random',
        }
    ]
    return jsonify(book)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5000)


