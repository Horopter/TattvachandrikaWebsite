from django.test import TestCase
from api.serializers import SubscriberTypeSerializer
from api.models import SubscriberType
import uuid


class TestSubscriberTypeSerializer(TestCase):
    def setUp(self):
        self.valid_data = {"_id": str(uuid.uuid4()), "name": "Regular"}
        self.invalid_data_missing_name = {"_id": str(uuid.uuid4())}
        self.invalid_data_empty_name = {"_id": str(uuid.uuid4()), "name": ""}

    def tearDown(self):
        SubscriberType.objects.all().delete()

    def test_valid_data(self):
        serializer = SubscriberTypeSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(SubscriberType.objects.count(), 1)

    def test_missing_name_field(self):
        serializer = SubscriberTypeSerializer(data=self.invalid_data_missing_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_empty_name_field(self):
        serializer = SubscriberTypeSerializer(data=self.invalid_data_empty_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_create_instance(self):
        serializer = SubscriberTypeSerializer(data={"_id": str(uuid.uuid4()), "name": "New Type"})
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        instance = serializer.save()
        self.assertEqual(instance.name, "New Type")

    def test_partial_update(self):
        instance = SubscriberType.objects.create(**self.valid_data)
        serializer = SubscriberTypeSerializer(instance, data={"name": "Updated Regular"}, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.name, "Updated Regular")