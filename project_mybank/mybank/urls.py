from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from project_mybank import settings
from mybank.views import about, contact, home, make_transaction_filled, transfer, view_all_customers, view_customer, view_transactions, view_transactions_page, view_your_account_details, view_your_account_details_page

urlpatterns = [
    url('home/$', home),
    url('view_all_customers/$', view_all_customers),
    path('view_customer/<user2>/', view_customer),
    path('make_transaction_filled/<user2>/', make_transaction_filled),
    url('transfer/$', transfer),
    url('view_your_account_details/$', view_your_account_details),
    url('view_your_account_details_page/$', view_your_account_details_page),
    url('view_transactions_page/$', view_transactions_page),
    url('view_transactions/$', view_transactions),
    url('contact/$', contact),
    url('about/$', about),
]