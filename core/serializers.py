from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import UserProfile, User
from blog.models import Post
from events.models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:userprofile-detail")

    class Meta:
        model = UserProfile
        fields = ['url', 'pic', 'roll_no', 'course', 'branch', 'icard', 'phoneno']


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:blog-detail")

    class Meta:
        model = Post
        fields = ['url', 'title', 'description', 'content', 'date', 'pic1', 'pic2', 'pic3', 'pic4', 'pic5']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:event-detail")

    class Meta:
        model = Event
        fields = ['url', 'event_name', 'description', 'content', 'date', 'pic1', 'pic2', 'pic3', 'pic4', 'pic5', 'pic6', 'pic7', 'pic8', 'pic9', 'pic10', 'pic11', 'status']