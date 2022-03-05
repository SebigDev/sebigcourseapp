from rest_framework import viewsets
from rest_framework.response import Response
from course.models import Course
from course.publisher import publish
from course.serialisers import CourseSerializer


class CoursesViewSet(viewsets.ViewSet):
    def list(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data) 
    
    def create(self, request):
        try:
            serializer = CourseSerializer(data=request.data)  
            serializer.is_valid(raise_exception=True) 
            serializer.save()
            publish('course_created', serializer.data)
            return Response(serializer.data, status=201) 
        except Exception as ex:
            print('EXCEPTIONS: ',ex)
            return Response('Failed to create course', status=400)  
    
       
class  CourseDetailViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            course = Course.objects.get(id=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=200)
        except:
            return Response('Course with ID: {} not available'.format(pk), status=404)
    
    def destroy(self, request, pk=None):
        try:
            course = Course.objects.get(id=pk)
            course.delete()
            return Response('Deleted successfully', status=204)
        except:
            return Response('Course with ID: {} not available'.format(pk), status=404)
    
    def update(self, request, pk=None):
        try:
            course = Course.objects.get(id=pk)
            serializer = CourseSerializer(course, data=request.data)
            serializer.save()
            return Response(serializer.data, status=204)
        except:
            return Response('Course with ID: {} not available'.format(pk), status=404)
