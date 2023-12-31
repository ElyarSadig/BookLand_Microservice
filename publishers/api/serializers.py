from rest_framework import serializers
from users.api.validation_utils import is_password_valid


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        error_message = is_password_valid(password=attrs["new_password"])

        if len(error_message) != 0:
            raise serializers.ValidationError({
                "result": {
                    "error_code": "InvalidPassword",
                    "error_message": error_message,
                    "errors": ""
                },
                "data": "",
            })

        return attrs


class UpdatePublisherProfileSerializer(serializers.Serializer):
    address = serializers.CharField(required=False, default="")
    phone_number2 = serializers.CharField(required=False, max_length=11, default="")
    publications_image = serializers.CharField(required=False, default="")
    card_number = serializers.CharField(required=False, default="", max_length=16, min_length=16)

