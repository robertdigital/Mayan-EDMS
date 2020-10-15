from django.utils.encoding import force_text

from rest_framework import serializers
from rest_framework.reverse import reverse

from mayan.apps.storage.models import SharedUploadedFile

from ..models.document_models import Document
from ..models.document_file_models import DocumentFile
from ..models.document_file_page_models import DocumentFilePage
from ..models.document_type_models import DocumentType, DocumentTypeFilename
from ..models.document_version_models import DocumentVersion
from ..models.document_version_page_models import DocumentVersionPage
from ..models.misc_models import RecentDocument

from ..settings import setting_language
from ..tasks import task_document_file_upload


class DocumentFileCreateSerializer(serializers.Serializer):
    comment = serializers.CharField(allow_blank=True)
    file = serializers.FileField(use_url=False)

    def save(self, document, _user):
        shared_uploaded_file = SharedUploadedFile.objects.create(
            file=self.validated_data['file']
        )

        task_document_file_upload.delay(
            comment=self.validated_data.get('comment', ''),
            document_id=document.pk,
            shared_uploaded_file_id=shared_uploaded_file.pk, user_id=_user.pk
        )


class DocumentFilePageSerializer(serializers.HyperlinkedModelSerializer):
    document_file_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        fields = ('document_file_url', 'image_url', 'page_number', 'url')
        model = DocumentFilePage

    def get_document_file_url(self, instance):
        return reverse(
            viewname='rest_api:documentfile-detail', args=(
                instance.document_file.document_id, instance.document_file_id,
            ), request=self.context['request'], format=self.context['format']
        )

    def get_image_url(self, instance):
        return reverse(
            viewname='rest_api:documentfilepage-image', args=(
                instance.document_file.document_id, instance.document_file_id,
                instance.pk,
            ), request=self.context['request'], format=self.context['format']
        )

    def get_url(self, instance):
        return reverse(
            viewname='rest_api:documentfilepage-detail', args=(
                instance.document_file.document_id, instance.document_file_id,
                instance.pk,
            ), request=self.context['request'], format=self.context['format']
        )


class DocumentFileSerializer(serializers.HyperlinkedModelSerializer):
    document_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()
    pages_url = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        extra_kwargs = {
            'document': {'view_name': 'rest_api:document-detail'},
            'file': {'use_url': False},
        }
        fields = (
            'checksum', 'comment', 'document_url', 'download_url', 'encoding',
            'file', 'mimetype', 'pages_url', 'size', 'timestamp', 'url'
        )
        model = DocumentFile
        read_only_fields = ('document', 'file', 'size')

    def get_size(self, instance):
        return instance.size

    def get_document_url(self, instance):
        return reverse(
            viewname='rest_api:document-detail', args=(
                instance.document_id,
            ), request=self.context['request'], format=self.context['format']
        )

    def get_download_url(self, instance):
        return reverse(
            viewname='rest_api:documentfile-download', args=(
                instance.document_id, instance.pk,
            ), request=self.context['request'], format=self.context['format']
        )

    def get_pages_url(self, instance):
        return reverse(
            viewname='rest_api:documentfilepage-list', args=(
                instance.document_id, instance.pk,
            ), request=self.context['request'], format=self.context['format']
        )

    def get_url(self, instance):
        return reverse(
            viewname='rest_api:documentfile-detail', args=(
                instance.document_id, instance.pk,
            ), request=self.context['request'], format=self.context['format']
        )


class DocumentFileWritableSerializer(serializers.ModelSerializer):
    document_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()
    pages_url = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        extra_kwargs = {
            'file': {'use_url': False},
        }
        fields = (
            'checksum', 'comment', 'document_url', 'download_url', 'encoding',
            'file', 'mimetype', 'pages_url', 'timestamp', 'url'
        )
        model = DocumentFile
        read_only_fields = ('document', 'file')

    def get_document_url(self, instance):
        return reverse(
            viewname='rest_api:document-detail', args=(
                instance.document_id,
            ), request=self.context['request'], format=self.context['format']
        )

    def get_download_url(self, instance):
        return reverse(
            viewname='rest_api:documentfile-download', args=(
                instance.document_id, instance.pk,
            ), request=self.context['request'], format=self.context['format']
        )

    def get_pages_url(self, instance):
        return reverse(
            viewname='rest_api:documentfilepage-list', args=(
                instance.document_id, instance.pk,
            ), request=self.context['request'], format=self.context['format']
        )

    def get_url(self, instance):
        return reverse(
            viewname='rest_api:documentfile-detail', args=(
                instance.document_id, instance.pk,
            ), request=self.context['request'], format=self.context['format']
        )