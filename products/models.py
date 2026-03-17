import decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    """
    Represents a product category
    (e.g. Produce, Dairy, Clothing, Electronics)
    """

    name = models.CharField(
        max_length=25,
        unique=True,
        help_text='Category\'s display name.'
    )
    slug = models.SlugField(
        max_length=25,
        unique=True,
        blank=True,
        help_text='Auto-generated URL-friendly identifier based on category\'s name.'
    )
    description = models.TextField(
        blank=True,
        help_text='(Optional) Description of category and its products.'
    )

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def save(self, *args, **kwargs) -> None:
        """Auto-generate URL-friendly slug from name, if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    """
    Represents a descriptive tag, used to label products for filtering and searching
    (e.g. 'Gluten-Free', 'Exclusive', 'Made In Canada')
    """

    name = models.CharField(
        max_length=25,
        unique=True,
        help_text='Display name for the tag.'
    )
    slug = models.SlugField(
        max_length=25,
        unique=True,
        blank=True,
        help_text='Auto-generated URL-friendly identifier based on tag\'s name.'
    )

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs) -> None:
        """Auto-generate URL-friendly slug from name, if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """
    Represents a product
    (e.g. Milk, Pencil, Television)
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text='Display name for the product.'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        help_text='Auto-generated URL-friendly identifier based on product\'s name.'
    )
    description = models.TextField(
        help_text='Description of product. Include related and keywords, used for search.'
    )
    base_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(decimal.Decimal('0.01'))],
        help_text='Base retail price of product, in CAD, before any discounts.'
    )
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(decimal.Decimal('0.00')),
            MaxValueValidator(decimal.Decimal('100.00'))
        ],
        help_text='Active discount as a percentage (e.g. 25.00 for 25% off base price).'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        help_text='Category the product belongs to.'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='products',
        help_text='(Optional) Any tags the product may have for labeling & filtering'
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        help_text='Timestamp of when the product was created.'
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        help_text='Timestamp of when the product was last modified'
    )

    class Meta:
        ordering = ['-created_at']

    @property
    def price(self) -> decimal.Decimal:
        """Calculate and return active price of product after any discounts"""
        if self.discount_percentage:
            discount_multiplier = decimal.Decimal('1') - (
                    self.discount_percentage / decimal.Decimal('100')
            )
            multiplied_price = self.base_price * discount_multiplier
            rounded_price = multiplied_price.quantize(decimal.Decimal('0.01'))
            return rounded_price
        return self.base_price

    def save(self, *args, **kwargs) -> None:
        """Auto-generate URL-friendly slug from name, if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
