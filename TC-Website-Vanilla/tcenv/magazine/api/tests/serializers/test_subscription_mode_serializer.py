from django.test import TestCase
from api.serializers import SubscriptionModeSerializer
from api.models import SubscriptionMode
import uuid


class TestSubscriptionModeSerializer(TestCase):
    def setUp(self):
        self.valid_data = {"_id": str(uuid.uuid4()), "name": "Monthly"}
        self.invalid_data_missing_name = {"_id": str(uuid.uuid4())}
        self.invalid_data_empty_name = {"_id": str(uuid.uuid4()), "name": ""}

    def tearDown(self):
        SubscriptionMode.objects.all().delete()

    def test_valid_data(self):
        serializer = SubscriptionModeSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(SubscriptionMode.objects.count(), 1)

    def test_missing_name_field(self):
        serializer = SubscriptionModeSerializer(data=self.invalid_data_missing_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_empty_name_field(self):
        serializer = SubscriptionModeSerializer(data=self.invalid_data_empty_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_create_instance(self):
        serializer = SubscriptionModeSerializer(data=self.valid_data)
        serializer.is_valid()
        instance = serializer.save()
        self.assertEqual(instance.name, "Monthly")
        self.assertIsNotNone(instance._id)

    def test_partial_update(self):
        instance = SubscriptionMode.objects.create(**self.valid_data)
        serializer = SubscriptionModeSerializer(instance, data={"name": "Updated Mode"}, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.name, "Updated Mode")
