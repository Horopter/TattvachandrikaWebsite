from django.test import TestCase
from api.serializers import SubscriptionLanguageSerializer
from api.models import SubscriptionLanguage
import uuid


class TestSubscriptionLanguageSerializer(TestCase):
    def setUp(self):
        self.valid_data = {"_id": str(uuid.uuid4()), "name": "English"}
        self.invalid_data_missing_name = {"_id": str(uuid.uuid4())}
        self.invalid_data_empty_name = {"_id": str(uuid.uuid4()), "name": ""}

    def tearDown(self):
        SubscriptionLanguage.objects.all().delete()

    def test_valid_data(self):
        serializer = SubscriptionLanguageSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(SubscriptionLanguage.objects.count(), 1)

    def test_missing_name_field(self):
        serializer = SubscriptionLanguageSerializer(data=self.invalid_data_missing_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_empty_name_field(self):
        serializer = SubscriptionLanguageSerializer(data=self.invalid_data_empty_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_create_instance(self):
        serializer = SubscriptionLanguageSerializer(data={"_id": str(uuid.uuid4()), "name": "XYZABC"})
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        instance = serializer.save()
        self.assertEqual(instance.name, "XYZABC")

    def test_partial_update(self):
        instance = SubscriptionLanguage.objects.create(**self.valid_data)
        serializer = SubscriptionLanguageSerializer(instance, data={"name": "Updated Language"}, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.name, "Updated Language")
