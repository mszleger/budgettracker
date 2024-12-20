from django.db import models

class Category(models.Model):
    """
    A model representing a category of operations.

    Attributes:
        name: Name of category.
    """
    name = models.CharField(max_length = 150)

class CategoryGroup(models.Model):
    """
    A model representing a relation between main and sub category of operations.

    Attributes:
        main_category: Foreign key of main category.
        sub_category: Foreign key of sub category.
    """
    main_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    sub_category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Currency(models.Model):
    """
    A model representing a currency.

    Attributes:
        code: Code of currency (for example USD).
        name: Full name of currency (for example United States Dollar).
    """
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 50)

class Operation(models.Model):
    """
    A model representing a financial operation.

    Attributes:
        amount: Amount of operation with 2 decimal places and a maximum of 10 digits.
        category: Foreign key of category of operation.
        currency: Foreign key of currency of operation.
        date: Date of operation.
        description: Optional longer description of operation.
        name: Name of operation.
    """
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete = models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank = True)
    name = models.CharField(max_length = 150)