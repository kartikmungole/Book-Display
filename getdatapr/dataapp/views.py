from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render



def book_list(request):
    # Fetch the API data
    response = requests.get('http://127.0.0.1:5000/api/books')
    
    if response.status_code == 200:
        books = response.json()  # Convert the response to JSON format
    else:
        books = []  # If the API is unavailable, default to an empty list

    # Pass the books data to the template
    return render(request, 'booklists.html', {'books': books})
