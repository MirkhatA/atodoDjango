from django.urls import path
from . import views
from .views import HomeView, TaskDetailView, AddTaskView, UpdateTaskView, DeleteTaskView, AddCategoryView, CategoryView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('task/edit/<int:pk>', UpdateTaskView.as_view(), name='update_task'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('deleteCat/<int:pk>', views.deleteCat, name='deleteCat'),
    path('uncross/<int:pk>', views.uncross, name='uncross'),
    path('tocross/<int:pk>', views.tocross, name='tocross'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:categ>/', CategoryView, name='category'),
]
