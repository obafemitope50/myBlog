from unicodedata import name
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts':posts})


# Create your views here.
def about(request):
    return render(request, "about.html")

# Create your views here.
def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, "post.html", {'posts':posts})


# Create your views here.
def contact(request):
    if request.method == "POST":   
        name = request.POST['name']
        email = request.POST['email'] 
        
        subject = "Website Inquiry"
        body = {
        'name': request.POST['name'],
        'email' : request.POST['email'],
        'phone_number' : request.POST['phonenumber'],
        'message' : request.POST['message'],
        }
        message = "\n".join(body.values())
        #send mail
        send_mail (subject, 
                  message,
                  email,
                  ['obafemitope18@yahoo.com'], #receiving-email, as a list
                ) 
        
        return render(request, "contact.html", {'name':name})
    else:
        return render(request, "contact.html", {})
    



# def contact(request):
#     if request.method == "POST": 
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#             body = {
#                 'name': form.cleaned_data['name'],
#                 'email': form.cleaned_data['email'],
#                 'phonenumber': form.cleaned_data['phonenumber'],
#                 'message': form.cleaned_data['message'],      
#             }
#             message = "\n".join(body.values())
#             try:
#                 send_mail(subject, message, 'admin@example', ['admin@example'])
#             except BadHeaderError:
#                 return HttpResponse ('Invalid header found.')
            
#             return redirect ("backend:index")
#     form = ContactForm
#     return render(request, "contact.html", {'form':form})