from flask import Flask, render_template, request, redirect, url_for, flash
from Controlador.controlador import Controlador

app = Flask(__name__)
app.secret_key = "secret_key"
control = Controlador()

@app.route("/")
def menu_principal():
    """
    Ruta para la página principal.
    """
    tareas = control.mostrar_tareas()
    return render_template("index.html", tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    """
    Ruta para agregar una tarea al inicio o al final.

    Returns:
        Redirige a la página principal con la tarea agregada.
    """
    descripcion = request.form["descripcion"]
    impacto = request.form.get("impacto", "")
    fecha = request.form.get("fecha", "")
    b = control.agregar_tarea(descripcion, impacto, fecha)

    if b:
        flash(f"La tarea '{descripcion}' fue agregada!")
    else:
        flash(f"La tarea '{descripcion}' ya existe en la lista.")

    return redirect(url_for("menu_principal"))

@app.route("/completar/<descripcion>", methods=["POST"])
def completar_tarea(descripcion):
    """
    Ruta para completar una tarea.
    
    Parámetros:
        descripcion(str): Descripción de la tarea.

    Returns:
        Redirige a la página principal con la tarea completada.
    """
    control.completar_tarea(descripcion)
    flash(f"La tarea '{descripcion}' fue completada!")
    return redirect(url_for("menu_principal"))

@app.route("/eliminar/<descripcion>", methods=["POST"])
def eliminar_tarea(descripcion):
    """
    Ruta para eliminar una tarea.

    Parámetros:
        descripcion(str): Descripción de la tarea.

    Returns:
        Redirige a la página principal con la tarea eliminada.
    """
    control.eliminar_tarea(descripcion)
    flash(f"La tarea '{descripcion}' fue eliminada.")
    return redirect(url_for("menu_principal"))

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=10000)


