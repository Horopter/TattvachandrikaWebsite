from django.test import TestCase
from mongoengine import connect, disconnect
from api.serializers import (
    SubscriptionSerializer,
    SubscriptionPlanSerializer,
    PaymentModeSerializer,
    SubscriptionLanguageSerializer,
    SubscriptionModeSerializer,
    MagazineSubscriberSerializer,
    SubscriberCategorySerializer,
    SubscriberTypeSerializer
)
import uuid


class TestSubscriptionSerializer(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.connection = connect(
            db="test_database",
            host="mongodb://localhost:27017/test_database",
            alias="test7"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.connection.drop_database("test_database")
        disconnect(alias="test7")

    def setUp(self):
        self.tearDown()
        try:
            # Create SubscriberCategory
            category_data = {"_id": str(uuid.uuid4()), "name": "Individual"}
            category_serializer = SubscriberCategorySerializer(data=category_data)
            self.assertTrue(category_serializer.is_valid(), category_serializer.errors)
            self.category = category_serializer.save()

            # Create SubscriberType
            stype_data = {"_id": str(uuid.uuid4()), "name": "Domestic"}
            stype_serializer = SubscriberTypeSerializer(data=stype_data)
            self.assertTrue(stype_serializer.is_valid(), stype_serializer.errors)
            self.stype = stype_serializer.save()

            # Create SubscriptionLanguage
            language_data = {"_id": str(uuid.uuid4()), "name": "English"}
            language_serializer = SubscriptionLanguageSerializer(data=language_data)
            self.assertTrue(language_serializer.is_valid(), language_serializer.errors)
            self.language = language_serializer.save()

            # Create SubscriptionMode
            mode_data = {"_id": str(uuid.uuid4()), "name": "Online"}
            mode_serializer = SubscriptionModeSerializer(data=mode_data)
            self.assertTrue(mode_serializer.is_valid(), mode_serializer.errors)
            self.mode = mode_serializer.save()

            # Create MagazineSubscriber
            subscriber_data = {
                "_id": str(uuid.uuid4()),
                "name": "Test Subscriber",
                "registration_number": f"REG{uuid.uuid4().hex[:8]}",
                "email": "subscriber@example.com",
                "hasActiveSubscriptions": False,
                "category": str(self.category.pk),
                "stype": str(self.stype.pk),
            }
            subscriber_serializer = MagazineSubscriberSerializer(data=subscriber_data)
            self.assertTrue(subscriber_serializer.is_valid(), subscriber_serializer.errors)
            self.subscriber = subscriber_serializer.save()

            # Create SubscriptionPlan
            subscription_plan_data = {
                "_id": str(uuid.uuid4()),
                "version": "v1",
                "start_date": "2024-01-01",
                "subscription_price": 200.0,
                "subscription_language": str(self.language.pk),
                "subscription_mode": str(self.mode.pk),
                "duration_in_months": 6,
            }
            subscription_plan_serializer = SubscriptionPlanSerializer(data=subscription_plan_data)
            self.assertTrue(subscription_plan_serializer.is_valid(), subscription_plan_serializer.errors)
            self.subscription_plan = subscription_plan_serializer.save()

            # Create PaymentMode
            payment_mode_data = {"_id": str(uuid.uuid4()), "name": "Credit Card"}
            payment_mode_serializer = PaymentModeSerializer(data=payment_mode_data)
            self.assertTrue(payment_mode_serializer.is_valid(), payment_mode_serializer.errors)
            self.payment_mode = payment_mode_serializer.save()

            # Set valid subscription data
            self.valid_data = {
                "_id": str(uuid.uuid4()),
                "subscriber": str(self.subscriber.pk),
                "subscription_plan": str(self.subscription_plan.pk),
                "start_date": "2024-02-01",
                "end_date": "2024-07-31",
                "payment_status": "Paid",
                "payment_mode": str(self.payment_mode.pk),
                "active": True,
            }
        except Exception as e:
            self.fail(f"Setup failed: {e}")

    def tearDown(self):
        for serializer_class in [
            SubscriptionSerializer,
            SubscriptionPlanSerializer,
            PaymentModeSerializer,
            SubscriptionLanguageSerializer,
            SubscriptionModeSerializer,
            MagazineSubscriberSerializer,
            SubscriberCategorySerializer,
            SubscriberTypeSerializer,
        ]:
            for obj in serializer_class.Meta.model.objects.all():
                obj.delete()

    def test_valid_data(self):
        serializer = SubscriptionSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        instance = serializer.save()
        self.assertEqual(instance.payment_status, "Paid")
        self.assertTrue(instance.active)

    def test_duplicate_subscription(self):
        subscription_serializer = SubscriptionSerializer(data=self.valid_data)
        self.assertTrue(subscription_serializer.is_valid(), subscription_serializer.errors)
        subscription_serializer.save()

        duplicate_serializer = SubscriptionSerializer(data=self.valid_data)
        self.assertFalse(duplicate_serializer.is_valid())
        self.assertIn("non_field_errors", duplicate_serializer.errors)

    def test_end_date_before_start_date(self):
        invalid_data = self.valid_data.copy()
        invalid_data["end_date"] = "2023-12-31"
        serializer = SubscriptionSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("end_date", serializer.errors)

    def test_partial_update(self):
        subscription_serializer = SubscriptionSerializer(data=self.valid_data)
        self.assertTrue(subscription_serializer.is_valid(), subscription_serializer.errors)
        subscription_instance = subscription_serializer.save()

        update_data = {"payment_status": "Paid", "active": False}
        serializer = SubscriptionSerializer(subscription_instance, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.payment_status, "Paid")
        self.assertFalse(updated_instance.active)

    def test_save_with_updated_payment_mode(self):
        subscription_serializer = SubscriptionSerializer(data=self.valid_data)
        self.assertTrue(subscription_serializer.is_valid(), subscription_serializer.errors)
        subscription_instance = subscription_serializer.save()

        new_payment_mode_data = {"_id": str(uuid.uuid4()), "name": "Debit Card"}
        new_payment_mode_serializer = PaymentModeSerializer(data=new_payment_mode_data)
        self.assertTrue(new_payment_mode_serializer.is_valid(), new_payment_mode_serializer.errors)
        new_payment_mode = new_payment_mode_serializer.save()

        update_data = {"payment_mode": str(new_payment_mode.pk)}
        serializer = SubscriptionSerializer(subscription_instance, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.payment_mode, new_payment_mode)

    def test_invalid_subscriber_reference(self):
        invalid_data = self.valid_data.copy()
        invalid_data["subscriber"] = "invalid_subscriber_id"
        serializer = SubscriptionSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("subscriber", serializer.errors)
