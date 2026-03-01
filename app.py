from flask import Flask, render_template

app = Flask(__name__,
            template_folder="vista/templates",
            static_folder="vista/static")

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/obtener")
def obtener():
    return "<h2>Página Obtener Locker</h2>"

@app.route("/liberar")
def liberar():
    return "<h2>Página Liberar Locker</h2>"

if __name__ == "__main__":
    app.run(debug=True)