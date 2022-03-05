from rest_framework import serializers
from course.models import Category, Channel, Course


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ChannelSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()
    class Meta:
        model = Channel
        fields = '__all__'
    
    def create(self, validated_data):
        category_data = validated_data.pop('categories')
        categories = CategorySerializer.create(CategorySerializer(), validated_data=category_data)
        channel = Channel.objects.create(categories=categories, channel_name=validated_data['channel_name'])
        return channel
        

class CourseSerializer(serializers.ModelSerializer):
    course_channel = ChannelSerializer()
    class Meta:
        model = Course
        fields = '__all__'
        
    def create(self, validated_data):
        channel_data = validated_data.pop('course_channel')
        course_channel = ChannelSerializer.create(ChannelSerializer(),validated_data=channel_data) 
        course = Course.objects.create(course_channel=course_channel, **validated_data)
        return course
               

    