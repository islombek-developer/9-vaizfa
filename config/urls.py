from django.contrib import admin
from django.urls import path
from student.views import home,teacher,group,student,create,delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('group/',group,name='group'),
    path('create/',create,name='create'),
    path('teacher/<int:g_id>/',teacher,name='teacher'),
    path('student/<int:t_id>/',student,name='student'),
    path('delete/<int:id>/',delete,name='delete'),

]
