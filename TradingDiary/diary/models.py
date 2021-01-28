from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    coin = models.CharField(max_length=100)
    price1 = models.IntegerField(blank=True,default=0)
    price2 = models.IntegerField(blank=True,default=0)
    number = models.IntegerField(blank=True,default=0)
    stoploss = models.IntegerField(blank=True,default=0)
    takeprofit = models.IntegerField(blank=True,default=0) 
    content = models.TextField()
    date_posted = models.DateTimeField(null=True, blank=True)
    # AUTHOR    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # MOOD
    EPIC = 'EP'
    GREAT = 'GR'
    NEUTRAL = 'NE'
    BAD = 'BA'
    PATHETIC = 'PA'
    MOOD_CHOICES = [
        (EPIC, 'Epic'),
        (GREAT, 'Great'),
        (NEUTRAL, 'Neutral'),
        (BAD, 'Bad'),
        (PATHETIC, 'Pathetic'),
    ]
    mood = models.CharField(
        max_length=2,
        choices=MOOD_CHOICES,
        default=NEUTRAL,
    )
    # LONG SHORT  
    LONG = 'LO'
    SHORT = 'SH'
    LONG_CHOICES = [
        (LONG, 'Long'),
        (SHORT, 'Short')
    ]
    long = models.CharField(
        max_length=2,
        choices=LONG_CHOICES,
        default=LONG,
    )
    # FORMATION 
    NOTHING = 'NO'
    TREND_LINE = 'TR'
    HEAD_AND_SHOULDERS = 'HS'
    SUPPORT_LINE = 'SL'
    RESISTANCE_LINE = 'RL'
    FORMATION_CHOICES = [
        (NOTHING, 'Nothing'),
        (TREND_LINE, 'Trend line'),
        (HEAD_AND_SHOULDERS, 'Head and shoulders'),
        (SUPPORT_LINE, 'Support line'),
        (RESISTANCE_LINE, 'Resistance line'),
    ]
    formation = models.CharField(
        max_length=2,
        choices=FORMATION_CHOICES,
        default=NOTHING,
    )
    # WHY OPEN?
    BOUNCE_LEVEL = 'BL'
    COMING_LEVEL = 'CL'
    FIBO = 'FI'
    BOUNCE_TREND = 'BT'
    COMING_TREND = 'CT'
    FALSE_LINE = 'FL'
    FALSE_LEVEL = 'FE'
    TRIANGLE = 'TR'
    FALSE_BREAKOUT = 'FB'







    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('diary:post-detail', kwargs={'pk': self.pk}) 
    