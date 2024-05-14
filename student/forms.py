from django import forms
from .models import Student

class CreatStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'age','teacher','group')

