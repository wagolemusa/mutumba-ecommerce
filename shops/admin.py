from django.contrib import admin

# Register your models here.
from .models import (Item, OrderItem, Order, 
								Payment,BillingAddress,Mpesapay,Coupon,
								Refund, Category, Contact)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'id')
	prepopulated_fields = {'id':('name',)}

def make_refund_accepted(modeladmin, request, queryset):
	queryset.update(refund_requested=False, refund_granted=True)
make_refund_accepted.short_description = 'Update order to refund granted'

class OrderAdmin(admin.ModelAdmin):
	list_display = ['user', 
									'ordered',
									'being_delivered',
									'received_requested',
									'refund_requested',
									'refund_granted',
									'billing_address',
									'payment',
									'coupon'
									]

	list_display_links = [
		'user',
		'billing_address',
		'payment',
		'coupon'
	]

	list_filter = [ 'ordered',
									'being_delivered',
									'received_requested',
									'refund_requested',
									'refund_granted'
								]
	search_fields = [
		'user__username',
		'ref_code'
	]

	actions = [make_refund_accepted]

class ContactAdmin(admin.ModelAdmin):
	list_display = [
		"full_name",
		"phone",
		"email",
		"timestamp",
	]

class MpesapayAdmin(admin.ModelAdmin):
	list_display = [
		"user",
		"amount",
		"phone",
		"cash",
		"timestamp",
	]

class OrderItemAdmin(admin.ModelAdmin):
	list_display = [
		 "user",
		 "item",
		 "quantity"
	]

admin.site.register(Item)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(BillingAddress)
admin.site.register(Mpesapay, MpesapayAdmin)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
