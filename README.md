<div align='center'>

<h1>Manejo de tareas</h1>
<p>Modulo 7 - Desafio 2</p>

<h4> <span> · </span> <a href="https://github.com/rolobergmann/desafio-7-2/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/rolobergmann/desafio-7-2/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/rolobergmann/desafio-7-2/issues"> Request Feature </a> </h4>


</div>

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
- [Contact](#handshake-contact)


## :star2: About the Project
### :space_invader: Tech Stack
<details> <summary>Client</summary> <ul>
<li><a href="">Django</a></li>
</ul> </details>
<details> <summary>Database</summary> <ul>
<li><a href="">postgresql</a></li>
</ul> </details>

## :toolbox: Getting Started

### :bangbang: Prerequisites

- asgiref==3.8.1
- Django==5.0.4
- django-environ==0.11.2
- psycopg2==2.9.9
- setuptools==69.5.1
- tzdata==2024.1


### :test_tube: Running Tests

#1. Importar el módulo `services`:
```bash
from desafioadl.services import recupera_tareas_y_sub_tareas, crear_nueva_tarea, crear_sub_tarea, elimina_tarea, elimina_sub_tarea, imprimir_en_pantalla
```
# 2. Recuperar todas las tareas y subtareas:
## Obtiene todas las tareas y subtareas
```bash
tareas, subtareas = recupera_tareas_y_sub_tareas()
```
## Imprime las tareas y subtareas
```bash
imprimir_en_pantalla(tareas, subtareas)
```
# 3. Crear una nueva tarea:
## Crea una nueva tarea con la descripción "Tarea de ejemplo"
```bash
nueva_tarea = crear_nueva_tarea("Tarea de ejemplo")
```
## Imprime la tarea creada
```bash
print(nueva_tarea)
```
# 4. Crear una nueva subtarea para una tarea específica:
## Obtiene la tarea con ID 1
```bash
tarea = tareas.get(pk=1)
```
## Crea una nueva subtarea para la tarea 1 con la descripción "Subtarea de ejemplo"
```bash
nueva_subtarea = crear_sub_tarea("Subtarea de ejemplo", tarea.id)
```
## Imprime la subtarea creada
```bash
print(nueva_subtarea)
```
#5. Eliminar una tarea y sus subtareas:
## Obtiene la tarea con ID 1
```bash
tarea = tareas.get(pk=1)
```
## Elimina la tarea y sus subtareas
```bash
elimina_tarea(tarea.id)
```
## Verifica que la tarea ya no existe
```bash
tarea = tareas.get(pk=1).first() if not tarea: print("La tarea ha sido eliminada correctamente") else: print("Error al eliminar la tarea")
```
# 6. Eliminar una subtarea específica:
## Obtiene la subtarea con ID 1
```bash
subtarea = subtareas.get(pk=1)
```
## Elimina la subtarea
```bash
elimina_sub_tarea(subtarea.id)
```
## Verifica que la subtarea ya no existe
```bash
subtarea = subtareas.get(pk=1).first() if not subtarea: print("La subtarea ha sido eliminada correctamente") else: print("Error al eliminar la subtarea")
```


## :handshake: Contact

Rolando Bergmann - - rolando.bergmann.p@gmail.com

Project Link: [https://github.com/rolobergmann/desafio-7-2](https://github.com/rolobergmann/desafio-7-2)
