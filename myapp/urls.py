from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, ),
    path('show_books/', views.show_books, ),
    path('show_log/', views.show_log, ),
    path('execute_sql/', views.execute_sql, ),
]
