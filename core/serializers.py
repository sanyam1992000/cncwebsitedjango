from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import UserProfile
from blog.models import Post, Comment
from events.models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_url = serializers.HyperlinkedIdentityField(view_name="core:userprofile-detail")
    user = UserSerializer(many=False)

    class Meta:
        model = UserProfile
        fields = ['user_url', 'user', 'pic', 'roll_no', 'course', 'branch', 'icard', 'phoneno', 'password2']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comment_user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['comment_user', 'comment_content', 'comment_date']


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:blog-detail")
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['url', 'title', 'description', 'content', 'date', 'pic1', 'pic2', 'pic3', 'pic4', 'pic5', 'comments']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:event-detail")

    class Meta:
        model = Event
        fields = ['url', 'event_name', 'description', 'content', 'date', 'pic1', 'pic2', 'pic3', 'pic4', 'pic5', 'pic6', 'pic7', 'pic8', 'pic9', 'pic10', 'pic11', 'status']


