from django import forms
from .models import Student

class CreatStudent(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    age=forms.IntegerField(widget=forms.TextInput({"class":"form-control", "type":"number"}))
    class Meta:
        model = Student
        fields = ('name', 'age','teacher','group')

