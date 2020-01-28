import uuid
from django.db import models


DECIMAL_LENGTH = 20
DECIMAL_PLACES = 5

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    filename = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    total_items_price = models.DecimalField(
        max_digits=DECIMAL_LENGTH,
        decimal_places=DECIMAL_PLACES,
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    invoice_number = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    client_name = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    client_lastname = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    client_id = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    item_code = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    item_description = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )


    item_amount = models.DecimalField(
        max_digits=DECIMAL_LENGTH,
        decimal_places=DECIMAL_PLACES,
        blank=False,
        null=False
    )

    item_price = models.DecimalField(
        max_digits=DECIMAL_LENGTH,
        decimal_places=DECIMAL_PLACES,
        blank=False,
        null=False
    )


    item_discount_rate = models.DecimalField(
        max_digits=DECIMAL_LENGTH,
        decimal_places=DECIMAL_PLACES,
        blank=False,
        null=False
    )


    file = models.ForeignKey(
        File,
        on_delete=models.PROTECT,
        related_name='invoices'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


