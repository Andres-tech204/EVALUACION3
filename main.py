from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = (nota1 + nota2 + nota3) / 3

            if promedio >= 40 and asistencia >= 75:
                resultado = 'Aprobado'
            else:
                resultado = 'Rechazado'

            return render_template('resultado.html', promedio=promedio, asistencia=asistencia, resultado=resultado)

        except ValueError:
            error = 'Ingresa valores numéricos válidos.'
            return render_template('ejercicio1.html', error=error)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        try:
            nombre1 = request.form['nombre1']
            nombre2 = request.form['nombre2']
            nombre3 = request.form['nombre3']

            nombres = [nombre1, nombre2, nombre3]
            nombre_mas_largo = max(nombres, key=len)
            longitud_nombre = len(nombre_mas_largo)

            return render_template('resultado_ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud_nombre=longitud_nombre)

        except KeyError:
            error = 'Ingresa nombres válidos.'
            return render_template('ejercicio2.html', error=error)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
