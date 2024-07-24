# movies/serializers.py

from rest_framework import serializers
from movies.models import Movie, Category, Episode
from treyler.models import Treyler

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TreylerSerializers(serializers.ModelSerializer):
    class Meta:
      model = Treyler
      fields = '__all__'


class EpisodeSerializers(serializers.ModelSerializer):
    class Meta:
      model = Episode
      fields = '__all__'
    