


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import CommentForm
from django.urls import reverse
from blog.models import Galeria, Post, Category_post, Comment
from django.views.generic import ListView
from django.db.models import Q
   
# Create your views here.

# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    galeria = Galeria.objects.order_by('id')
    posts2 = Post.objects.filter(status=1).order_by('-visit_num')

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    paginador=Paginator(posts, 8)
    num_pagina=request.GET.get('page')
    ult_post= paginador.get_page(num_pagina)

    paginador2=Paginator(posts2, 8)
    num_pagina2=request.GET.get('page')
    ult_post2= paginador2.get_page(num_pagina2)


    context = {
        'page_obj': page_obj,
        'galeria': galeria,
        'ult_post':ult_post,
        'ult_post2':ult_post2,
    }
    return render(request, "index.html", context)


def blog_index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
   
    

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, "blog_index.html", context)



def blog_category(request, category_post):
    posts = Post.objects.filter(
        categories__name__contains=category_post
    ).order_by(
        '-created_on'
    )
    
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "category_post": category_post,
         "page_obj": page_obj,
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    
    post = Post.objects.get(pk=pk)
    
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
            return HttpResponseRedirect(reverse('blog_detail', args=(post.pk,)))
    else:
        comment_form = CommentForm()
    posts = Post.objects.filter(status=1).order_by('-created_on')
    

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
  
    
    
    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        'page_obj': page_obj,
    }

    return render(request, "blog_detail.html", context)
#Inicio buscador

def buscar(request):
      if request.method=="POST":
            search = request.POST['search']
            print(search)
            if search !="":
                  resultados="Resultados para:"
                  prods = Post.objects.filter(Q(title__icontains=search)|Q(short_desciption__icontains=search)|Q(teatro__name__icontains=search)|Q(cine__name__icontains=search)|Q(categories__name__icontains=search)|Q(content__icontains=search))
                  cantidad=(len(prods))                
                  return render(request, "search.html", {"productos": prods, "nombre":search, "search":True, "resultados":resultados, "cantidad":cantidad} )
                  
            else:
             output = "No ingresaste ningun dato"
             return render(request, "search.html", {'mensaje':output})