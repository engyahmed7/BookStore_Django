from django.db import models

# Create your models here.
class BokkStore(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    rate = models.PositiveBigIntegerField()
    views = models.IntegerField()
    published = models.DateField()

    def __str__(self):
        return f"Title: {self.title}"
    
    class Meta:
        verbose_name='Book Store' 
        verbose_name_plural='Book Stores'
