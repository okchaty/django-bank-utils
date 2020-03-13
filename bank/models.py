# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Bank(TimeStampedModel):
    name = models.CharField(
        max_length=45,
        help_text="bank name",
    )
    country = models.ForeignKey(
        "country.Country",
        on_delete=models.PROTECT,
    )
    account_types = models.ManyToManyField("bank.AccountType")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "bank"
        ordering = ["-created"]

    def __str__(self):
        return "{}, {}".format(self.name, self.country.name)


class AccountType(TimeStampedModel):
    name = models.CharField(
        max_length=45,
        help_text="name account type",
    )

    class Meta:
        db_table = "accounttype"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class BankAccount(TimeStampedModel):
    account_number = models.CharField(
        max_length=45,
        blank=True,
        null=True,
    )
    inter_account_number = models.CharField(
        max_length=45,
        blank=True,
        null=True,
    )
    account_owner_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    account_owner_id = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Account owner id, could be RUC, VAT, etc"
    )
    bank = models.ForeignKey(
        "bank.Bank",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    accounttype = models.ForeignKey(
        "bank.AccountType",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    currency = models.ForeignKey(
        "currency.Currency",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    
    class Meta:
        db_table = "bankaccount"
        ordering = ["-created"]
