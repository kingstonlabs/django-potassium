from django.conf import settings

from lanthanum.schema_fields import TextField, ObjectField, CharField

from .rendering import MarkdownType


class MarkdownField(TextField):
    class Meta:
        python_type = MarkdownType


class LinkField(ObjectField):
    url = CharField(required=True)
    text = CharField(required=True)
    style = CharField(
        choices=[
            ('major', 'Major'),
            ('minor', 'Minor')
        ],
        default='minor',
        required=True
    )


class FileField(ObjectField):
    file_path = CharField(required=True)
    alt_description = CharField(required=False)

    def __init__(self, *args, **kwargs):
        self._media_type = kwargs.get('media_type')
        super().__init__(**kwargs)

    @property
    def schema(self):
        schema = super().schema
        file_path = schema['properties']['file_path']

        if self._required:
            file_path['minLength'] = 1

        media_link = {
            "href": "{}{{{{self}}}}".format(settings.MEDIA_URL)
        }
        if self._media_type is not None:
            media_link['mediaType'] = self._media_type

        file_path["links"] = [media_link]

        return schema

    @property
    def file(self):
        """
        Return a field file from storage to show in templates
        https://docs.djangoproject.com/en/2.1/_modules/django/db/models/fields/files/#FieldFile
        """
        pass

    @property
    def url(self):
        return "{}{}".format(settings.MEDIA_URL, self.file_path)


class ImageField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs['media_type'] = 'image'
        super().__init__(**kwargs)
