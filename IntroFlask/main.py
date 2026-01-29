from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms


app = Flask(__name__)
app.secret_key="Clave secreta"
csrf=CSRFProtect()

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

@app.route("/operasBas", methods =["GET","POST"])
def operas1():
    n1=0
    n2=0
    res =0
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        res = float(n1)+float(n2)
    return render_template("operaBas.html",n1=n1,n2=n2,res=res)

@app.route('/alumnos')
def alumnos():
    return render_template("alumnos.html")

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    resultado = 0
    if request.method == "POST":
        x1 = float(request.form["x1"])
        y1 = float(request.form["y1"])
        x2 = float(request.form["x2"])
        y2 = float(request.form["y2"])
        resultado = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return render_template("distancia.html", resultado=resultado)

@app.route("/resultado", methods=["GET","POST"])
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
    
@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    total = ""
    nombre = ""

    if request.method == "POST":
        nombre = request.form.get("nombre")
        boletos = int(request.form.get("boletos"))
        compradores = int(request.form.get("compradores"))
        tarjeta = request.form.get("tarjeta")

        if boletos <= compradores * 7:
            total = boletos * 12

            if boletos > 5:
                total = total * 0.85
            elif boletos >= 3:
                total = total * 0.90

            if tarjeta == "si":
                total = total * 0.90
        else:
            total = "No se pueden comprar más de 7 boletos por persona"

    return render_template("cinepolis.html", total=total, nombre=nombre)

@app.route("/usuarios", methods=["GET","POST"])
def usuarios():
    mat=0
    nom=""
    apa=""
    ama=""
    email=""
    usuarios_class=forms.UserForm(request.form)
    if request.method=="POST":
        mat=usuarios_class.Matricula.data
        nom=usuarios_class.Nombre.data
        apa=usuarios_class.Apaterno.data
        ama=usuarios_class.Amaterno.data
        email=usuarios_class.Correo.data
        
        
        
    return render_template("usuarios.html", form=usuarios_class, mat=mat, nom=nom, apa=apa, ama=ama, email=email)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
    
    """
    sbakdjasd
    """