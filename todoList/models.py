from django.db import models


class TodoList(models.Model):
    content = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['date_created']

