"""cncweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordChangeView, PasswordChangeDoneView
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change_password/', PasswordChangeView.as_view(), name='change_password'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('events/', include('events.urls', namespace='events')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('api-auth/', include('rest_framework.urls')),

]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
