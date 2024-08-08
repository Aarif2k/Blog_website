from django.shortcuts import render
import logging
from .models import Post,About
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import Contact

# static demo data
# posts = [
#         {'id':1,'date':'January 1, 2023','title':'Post - 1','p':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla.'},
#         {'id':2,'date':'January 2, 2023','title':'Post - 2','p':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla.'},
#         {'id':3,'date':'January 3, 2023','title':'Post - 3','p':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla.'},
#         {'id':4,'date':'January 4, 2023','title':'Post - 4','p':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla.'},
#     ]



# Create your views here.
# def index(request):
#     header_h1 = "Welcome to Blog Home"
#     posts = Post.objects.all()
#     return render(request,"index.html",{'header_title':header_h1,'posts':posts})

def index(request):
    header_h1 = "Welcome to Blog Home"
    all_posts = Post.objects.all().order_by('created_at_date') 

    # Paginate
    paginator = Paginator(all_posts, 4)  # Show 4 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # for unique category
    # Fetch unique categories
    # unique_categories = set(Post.objects.values_list('category', flat=True))

    # context = {
    #     'unique_categories': unique_categories,
    # }

    return render(request, 'index.html',{'header_title': header_h1, 'page_obj': page_obj})

def error(request,exception):
    return render(request,"error_page.html",status=404)

def about(request):
    about_content = About.objects.first().content
    return render(request,"about.html",{'about_content':about_content})

# def contact(request):
#     if request.method =='POST':
#         form = ContactForm(request.POST)
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         logger = logging.getLogger("TESTING")
#         if form.is_valid():
#             logger.debug(f'post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
#             success_message = 'Your message has been recorded !'
#             return render(request,'contact.html',{'form':form,'success_message':success_message})
#         else:
#             logger.debug("Form is invalid")
#         return render(request,'contact.html',{'form':form,'name':name,'email':email,'message':message})
#     return render(request,"contact.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        logger = logging.getLogger("TESTING")
        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact.save()
            logger.debug(f'post data is {form.cleaned_data["name"]} {form.cleaned_data["email"]} {form.cleaned_data["message"]}')
            success_message = 'Your message has been recorded!'
            return render(request, 'contact.html', {'form': form, 'success_message': success_message})
        else:
            logger.debug("Form is invalid")
            return render(request, 'contact.html', {'form': form, 'name': name, 'email': email, 'message': message})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def detail(request,slug):
    
    try:
        post = Post.objects.get(slug = slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    # post = next((item for item in posts if item['id'] == detail_id),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    return render(request,"detail.html",{'post':post,'related_posts':related_posts})
