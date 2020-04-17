from django.contrib import admin
from django.urls import path
from core import views
from core.views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.test_view)
    path('',TestView.as_view(),name='test')
]
