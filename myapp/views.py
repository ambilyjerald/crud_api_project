
from django.shortcuts import render
from rest_framework import generics

from myapp.models import staff
from myapp.serializer import staff_serializer


# Create your views here.
class staff_list_generic_view(generics.ListCreateAPIView):
    queryset = staff.objects.all()
    serializer_class = staff_serializer


class staff_list_generic_view_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = staff.objects.all()
    serializer_class = staff_serializer
