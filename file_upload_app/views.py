import magic
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileSerializer
from .tasks import process_uploaded_file


class FileUploadView(APIView):
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            uploaded_file = file_serializer.validated_data['file']
            file_type = magic.Magic()
            mime_type = file_type.from_buffer(uploaded_file.read(1024))

            file_instance = file_serializer.save()
            file_id = file_instance.id

            process_uploaded_file.delay(file_id, mime_type)

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
