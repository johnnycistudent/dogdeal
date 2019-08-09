{"changed":true,"filter":false,"title":"models.py","tooltip":"/products/models.py","value":"from django.db import models\nfrom django.contrib.auth.models import User\nfrom django.utils import timezone\n\n# Create your models here.\nclass ProductSelling(models.Model):\n    GENDER_CHOICES = (('Male', 'Male'),\n        ('Female', 'Female'),\n        )\n    STATUS = (('Available', 'Available'),\n            ('Sold', 'Sold Out'),\n        )\n    \n    title = models.CharField(max_length=250, blank=False)\n    description = models.TextField()\n    published = models.DateTimeField(auto_now_add=True)\n    price = models.DecimalField(max_digits=6, decimal_places=2)\n    breed = models.CharField(max_length=250)\n    gender = models.CharField(choices=GENDER_CHOICES, max_length=150, blank=True)\n    image = models.ImageField(upload_to=\"images\", blank=True, null=True)\n    color = models.CharField(max_length=250)\n    dob = models.DateField()\n    location = models.CharField(max_length=250)\n    status = models.CharField(choices=STATUS, default=('Available', 'Available'), max_length=150, blank=False)\n    sold_date = models.DateTimeField(\n        blank=True, default=None, null=True\n    )\n    views = models.BigIntegerField(default=0)\n    upvotes = models.IntegerField(default=0)\n    \n    def __str__(self):\n        return self.title\n        \n\n\n\n\nclass ProductWanted(models.Model):\n    GENDER_CHOICES = (('Male', 'Male'),\n        ('Female', 'Female'),\n        ('No Preference', 'No preference'),\n        )\n    STATUS = (('Looking', 'Looking'),\n            ('Found', 'Found!'),\n        )\n    \n    title = models.CharField(max_length=250, blank=False)\n    description = models.TextField()\n    published = models.DateTimeField(auto_now_add=True)\n    price = models.DecimalField(max_digits=6, decimal_places=2)\n    breed = models.CharField(max_length=250)\n    gender = models.CharField(choices=GENDER_CHOICES, max_length=150, blank=True)\n    image = models.ImageField(upload_to=\"images\", blank=True, null=True)\n    color = models.CharField(max_length=250)\n    dob = models.DateField()\n    location = models.CharField(max_length=250)\n    status = models.CharField(choices=STATUS, default=('Looking', 'Looking'), max_length=150, blank=True)\n    sold_date = models.DateTimeField(\n        blank=True, default=None, null=True\n    )\n    views = models.BigIntegerField(default=0)\n    upvotes = models.IntegerField(default=0)\n    posted_by = models.ForeignKey(User, null=True,\n        \t\t\ton_delete=models.CASCADE)\n    \n    def __str__(self):\n        return self.title\n        \n        \nclass Comment(models.Model):\n    product = models.ForeignKey(ProductWanted, on_delete=models.CASCADE, related_name='comments')\n    created_on = models.DateTimeField(null=True, blank=True, default=timezone.now)\n    author = models.ForeignKey(User, on_delete=models.CASCADE)\n    comment = models.TextField()\n\n    def __str__(self):\n        return self.comment        ","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":66,"column":23},"end":{"row":66,"column":24},"action":"remove","lines":["e"],"id":2},{"start":{"row":66,"column":22},"end":{"row":66,"column":23},"action":"remove","lines":["m"]},{"start":{"row":66,"column":21},"end":{"row":66,"column":22},"action":"remove","lines":["a"]},{"start":{"row":66,"column":20},"end":{"row":66,"column":21},"action":"remove","lines":["n"]}],[{"start":{"row":66,"column":20},"end":{"row":66,"column":21},"action":"insert","lines":["t"],"id":3},{"start":{"row":66,"column":21},"end":{"row":66,"column":22},"action":"insert","lines":["i"]},{"start":{"row":66,"column":22},"end":{"row":66,"column":23},"action":"insert","lines":["t"]},{"start":{"row":66,"column":23},"end":{"row":66,"column":24},"action":"insert","lines":["l"]},{"start":{"row":66,"column":24},"end":{"row":66,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"remove","lines":["    dob = models.DateField()",""],"id":5}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564495682779}