"""Posts model"""
#importaciones ----------------------------------------------
# Django
from django.contrib import admin
# Models
from post.models import Post

#code ----------------------------------------------

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post en admin"""
    list_display = ( 
    'user',
     'title', 'photo')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')

