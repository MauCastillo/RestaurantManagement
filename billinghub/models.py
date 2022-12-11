from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    document = models.IntegerField(
        default=1,
        unique=True,
        validators=[
            MaxValueValidator(999999999999),
            MinValueValidator(999999)
        ]
    )
    
    def __str__(self):
        return self.first_name

class Bill(models.Model):
    class Meta:
        unique_together = (('bill_date', 'price','client'))
        
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    creation_date = models.DateField()
    modified_date = models.DateField()
    bill_date = models.DateField()
    price =  models.IntegerField(
        default=100,
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(-999999)
        ]
    )
    
    def __str__(self):
        return "%s %s %s" % (self.client, self.bill_date, self.price)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.creation_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Bill, self).save(*args, **kwargs)