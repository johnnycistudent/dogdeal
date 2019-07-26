from django.shortcuts import render
from django.db.models import Q
from products.models import ProductSelling, ProductWanted

# Create your views here.
def do_search(request):
	products = ProductSelling.objects.filter(title__icontains=request.GET['q'])
	
	# query = request.GET.get('query')
	
	# # if query:
		
	# # 	dogs_on_sale = ProductSelling.objects.filter(
	# # 								Q(title__icontains=query) |
	# # 								Q(description__icontains=query) |
	# # 								Q(breed=query) |
	# # 								Q(location__icontains=query)
	# # 								)
									
	# # 	dogs_wanted = ProductWanted.objects.filter(
	# # 								Q(title__icontains=query) |
	# # 								Q(description__icontains=query) |
	# # 								Q(breed=query) |
	# # 								Q(location__icontains=query)
	# # 								)							
		
	return render(request, "dogs_for_sale.html", {"products": products} ) 
	