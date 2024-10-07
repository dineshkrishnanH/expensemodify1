from django import forms

from budget.models import Expense

from django. contrib. auth.models import User

class ExpenseForm(forms.ModelForm):

    class Meta:

        model=Expense

        #fields="__all__"

        exclude=("created_date","status","udated_date")

        widgets={
            
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "amount":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter amount","style":"width: 100%; font-size: 16px;"}),
            "due_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "user":forms.Textarea(attrs={"class":"form-control"}),
            "category":forms.Textarea(attrs={"class":"form-control form-select custom-category-class","style":"width: 100%; padding: 16px;"}),

        }

class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","password"]

        widgets={
            "password":forms.PasswordInput()
        }



class SignInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField(widget=forms.PasswordInput())