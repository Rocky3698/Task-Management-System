from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.category_form,name='add_category')
]