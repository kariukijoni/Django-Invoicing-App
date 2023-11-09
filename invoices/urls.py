# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login',views.login,name='login'),
#     path('dashboard',views.dashboard,name='dashboard'),
# ]


from django.urls import path
from . import views

urlpatterns = [
path('login',views.login, name='login'),
path('logout',views.logout, name='logout'),
path('dashboard',views.dashboard, name='dashboard'),
path('invoices',views.invoices, name='invoices'),
path('products',views.products, name='products'),
path('clients',views.clients, name='clients'),

# create url paths
path('invoices/create',views.create_invoice,name='create-invoice'),
path('invoices/create-build/<slug:slug>',views.create_build_invoice,name='create-build-invoice')

]