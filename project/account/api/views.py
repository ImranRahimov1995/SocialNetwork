from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from account.models import Profile,PublicStatus
from braces.views import CsrfExemptMixin

# from rest_framework import authentication
# from rest_framework.views import APIView
# from rest_framework.response import Response



class PublicStatusRetrieveView(CsrfExemptMixin,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicStatusSerializer
    queryset = PublicStatus.objects.all()
    lookup_field = 'owner'
    permission_classes = [IsAuthenticated,]


# class TestView(APIView):
#     permission_classes = [IsAuthenticated,]
#     authentication_classes = [authentication.SessionAuthentication, authentication.BasicAuthentication]

#     def get(self, request, format=None):
        
#         print(request.data)
#         test_data = 'ok'
#         return Response(test_data)

#     def post(self, request, format=None):
        
#         print(request.data)
#         test_data = 'ok'
#         return Response(test_data)