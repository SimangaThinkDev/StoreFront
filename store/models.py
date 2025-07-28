from django.db import models

class Product(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    created_at = models.DateTimeField( auto_now_add=True )
    last_update = models.DateTimeField( auto_now=True )
    # Relationships
    collection = models.ForeignKey( 'Collection', on_delete=models.PROTECT )
    promotions = models.ManyToManyField('Promotion')
    # Note that I named it in plural form...


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField( max_length=80 )
    last_name  = models.CharField( max_length=80 )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255) # I do not get this one...
    birth_date = models.DateField(null=True)
    membership = models.CharField( max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE )

    # Relationships
    order = models.ForeignKey( 'Order', on_delete=models.CASCADE )

    class Meta:
        """Where we define metadata about our model"""
        indexes = [
            models.Index( fields=['first_name', 'last_name'] )
        ]


class Order(models.Model):

    PENDING_STATUS = 'P'
    COMPLETE_STATUS = 'C'
    FAILED_STATUS = 'F'

    PAYMENT_STATUS_ENUM = [
        (PENDING_STATUS, 'Pending'),
        (COMPLETE_STATUS, 'Complete'),
        (FAILED_STATUS, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True) # Automatically populated at creation
    payment_status = models.CharField( max_length=1, choices=PAYMENT_STATUS_ENUM, default=PENDING_STATUS )

    item = models.ForeignKey( 'Item', on_delete=models.PROTECT )


class Address(models.Model):

    street = models.CharField( max_length=255 )
    city   = models.CharField( max_length=255 )
    zip_code = models.CharField( max_length=255 )

    customer = models.OneToOneField( Customer, on_delete=models.CASCADE, primary_key=True )


class Collection(models.Model):

    title = models.CharField(max_length=100)
    # One to many relationship
    featured_product = models.ForeignKey( Product, 
                                         on_delete=models.SET_NULL, 
                                         null=True,
                                          related_name='+' )


class Item( models.Model ):

    pass


class Cart( models.Model ):

    created_at = models.DateTimeField(auto_now_add=True)

class CartItem( models.Model ):
    cart     = models.ForeignKey( 'Cart', on_delete=models.CASCADE )
    product  = models.ForeignKey( 'Product', on_delete=models.CASCADE )
    quantity = models.PositiveSmallIntegerField()


class OrderItem( models.Model ):

    order   = models.ForeignKey( 'Order', on_delete=models.PROTECT )
    product = models.ForeignKey( 'Product', on_delete=models.PROTECT )
    quatity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Promotion( models.Model ):
    description = models.CharField( max_length=255 )
    discount = models.FloatField()