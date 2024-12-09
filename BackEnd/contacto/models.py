from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre