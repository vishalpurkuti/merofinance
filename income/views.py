from django import forms
from django.http import request
from django.shortcuts import redirect, render
from . forms import AddIncomeCategoryForm
# Create your views here.


def addIncomeCategory(request):
    if request.method == 'GET':
        form = AddIncomeCategoryForm()
        context = {
            'form': form
        }
        return render(request, 'pages/add_income_form.html', context)
    else:
        myform = AddIncomeCategoryForm(request.POST)
        data = myform.save(commit=False)
        data.user = request.user
        data.save()
        return redirect('account')
