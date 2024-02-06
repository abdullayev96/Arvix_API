from django.db import models




class Category(models.Model):
     name  = models.CharField(max_length=300, verbose_name="Kategoriya:")

     def __str__(self):
          return self.name


     class Meta:
         verbose_name = "Kategoriya_"



class MyResult(models.Model):
     NEW = "Birinchi topshirish"
     EXECUTION = "Qayta topshirish"


     STATUS_CHOICES = (
          (NEW, 'Birinchi topshirish'),
          (EXECUTION, 'Qayta topshirish'),

     )
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
     status = models.CharField(max_length=30, choices=STATUS_CHOICES,
                               verbose_name="Turi:",default="Birinchi topshirish")
     result = models.CharField()
     file = models.FileField(upload_to="web/")
     date = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.date


     class Meta:
          verbose_name = "Mening Natijalarim_"




