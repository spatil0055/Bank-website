from rest_framework import serializers
from .models import User,openaccount,depositetype,applyloan,heroImages
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']
        # fields = ['id','name','email','password','image']
        
        # hide password
        extra_kwards={
            'password':{'write_only':True}
        }
    
    # hashpassword
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=openaccount
        fields='__all__'

class DepositeSerializer(serializers.ModelSerializer):
    class Meta:
        model=depositetype
        fields='__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=applyloan
        fields='__all__'


class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=heroImages
        fields='__all__'