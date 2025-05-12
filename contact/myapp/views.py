from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # Add this import

from .models import Contact
from .serializers import ContactSerializer

@api_view(['GET', 'POST'])
def submit_contact(request):
    # Handle GET request (fetch all contacts)
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    # Handle POST request (save a new contact)
    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Contact saved!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)