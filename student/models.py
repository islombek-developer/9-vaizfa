from django.db import models



class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_taught')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='groups_taught')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#=============================

class Category(models.Model):
    name=models.CharField(max_length=100)
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    Category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

