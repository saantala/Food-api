from .models import User
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=255)
    phone_number = serializers.CharField(allow_null=False,allow_blank=False)
    password = serializers.CharField(min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        email_exists = User.objects.filter(email=attrs['email']).exists()
        phone_number_exists = User.objects.filter(phone_number=attrs['phone_number']).exists()

        if username_exists or email_exists or phone_number_exists:
            raise serializers.ValidationError('User with this username, email, or phone number already exists')
            
        return super().validate(attrs)

        

