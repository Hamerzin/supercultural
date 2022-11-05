

# Register your models here.
from django.contrib import admin
from blog.models import Notas, Post, Category_post, Comment, Teatros, Cines, Profile, Galeria, UserFavorites
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'short_desciption', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class NotasAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_filter = ("status",)
    list_display = ('title', 'slug', 'short_desciption', 'status','created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class TeatrosAdmin(SummernoteModelAdmin):
     summernote_fields = ('descripcion',)
     list_filter = ("name",)
     list_display = ('name', 'ubicacion','imagen1','pagina')
     search_fields = ['title', 'content']
     



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')



admin.site.register(Post, PostAdmin)
admin.site.register(Notas, NotasAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category_post)
admin.site.register(Teatros,TeatrosAdmin)
admin.site.register(Cines)
admin.site.register(Profile)
admin.site.register(Galeria)
admin.site.register(UserFavorites)


