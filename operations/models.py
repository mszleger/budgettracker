from django.db import models

class Category(models.Model):
    '''
    A model representing a category of operations.

    Attributes:
        main_category: The category to which the current category belongs.
        name: Name of category.
        operations: List of operations in current Category.
        owner: The user who created the current category.
        sub_categories: The sub categories of current category.
    '''
    main_category = models.ForeignKey('self', related_name='sub_categories', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150)
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        '''
        Dunder returning string representation of Category.

        :return: String representation of Category.
        :rtype: str
        '''
        return f'{self.name}'


class Currency(models.Model):
    '''
    A model representing a currency.

    Attributes:
        code: Code of currency (for example USD).
        name: Full name of currency (for example United States Dollar).
        operations: List of operations in current Currency.
        owner: The user who created the current Currency.
    '''
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='currencies', on_delete=models.CASCADE)

    def __str__(self):
        '''
        Dunder returning string representation of Currency.

        :return: String representation of Currency.
        :rtype: str
        '''
        return f'{self.name}'


class Operation(models.Model):
    '''
    A model representing a financial operation.

    Attributes:
        amount: Amount of operation with 2 decimal places and a maximum of 10 digits.
        category: Foreign key of category of operation.
        currency: Foreign key of currency of operation.
        date: Date of operation.
        description: Optional longer description of operation.
        name: Name of operation.
        owner: The user who created the current Operation.
    '''
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='operations', on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, related_name='operations', on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=150)
    owner = models.ForeignKey('auth.User', related_name='operations', on_delete=models.CASCADE)

    def __str__(self):
        '''
        Dunder returning string representation of Operation.

        :return: String representation of Operation.
        :rtype: str
        '''
        return f'{self.name}'