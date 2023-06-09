from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=40)
    position = models.PositiveSmallIntegerField(default=1)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.title
