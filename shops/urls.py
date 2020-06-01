from django.urls import path

from .views import (
	ItemDetailView,
	OrderSummaryView,
	CheckoutView,
	HomeView,
	about,
	add_to_cart,
	remove_from_cart,
	remove_single_item_from_cart,
	PaymentViews,
	Mpesa,
	AddCouponView,
	RequestRefundView,
	list_category,
	
)

app_name = 'shops'
	
urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('product/<slug>/', ItemDetailView.as_view(), name='product'),
	path('category/<slug>/', list_category, name='list_category'),
	path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
	path('checkout/', CheckoutView.as_view(), name='checkout'),
	path('about/', about, name='about'),
	path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
	path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
	path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
						 name='remove-single-item-from-cart'),
	path('payment/<payment_option>/', PaymentViews.as_view(), name='payment'),
	path('mpesapay/<payment_option>/', Mpesa.as_view(), name='mpesapay'),
	path('add-coupan/', AddCouponView.as_view(), name='add-coupan'),
	path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
	
]
