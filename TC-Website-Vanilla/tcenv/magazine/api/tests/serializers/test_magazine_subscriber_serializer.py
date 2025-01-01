from django.test import TestCase
from mongoengine import connect, disconnect
from api.serializers import MagazineSubscriberSerializer
from api.models import MagazineSubscriber, SubscriberCategory, SubscriberType
import uuid


class TestMagazineSubscriberSerializer(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Connect to the test MongoDB database
        cls.connection = connect(
            db="test_database",  # Replace with your test database name
            host="mongodb://localhost:27017/test_database",  # Update the host if needed
            alias="test1"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Drop the test database and disconnect
        cls.connection.drop_database("test_database")
        disconnect(alias="test1")

    def setUp(self):
        self.tearDown()
        self.category = SubscriberCategory.objects.create(_id=str(uuid.uuid4()), name="Domestic")
        self.stype = SubscriberType.objects.create(_id=str(uuid.uuid4()), name="Regular")
        self.valid_data = {
            "_id": str(uuid.uuid4()),
            "name": "Jane Doe",
            "registration_number": "REG12345",
            "email": "jane.doe@example.com",
            "category": str(self.category._id),
            "stype": str(self.stype._id),
        }
        self.invalid_data_missing_name = {"_id": str(uuid.uuid4()), "email": "jane.doe@example.com"}

    def tearDown(self):
        MagazineSubscriber.objects.all().delete()
        SubscriberCategory.objects.all().delete()
        SubscriberType.objects.all().delete()

    def test_valid_data(self):
        serializer = MagazineSubscriberSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(MagazineSubscriber.objects.count(), 1)

    def test_missing_required_field(self):
        serializer = MagazineSubscriberSerializer(data=self.invalid_data_missing_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_partial_update(self):
        instance = MagazineSubscriber.objects.create(**self.valid_data)
        serializer = MagazineSubscriberSerializer(
            instance, data={"name": "Updated Name"}, partial=True
        )
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.name, "Updated Name")
