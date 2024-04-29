from django.contrib import admin
from .models import Tarea, SubTarea, TareaAdmin, SubTareaAdmin

# Register your models here.
admin.site.register(Tarea, TareaAdmin)
admin.site.register(SubTarea, SubTareaAdmin)