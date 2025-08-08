
from django.db import models

class Book(models.Model):
   
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

 
    # null=True → This allows the database to store NULL for this field if no value is provided.
    # blank=True → This allows Django forms (like admin or ModelForm) to accept empty values for this field.
    description = models.CharField(max_length=500, null=True, blank=True)

    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2083, null=True, blank=True)
    follow_author = models.CharField(max_length=2083, blank=True, null=True)
    book_available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"


    def __str__(self):
        return self.title


class Order(models.Model):
	product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title
