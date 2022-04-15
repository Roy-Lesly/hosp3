from django.db import models


# Create your models here.
class ActivationKey(models.Model):
    KEYS = (('1', 'RDV1P'),
            ('2', 'POTRJ'),
            ('3', 'XZHDS'),
            ('4', 'FIBQN'),
            ('5', '32JKS'),)
    key = models.CharField(max_length=5, unique=True, default='', choices=KEYS)
    duration = models.DurationField(max_length=50, )
