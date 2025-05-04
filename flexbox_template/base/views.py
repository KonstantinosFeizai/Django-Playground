from django.shortcuts import render

# Create your views here.
# Views are python function that take a web request and return a web response.
# The web response can be HTML, JSON, XML, or an image. It can also be a redirect or a 404 error.
# The view function is called when the URL pattern is matched. The view function takes a request object as an argument and returns a response object.
# The request object contains information about the request, such as the HTTP method (GET, POST, etc.), the URL, and any data sent with the request.
# The response object contains information about the response, such as the HTTP status code, the content type, and the data to be sent back to the client.
# The view function can also access the database and perform any necessary logic before returning the response.


def home(request):
    return render(request, 'base/home.html')
