from django.shortcuts import render ,redirect
from .forms import CategoryForm
# Create your views here.
def category_form(request):
    if request.method=='POST':
        category_form=CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form=CategoryForm(request.POST)

    return render(request,'category_form.html',{'form':category_form})