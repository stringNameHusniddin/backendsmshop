from rest_framework import serializers
from .models import Buy, ChatGlobal, ChatOnly, Comentariya, Product, Account

class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'is_biznes', 'image', 'password', ]
        extra_kwargs = {
			'password': {'write_only': True},
		}	

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            image=self.validated_data['image'],
            is_biznes=self.validated_data['is_biznes'],
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account
    
class BuySerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Buy

class ChatGSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ChatGlobal

class ChatOSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ChatOnly

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product

class ComentariyaSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comentariya