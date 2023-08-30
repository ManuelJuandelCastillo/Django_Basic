from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    # metodo que muestra el nombre del proyecto en el panel de admin
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)

    #agregamos una clave foranea para seleccionar el proyecto al que pertenece la tarea
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #el parametro on_delete=models.CASCADE elimina las tareas cuando se elimina el proyecto al que pertenecen

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name
    