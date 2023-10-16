from rest_framework import serializers
from .models import Client, Site, FilterWords, Notification, Article

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# Repeat the above pattern for the rest of the models.

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class FilterWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterWords
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
