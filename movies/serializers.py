# movies/serializers.py

from rest_framework import serializers
from .models import Movie, Category

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
