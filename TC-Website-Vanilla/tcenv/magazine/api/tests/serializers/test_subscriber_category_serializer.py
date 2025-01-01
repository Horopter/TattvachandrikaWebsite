from django.test import TestCase
from mongoengine import connect, disconnect
from api.serializers import SubscriberCategorySerializer
from api.models import SubscriberCategory
import uuid


class TestSubscriberCategorySerializer(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Connect to the test MongoDB database
        cls.connection = connect(
            db="test_database",  # Replace with your test database name
            host="mongodb://localhost:27017/test_database",  # Update the host if needed
            alias="test3"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Drop the test database and disconnect
        cls.connection.drop_database("test_database")
        disconnect(alias="test3")

    def setUp(self):
        self.valid_data = {"_id": str(uuid.uuid4()), "name": "Domestic"}
        self.invalid_data_missing_name = {"_id": str(uuid.uuid4())}
        self.invalid_data_empty_name = {"_id": str(uuid.uuid4()), "name": ""}

    def tearDown(self):
        SubscriberCategory.objects.all().delete()

    def test_valid_data(self):
        serializer = SubscriberCategorySerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(SubscriberCategory.objects.count(), 1)

    def test_missing_name_field(self):
        serializer = SubscriberCategorySerializer(data=self.invalid_data_missing_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_empty_name_field(self):
        serializer = SubscriberCategorySerializer(data=self.invalid_data_empty_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_create_instance(self):
        serializer = SubscriberCategorySerializer(data={"_id": str(uuid.uuid4()), "name": "New Category"})
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        instance = serializer.save()
        self.assertEqual(instance.name, "New Category")

    def test_partial_update(self):
        instance = SubscriberCategory.objects.create(**self.valid_data)
        serializer = SubscriberCategorySerializer(instance, data={"name": "Updated Domestic"}, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.name, "Updated Domestic")
