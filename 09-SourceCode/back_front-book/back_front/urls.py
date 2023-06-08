"""
URL configuration for back_front project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('user.urls', 'user'), namespace="user")),
    path('book/', include(('book.urls', 'book'), namespace="book")),
    path('chapter/', include(('chapter.urls', 'chapter'), namespace="chapter")),
    path('star/', include(('star.urls', 'star'), namespace="star")),
    path('label/', include(('label.urls', 'label'), namespace="label")),
    path('author/', include(('author.urls', 'author'), namespace="author")),
    path('comment/', include(('comment.urls', 'comment'), namespace="comment")),
    path('note/', include(('note.urls', 'note'), namespace="note")),

]
