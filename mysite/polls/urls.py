from django.urls import path
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    #dont forget commas it is a list.
    path('2223' , views.main , name = 'test'),
    path('2224' , views.main1 , name = 'test1'),

    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
