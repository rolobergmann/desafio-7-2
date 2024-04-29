## Ejemplos de cómo llamar a las funciones en `services.py` desde la shell de Django

# 1. Importar el módulo `services`:

from desafioadl.services import recupera_tareas_y_sub_tareas, crear_nueva_tarea, crear_sub_tarea, elimina_tarea, elimina_sub_tarea, imprimir_en_pantalla


#2. Recuperar todas las tareas y subtareas:

# Obtiene todas las tareas y subtareas
tareas, subtareas = recupera_tareas_y_sub_tareas()

# Imprime las tareas y subtareas
imprimir_en_pantalla(tareas, subtareas)

# 3. Crear una nueva tarea:

# Crea una nueva tarea con la descripción "Tarea de ejemplo"
nueva_tarea = crear_nueva_tarea("Tarea de ejemplo")

# Imprime la tarea creada
print(nueva_tarea)


# 4. Crear una nueva subtarea para una tarea específica:

# Obtiene la tarea con ID 1
tarea = tareas.get(pk=1)

# Crea una nueva subtarea para la tarea 1 con la descripción "Subtarea de ejemplo"
nueva_subtarea = crear_sub_tarea("Subtarea de ejemplo", tarea.id)

# Imprime la subtarea creada
print(nueva_subtarea)

#5. Eliminar una tarea y sus subtareas:


# Obtiene la tarea con ID 1
tarea = tareas.get(pk=1)

# Elimina la tarea y sus subtareas
elimina_tarea(tarea.id)

# Verifica que la tarea ya no existe
tarea = tareas.get(pk=1).first()
if not tarea:
    print("La tarea ha sido eliminada correctamente")
else:
    print("Error al eliminar la tarea")

# 6. Eliminar una subtarea específica:

# Obtiene la subtarea con ID 1
subtarea = subtareas.get(pk=1)

# Elimina la subtarea
elimina_sub_tarea(subtarea.id)

# Verifica que la subtarea ya no existe
subtarea = subtareas.get(pk=1).first()
if not subtarea:
    print("La subtarea ha sido eliminada correctamente")
else:
    print("Error al eliminar la subtarea")
