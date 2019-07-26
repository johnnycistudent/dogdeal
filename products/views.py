from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductSelling, ProductWanted, Comment


# Create your views here.
def all_dogs_selling(request):
    dogs_for_sale = ProductSelling.objects.all()
    return render(request, "dogs_for_sale.html", {"dogs_for_sale": dogs_for_sale})
    
    
def view_dog_ad(request, pk):
    """
    Show single dog advertisement
    """
    
    ad = get_object_or_404(ProductSelling, pk=pk)
    ad.views += 1
    ad.save()
    
    return render(request, "view_dog_ad.html", {"ad": ad })
    