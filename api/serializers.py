# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py

from .models import University, Student, GeeksModel

'''
To perform HTTP-based interaction we have to define rules to convert Django models (python objects) to the json strings and vice versa. 
This is a serialization/deserialization task. So, let’s define some model-based serializers:

'''


# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):  # .HyperlinkedModelSerializer
    # specify model and fields
    class Meta:
        model = GeeksModel
        fields = '__all__'


class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
