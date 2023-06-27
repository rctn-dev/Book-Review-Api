from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    date_released=models.DateTimeField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} written by {self.author}'

class Comment(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment=models.TextField(blank=True, null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return f'{self.user} rated {self.book} with {self.rating} points'
    


