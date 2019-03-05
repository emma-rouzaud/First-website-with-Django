from django.conf.urls import include, url
import blog.views

urlpatterns = [
    url(r'^$', blog.views.index, name='index'),
    url(r'^home$', blog.views.index, name='home'),
    url(r'^about$', blog.views.about, name='about'),
]
