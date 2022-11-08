from django.contrib.sitemaps import Sitemap # Importamos la clase Sitemap
from blog.models import Post # Importamos nuestro modelo

class PostSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.created_on   