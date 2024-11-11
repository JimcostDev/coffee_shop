from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "available",
            "picture",
        ]
        #fields = '__all__'