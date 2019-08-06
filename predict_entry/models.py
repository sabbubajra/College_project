from django.db import models

PHONE_CHOICES=[
    ('Yes','Yes'),
    ('No','No')
]

MULTIPLE_CHOICES=[
    ('Yes','Yes'),
    ('No','No'),
    ('No phone service','No phone service')
]

INTERNET_CHOICES=[
    ('DSL','DSL'),
    ('Fiber optic','Fiber optic'),
    ('No','No')
]

ONLINESEC_CHOICES=[
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('No internet service', 'No internet service')
]
ONLINEBAC_CHOICES=[
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('No internet service', 'No internet service')
]
STREAMOV_CHOICES=[
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('No internet service', 'No internet service')
]
STREAMTV_CHOICES=[
    ('Yes','Yes'),
    ('No','No'),
    ('No internet service','No internet service')
]
CONTRACT_CHOICES=[
    ('One year','One year'),
    ('Month-to-month','Month-to-month'),
    ('Two year','Two year')
]
PAYMENT_CHOICES=[
    ('Bank transfer (automatic)','Bank transfer (automatic)'),
    ('Credit card (automatic)','Credit card (automatic)'),
    ('Electronic check','Electronic check'),
    ('Mailed check','Mailed check')
]
TECH_CHOICES=[
    ('Yes','Yes'),
    ('No','No')
]


class Predict(models.Model):
    internet_service = models.CharField(choices=INTERNET_CHOICES, max_length=50,default=1)
    tenure = models.IntegerField(default=1)
    phone_service=models.CharField(choices=PHONE_CHOICES,max_length=50,default=1)
    multiple_lines=models.CharField(choices=MULTIPLE_CHOICES,max_length=50,default=1)
    contract=models.CharField(choices=CONTRACT_CHOICES,max_length=50,default=1)
    payment=models.CharField(choices=PAYMENT_CHOICES,max_length=50,default=1)
    online_security=models.CharField(choices=ONLINESEC_CHOICES,max_length=50,default=1)
    online_backup=models.CharField(choices=ONLINEBAC_CHOICES,max_length=30,default=1)
    stream_tv=models.CharField(choices=STREAMTV_CHOICES,max_length=50,default=1)
    stream_mov=models.CharField(choices=STREAMOV_CHOICES,max_length=50,default=1)
    tech_support=models.CharField(choices=TECH_CHOICES,max_length=50,default=1)

    def __str__(self):
        return self.internet_service