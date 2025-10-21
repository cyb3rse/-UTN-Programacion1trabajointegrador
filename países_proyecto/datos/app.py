from flask import Flask, render_template
import csv
import os  # opcional si querés manejar rutas

app = Flask(__name__)

@app.route('/')
def mostrar_paises():
    # Aseguramos que busque el CSV en la misma carpeta que app.py
    ruta_csv = os.path.join(os.path.dirname(__file__), 'paises.csv')
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector)
        datos = list(lector)
    return render_template('index.html', encabezado=encabezado, datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
