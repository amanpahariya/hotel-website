from django.db import models

# Create your models here.

class contactform(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    cell = models.CharField(max_length=10)
    info = models.CharField(max_length=500)


    class Meta:
        verbose_name_plural = "contactform"

    def __str__(self):
        return self.email


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    description =  models.CharField(max_length=500)
    images = models.ImageField(upload_to='pics')


class Book:
    mem : int
    rooms : int
    price : int
    total : int
    check1 : str
    check2 : str


class Customer_Data(models.Model):
            registration = models.AutoField(primary_key=True)
            prefix = models.CharField(max_length=5)
            first_name = models.CharField(max_length=20)
            last_name = models.CharField(max_length=20)
            email = models.CharField(max_length=50)
            cell_number = models.IntegerField()
            country = models.CharField(max_length=20)
            add1 = models.CharField(max_length=200)
            add2 = models.CharField(max_length=200)
            city = models.CharField(max_length=50)
            zip_or_postal = models.IntegerField()
            check1  = models.CharField(max_length=200)
            check2 = models.CharField(max_length=200)
            total = models.FloatField()
            mem = models.IntegerField()
            rooms = models.IntegerField()

            def __str__(self):
                return self.first_name

class creditcard(models.Model):
    cardnumber = models.CharField(primary_key=True , max_length=10)
    cvv = models.CharField(max_length=3)
    MM_YY = models.CharField(max_length=9)
    card_holder_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.cardnumber)