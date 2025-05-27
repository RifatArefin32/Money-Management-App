from django.urls import path
from . import views
urlpatterns = [
    path('income-records/', views.show_income_records),
    path('accounts/', views.show_accounts)
]
