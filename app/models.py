from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="")
    description = models.CharField(max_length=255, null=True, blank=True)


class Partner(models.Model):
    image = models.ImageField(upload_to="")
    url = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=1)


class News(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="")
    date = models.DateField()
    body = models.DateField(max_length=255)


class Application(models.Model):
    class ApplicationChoices(models.TextChoices):
        main_page = ("main_page", "Bosh sahifa")
        service = ("service", "Server")
        get_tt = ("get_tt", "Texnik malumot olish")
        partner = ("partner", "Hamkor")
        order = ("order", "Buyruq")

    full_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255,
                              choices=ApplicationChoices.choices,
                              default=ApplicationChoices.main_page
                              )


class Product(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    order = models.IntegerField(default=1)
    image = models.ImageField(upload_to="")
    short_description = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    guarantee = models.CharField(max_length=255)
    is_main_page = models.BooleanField()
    category = models.ForeignKey("Category", related_name="products", on_delete=models.CASCADE, null=True)


class ProductImage(models.Model):
    image = models.ImageField(upload_to="")
    product = models.ForeignKey(
        Product, related_name="product_images", on_delete=models.CASCADE
    )


class ProductCharacteristic(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    order = models.IntegerField(default=1)
    product = models.ForeignKey(
        Product, related_name="productCharacteristic", on_delete=models.CASCADE
    )


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="")
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="")
    image = models.ImageField(upload_to="")
    short_description = models.CharField(max_length=255)


class CompanyAchievements(models.Model):
    year = models.IntegerField(default=1)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to="")
    company = models.ForeignKey(
        Company, related_name="company_achievements", on_delete=models.CASCADE
    )


class Region(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(default=1)
    company = models.ForeignKey(
        Company, related_name="company_region", on_delete=models.CASCADE
    )


class Achievements(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="")
    order = models.IntegerField(default=1)


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    url = models.ImageField(upload_to="")
    order = models.IntegerField(default=1)