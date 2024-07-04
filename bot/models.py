from django.db import models
# from foods.models import Food


# class UserPhones(models.Model):
#     user_id = models.BigIntegerField(unique=True)
#     phone = models.CharField(max_length=15)
#     warranty_img = models.CharField(max_length=255)


# # Create your models here.
# class User(models.Model):
#     user_id = models.BigIntegerField(unique=True)
#     phone = models.CharField(max_length=15)
#     name = models.CharField(max_length=255)
#     lang = models.CharField(max_length=10, null=True, blank=True)

#     def __str__(self):
#         return str(self.name)

# # class Basket(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     food = models.ForeignKey(Food, on_delete=models.CASCADE)
# #     count = models.PositiveIntegerField()

#     # def __str__(self) -> str:
#     #     return str(f"{self.user.phone} x{self.count} {self.food.name_uz}")



# class Warranty(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     warranty_img = models.CharField(max_length=255)


#     def __str__(self):
#         return f"{self.user.name}"

#     # Fayl ID sini saqlash uchun


# class YourModel(models.Model):
#     field1 = models.CharField(max_length=255)
#     field2 = models.IntegerField()
#     field3 = models.DateField()

#     def __str__(self):
#         return self.field1


# # movies/models.py
