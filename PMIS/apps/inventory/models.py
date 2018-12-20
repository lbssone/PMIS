from django.db import models

# Create your models here.        
        
class Material(models.Model):
    number = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, null=True)
    inventory = models.PositiveIntegerField(blank=True, null=True)
    level =  models.PositiveIntegerField(blank=True, null=True)
    # related_components = models.ForeignKey(Component, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Component(models.Model):
    number = models.PositiveIntegerField(blank=True, null=True)
    number_needed = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, null=True)
    inventory = models.PositiveIntegerField(blank=True, null=True)
    level =  models.PositiveIntegerField(blank=True, null=True)
    required_material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    number = models.PositiveIntegerField(blank=True, null=True)
    UV = '抗UV'
    WIND = '防風'
    LIGHT = '輕量'
    FEATURE_CHOICES = (
        (UV, '抗UV'),
        (WIND, '防風'),
        (LIGHT, '輕量')
    )
    u_feature = models.CharField(
        max_length=50,
        choices=FEATURE_CHOICES,
        null=True,
    )
    STRAIGHT = '直傘'
    AUTO_F = '自動摺傘'
    MANUAL_F = '手開摺傘'
    TYPE_CHOICES = (
        (STRAIGHT, '直傘'),
        (AUTO_F, '自動摺傘'),
        (MANUAL_F, '手開摺傘')
    )
    u_type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        null=True,
    )
    inventory = models.PositiveIntegerField(blank=True, null=True)
    level =  models.PositiveIntegerField(blank=True, null=True)
    components_required = models.ManyToManyField(Component, blank=True)

    def __str__(self):
        return '{}{}'.format(self.u_feature, self.u_type)

    def getComponents(self):
        return self.components_required.all() 
         
    @property
    def name(self):
        return '{}{}'.format(self.u_feature, self.u_type)
