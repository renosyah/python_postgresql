from django.conf.urls import url 
from app import views 

 # Create your url here.
urlpatterns = [ 
    url(r'^api/student$', views.student_add),
    url(r'^api/students$', views.student_list),
    url(r'^api/student/(?P<id>[-\w]+)$', views.student),
]