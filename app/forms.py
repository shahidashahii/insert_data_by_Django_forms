from django import forms
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    sid=forms.IntegerField()
    email=forms.EmailField()
   