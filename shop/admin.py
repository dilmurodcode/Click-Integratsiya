from django.contrib import admin
from shop.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "address",
        "total_cost",
        "payment_method",
        "is_paid",
    )
    list_display_links = ("is_paid", "customer_name")
    search_fields = ("customer_name","address")
    ordering = ("-total_cost",)