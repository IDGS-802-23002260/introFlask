from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "IDGS-802-Flask"
    lista = ['Juan', 'Karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/formulario')
def formulario():
    return render_template("formularios.html")

@app.route('/reportes')
def reportes():
    return render_template("reportes.html")

@app.route('/hola')
def hola():
    return "Hola, Hola"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1 + n2)

@app.route("/default/")
@app.route("/default/<string:param>")
def func2(param="Juan"):
    return f"<h1>¡Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
            <label>Name:</label>
            <input type="text" name="name" required><br><br>

            <label>Apellido paterno:</label>
            <input type="text" name="apaterno" required>
        </form>
    '''

@app.route("/operasBas")
def opera1():
    return render_template("operaBas.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    n1 = float(request.form.get("n1"))
    n2 = float(request.form.get("n2"))
    op = request.form.get("operacion")

    if op == "suma":
        return f"La suma es: {n1 + n2}"
    if op == "resta":
        return f"La resta es: {n1 - n2}"
    if op == "multiplicacion":
        return f"La multiplicación es: {n1 * n2}"
    if op == "division":
        return f"La división es: {n1 / n2}"


if __name__ == '__main__':
    app.run(debug=True)