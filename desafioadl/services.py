from django.db import models
from desafioadl.models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    """
    Recupera todas las tareas y sus subtareas.
    """
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return tareas, subtareas

def crear_nueva_tarea(descripcion):
    """
    Crea una nueva tarea.
    """
    nueva_tarea = Tarea.objects.create(descripcion=descripcion)
    return nueva_tarea

def crear_sub_tarea(descripcion_subtarea, tarea_id):
    """
    Crea una nueva subtarea para una tarea específica.
    """
    tarea = Tarea.objects.get(pk=tarea_id)
    nueva_subtarea = SubTarea.objects.create(descripcion=descripcion_subtarea, **{'tarea_id': tarea})
    return nueva_subtarea

def elimina_tarea(tarea_id):
    """
    Elimina una tarea y sus subtareas.
    """
    tarea = Tarea.objects.get(pk=tarea_id)
    tarea.delete()
    return tarea

def elimina_sub_tarea(subtarea_id): 
    """
    Elimina una subtarea específica.
    """
    subtarea = SubTarea.objects.get(pk=subtarea_id)
    subtarea.delete()
    return subtarea

def imprimir_en_pantalla(tareas, subtareas):
    """
    Imprime las tareas y subtareas de forma ordenada.
    """
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in subtareas.filter(tarea_id=tarea):
            print(f"\t[{subtarea.id}] {subtarea.descripcion}")

