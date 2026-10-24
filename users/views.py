from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import UserSerializer, StudentSerializer, ProductSerializer, CategorySerializer
from .models import User, Student, Product,Category

user = {
    "name": "Daniel",
    "email": "daniel@mail.com",
    "phone": "668820160",
    "campus": "UREF",
    "gender": "1"
}


@api_view(["GET"])
def get_user(request):
    return Response(UserSerializer(user).data)


@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)

@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PATCH", "DELETE"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == "PATCH":
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    model = Product
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
    
    @action(detail=False, methods=['get'])
    def expensive(self, request):
        products = Product.objects.order_by('-price')[:5]
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()