from django.urls import path, include
from .views import text, CreateUserView, LoginView, UserView, LogoutView

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    #path('admin/', admin.site.urls),
    path("text/", text),
    path("test/", CreateUserView.as_view()),
    path("login/", LoginView.as_view()),
    path("get_user_authenticate_or_not/", UserView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]