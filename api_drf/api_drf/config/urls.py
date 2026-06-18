from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from products.views import ProductViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path
from .import views
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Gera o arquivo de esquema bruto (.yaml)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
# Interface do Swagger UI
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
# Interface alternativa do Redoc (Opcional, mas muito elegante)
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# permitir o fluxo de login
    path('login/', views.login_view, name='login'),
# permitir o fluxo de login
    path('logout/', views.logout_view, name='logout'),
# permitir o cadastro de um novo usuário
    path('register/', views.register_view, name='register'),
# recurso para verificar se o usuário está autenticado,
# antes de acessar o recurso
    path('dashboard/', views.dashboard, name='dashboard'),
]
