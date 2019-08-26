from django.urls import path

from employeeapp import views
app_name='employeeapp'
urlpatterns = [

    path('fn_add/',views.fn_add,name='fn_add'),
    path('dele/',views.dele,name='dele'),
    path('fn_update/',views.fn_update,name='fn_update'),
    path('query/', views.query, name='query'),
    path('update_emp/', views.update_emp, name='update_emp'),
    path('sess/', views.sess, name='sess'),
]