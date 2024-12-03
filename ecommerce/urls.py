from django.contrib import admin
from django.urls import path, include
import debug_toolbar

admin.site.site_header = 'Store Front'
admin.site.index_title = 'Admin'
admin.site.site_title = 'Store Front'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls)),
]
