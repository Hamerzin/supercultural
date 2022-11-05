
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar= models.ImageField(upload_to='profileimg/',default='no-avatar.jpg')
    
# Create your models here.
class Cines(models.Model):
    name=models.CharField(max_length=250)
    ubicacion=models.CharField(max_length=250)
    linkmaps=models.CharField(max_length=500,blank=True, null=True)
    imagen1=models.ImageField(upload_to='cines/', blank=True, null=True)
    imagen2=models.ImageField(upload_to='cines/', blank=True, null=True)
    pagina=models.CharField(max_length=250,blank=True, null=True)
    descripcion=models.TextField()
    def __str__(self):
        return self.name
    

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Teatros(models.Model):
    name=models.CharField(max_length=250)
    ubicacion=models.CharField(max_length=250)
    linkmaps=models.CharField(max_length=500,blank=True, null=True)
    imagen1=models.ImageField(upload_to='teatros/', blank=True, null=True)
    imagen2=models.ImageField(upload_to='teatros/', blank=True, null=True)
    pagina=models.CharField(max_length=250,blank=True, null=True)
    descripcion=models.TextField()
    
    def __str__(self):
        return self.name

class Category_post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    verbose_name_plural = 'categories'
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    bio= models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='blog_bio', default="1",blank=True, null=True)
    mp3= models.FileField(upload_to='audios/', blank=True, null=True)
    linkyoutube= models.CharField(max_length=400, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    fecha=models.CharField(max_length=400, blank=True, null=True)
    hora=models.CharField(max_length=400, blank=True, null=True)
    short_desciption = models.CharField(max_length=400, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    descripcion_imagen=models.CharField(max_length=400, unique=True, blank=True, null=True)
    image2 = models.ImageField(upload_to='images/',blank=True, null=True)
    descripcion_imagen2=models.CharField(max_length=400, unique=True, blank=True, null=True)
    image3 = models.ImageField(upload_to='images/',blank=True, null=True)
    descripcion_imagen3=models.CharField(max_length=400, unique=True, blank=True, null=True)
    image4 = models.ImageField(upload_to='images/',blank=True, null=True)
    descripcion_imagen4=models.CharField(max_length=400, unique=True, blank=True, null=True)
    
    image5 = models.ImageField(upload_to='images/',blank=True, null=True)
    descripcion_imagen5=models.CharField(max_length=400, unique=True, blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    teatro=models.ManyToManyField('Teatros', related_name='teatros', default='1',blank=True, null=True)
    cine=  models.ManyToManyField('Cines', related_name='cines',blank=True, null=True)
    categories = models.ManyToManyField('Category_post', related_name='posts')
    visit_num = models.PositiveIntegerField(default=0)
    precio=models.IntegerField(default=0)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

  
class UserFavorites(models.Model):
    user=models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_fav')
    favoritos=models.ForeignKey(Post,on_delete= models.CASCADE, related_name='user_fav')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)


class Galeria(models.Model):
    imagen=models.ImageField(upload_to='galeria/')
    info=models.CharField(max_length=200, blank=True, null=True )
    def __str__(self):
        return self.info
class Notas(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='notas_posts')
    bio= models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='notas_bio', default="1",blank=True, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    short_desciption = models.CharField(max_length=400, unique=True, blank=True, null=True)
    image1 = models.ImageField(upload_to='notas/')
    image2 = models.ImageField(upload_to='notas/')
    image3 = models.ImageField(upload_to='notas/')
    image4 = models.ImageField(upload_to='notas/')
    image5 = models.ImageField(upload_to='notas/')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField('Category_post', related_name='notas_posts')
    visit_num = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        self.title
