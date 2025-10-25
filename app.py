from flask import Flask, render_template, request
import math
import forms

app = Flask(__name__)
""" desde donde arrancará mi proyecto es lo que indica el ('/') """
@app.route('/index')
def index():
    titulo = "Pagina de Inicio"
    listado = ['Python', 'Flask', "Jinja2", "Html", "'CSS"]
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/calculos', methods=['GET', 'POST'])
def calculos():
    
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        opera = request.form['operacion']
        if opera == 'suma':
            res = int(numero1) + int(numero2)
        if opera == 'resta':
            res = int(numero1) - int(numero2)
        if opera == 'multiplicacion':
            res = int(numero1) * int(numero2)
        if opera == 'division':
            res = int(numero1) / int(numero2)
        return render_template('calculos.html', res=res, numero1=numero1, numero2=numero2)
    return render_template('calculos.html') 

@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
      if request.method == 'POST':
        x1 = request.form['x1']
        y1 = request.form['y1']
        x2 = request.form['x2']
        y2 = request.form['y2']

        num1 = int(x2) - int(x1);
        num2 = int(y2) - int(y1);

        opera = (math.pow(num1, 2) + math.pow(num2, 2));
        res = math.sqrt(opera); 

        return render_template('distancia.html', res=res, x1=x1, y1=y1, x2=x2, y2=y2)
      return render_template('distancia.html')

@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    matri=0
    nombre=''
    apellido=''
    email=''

    alumno_clas = forms.UserForm(request.form)

    if request.method == 'POST' and alumno_clas.validate() :
        matri = alumno_clas.matricula.data
        nombre = alumno_clas.nombre.data
        apellido = alumno_clas.apellido.data
        email = alumno_clas.correo.data

    return render_template('Alumnos.html', form=alumno_clas, matri=matri, nombre=nombre, apellido=apellido, email=email)

@app.route('/hola')
def about():
    return "Hola desde carpeta hola"

""" variable tipo string llamada user """
@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:num>')
def func(num):
    return f"El numero es: {num}"

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f"La suma es: {num1 + num2}"

""" La ruta user recibe dos parametros diferentes, entonces 
NO se confundira con la del user de la de arriba. Lo ÚNICO que
debe ser diferente es que el metodo debe ser diferente """
@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} nombre {}".format(id,username)

@app.route('/suma/<float:n1>/<float:n2>')
def func1(n1, n2):
    return "La suma es: {}".format(n1+n2)

@app.route('/default/')
@app.route('/default/string:dft>')
def func2(dft="sss"):
    return "El valor de dft es: "+dft

@app.route('/prueba')
def func4():
    return '''

    <html>
        <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <h1>Pagina de prueba </h1>
        </head>
        <body>
            <h1>Holaaaaa</h1>
            <p>Esta pagina es para probar el retorno</p>
        </body>
    </html>
'''

""" crear sistema de arranque del proyecto """
if __name__ == '__main__':
    app.run(debug=True)