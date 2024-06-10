from django.urls import path, include

from myapp import views

urlpatterns = [

    path('staff_list_generic_view/',views.staff_list_generic_view.as_view(),name='staff_list_generic_view'),
    path('staff_list_generic_view_detail/<int:pk>/',views.staff_list_generic_view_detail.as_view(),name='staff_list_generic_view_detail'),

]
