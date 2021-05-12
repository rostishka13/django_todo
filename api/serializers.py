from django.contrib.auth.models import User
from rest_framework import serializers
from base.models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'task']


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

        extra_kwargs = {
        'password': {'write_only': True}
            }


    def save(self):
        user = User(email = self.validated_data['email'],
                    username = self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']


        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'})

        user.set_password(password)
        user.save()
        return user

