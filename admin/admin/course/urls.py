from django.urls import path
from course.views import CourseDetailViewSet, CoursesViewSet

urlpatterns = [
    path('courses', CoursesViewSet.as_view({
          'get': 'list',
          'post': 'create'
        })),
     path('courses/<str:pk>', CourseDetailViewSet.as_view({
          'get': 'retrieve',
          'delete': 'destroy',
          'put': 'update'
        }))
]