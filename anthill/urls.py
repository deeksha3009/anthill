"""anthill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from capstone.views import home,signin,signup,signout,dashboard,create_group,group_page,add_members,add_guides,updates,add_milestone,view_milestones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('login/',signin),
    path('signup/',signup),
    path('logout/',signout),
    path('create_group/',create_group),
    path('dashboard/', dashboard),
    path('group/<int:gid>/', group_page),
    path('upt/<int:gid>/',updates),
    path('miles/<int:gid>/',add_milestone),
    path('milestone/<int:mid>/',view_milestones),
    path('add_member/<int:gid>/',add_members),
    path('add_guide/<int:gid>/',add_guides),
    # path('add_goals/<int:mid>/',add_goals),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
