from .models import Employee
from django import forms
from django.contrib.auth.models import User

class EmployeeForms(forms.ModelForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Employee
        fields = ['employee_id','department','phone','address']


    def clean(self):
      cleaned_data = super().clean()
      p1=cleaned_data.get('password1')
      p2=cleaned_data.get('password2')

      if p1 and p2 and p1 != p2:
        raise forms.ValidationError("Password doesnt match")
      return cleaned_data

    def save(self, commit = True):
         # Get form data
      cleaned_data = self.cleaned_data
      username = cleaned_data.get('username')
      password = cleaned_data.get('password1')

     # Create user
      user = User(username = username)
      user.set_password(password)
      user.save()

     # Create employee instance
      employee = super().save(commit=False)
      employee.user = user
  
      if commit:
        employee.save()
    
      return employee
