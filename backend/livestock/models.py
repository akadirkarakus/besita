from datetime import date, timedelta
from django.db import models
from django.utils import timezone

class Breed(models.Model):
    
    breed_name = models.CharField(max_length=50) #VARCHAR
    comment = models.TextField(blank=True, null=True) #TEXT
    status = models.BooleanField(default=1)
    
    def __str__(self):
        return self.breed_name
    
    
class Paddock(models.Model):
    
    paddock_name = models.CharField(max_length=20)
    capacity = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=1)
    
    def __str__(self):
        return self.paddock_name
    
    
class Animal(models.Model):
    
    HEALTH_STATUS_CHOICES = [
        ('healthy', 'Sağlıklı'),
        ('sick', 'Hasta'),
        ('ready_for_sale', 'Kesime Hazır')
    ]
    
    gender_choises = [('e','Erkek'),('d','Dişi')]
    kupe_no = models.CharField(unique=True, max_length=20)
    rfid_no = models.CharField(unique=True, max_length=20)
    gender = models.CharField(choices=gender_choises, max_length=1)
    birth_date = models.DateField(blank=True, null=True)
    breed_no = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, verbose_name="Irkı")
    paddock_no = models.ForeignKey(Paddock, on_delete=models.SET_NULL, null=True)
    health_status = models.CharField(max_length=20, choices=HEALTH_STATUS_CHOICES, default='healthy', verbose_name="Sağlık Durumu")
    health_status_updated_at = models.DateTimeField(auto_now=True, verbose_name="Sağlık Durumu Güncellenme Tarihi")
    health_notes = models.TextField(blank=True, null=True, verbose_name="Sağlık Notları")
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.kupe_no
    
    @property
    def age(self):
        if self.birth_date:
            result = date.today() - self.birth_date
            return result
        else:
            return None
    
    
        
        
        
    class Meta:
        verbose_name = "Hayvan"
        verbose_name_plural = "Hayvanlar"
    

class WeightRecord(models.Model):
    
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE,related_name="weights", verbose_name="Hayvan" )
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ağırlık (kg)")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Tarım Tarihi")
    batch_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="Toplu Tartım Kodu")
    notes = models.TextField(blank=True, null=True, verbose_name="Tartım Notları")
    
    def get_weight_gain(self):
        """Önceki tartımdan kaç kilo artış"""
        previous = WeightRecord.objects.filter(
            animal_id=self.animal_id, 
            date__lt=self.date
        ).order_by('-date').first()
        
        if previous:
            return round(float(self.weight) - float(previous.weight), 2)
        return None
    
    def get_daily_gain(self):
        """Tartımlar arası günlük ortalama kilo artışı"""
        weight_gain = self.get_weight_gain()
        if weight_gain is None:
            return None
        
        previous = WeightRecord.objects.filter(
            animal_id=self.animal_id, 
            date__lt=self.date
        ).order_by('-date').first()
        
        if previous:
            days_diff = (self.date.date() - previous.date.date()).days
            if days_diff > 0:
                return round(weight_gain / days_diff, 3)
        return None
        
            
        
    def __str__(self):
        return f"{self.animal_id.kupe_no} - {self.weight} kg - {self.date.strftime('%d.%m.%Y')}"
    
    class Meta:
        verbose_name = "Tartım Kaydı"
        verbose_name_plural = "Tartım Kayıtları"
        ordering = ['-date']    
        