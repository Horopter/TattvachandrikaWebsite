from django.test import TestCase
from mongoengine import connect, disconnect
from api.serializers import SubscriptionLanguageSerializer
from api.models import SubscriptionLanguage
import uuid


class TestSubscriptionLanguageSerializer(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Connect to the test MongoDB database
        cls.connection = connect(
            db="test_database",  # Replace with your test database name
            host="mongodb://localhost:27017/test_database",  # Update the host if needed
            alias="test5"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Drop the test database and disconnect
        cls.connection.drop_database("test_database")
        disconnect(alias="test5")

    def setUp(self):
        # Valid data for a SubscriptionLanguage instance
        self.valid_data = {"_id": str(uuid.uuid4()), "name": "English"}
        self.invalid_data_missing_name = {"_id": str(uuid.uuid4())}
        self.invalid_data_empty_name = {"_id": str(uuid.uuid4()), "name": ""}

    def tearDown(self):
        SubscriptionLanguage.objects.all().delete()

    def test_valid_data(self):
        serializer = SubscriptionLanguageSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        instance = serializer.save()
        self.assertEqual(instance.name, self.valid_data["name"])

    def test_missing_name_field(self):
        serializer = SubscriptionLanguageSerializer(data=self.invalid_data_missing_name)
        self.assertFalse(serializer.is_valid(), "Serializer should not validate missing 'name' field.")
        self.assertIn("name", serializer.errors, "'name' field validation error not raised.")

    def test_empty_name_field(self):
        serializer = SubscriptionLanguageSerializer(data=self.invalid_data_empty_name)
        self.assertFalse(serializer.is_valid(), "Serializer should not validate empty 'name' field.")
        self.assertIn("name", serializer.errors, "'name' field validation error not raised.")

    def test_create_instance(self):
        new_data = {"_id": str(uuid.uuid4()), "name": "XYZABC"}
        serializer = SubscriptionLanguageSerializer(data=new_data)
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        instance = serializer.save()
        self.assertEqual(instance.name, new_data["name"])

    def test_partial_update(self):
        instance = SubscriptionLanguage.objects.create(**self.valid_data)
        serializer = SubscriptionLanguageSerializer(instance, data={"name": "Updated Language"}, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.name, "Updated Language")
