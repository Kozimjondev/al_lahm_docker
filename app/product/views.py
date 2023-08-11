from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import Product, Review, Accessory, Connection
from .serializers import ProductSerializer, AccessorySerializer, ConnectionSerializer, ReviewSerializer
from rest_framework import permissions, generics
from .permissions import IsAdminOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    @swagger_auto_schema(operation_summary="Maxsulotlar ro'yhati")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Maxsulot yaratish")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    @swagger_auto_schema(operation_summary="Har bir maxsulotni ko'rish (Faqat admin uchun)")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir maxsulotni o`zgartirish (Faqat admin uchun)")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir maxsulotni o'chirish (Faqat admin uchun)")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AccessoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Accessory.objects.all().order_by('-created_at')
    serializer_class = AccessorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    @swagger_auto_schema(operation_summary="Aksessuarlar ro'yhati")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Aksessuar yaratish")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AccessoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication, )

    @swagger_auto_schema(operation_summary="Har bir aksessuarni ko'rish (Faqat admin uchun)")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir aksessuarni o`zgartirish (Faqat admin uchun)")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir aksessuarni o'chirish (Faqat admin uchun)")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ("post",)
    throttle_scope = "review-post"
    authentication_classes = (BasicAuthentication, )

    @swagger_auto_schema(operation_summary="Otzivlar ro'yhati")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Otziv qoldirish")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ConnectionPostView(generics.CreateAPIView):
    serializer_class = ConnectionSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ("post",)
    throttle_scope = "connection-post"
    authentication_classes = (BasicAuthentication, )

    @swagger_auto_schema(operation_summary="To'liq ismi, telefon raqami va xabar qoldirish")
    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ConnectionListAPIView(generics.ListAPIView):
    queryset = Connection.objects.all().order_by('created_at')
    serializer_class = ConnectionSerializer
    permission_classes = (permissions.IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    @swagger_auto_schema(operation_summary="Bog'lanish uchun qoldirgan xabarlar ro'yhati")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([permissions.AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None and user.is_superuser:
        token, _ = Token.objects.get_or_create(user=user)
        response = {
            "message": "Login successful",
            "token": token.key
        }
        return Response(data=response, status=200)
    else:
        return Response(data={'message': 'Invalid credentials'}, status=401)
