from django.db import models

# Create your models here.


class Expense(models.Model):

    title=models.CharField(max_length=100)

    amount=models.DecimalField(max_digits=100, decimal_places=2)

    created_date=models.DateTimeField(auto_now_add=True)

    user=models.CharField(max_length=200)

    due_date=models.DateTimeField(null=True)

    category_choices=(
        ("food","food"),
        ("travel","travel"),
        ("health","health"),
        ("others","others"),
    )

    category=models.CharField(max_length=200,choices=category_choices,)

    status_choices=(
        ("others","others"),
        ("in-progress","in-progress"),
        ("done","done")
    )

    status=models.CharField(max_length=200,choices=status_choices,)
    updated_date=models.DateField(auto_now=True)

    user=models.CharField(max_length=200)

    def __str__(self) -> str:
        
        return self.title