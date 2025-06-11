from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="cafe.images/")
    
    def __str__(self):
        return self.name 
    
    
class About(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_creation = models.CharField(max_length=50)
    image = models.ImageField(upload_to="about.images/")
    
    def __str__(self):
        return self.title
    
    
class Work_Team(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="work_team.images/")
    duty = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title
    
    
class Menu(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu.images/")
    content = models.TextField()
    price = models.IntegerField(default=0, blank=True, null=True)
    meals = models.CharField(max_length=200)
    drinks = models.CharField(max_length=200)
    recommend = models.CharField(max_length=50)
    discount = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Reviews(models.Model):
    name = models.CharField(max_length=100)
    content =models.TextField()
    rating = models.IntegerField(default=0, blank=True, null=True)
    evaluation = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="contact.images/")
    email = models.EmailField(max_length=256)
    content = models.TextField()
    location = models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
    
class Reservation(models.Model):
    name =models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    number_of_people = models.CharField(max_length=3)
    check_in_date = models.DateField()
    time = models.IntegerField(default=0, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="reservation.images/")
    
    
    
    def __str__(self):
        return self.name
    
class PeopleNumber(models.Model):
    number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.number 
    
    
    
class SiteSettings(models.Model):
    atitle = models.CharField(max_length=100, blank=True, null=True)
    amidle_title = models.CharField(max_length=100, blank=True, null=True)
    amidle_content = models.TextField(blank=True, null=True)
    subtitle = models.CharField(max_length=50, blank=True, null=True)
    phone = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    imiddleinfo = models.CharField(max_length=150, blank=True, null=True)
    opening_Hours = models.CharField(max_length=100)
    time = models.IntegerField(default=0, blank=True, null=True)
    icon = models.URLField(blank=True, null=True)
    button = models.CharField()
    
    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
        
    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings,self).save(*args, **kwargs)
        
    def __str__(self):
        return "Settings"  