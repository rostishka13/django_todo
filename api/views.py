from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import TaskSerializer, UserSerializer, RegistrationSerializer
from base.models import Task
from rest_framework import status, mixins, generics
from rest_framework import permissions



# Create your views here.

##############################FIRST  METHOD ###############
# @api_view(['GET', 'POST'])
# def task_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Task.objects.all()
#         serializer = TaskSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TaskSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TaskSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
########SECOND METHOD ##########
# @api_view(["GET"])
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/task-list/',
# 		'Detail View':'/task-detail/<str:pk>/',
# 		'Create':'/task-create/',
# 		'Update':'/task-update/<str:pk>/',
# 		'Delete':'/task-delete/<str:pk>/',
# 		}
#
# 	return Response(api_urls)
#
# @api_view(['GET'])
# def taskList(request):
# 	tasks = Task.objects.all()
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)
#
#
# @api_view(['GET'])
# def taskDetail(request, pk):
# 	task = Task.objects.get(id = pk)
# 	serializer = TaskSerializer(task, many=False)
# 	return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskCreate(request):
#
# 	serializer = TaskSerializer(data = request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 	return Response(serializer.data)
#
# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Task.objects.get(id = pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 	return Response(serializer.data)
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Task.objects.get(id = pk)
# 	task.delete()
# 	return Response("Your task successfully deleted")



# USING API CLASS_BASED VIEWS
# class TaskList(APIView):
# 	"""
# 	List all task, or create a new task
# 	"""
# 	def get(self, request, format=None):
# 		task = Task.objects.all()
# 		serializer = TaskSerializer(task, many = True)
# 		return Response(serializer.data)
#
# 	def post(self, request, format=None):
# 		serializer = TaskSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#
# class TaksDetail(APIView):
# 	"""
# 	Retrieve, update or delete a task instance
# 	"""
#
# 	def get_object(self, pk):
# 		try:
# 			return  Task.objects.get(pk=pk)
# 		except Task.DoesNotExist:
# 			raise Http404
#
# 	def get(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = TaskSerializer(snippet)
# 		return Response(serializer.data)
#
# 	def put(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = TaskSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	def delete(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)




# Using mixins

# class TaskList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class TaskDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# Using generic class-based  views

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]



class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]





class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]



@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'successfully registered a new user'
        data['email'] = user.email
        data['username'] = user.username
        token = Token.objects.get(user=user).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)
