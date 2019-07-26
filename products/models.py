from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ProductSelling(models.Model):
    GENDER_CHOICES = (('Male', 'Male'),
        ('Female', 'Female'),
        )
    STATUS = (('Available', 'Available'),
            ('Sold', 'Sold Out'),
        )
    
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    breed = models.CharField(max_length=250)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=150, blank=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    color = models.CharField(max_length=250)
    dob = models.DateField()
    location = models.CharField(max_length=250)
    status = models.CharField(choices=STATUS, default=('Available', 'Available'), max_length=150, blank=False)
    sold_date = models.DateTimeField(
        blank=True, default=None, null=True
    )
    views = models.BigIntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
        




class ProductWanted(models.Model):
    GENDER_CHOICES = (('Male', 'Male'),
        ('Female', 'Female'),
        ('No Preference', 'No preference'),
        )
    STATUS = (('Looking', 'Looking'),
            ('Found', 'Found!'),
        )
    
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    breed = models.CharField(max_length=250)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=150, blank=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    color = models.CharField(max_length=250)
    dob = models.DateField()
    location = models.CharField(max_length=250)
    status = models.CharField(choices=STATUS, default=('Looking', 'Looking'), max_length=150, blank=True)
    sold_date = models.DateTimeField(
        blank=True, default=None, null=True
    )
    views = models.BigIntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    posted_by = models.ForeignKey(User, null=True,
        			on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
        
class Comment(models.Model):
    product = models.ForeignKey(ProductWanted, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(null=True, blank=True, default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment        