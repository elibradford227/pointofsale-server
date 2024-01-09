from django.http import HttpResponseServerError
from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pointofsaleapi.models import Item

class ItemView(ViewSet):
    """Level up Item view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single items

        Returns:
            Response -- JSON serialized item
        """
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        """Handle GET requests to get all items

        Returns:
            Response -- JSON serialized list of items
        """
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def create(self, request):
        """Handle POST operations

        Returns
          Response -- JSON serialized item instance
        """
        item = Item.objects.create(
            name = request.data["name"],
            price = request.data["price"],
        )

        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a item

        Returns:
          Response -- Empty body with 204 status code
        """

        item = Item.objects.get(pk=pk)
      
        item.name = request.data["name"],
        item.price = request.data["price"],

        item.save()
        
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, response, pk):
        """Deletes Data

        Returns:
            Response: Empty body with 204 code
        """
        item = Item.objects.get(pk=pk)
        item.delete()
        return response(None, status=status.HTTP_204_NO_CONTENT)
        

class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for items

    """
    class Meta:
        model = Item
        fields = ('id', 'name', 'price')
        depth = 1