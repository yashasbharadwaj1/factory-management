from django.db import models
import datetime
# Create your models here.
class supplier(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    def __str__(self):
       return self.name  
class Category(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name    
class Products(models.Model):
    name = models.CharField(max_length=60)
    supplier_associated=models.ForeignKey(supplier,related_name='sup',on_delete=models.CASCADE,default=1) 
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/',blank=True)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products();
    def __str__(self):
        return self.name    

class Customer(models.Model):
    name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10,default=134235554)
    email=models.EmailField(default='a@example.com')
    password = models.CharField(max_length=100,default='bro')

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    def __str__(self):
        return self.name
class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    supplier_to_associate_request=models.ForeignKey(supplier,related_name='sta',on_delete=models.CASCADE,default=1)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    date=models.DateTimeField(default=datetime.datetime.today)
    quantity=models.IntegerField(default=0)
    brand=models.CharField(max_length=20,default='x')
    size=models.CharField(max_length=20,default='y')
    rate=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    tax=models.CharField(max_length=7,default='m%')
    tax_amount=models.CharField(max_length=10,default='mn')
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    status=models.BooleanField(default=False)
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

class customerservice(models.Model):
    name=models.CharField(max_length=20)
    product_name=models.CharField(max_length=30)
    ph_no=models.IntegerField()
    issues=models.CharField(max_length=30)
    img_describing_the_problem=models.ImageField(upload_to='uploads/products/')
