from django.contrib import admin
from django.urls import path, include, reverse
from .views import *

urlpatterns = [
    path('records', RecordListView.as_view(), name='home'),
    path('create/', RecordCreateView.as_view(), name='create'),
    path('update/<int:pk>', RecordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', RecordDeleteview.as_view(), name='delete'),
    path('record/<int:pk>', RecordDetailView.as_view(), name='details'),
]