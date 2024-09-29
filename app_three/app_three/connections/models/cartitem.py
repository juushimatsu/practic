from django.db import models

class CartItem(models.Model):
    product_id = models.IntegerField()  # ID товара
    product_type = models.CharField(max_length=20)  # 'clothing' или 'accessory'
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product_type} {self.product_id} (Quantity: {self.quantity})"
