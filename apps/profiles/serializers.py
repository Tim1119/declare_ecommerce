from rest_framework import fields, serializers
from apps.profiles.models import Profile

class ProfileSerialaizer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name")
    email = serializers.EmailField(source='user.email')


    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'address',
            'gender',
            'profile_photo',
            'city',
            'country'
        ]