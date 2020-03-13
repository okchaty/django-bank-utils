from django.contrib import admin
from .models import Bank, AccountType, BankAccount


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
        "is_active"
    )
    list_filter = ("is_active",)


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
    )


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "bank",
        "account_number",
        "inter_account_number",
        "account_owner_name",
        "account_owner_id",
        "accounttype",
        "currency",
    )
