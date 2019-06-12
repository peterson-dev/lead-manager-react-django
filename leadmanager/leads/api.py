from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer 

# Lead Viewset
# allows us to create full crud api without having to specify explicit methods for the functionality 
class LeadViewSet(viewsets.ModelViewSet):
  queryset = Lead.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = LeadSerializer