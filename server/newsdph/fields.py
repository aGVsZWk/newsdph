from packaging import version

from marshmallow import fields, ValidationError


class Version(fields.Field):
    """Version field that deserializes to a Version object."""

    def _deserialize(self, value, *args, **kwargs):
        try:
            return version.Version(value)
        except version.InvalidVersion:
            raise ValidationError("Not a valid version.")

    def _serialize(self, value, *args, **kwargs):
        return str(value)
