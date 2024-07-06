from django.shortcuts import render , get_object_or_404 , redirect
from django.views import  View
from .models import Product
from . import tasks
from django.contrib import messages
class HomeView(View):
    template_name = 'home/home.html'
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, self.template_name , {'products':products})

class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request , 'home/detail.html' , {'product':product})


class BucketHome(View):

    template_name = 'home/bucket.html'
    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request , self.template_name , {'objects':objects})


class DeleteBucketObject(View):
    def get(self, request, key):
        tasks.delete_bucket_objects_task.delay(key)
        messages.success(request , 'your object deleting' , 'info')
        return redirect('home:bucket')