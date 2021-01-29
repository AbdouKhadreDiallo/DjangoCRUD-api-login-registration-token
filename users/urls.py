
from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView,MyObtainTokenPairView

app_name = 'users'

urlpatterns = [
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]