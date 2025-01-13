from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = round((nota1 + nota2 + nota3) / 3, 2)
            if promedio >= 40 and asistencia >= 75:
                estado = '<span style="color: blue; font-weight: bold;">APROBADO</span>'
            else:
                estado = '<span style="color: red; font-weight: bold;">REPROBADO</span>'
            resultado = f"<b>Promedio: {promedio}</b><br>{estado}"
        except ValueError:
            resultado = "Por favor ingrese valores válidos."
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_max = None
    caracteres = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_max = max(nombres, key=len)
        caracteres = len(nombre_max)

    return render_template('ejercicio2.html', nombre_max=nombre_max, caracteres=caracteres)

if __name__ == '__main__':
    app.run(debug=True)





