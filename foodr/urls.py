"""foodr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from foodr import settings
from recipes.views import RecipeListView, RecipeView, AddRecipeByUrlView
import recipes.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipes/<int:pk>/', RecipeView.as_view(), name="recipe"),
    path('recipes/add-by-url/', AddRecipeByUrlView.as_view(), name="add-by-url"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
