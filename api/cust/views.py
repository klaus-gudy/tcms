from rest_framework.generics import CreateAPIView, ListAPIView
from api.cust.serializers import CustomerSerializer

from cust.models import Customer

class CustomerCreateAPIView(CreateAPIView):
    serializer_class= CustomerSerializer

class CustomerListAPIView(ListAPIView):
    serializer_class= CustomerSerializer
    model = Customer
    queryset = Customer.objects.all()


