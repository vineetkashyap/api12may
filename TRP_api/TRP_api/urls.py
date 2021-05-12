from django.contrib import admin
from django.urls import path,include
from api import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from knox import views as knox_views
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('truckowner',views.TruckOwnerModel_View,basename='truckowner')
router.register('transporter',views.TransporterModel_View,basename='transporter')
router.register('agent',views.Tranage_AgentSerializer_View,basename='agent')
router.register('vehicle',views.VehicleRegistraionModelSerializer_View,basename='vehicle')
router.register('driver',views.DriverRegistrationSerializer_View,basename='driver')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token),
    path('getuser/',views.student_data,name='stu'),

    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),



]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)