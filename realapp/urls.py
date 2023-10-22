from . import views
from django.urls import path

app_name = 'realapp'


urlpatterns = [
    path('create/', views.TypeCreateView.as_view(), name='create'),
    path('',views.TypeListView.as_view(),name='list'),
    path('<int:pk>/' ,views.TypeDetailView.as_view(),name="detail"),
    path('index/', views.Indexview.as_view(),name='index'),
    path('update/<int:pk>/', views.TypeUpdateView.as_view(),name="update"),
    path('delete/<int:pk>/', views.TypeDeleteView.as_view(),name='delete'),

]
