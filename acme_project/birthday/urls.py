from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.birthday, name='create'),
    # Маршрут для вывода списка всех в БД.
    path('list/', views.birthday_list, name='list'),
    # Маршрут для редактирования записи в БД.
    path('<int:pk>/edit/', views.birthday, name='edit'),
    path('<int:pk>/delete/', views.delete_birthday, name='delete'),
]
