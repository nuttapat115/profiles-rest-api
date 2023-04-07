from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    ''' Test api view'''

    def get(self, request, format=None):
        ''' Return a list of APIView features'''

        an_apiview = [
            'Uss HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the mosrt control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
