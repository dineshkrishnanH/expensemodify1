from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from budget.forms import ExpenseForm

from django.contrib import messages

from budget.models import Expense

from django import forms

from django.db.models import Q



class ExpenseCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=ExpenseForm()

        
        return render(request,"expense_create.html",{"form":form_instance})

    
    def post(self,request,*args,**kwargs):

        form_instance=ExpenseForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"expense creates successfully")

            return redirect("expense-list")
        else:

            messages.error(request,"expense is failed")

            return render(request,"expense_create.html",{"form":form_instance})
        
        
class ExpenseListView(View):

        def get(self,request,*args,**kwargs):

            search_text=request.GET.get("search_text")

            selected_category=request.GET.get("category","all")

            if selected_category == "all":
             
               qs=Expense.objects.all()

            else:
                 
                qs=Expense.objects.filter(category=selected_category)

                
            if search_text!=None:
                qs=Expense.objects.filter(Q(title__icontains=search_text)|Q(description__icontains=search_text))
             

            return render(request,"expense_list.html",{"expense":qs,"selected":request.GET.get("category",'all')})
        
        
class expenseDetialView(View):
        
        def get(self,request,*args,**kwargs):
             
             
             #extract from  id from url
             id=kwargs.get("pk")

             #fecth task object with id
             qs=Expense.objects.get(id=id)


             return render(request,"expense_detail.html",{"expense":qs})
             
class ExpenseUpdateView(View):
             
        def get(self,request,*args,**kwargs):
             
             
             #extract pk from kwargs
             id=kwargs.get("pk")


             #fecth task object with id=id
             expense_obj=Expense.objects.get(id=id)
             

             #intialize expenseform with expense_obj
             form_instance=ExpenseForm(instance=expense_obj)


             #adding status feild to from_instance
             form_instance.fields["status"]=forms.ChoiceField(choices=Expense.status_choices,widget=forms.Select(attrs={"class":"form-control form-select"}),initial=expense_obj.status)



             return render(request,"expense_edit.html",{"form":form_instance})
        
        
        def post(self,request,*args,**kwargs):
             
             #extract id from kwargs
             id=kwargs.get("pk")


             #fetch expense object with id
             expense_obj=Expense.objects.get(id=id)

             #intialize expenseform with request.POST
             form_instance=ExpenseForm(request.POST,instance=expense_obj)

             #CHECK FORM IS VALID
             if form_instance.is_valid():
                  
                  #add status to forms instance
                  form_instance.instance.status=request.POST.get("status")

                  #save form_instance
                  form_instance.save()
                  
                  #redirect to task list
                  return redirect("expense-list")
             
             else:
             
                return render(request,"expense_edit.html",{"form":form_instance})
             
             
class ExpenseDeleteView(View):

    def get(self,request,*args,**kwargs):
         
         #extract id and delete expense object with this id

        Expense.objects.get(id=kwargs.get("pk")).delete()

        return redirect("expense-list")
    
from django.db.models import Count 


class ExpenseSummaryView(View):
     
     
     def get(self,request,*args,**kwargs):
          
        qs=Expense.objects.all()

        total_expense_count=qs.count()


        category_summary=Expense.objects.all().values("category").annotate(cat_Count=Count("category"))
        print(category_summary)


        status_summary=Expense.objects.all().values("status").annotate(cat_count=Count("status"))
        print(status_summary)


        context={
                "total_expense_count":total_expense_count,

                  "category_summary":category_summary,

                  "status_summary":status_summary,
               
          }
        
        return render(request,"expense_summary.html",context)

        
     

     

           


    

