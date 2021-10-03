from django.db import models


class Option(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    TABLE = 'TB'
    SHOWCASE = 'SC'
    SHELF = 'SF'
    WARDROBE = 'WR'
    COMMODE = 'CM'
    TV_STAND = 'TV'
    BED = 'BE'
    CATEGORY = [
        (TABLE, 'Стіл'),
        (SHOWCASE, 'Вітрина'),
        (SHELF, 'Полиця'),
        (WARDROBE, 'Шафа'),
        (COMMODE, 'Комод'),
        (TV_STAND, 'Тумба під телевізор'),
        (BED, 'Ліжко')
    ]

    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY,
        default=TABLE,
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.title


class Property(models.Model):
    characteristic = models.CharField(max_length=100)


class PropertyValue(models.Model):
    characteristic_value = models.CharField(max_length=100)