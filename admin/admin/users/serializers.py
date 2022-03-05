from rest_framework import serializers
from users.models import Address, User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
    

class UserSerializer(serializers.ModelSerializer):
    address  = AddressSerializer()
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self,validated_data):
        address_data = validated_data.pop('address')
        
        address = AddressSerializer.create(AddressSerializer(), validated_data=address_data)
        user = User.objects.create(address=address, **validated_data)
        return user
        

