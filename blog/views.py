
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CommentForm
from django.urls import reverse
from blog.models import Galeria, Post, Category_post, Comment, UserFavorites
from django.views.generic import ListView
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
   
# Create your views here.

# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    galeria2 = Galeria.objects.order_by('id')
    posts2 = Post.objects.filter(status=1).order_by('-visit_num')

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    paginador=Paginator(posts, 8)
    num_pagina=request.GET.get('page')
    ult_post= paginador.get_page(num_pagina)

    paginador2=Paginator(posts2, 5)
    num_pagina2=request.GET.get('page')
    ult_post2= paginador2.get_page(num_pagina2)
    cat=Category_post.objects.all()
    
    paginadorgal=Paginator(galeria2, 12)
    num_gal=request.GET.get('1')
    galeria=paginadorgal.get_page(num_gal)
    


    context = {
        'page_obj': page_obj,
        'galeria': galeria,
        'ult_post':ult_post,
        'ult_post2':ult_post2,
        "categoria":cat,
    }
    return render(request, "index.html", context)


def blog_index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
   
    

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    paginator2 = Paginator(posts, 15)
    page_number2 = request.GET.get('page')
    page_obj2 = paginator2.get_page(page_number2)
    total=len(posts)
    actual=len(page_obj2)
    cat=Category_post.objects.all()
    
    context = {
        'page_obj': page_obj,
        'page_obj2': page_obj2,
        'total':total,
        'actual':actual,
        'categoria':cat,
    }
    return render(request, "blog_index.html", context)



def blog_category(request, category_post):
    posts = Post.objects.filter(
        categories__name__contains=category_post
    ).order_by(
        '-created_on'
    )
    
    posts2= Post.objects.filter(status=1).order_by('-created_on')
    cat=Category_post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    paginator2 = Paginator(posts2, 6)
    page_number2 = request.GET.get('page')
    page_obj2 = paginator2.get_page(page_number2)
    total=len(posts)
    actual=len(page_obj)
    context = {
        "category_post": category_post,
         "page_obj": page_obj,
         "page_obj2": page_obj2,
         "actual":actual,
         "total":total,
         'categoria':cat,
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, slug):
    
    post = Post.objects.get(slug=slug)
    
    post.visit_num += 1
    post.save()
    
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return HttpResponseRedirect(reverse('blog_detail', args=(post.slug,)))
    else:
        comment_form = CommentForm()
    posts = Post.objects.filter(status=1).order_by('-created_on')
    

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cat=Category_post.objects.all()
  
    
    
    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        'page_obj': page_obj,
        'categoria':cat,
    }

    return render(request, "blog_detail.html", context)
#Inicio buscador

def buscar(request):
    posts_list = Post.objects.all()
    query = request.GET.get('q')
      
    if query:
            resultados="Resultados para:"
            posts_list = Post.objects.filter(Q(title__icontains=query)|Q(short_desciption__icontains=query)|Q(teatro__name__icontains=query)|Q(cine__name__icontains=query)|Q(categories__name__icontains=query)|Q(content__icontains=query)).distinct()
            cantidad=(len(posts_list))
            paginator = Paginator(posts_list, 2)
            page_number = request.GET.get('page')
            try:
                posts = paginator.page(page_number)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            total=len(posts_list)
            cat=Category_post.objects.all()
            actual=len(posts)
            context = {
               'posts': posts,
               "resultados":resultados,
                "cantidad":cantidad,
                "nombre":query,
                "page_obj2":posts,
                "actual":actual,
                "total":total,
                "categoria":cat,

                }
        
            
            return render (request, "search.html",  context )
    else:
        mensaje="No ingreso ningun dato"
        
        return render (request, "search.html",{"mensaje":mensaje})


        


#seccion de contacto
def contact(request):
    contact_form = ContactForm()
    cat=Category_post.objects.all()
    myDate = datetime.now()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            subject = request.POST.get('subject', '')

          
            email = EmailMessage(
                "Super Cultural: Nuevo mensaje de contacto",
                "Hola Recibiste un mensaje desde el \nformulario de contacto De: {}\n Email {}\n Asunto: {} \nEscribió:\n\n{}".format(name, email, subject, content),
                "contacto@supercultural.com.ar",
                ["natalibirri@gmail.com"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "contact.html",{'form':contact_form, 'myDate':myDate, 'categoria':cat,})


def about(request):
    cat=Category_post.objects.all()
    return render(request, "about.html",{'categoria':cat})

def favorite(request, pk):
        favorite = Post.objects.get(pk=pk)
        favorites=UserFavorites.objects.all()

        favorites.user = request.user
        favorites.favoritos.add(favorite)
        favorites.save()
        messages.add_message(request, messages.INFO, 'Deal Favorited.')
        return redirect('index')

def favourites(request, slug):

    post = get_object_or_404(UserFavorites, id=slug)
    if post.favoritos.filter(id=request.user.ide).exist():
        post.favourites.remove(request.user)
    else:
        post.favoritos.add(request.user)
        
    
    return render(request, 'post_detail.html')

    