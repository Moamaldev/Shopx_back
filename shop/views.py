from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework import generics




class ProductView(APIView): 
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get(self, request):
        query = Product.objects.all()
        data = []
        serializers = ProductSerializer(query, many=True)
        for product in serializers.data: # for x in  10  => x = 0 > 10 || p in s || data
            fav_query = Favorite.objects.filter( # u , pid 
                user=request.user).filter(product_id=product['id'])
            if fav_query:
                product['favorit'] = fav_query[0].isFavorit
            else:
                product['favorit'] = False
            data.append(product)
        return Response(data)

class FavoritView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        data = request.data["id"]
        print(data)
        try:
            product_obj = Product.objects.get(id=data)
            # print(data)
            user = request.user
            single_favorit_product = Favorite.objects.filter(
                user=user).filter(product=product_obj).first()
            if single_favorit_product:
                print("single_favorit_product")
                ccc = single_favorit_product.isFavorit #T
                single_favorit_product.isFavorit = not ccc
                single_favorit_product.save()
            else:
                Favorite.objects.create(
                    product=product_obj, user=user, isFavorit=True)
            response_msg = {'error': False}
        except:
            response_msg = {'error': True}
        return Response(response_msg)
    
class CategoryView(APIView): 
    def get (self , request):
        query = Catagory.objects.all()
        serializers = CategorySerializer(query, many=True)
        return Response(serializers.data)
    

class RegisterView(APIView):
    def post(self, request):
        serializers = Userserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response({"error": True})

Userx = get_user_model()

class UserView(generics.RetrieveAPIView): 
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    queryset  = Userx.objects.all()
    serializer_class  = UserDetailSerializer
    lookup_field = 'id'

#filter with token
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication
    authentication_classes = [TokenAuthentication, ]

    def get(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user from the token
        return Response({
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })
        

#unwichtig
class GetAllOrderView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def get  (self , request):
        query = Order.objects.all()
        serializers = OrderSerializers(query, many=True)
        return Response(serializers.data)
    
    
class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def post(self, request):
        serializers = OrderSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response({"error": True})


class GetOrderByUserView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def get  (self , request):   
        user = request.user
        try:

           query = Order.objects.filter(user = user )
           serializers = OrderSerializers(query, many=True)
           response_msg = {"error": False, "data": serializers.data}

        except:
            response_msg = {"error": True, "data": "no data"}
        return Response(response_msg)


class ReviewView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def get  (self , request):
        query = Review.objects.all()
        serializers = ReviewSerializers(query, many=True)
        return Response(serializers.data)


class ReviewCreate(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def post(self, request):
        serializers = ReviewSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response({"error": True})
    

# # Create your views here.
