from django.urls import path
from pages import views
from . import views

urlpatterns = [
    path("", views.landing, name='landing'),
    path('login/', views.log_in, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('addMember/', views.registerPage, name='addMember'),
    path('search-members/', views.search_members, name='search_members'),
    path('delete_member/', views.delete_member, name='delete_member'),
    path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
    path('available_providers/', views.available_providers, name='available_providers'),
    path('add_provider/', views.add_provider, name='add_provider'),
    path('update_provider/<int:provider_id>/', views.update_provider, name='update_provider'),
    path('coverage/', views.coverage_page, name='coverage_page'),
    path('add_coverage/', views.add_coverage, name='add_coverage'),
    path('update_coverage/<str:coverage_id>/', views.update_coverage, name='update_coverage'),
    path('nurse_list/', views.nurse_list, name='nurse_list'),
    path('nurse_detail/<int:pk>/', views.nurse_detail, name='nurse_detail'),
    path('add_nurse/', views.nurse_new, name='add_nurse'),
    path('edit_nurse/<int:pk>/', views.nurse_edit, name='edit_nurse'),
    path('delete_nurse/<int:pk>/', views.nurse_delete, name='delete_nurse'),
]