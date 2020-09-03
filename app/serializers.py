from rest_framework import serializers 
from app.models import Student

 # Create your model serializer here.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'nim', 'name', 'departement', 'status')