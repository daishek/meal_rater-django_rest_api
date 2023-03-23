
from django.db import models
from django.db.models import Sum, Avg
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=100, help_text="Max length is 100")
    description = models.TextField(max_length=300, help_text="Max length is 300")

    def no_of_ratings(self):
        return Rating.objects.filter(meal=self).count()
    
    def avg_rating(self):
        # total = Rating.objects.filter(meal=self.id).aggregate(Sum('rate'))///qsdqs
        total = Rating.objects.filter(meal = self.id).aggregate(Sum('rate'))['rate__sum']
        ratings_count = self.no_of_ratings()
        
        if ratings_count == 0: return 0

        avg = total/ratings_count
        return avg
    def get_avg(self):
        return Rating.objects.filter(meal=self).aggregate(Avg('rate'))
    
    def __str__(self) -> str:
        return f"{self.id} - {self.title}"
    

class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"{self.id}"

    class Metta:
        unique_together = (('user', 'meal'), )
        index_together = (('user', 'meal'), )




from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)