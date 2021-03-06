from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from djvue.views import FileUploadView

from .serializers import LoginSerializer, ProfileSerializer, PDFUploadSerializer


class PDFUploadView(FileUploadView):
    permission_classes = (AllowAny,)
    serializer_class = PDFUploadSerializer


class LoginView(CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    serializer_class = LoginSerializer
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        """
        Used only to serve the serializer definition
        """
        serializer = self.get_serializer()
        data = {"serializer": serializer}
        return Response(data)


class ProfileView(CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        """
        Used only to serve the serializer definition
        """
        serializer = self.get_serializer()
        data = {"serializer": serializer}
        return Response(data)
