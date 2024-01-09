from django.http import HttpResponseServerError
from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pointofsaleapi.models import OrderItem

class OrderItemView(ViewSet):
    """Level up orderitem view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order items

        Returns:
            Response -- JSON serialized order item
        """
        order_item = OrderItem.objects.get(pk=pk)
        serializer = OrderItemSerializer(order_item, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        """Handle GET requests to get all order items

        Returns:
            Response -- JSON serialized list of order items
        """
        order_item = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def create(self, request):
        """Handle POST operations

        Returns
          Response -- JSON serialized order item instance
        """
        order_item = OrderItem.objects.create(
            order = request.data["order"],
            item = request.data["item"]
        )

        serializer = OrderItemSerializer(order_item, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a order item

        Returns:
          Response -- Empty body with 204 status code
        """

        order_item = orderitem.objects.get(pk=pk)
      
        order_item.order = request.data["order"],
        order_item.item = request.data["item"]

        order_item.save()
        
        serializer = OrderItemSerializer(order_item, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, response, pk):
        """Deletes Data

        Returns:
            Response: Empty body with 204 code
        """
        order_item = OrderItem.objects.get(pk=pk)
        order_item.delete()
        return response(None, status=status.HTTP_204_NO_CONTENT)
        

class OrderItemSerializer(serializers.ModelSerializer):
    """JSON serializer for order items

    """
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'item')
        depth = 1