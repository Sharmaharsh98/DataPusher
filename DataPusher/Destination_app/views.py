from rest_framework.response import Response
from .serializers import DestinationSerializers, Destination_model
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from .permissions import AuthenticateOrNot

from rest_framework import status, viewsets
from  django.shortcuts import get_object_or_404


# Create your views here.
class DestinationView(viewsets.ViewSet):
    serializers_class = DestinationSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [AuthenticateOrNot]

    def create(self, request):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, content_type="application/json", status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def list(self, request):
        data = Destination_model.objects.all()
        serializer = self.serializers_class(data, many=True)
        return Response(data=serializer.data, content_type="application/json", status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        data = get_object_or_404(Destination_model ,pk=pk)    
        serializer = self.serializers_class(data)
        return Response(data=serializer.data, content_type="application/json", status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        data = get_object_or_404(Destination_model, pk=pk)
        serializer = self.serializers_class(data=request.data, instance=data )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, content_type="application/json", status=205)
        return Response(data=serializer.errors, status=400)
    
    def partial_update(self, request, pk=None):
        data = get_object_or_404(Destination_model, pk=pk)
        serializer = self.serializers_class(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, content_type="application/json", status=205)
        return Response(data=serializer.errors, status=400)

    def destroy(self, request, pk=None):
        data = get_object_or_404(Destination_model, pk=pk)
        data.delete()
        return Response(data=None, status=204)

'''
# Create your views here.
class DestinationView(ModelViewSet):
    serializer_class = DestinationSerializers
    queryset = Destination_model.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
'''