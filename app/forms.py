from django import forms
def check_for_a(value):
    if value[0]=='S':
        raise forms.ValidationError('name starts with S')



def lenght(value):
    if len(value)<5:
        raise forms.ValidationError('invalid')
    






class Studentform(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_a,lenght])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField()
    