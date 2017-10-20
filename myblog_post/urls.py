from  django.conf.urls import url
import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^page/(\d+)$',views.index),
    url(r'^post/(\d+)$',views.details),
]