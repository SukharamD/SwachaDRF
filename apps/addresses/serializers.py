from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    full_address = serializers.ReadOnlyField()

    class Meta:
        model = Address
        exclude = ["user", "created_at"]

    def create(self, validated_data):
        user = self.context["request"].user

        if validated_data.get("is_default", False):
            Address.objects.filter(
                user=user,
                is_default=True
            ).update(is_default=False)

        validated_data["full_address"] = (
            f"{validated_data['house_or_flat']}, "
            f"{validated_data['street']}, "
            f"{validated_data['area']}, "
            f"{validated_data['city']}, "
            f"{validated_data['state']} - "
            f"{validated_data['pincode']}"
        )

        return Address.objects.create(
            user=user,
            **validated_data
        )
    