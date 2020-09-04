from django.conf.urls import url 
from app import views 
 

 # Create your url here.
urlpatterns = [ 
    url(r'^api/student$', views.student_add),
    url(r'^api/students$', views.student_list),
    url(r'^api/student/(?P<id>[-\w]+)$', views.student),
    url(r'^api/student/(?P<id>[-\w]+)/image$', views.image_profile_add),
    url(r'^api/images$', views.image_profile_list),
    url(r'^api/image/(?P<id>[-\w]+)$',views.image_profile),
    url(r'^api/image/(?P<id>[-\w]+)/validate$', views.validate_image_profile),
]