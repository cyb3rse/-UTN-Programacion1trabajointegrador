from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>¡Hola desde Flask!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
