from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ProductSelling, ProductWanted, Comment
from .forms import AddSaleAdForm, AddWantedAdForm, AddCommentForm


# DOGS FOR SALE VIEWS #

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
    
   
    
def view_dog_ad(request, pk):
    """
    Show single Dog-for-Sale advertisement
    """
    
    ad = get_object_or_404(ProductSelling, pk=pk)
    ad.views += 1
    ad.save()
    
    return render(request, "view_dog_ad.html", {"ad": ad })

@login_required()    
def add_dog_sale_ad(request):
    """
    Allows Superusers to Add or Edit Dog-for-Sale Ad through a form
    """
    user = request.user
    
    if user.is_superuser:
        if request.method == "POST":
            form = AddSaleAdForm(request.POST)
            if form.is_valid():
                ad = form.save(commit=False)
                ad.author = request.user
                ad.save()
                return redirect('view_dog_ad', pk=ad.pk)
            else:
                messages.error(request, "Could not add Request at this time")
                return redirect('dogs_for_sale')
        else:
            form = AddSaleAdForm()
    return render(request, "add_dog_sale.html", {"form": form})    

@login_required()
def delete_dog_sale_ad(request, pk):
    """
    Allows Superusers to delete a Dog-for-Sale ad
    """
    user = request.user
    
    if user.is_superuser:
        ad_to_delete = get_object_or_404(ProductSelling, pk=pk)
        ad_to_delete.delete()
    
    messages.success(request, "Ad successfully deleted")
    return redirect('dogs_for_sale') 
        
        
    
    
# WANTED DOGS VIEWS #    

def wanted_dogs(request):
    """
    Show wanted requests.
    """
    wanted_dogs = ProductWanted.objects.all()
    return render(request, "wanted_dogs.html", {"wanted_dogs": wanted_dogs}) 


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
def delete_dog_wanted_ad(request, pk):
    """
    Allows Superusers to delete a Dog-for-Sale ad
    """
    user = request.user

    if user.is_superuser:
        wanted_ad_to_delete = get_object_or_404(ProductWanted, pk=pk)
        wanted_ad_to_delete.delete()

    
    messages.success(request, "Wanted Ad successfully deleted")
    return redirect('wanted_dogs')                 
    
@login_required()    
def add_dog_wanted_ad(request):
    """
    Allows users to Add or Edit Dog Wanted Ad through a form
    """
    
    
    if request.method == "POST":
        form = AddWantedAdForm(request.POST)
        if form.is_valid():
            wanted_ad = form.save(commit=False)
            wanted_ad.author = request.user
            wanted_ad.save()
            return redirect('wanted_dog_ad', pk=wanted_ad.pk)
        else:
            messages.error(request, "Could not add Request at this time")
            return redirect('wanted_dogs')
    else:
        form = AddWantedAdForm()
    return render(request, "add_dog_wanted.html", {"form": form})
            
                
# COMMENTS ON WANTED ADS #

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