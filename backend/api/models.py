from django.db import models

# Create your models here.


class Predict(models.Model):
    id_predict = models.AutoField(primary_key=True)
    image = models.TextField(blank=True, null=True)
    bonne_pred = models.BooleanField()
    libele = models.CharField(max_length=255, blank=True, null=True)
    jour = models.CharField(max_length=255, blank=True, null=True)
    feedback = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predict'
