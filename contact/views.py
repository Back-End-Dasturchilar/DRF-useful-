from .models import Contact, ContactInfo
from .serializers import ContactInfoSerializer, ContactSerializer
from rest_framework import generics


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()[:1]
    serializer_class = ContactInfoSerializer
