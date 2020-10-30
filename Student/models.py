from django.db import models

# Create your models here.

class Student(models.Model):
    Student_id = models.AutoField(primary_key=True)
    Admission_no = models.IntegerField()
    Student_name = models.CharField(max_length=50)
    Father_name = models.CharField(max_length=50)
    Mother_name = models.CharField(max_length=50)
    Student_DOB = models.DateField()
    Student_class = models.IntegerField()
    Student_sec = models.CharField(max_length=1)
    Student_Address = models.CharField(max_length=150)
    Student_Phone = models.CharField(max_length=15)
    Student_Email = models.EmailField()
    Student_gender = models.CharField(max_length=15)
    Student_photo = models.ImageField(upload_to='Profile_Pic')

    def __str__(self):
        return self.Student_name
