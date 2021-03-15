from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from app.models import Status
from .serializers import StatusModelSerializer
from authentication.api.permissions import IsOwnerOrReadOnly 

"""Example usage of APIView"""

# List API View with APIView (HTTP method: GET)
class StatusListSearchAPIView(APIView):

    def get(self, request, format=None):
        
        """queryset to retrieve"""
        qs = Status.objects.all()
        
        """serializing the model queryset"""
        serializer = StatusModelSerializer(qs, many=True) 

        """return serialized data"""
        return Response(serializer.data)

"""Creating individual API view to handle each individual HTTP method"""

# List API & Search API View with Generic view (HTTP method: GET)
class StatusAPIView(generics.ListAPIView):

    """serializer class"""
    serializer_class = StatusModelSerializer

    """permission for this view"""
    permission_classes = []
    
    """authentication applied to this view"""
    authentication_classes = []

    """overriding get_queryset to add Serach Capability"""
    def get_queryset(self):
        queryset = Status.objects.all()
        search_query = self.request.GET.get('q')
        if search_query is not None:
            queryset = queryset.filter(content__icontains=search_query)
        
        return queryset


# Create API View with Generic view (HTTP method: POST)
class StatusCreateAPIView(generics.CreateAPIView):

    """queryset for this view"""
    queryset = Status.objects.all()

    """serializer class"""
    serializer_class = StatusModelSerializer
    
    """permission for this view"""
    permission_classes = []
    
    """authentication applied to this view"""
    authentication_classes = []

# Detail API View with Generic view (HTTP method: GET)
class StatusDetailAPIView(generics.RetrieveAPIView):
    """permission for this view"""
    permission_classes = []
    
    """authentication applied to this view"""
    authentication_classes = []

    """queryset for this view"""
    queryset = Status.objects.all()

    """serializer class"""
    serializer_class = StatusModelSerializer

    """Model field used to for performing object lookup of individual model instances"""
    lookup_field = 'id' # or 'slug'

# Update API View with Generic view (HTTP method: PUT)
class StatusUpdateAPIView(generics.UpdateAPIView):
    """permission for this view"""
    permission_classes = []
    
    """authentication applied to this view"""
    authentication_classes = []

    """queryset for this view"""
    queryset = Status.objects.all()

    """serializer class"""
    serializer_class = StatusModelSerializer

    """Model field used to for performing object lookup of individual model instances"""
    lookup_field = 'id' # or 'slug'


# Delete API View with Generic view (HTTP method: DELETE)
class StatusDeleteAPIView(generics.DestroyAPIView):
    """permission for this view"""
    permission_classes = []
    
    """authentication applied to this view"""
    authentication_classes = []

    """queryset for this view"""
    queryset = Status.objects.all()

    """serializer class"""
    serializer_class = StatusModelSerializer

    """Model field used to for performing object lookup of individual model instances"""
    lookup_field = 'id' # or 'slug'
    
    
"""Creating individual API view to handle more than one HTTP methods together (Using Mixins)"""

# List API, Search API & Create API View with Mixins (HTTP methods: GET & POST)
class StatusListCreateMixinAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    """serializer class"""
    serializer_class = StatusModelSerializer

    """authentication classes applied to this view"""
    # authentication_classes = [SessionAuthentication] # Tells how the user is authenticated

    """permission classes for this view"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # You can only read this View If you are not authenticated
    
    """overriding get_queryset to add Serach Capability"""
    def get_queryset(self):
        # author = self.request.user
        queryset = Status.objects.all()
        search_query = self.request.GET.get('q')
        if search_query is not None:
            queryset = queryset.filter(content__icontains=search_query)
        
        return queryset
    
    """HTTP POST method, that implements creating and saving a new model instance."""
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    """Called by CreateModelMixin when saving a new object instance"""
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


# Detail API, Update API & Delete API View with Mixins (HTTP methods: GET, PUT & DELETE)
class StatusDetailUpdateDeleteMixinAPIView(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):

    """permission for this view"""
    permission_classes = [IsOwnerOrReadOnly]
    
    """authentication applied to this view"""
    # authentication_classes = []

    """queryset for this view"""
    queryset = Status.objects.all()

    """serializer class"""
    serializer_class = StatusModelSerializer

    """Model field used to for performing object lookup of individual model instances"""
    lookup_field = 'id' # or 'slug'

    """HTTP PUT method, that implements updating and saving an existing model instance."""
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    """HTTP DELETE method, that implements deletion of an existing model instance."""
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
 




    

    

    
