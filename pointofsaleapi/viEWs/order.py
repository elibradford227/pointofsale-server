from django.http import HttpResponseServerError
from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pointofsaleapi.models import Order, User, OrderItem, Item
from .item import ItemSerializer
from django.views.decorators.http import require_http_methods
from .revenue import RevenueView

class OrderView(ViewSet):
    """Level up Order view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single orders

        Returns:
            Response -- JSON serialized order
        """
        order = Order.objects.get(pk=pk)
        
        orderitem_id = OrderItem.objects.filter(order=order.pk)
        items = []
        for item in orderitem_id:
            items.append(item.item_id)
        order.items = Item.objects.filter(pk__in=items)
        
        serializer = OrderSerializer(order, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        """Handle GET requests to get all orders

        Returns:
            Response -- JSON serialized list of orders
        """
        order = Order.objects.all()
    
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def create(self, request):
        """Handle POST operations

        Returns
          Response -- JSON serialized Order instance
        """
        user = User.objects.get(uid=request.data['uid'])
        
        order = Order.objects.create(
            user = user,
            name = request.data["name"],
            status = 'Open',
            customer_phone = request.data["customer_phone"],
            customer_email = request.data["customer_email"],
            type = request.data["type"],
            closed = False
        )

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a Order

        Returns:
          Response -- Empty body with 204 status code
        """

        order = Order.objects.get(pk=pk)
        
        user = User.objects.get(uid=request.data['uid'])
      
        order.user = user
        order.name = request.data["name"]
        order.status = request.data["status"]
        order.customer_phone = request.data["customer_phone"]
        order.customer_email = request.data["customer_email"]
        order.type = request.data["type"]
        order.closed = request.data["closed"]

        order.save()
        
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, response, pk):
        """Deletes Data

        Returns:
            Response: Empty body with 204 code
        """
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
        

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders

    """
    
    items = ItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'name', 'user', 'status', 'customer_phone', 'customer_email', 'type', 'closed', 'items')
        depth = 1