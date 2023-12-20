from flask import render_template, request, redirect, url_for, session, Blueprint
from app import db
from app.models.recomendaciones import Recomendacion
from app.models.usuarios import Usuario


recomendaciones_bp = Blueprint('recomendaciones', __name__)




@recomendaciones_bp.route('/recomendaciones', methods=['GET', 'POST'])

def recomendaciones():



    if request.method == 'POST':
        # Procesa los datos del formulario de recomendaciones y guarda en la tabla Recomendaciones

        dureza_caucho = request.form['dureza_caucho']
        estilo_conduccion = request.form['estilo_conduccion']
        estructura_neumatico = request.form['estructura_neumatico']
        tipo_ambiente = request.form['tipo_ambiente']
        altura_anchura = request.form['altura_anchura ']
        tipo_vehiculo = request.form['tipo_vehiculo']



        nueva_recomendacion = Recomendacion(


            dureza_caucho=dureza_caucho,
            estilo_conduccion=estilo_conduccion,
            estructura_neumatico=estructura_neumatico,
            tipo_ambiente=tipo_ambiente,
            altura_anchura=altura_anchura,
            tipo_vehiculo=tipo_vehiculo
        )

        db.session.add(nueva_recomendacion)
        db.session.commit()

        def recomendar_llanta(tipo_vehiculo, peso, potencia, tipo_carretera, condiciones_clima):
            recomendaciones = {
                ('camioneta', 'off-road'): 'Llantas Todo Terreno',
                ('sedan', 'carretera', 'normal'): 'Llantas para Carretera',
                ('suv', lambda x: x > 2000): 'Llantas Reforzadas'
            }

            for condiciones, recomendacion in recomendaciones.items():
                if all(condicion == valor if not callable(condicion) else condicion(valor) for condicion, valor in
                       zip(condiciones, (tipo_vehiculo, tipo_carretera, peso))):
                    return recomendacion

            return 'No se puede determinar la recomendación de llantas.'

        # Ejemplo de uso
        tipo_vehiculo=tipo_vehiculo
        peso = 2500
        potencia = 200
        tipo_carretera = 'off-road'
        condiciones_clima = 'normal'

        recomendacion = recomendar_llanta(tipo_vehiculo, peso, potencia, tipo_carretera, condiciones_clima)
        print(f"Recomendación de llantas: {recomendacion}")

        return render_template('formulario.html')



