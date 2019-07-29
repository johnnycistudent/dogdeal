from django.shortcuts import render
from django.db.models import Q
from products.models import ProductSelling, ProductWanted

# Create your views here.
def do_search(request):
	query = ProductSelling.objects.filter(description__icontains=request.GET['q'])
	
	# query = request.GET.get('query')
	
	# if query:
		
	# 	products = ProductSelling.objects.filter(
	# 								Q(title__icontains=query) |
	# 								Q(description__icontains=query) |
	# 								Q(breed=query) |
	# 								Q(location__icontains=query)
	# 								)
									
	# # # 	dogs_wanted = ProductWanted.objects.filter(
	# # # 								Q(title__icontains=query) |
	# # # 								Q(description__icontains=query) |
	# # # 								Q(breed=query) |
	# # # 								Q(location__icontains=query)
	# # # 								)							
		
	return render(request, "search.html", {"query": query} ) 
	