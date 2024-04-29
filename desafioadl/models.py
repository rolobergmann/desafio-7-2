from django.db import models
from django.contrib import admin
# Create your models here.

class Tarea(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.TextField(max_length=255, default="")
    eliminada = models.BooleanField(default=False)

    class Meta:
        db_table = "tarea"

class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'eliminada')


class SubTarea(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE, null=False)
    descripcion = models.TextField(max_length=255, default="")
    eliminada = models.BooleanField(default=False)

    class Meta:
        db_table = "subtarea"

class SubTareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tarea_id', 'descripcion', 'eliminada')
