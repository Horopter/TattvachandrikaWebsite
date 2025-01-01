from django.test import TestCase
from api.serializers import PaymentModeSerializer
from api.models import PaymentMode
import uuid


class TestPaymentModeSerializer(TestCase):
    def setUp(self):
        self.valid_data = {"_id": str(uuid.uuid4()), "name": "Credit Card"}
        self.invalid_data_missing_name = {"_id": str(uuid.uuid4())}

    def tearDown(self):
        PaymentMode.objects.all().delete()

    def test_valid_data(self):
        serializer = PaymentModeSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(PaymentMode.objects.count(), 1)

    def test_missing_required_field(self):
        data = {"_id": str(uuid.uuid4())}  # Missing 'name'
        serializer = PaymentModeSerializer(data=data)
        self.assertFalse(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")


    def test_partial_update(self):
        instance = PaymentMode.objects.create(**self.valid_data)
        serializer = PaymentModeSerializer(instance, data={"name": "Debit Card"}, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.name, "Debit Card")
