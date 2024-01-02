from django.db import models
from django.template.defaultfilters import slugify

class Record(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    msisdn = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True,null=True)
    attended = models.CharField(max_length=3, default="no")
    no_of_uses = models.IntegerField(default=0)  
    number = models.CharField(max_length=20, default='No number given')

    def __str__(self):
        
        return f"{self.first_name} {self.last_name} - {self.code}"
    
class Event(models.Model):
    event_title = models.CharField(max_length=50)
    validation_field = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    dataset = models.FileField(upload_to='datasets/')
    
    def __str__(self):
        return self.event_title
    
    def save(self, *args, **kwargs): 
        self.validation_field = self.validation_field.lower()
        self.slug = slugify(self.event_title)
        super().save(*args, **kwargs)
        
# This model stores daily attendance details 
class AttendanceRecord(models.Model): 
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendance_records', null=True)
    present = models.JSONField(default=list)
    absent = models.JSONField(default=list)
    checked_in = models.JSONField(default=dict)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self): 
        return f'{self.database.database_title} records {self.id}'


        

        
