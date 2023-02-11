from django.urls import path, include
from .views import text, CreateUserView, LoginView, UserView, LogoutView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("text/", text),
    path("test/", CreateUserView.as_view()),
    path("login/", LoginView.as_view()),
    path("get_user_authenticate_or_not/", UserView.as_view()),
    path("logout/", LogoutView.as_view())
]