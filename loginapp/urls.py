from django.urls import path

from loginapp import views
app_name='loginapp'
urlpatterns = [

    path('fn_login/',views.fn_login,name='fn_login'),

    path('fn_regist/',views.fn_regist,name='fn_regist'),
    path('getcaptcha/', views.getcaptcha, name='getcaptcha'),
    path('registajax/', views.registajax, name='registajax'),
    path('getcaptcha_ajax/', views.getcaptcha_ajax, name='getcaptcha_ajax'),
    path('cook/',views.cook,name='cook'),

]