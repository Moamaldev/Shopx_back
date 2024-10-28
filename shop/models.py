from django.db import models
from django.contrib.auth.models import User
import uuid


class Entity(models.Model):# models.Model base that django give as to define Tabel in database
    class Meta:  # Meta to tell django do'nt select this class you must set abstract = True
        abstract = True  #undo magrition 

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # django create int id for more secure use UUIDField randomly generated
    created = models.DateTimeField(editable=False, auto_now_add=True)# time now when add
    updated = models.DateTimeField(editable=False, auto_now=True) # time now when updated


class Catagory(Entity):
    titel = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_img/")#pillw library 
    data  = models.DateField(auto_now_add=True)
    def __str__(self) :
        return f"titel = {self.titel}|   |   id ={self.id}"
    
class Product(Entity):
    titel = models.CharField(max_length=100)
    data  = models.DateField(auto_now_add=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    img = models.ImageField(upload_to="products_img/")
    purchasing_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    def __str__(self):
        return self.titel
    
class Favorite(Entity):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.Case)
    isFavorit = models.BooleanField(default=False)

    def __str__(self):
        return f"productID ={self.product.id}user={self.user.username}|ISFavorite={self.isFavorit}"


class Review(Entity):
    user = models.ForeignKey(User, on_delete=models.Case)
    subject = models.TextField(max_length=50 , blank=True)
    commint = models.TextField(max_length=200 , blank=True)
    review_point = models.IntegerField( default=1 )
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    def __str__(self):
     return f"productName ={self.product.titel} |  UserName ={self.user.username}       |  subject={self.subject}   |  comment ={self.commint} "



class Order(Entity):
    Status_Choices =(
        ('PROCESSING', 'PROCESSING'),
        ('SHIPPED', 'SHIPPED'),
        ('COMPLETED', 'COMPLETED'),
        ('Rejected', 'Rejected'),
    )

    Status = models.CharField(max_length=100 , choices=Status_Choices , default='PROCESSING')
    user = models.ForeignKey(User, on_delete=models.Case)
    # order_description = models.TextField()
    # prouducts_test = models.ManyToManyField(Product)
    products_list = models.JSONField(default=list)    # JSONField to store the list of products
    total = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=50)
    def __str__(self):
        return f"email={self.email}  | number ={self.phone}  | address ={self.address}  |  Status = {self.Status} "


