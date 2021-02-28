from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.redirect_to_dashboard, name='homepage'),
    path('dashboard', views.homepage, name='homepage'),

    # routes for province
    path('<slug:slug>/list', views.crud_list, name='crud_list'),
    path('<slug:slug>/add', views.crud_create_or_update, name='crud_add'),
    path('<slug:slug>/<int:id>/edit', views.crud_create_or_update, name='crud_edit'),


    # path('province/add',views.province_form,name='province_add'),
    # path('province/<int:id>/edit', views.province_form,name='province_update'),
    # path('province/delete/<int:id>', views.province_delete, name='province_delete'),

    # routes for district
    # path('district/list/', views.district_list, name='district_list'),
    # path('district/add',views.district_form,name='district_add'),
    # path('district/<int:id>/edit', views.district_form,name='district_update'),
    # path('district/delete/<int:id>', views.district_delete, name='district_delete'),

    # routes for local_level
    # path('local_level/list/', views.locallevel_list, name='locallevel_list'),
    # path('local_level/add',views.locallevel_form,name='locallevel_add'),
    # path('local_level/<int:id>/edit', views.locallevel_form,name='locallevel_update'),
    # path('local_level/delete/<int:id>', views.locallevel_delete, name='locallevel_delete'),

    # routes for local_level_type
    # path('local_level_type/list', views.locallevel_type_list,name='locallevel_type_list'),
    # path('local_level_type/add',views.locallevel_type_form,name='locallevel_type_add'),
    # path('local_level_type/<int:id>/edit', views.locallevel_type_form,name='locallevel_type_update'),
    # path('local_level_type/delete/<int:id>/', views.locallevel_type_delete, name='locallevel_type_delete'),

    # routes for nepali_month
    # path('nepali_month/list', views.nepalimonth_list, name='nepalimonth_list'),
    # path('nepali_month/add',views.nepalimonth_form,name='nepalimonth_add'),
    # path('nepali_month/<int:id>/edit', views.nepalimonth_form,name='nepalimonth_update'),
    # path('nepali_month/delete/<int:id>/', views.nepalimonth_delete, name='nepalimonth_delete'),

    # routes for fiscal_year
    # path('fiscal_year/list/', views.fiscalyear_list, name='fiscalyear_list'),
    # path('fiscal_year/add',views.fiscalyear_form,name='fiscalyear_add'),
    # path('fiscal_year/<int:id>/', views.fiscalyear_form,name='fiscalyear_update'),
    # path('fiscal_year/delete/<int:id>/', views.fiscalyear_delete, name='fiscalyear_delete'),

    # routes for gender
    # path('gender/list/', views.gender_list, name='gender_list'),
    # path('gender/add',views.gender_form,name='gender_add'),
    # path('gender/<int:id>/', views.gender_form,name='gender_update'),
    # path('gender/delete/<int:id>/', views.gender_delete, name='gender_delete'),
]
