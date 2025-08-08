from django.shortcuts import render 

# Importing class-based views to easily list and display book details.
from django.views.generic import ListView, DetailView

#Allows creating forms to add objects
from django.views.generic.edit import CreateView

#Adds login protection to views — redirects user to login page if not logged in.
from django.contrib.auth.mixins import LoginRequiredMixin 

#Importing your models: Book and Order to interact with the database.
from .models import Book, Order

#For search functionality – allows combining multiple filters (OR logic).
from django.db.models import Q 

from django.http import JsonResponse
import json



class BooksListView(ListView): #built-in Django class to list database objects.
    model = Book   #list all objects from the Book model.
    template_name = 'list.html' # Render using list.html template.


class BooksDetailView(DetailView): #Django view for displaying a single object.
    model = Book #fetches book using pk in the URL.
    template_name = 'detail.html' #Uses detail.html to display details.


class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'
      

	def get_queryset(self): 
		query = self.request.GET.get('q') #Get the query string from the URL like /search?q=python.
		
		#Q() is used to build complex queries
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)
        #title__icontains=query: Look in the title field of the Book model.
        #Q(author__icontains=query): Same logic, but applied to the author field.


#LoginRequiredMixin: Forces user to log in.
#DetailView: Shows book details for confirmation before purchase.
#login_url = 'login' → Where to redirect if user isn’t logged in.
class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url     = 'login'


#request.body → Raw request body from frontend (likely from JavaScript).
#json.loads(...) → Converts JSON string to Python dictionary.
#body['productId'] → Extracts product ID sent from frontend.
#Book.objects.get(...) → Finds the product using that ID.
#Order.objects.create(...) → Creates a new order in DB.
#JsonResponse(...) → Returns a JSON response back to frontend.

def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Book.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)

