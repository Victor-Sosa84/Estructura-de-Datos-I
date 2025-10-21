from flask import Flask, render_template, request, redirect, url_for, flash
from Controlador.controlador import Controlador

app = Flask(__name__)
app.secret_key = "secret_key"
control = Controlador()

@app.route("/")
def menu_principal():
    tareas = control.mostrar_tareas()
    return render_template("index.html", tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    descripcion = request.form["descripcion"]
    accion = request.form["accion"]

    if accion == "inicio":
        b = control.agregar_tarea_inicio(descripcion)
    elif accion == "final":
        b = control.agregar_tarea_final(descripcion)

    if b:
        flash(f"La tarea '{descripcion}' fue agregada!")
    else:
        flash(f"La tarea '{descripcion}' no fue agregada. Ya existente en la lista.")

    return redirect(url_for("menu_principal"))

@app.route("/completar/<descripcion>", methods=["POST"])
def completar_tarea(descripcion):
    control.completar_tarea(descripcion)
    flash(f"La tarea '{descripcion}' fue completada!")
    return redirect(url_for("menu_principal"))

@app.route("/eliminar/<descripcion>", methods=["POST"])
def eliminar_tarea(descripcion):
    control.eliminar_tarea(descripcion)
    flash(f"La tarea '{descripcion}' fue eliminada.")
    return redirect(url_for("menu_principal"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


