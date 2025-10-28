# Proyecto To Do List - Versión 2.0

Esta es la versión 2.0 de la aplicación web **To-Do List**, desarrollada con **Python** y **Flask**, aplicando el patrón **MVC (Modelo-Vista-Controlador)**.
Se utilizan **listas enlazadas** para manejar internamente las tareas, y se ha mejorado la interfaz y la funcionalidad respecto a la versión inicial.

---

## Funcionalidades principales:
- **Agregar tareas** a la lista.
- **Marcar** tareas como **completadas**.
- **Eliminar** tareas.
- Evitar tareas duplicadas.
- Visualizar el estado actual de cada tarea (Pendiente o Completada).
- Asignar un **nivel de impacto** *opcional* a cada tarea: Bajo, Medio o Alto.
- Registrar una **fecha límite** *opcional* para cada tarea.
- **Sección de Pendientes y Completadas** separadas para mayor claridad.
- **Panel derecho** *opcional* para notas libres y prioridades del usuario. 

---

## Tecnologías/Herramientas utilizadas

- [Python 3](https://www.python.org/)
- [Flask 3](https://flask.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/) para el diseño visual
- Jinja2 como motor de plantillas HTML
- HTML, CSS moderno

---

## Conceptos aplicados

- Patrón **MVC (Modelo-Vista-Controlador)**
- Uso de **listas enlazadas dinámicas** para la gestión de tareas.
- **Enrutamiento y redirección** con Flask
- **Uso de formularios y métodos POST**
- Sistema de **mensajes con flash()**
- Diseño **responsivo y atractivo** con Bootstrap
- Seperación de **lógica y presentación** en el proyecto

---

## Notas importantes

- Las secciones de **Notas** y **Prioridades** son **texto libre** y no afectan la lógica de las tareas
- El **impacto** de la tarea es opcional; si no se asigna, se considera "ninguno"
- Listo para desplegar en cualquier navegador o en servicios de hosting web como Render
- Interfaz pensada para **facilidad de uso y claridad**, manteniendo la lista principal a la izquierda y panel derecho para información complementaria