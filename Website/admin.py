# from django.contrib import admin
# from .models import Post,Category

# # Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)

from django.contrib import admin
from .models import Post, Category ,About

class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at_date') 

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(About)