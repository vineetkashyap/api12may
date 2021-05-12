from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from api import views
from knox import views as knox_views
# from rest_framework.routers import DefaultRouter
# router= DefaultRouter()
# router.register('truckownerregistration',views.TruckOwnerModel_View,basename='truckownerregistration')
# # router.register('reg2',views.TruckOwnerVehicleRegistraionModel_View,basename='reg2')
# # router.register('reg3',views.TruckOwnerDriverRegistration_View,basename='reg3')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token),
    path('getdata/',views.MyList.as_view()),
    path('setdata/',views.MyList1.as_view()),
    path('getonedata/<int:pk>',views.MyList2.as_view()),
    path('getuser/',views.student_data),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
