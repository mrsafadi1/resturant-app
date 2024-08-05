from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from .models import *
from .serializers import *

# @api_view(['GET'])
# @permission_classes([AllowAny])
class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        # if self.request.method == 'GET':
        self.permission_classes = [AllowAny]
        # elif self.request.method == 'POST':
        #     self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
     
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        date = serializer.validated_data['date']
        time = serializer.validated_data['time']

        # Check if the time is available
        available_times = Booking.get_available_times(date)
        
        if time not in available_times:
            response = f"error: The selected time is not available. {available_times}"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
class BookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]

        return super().get_permissions()
     
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        date = serializer.validated_data['date']
        time = serializer.validated_data['time']

        # Check if the time is available
        available_times = Booking.get_available_times(date)
        if time not in available_times:
            return Response({"error": "The selected time is not available."}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)
        return Response(serializer.data)

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        return super().get_permissions()
    
class MenuRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]

        return super().get_permissions()
    