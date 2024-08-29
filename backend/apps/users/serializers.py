from rest_framework import serializers
from .models import Educator, Parent, Student


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'password']
        extra_kwargs = {'password': {'write_only': True}}


class StudentSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = Student
        fields = UserSerializer.Meta.fields + [
            'parent_id', 'age', 'grade_level', 'sensory_preference', 'communication_preference',
            'attention_span', 'reading_writing_skills', 'math_skills', 'technology_comfort', 'interests'
        ]

    def create(self, validated_data):
        student = Student.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            parent_id=validated_data['parent_id'],
            age=validated_data['age'],
            grade_level=validated_data['grade_level'],
            sensory_preference=validated_data['sensory_preference'],
            communication_preference=validated_data['communication_preference'],
            attention_span=validated_data['attention_span'],
            reading_writing_skills=validated_data['reading_writing_skills'],
            math_skills=validated_data['math_skills'],
            technology_comfort=validated_data['technology_comfort'],
            interests=validated_data['interests']
        )
        return student


class ParentSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = Parent
        fields = UserSerializer.Meta.fields + ['number_of_children']

    def create(self, validated_data):
        user = Parent.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            number_of_children=validated_data['number_of_children']
        )
        return user


class EducatorSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = Educator
        fields = UserSerializer.Meta.fields + ['subject']

    def create(self, validated_data):
        user = Educator.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            subject=validated_data['subject']
        )
        return user
