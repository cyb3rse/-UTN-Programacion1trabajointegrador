from flask import Flask, render_template
import csv
import os

# 🚀 Inicialización de Flask
app = Flask(__name__, template_folder="plantillas")

@app.route('/')
def mostrar_paises():
    paises = []
    ruta_csv = os.path.join(os.path.dirname(__file__), "paises.csv")

    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises.append(fila)

    return render_template('index.html', paises=paises)
