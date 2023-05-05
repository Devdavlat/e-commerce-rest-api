from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializer import ProductSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(["GET"])
def get_product_list(request):
    products = Product.objects.all()
    # products_data = [{'id': product.id, 'title': product.title} for product in products]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["POST", "GET"])
def category(request):
    serializer_class = CategorySerializer
    queryset = Product.objects.all()
    serializer = serializer_class(queryset, many=True)
    if request.method == "POST":
        serializer = serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
