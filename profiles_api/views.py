from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    ''' Test api view'''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        ''' Return a list of APIView features'''

        an_apiview = [
            'Uss HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the mosrt control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        ''' Handle updating an object'''
        return Response({'message': 'PUT'})
    
    def patch(self, request, pk=None):
        ''' Handle  update an object'''

        return Response({'message': 'PATCH'})
    
    def delete(self, request, pk=None):
        ''' Handle deleting an object'''
        return Response({'message': 'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    '''Test API Viewset'''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''Return a list'''
        an_viewset = [
            'Uss action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Rounters',
            'Provides more fuctionality eith less code',
        ]

        return Response({'message': 'Hello!', 'an_viewset': an_viewset})

    def create(self, request):
        '''Create'''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        ''' retrieve'''
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        ''' update'''
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        ''' partroy_update'''
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        ''' destroy'''
        return Response({'http_method': 'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    ''' Handle creating and updating profiles'''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')