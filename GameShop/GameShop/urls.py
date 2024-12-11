from django.contrib import admin
from django.urls import path

from task1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up_by_django),
    path('platform/', Platform.as_view()),
    path('platform/games/', games),
    path('platform/cart/', cart)
]