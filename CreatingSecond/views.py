from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from .models import CurrentTime
from .serializers import TimeModelSerializer

class CurrentTimeViewSet(viewsets.ModelViewSet):
    queryset = CurrentTime.objects.all()
    serializer_class = TimeModelSerializer

    def create(self, request, *args, **kwargs):
        current_time_str = datetime.now().strftime('%H:%M:%S')
        current_time_instance = CurrentTime(current_time=current_time_str)
        current_time_instance.save()
        serializer = self.get_serializer(current_time_instance)
        return Response(serializer.data)
