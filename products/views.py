from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ProductSelling, ProductWanted, Comment
from .forms import AddCommentForm


# Create your views here.
def all_dogs_selling(request):
    """
    Show all dogs for sale.
    """
    dogs_for_sale = ProductSelling.objects.all().order_by('published')
    paginator = Paginator(dogs_for_sale, 6)
    page = request.GET.get('page')
    try:
        dogs_for_sale = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dogs_for_sale = paginator.page(1)
    except EmptyPage:
        dogs_for_sale = paginator.page(paginator.num_pages)    
        
    return render(request, "dogs_for_sale.html", {"dogs_for_sale": dogs_for_sale})
    
def wanted_dogs(request):
    """
    Show wanted requests.
    """
    wanted_dogs = ProductWanted.objects.all()
    return render(request, "wanted_dogs.html", {"wanted_dogs": wanted_dogs})    
    
def view_dog_ad(request, pk):
    """
    Show single dog for sale advertisement
    """
    
    ad = get_object_or_404(ProductSelling, pk=pk)
    ad.views += 1
    ad.save()
    
    return render(request, "view_dog_ad.html", {"ad": ad })
    

@login_required()
def delete_dog_sale_ad(request, pk):
    """
    Allows Superusers to delete a dog for sale ad
    """
    user = request.user
    
    if user.is_superuser:
        ad_to_delete = get_object_or_404(ProductSelling, pk=pk)
        ad_to_delete.delete()
    
    messages.success(request, "Ad successfully deleted")
    return redirect('dogs_for_sale') 
        
        
    
    
def view_wanted_dog_ad(request, pk):
    """
    Show single dog advertisement
    """
    
    wanted_ad = get_object_or_404(ProductWanted, pk=pk)
    wanted_ad.views += 1
    wanted_ad.save()
    comments = Comment.objects.filter(product=pk).order_by('created_on')
    
    return render(request, "wanted_dog_ad.html",
                {"wanted_ad": wanted_ad,
                'comments': comments,
                })    
                

@login_required()             
def add_comment(request, pk):                
    product = get_object_or_404(ProductWanted, pk=pk)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
    
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.product = product
            comment.save()
            return redirect('wanted_dog_ad', pk=product.pk)
    else:
        form = AddCommentForm(request.POST)
    return render(request, "add_comment_wanted.html", {"form": form})
    
@login_required()
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product = comment.product
    comment.delete()
    return redirect('wanted_dog_ad', pk=product.pk)    