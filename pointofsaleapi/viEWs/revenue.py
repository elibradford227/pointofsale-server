from django.http import HttpResponseServerError
from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from pointofsaleapi.models import Revenue, Order

class RevenueView(ViewSet):
    """Level up revenue view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single revenue instances

        Returns:
            Response -- JSON serialized revenue
        """
        revenue = Revenue.objects.get(pk=pk)
        serializer = RevenueSerializer(revenue, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        """Handle GET requests to get all revenue instancves

        Returns:
            Response -- JSON serialized list of revenues
        """
        revenue = Revenue.objects.all()
        serializer = RevenueSerializer(revenue, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def create(self, request):
        """Handle POST operations

        Returns
          Response -- JSON serialized revenue instance
        """
        order = Order.objects.get(pk=request.data['order'])
        
        revenue = Revenue.objects.create(
            order = order,
            total = request.data["total"],
            payment_type = request.data["payment_type"],
            tip = request.data["tip"],
            order_type = request.data["order_type"],
        )

        serializer = RevenueSerializer(revenue, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a revenue instance

        Returns:
          Response -- Empty body with 204 status code
        """

        revenue = Revenue.objects.get(pk=pk)
      
        revenue.order = request.data["order"]
        revenue.total = request.data["total"]
        revenue.payment_type = request.data["payment_type"]
        revenue.tip = request.data["tip"]
        revenue.order_type = request.data["order_type"]

        revenue.save()
        
        serializer = RevenueSerializer(revenue, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, response, pk):
        """Deletes Data

        Returns:
            Response: Empty body with 204 code
        """
        revenue = Revenue.objects.get(pk=pk)
        revenue.delete()
        return response(None, status=status.HTTP_204_NO_CONTENT)
        

class RevenueSerializer(serializers.ModelSerializer):
    """JSON serializer for revenues

    """
    class Meta:
        model = Revenue
        fields = ('id', 'order', 'total', 'payment_type', 'tip', 'order_type')
        depth = 1