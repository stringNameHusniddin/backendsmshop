
from .serializers import AccountSerializers, BuySerializers, ChatGSerializers, ChatOSerializers, ProductSerializers, ComentariyaSerializers
from rest_framework import viewsets
from .models import Buy, ChatGlobal, ChatOnly, Comentariya, Product, Account
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AccountView(viewsets.ModelViewSet):
    serializer_class = AccountSerializers
    queryset = Account.objects.all()

class BuyView(viewsets.ModelViewSet):
    serializer_class = BuySerializers
    queryset = Buy.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

class ComentariyaView(viewsets.ModelViewSet):
    serializer_class = ComentariyaSerializers
    queryset = Comentariya.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

class ChatOView(viewsets.ModelViewSet):
    serializer_class = ChatOSerializers
    queryset = ChatOnly.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

class ChatGView(viewsets.ModelViewSet):
    serializer_class = ChatGSerializers
    queryset = ChatGlobal.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]