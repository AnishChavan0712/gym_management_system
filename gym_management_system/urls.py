from django.contrib import admin
from django.urls import path
from gym.views import *  # Import views from the 'gym' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('members/', members_list, name='members_list'),  # Members list
    path('member/<int:id>/', member_detail, name='member_detail'),
      path('add-member/', add_member, name='add_member')  # Member details
]
