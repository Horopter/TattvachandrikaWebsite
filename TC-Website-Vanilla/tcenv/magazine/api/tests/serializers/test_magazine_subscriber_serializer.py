from django.test import TestCase
from api.serializers import MagazineSubscriberSerializer
from api.models import MagazineSubscriber, SubscriberCategory, SubscriberType
import uuid


class TestMagazineSubscriberSerializer(TestCase):
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
