from flask import Blueprint, render_template, request, redirect, jsonify, Flask
from controls.tda.stack.stackOperation import StackOperation
from flask_cors import CORS

router = Blueprint('router', __name__)

# Página de inicio
@router.route('/')
def home():
    return render_template("template.html")

# Mostrar lista de comandos
@router.route('/comando')
def lista_comandos():
    file_path = r"C:\Users\A S U S\Downloads\Practica1\data\stack_data.json"
    try:
        pd = StackOperation.from_json(file_path)  # Cargar los datos desde JSON
        lista_comandos = list(pd)  # Convertir la instancia de StackOperation a lista
    except Exception as e:
        lista_comandos = []
        print(f"Error cargando comandos: {e}")
    return render_template("comando/lista.html", lista=lista_comandos, encontrado=None, not_found=None)

# Ver página para guardar comando
@router.route('/comando/ver')
def ver_guardar():
    return render_template("comando/guardar.html")

# Guardar comando
@router.route('/comando/guardar', methods=["POST"])
def guardar_comando():
    file_path = r"C:\Users\A S U S\Downloads\Practica1\data\stack_data.json"
    try:
        pd = StackOperation.from_json(file_path)  # Cargar los datos desde JSON
    except Exception as e:
        pd = StackOperation()
        print(f"Error inicializando pila: {e}")

    data = request.form
    
    if "comando" not in data:
        return jsonify({"error": "El comando no fue proporcionado"}), 400
        
    comando = data["comando"]
    pd.push(comando)
    try:
        pd.to_json(file_path)  # Guardar los datos en JSON después de agregar el comando
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    print("Comando guardado correctamente:", comando)
    return redirect("/comando", code=302)

# Buscar comando
@router.route('/comando/buscar', methods=["POST"])
def buscar_comando():
    parametro = request.form.get("parametro")
    tipo_busqueda = request.form.get("tipo_busqueda", "lineal")
    file_path = r"C:\Users\A S U S\Downloads\Practica1\data\stack_data.json"
    try:
        stack_operation = StackOperation.from_json(file_path)
        resultados = []

        if tipo_busqueda == "lineal":
            resultados = stack_operation.linear_search(parametro).toArray
        elif tipo_busqueda == "binaria":
            resultados = stack_operation.binary_search(parametro).toArray

        if resultados:
            return render_template("comando/lista.html", lista=resultados, not_found=None)
        else:
            return render_template("comando/lista.html", lista=[], not_found=parametro)
    except Exception as e:
        print(f"Error buscando comandos: {e}")
        return render_template("comando/lista.html", lista=[], encontrado=None, not_found=parametro)


# Ordenar comandos
@router.route('/comando/ordenar', methods=["POST"])
def ordenar_comando():
    campo = request.form["campo"]
    direccion = int(request.form["direccion"])
    algoritmo = int(request.form["algoritmo"])
    file_path = r"C:\Users\A S U S\Downloads\Practica1\data\stack_data.json"
    
    try:
        pd = StackOperation.from_json(file_path)
        
        if campo == "comando":
            # Ajuste para orden descendente
            if direccion == -1:
                pd.sort(algoritmo, -1)  # Usando -1 para indicar orden descendente
            else:
                pd.sort(algoritmo, 1)   # Por defecto orden ascendente si direccion es 1
        
    except Exception as e:
        print(f"Error ordenando comandos: {e}")
    
    return render_template("comando/lista.html", lista=list(pd), encontrado=None, not_found=None)


# Configuración del blueprint en la aplicación principal
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(router, url_prefix='/')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
