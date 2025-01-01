from django.test import TestCase
from mongoengine import connect, disconnect
from api.serializers import SubscriptionPlanSerializer, SubscriptionLanguageSerializer, SubscriptionModeSerializer
from api.models import SubscriptionPlan, SubscriptionLanguage, SubscriptionMode
import uuid

class TestSubscriptionPlanSerializer(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Connect to the test MongoDB database
        cls.connection = connect(
            db="test_database",  # Replace with your test database name
            host="mongodb://localhost:27017/test_database",  # Update the host if needed
            alias="test7"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Drop the test database and disconnect
        cls.connection.drop_database("test_database")
        disconnect(alias="test7")

    def setUp(self):
        # Clean up database
        self.tearDown()

        # Use serializers to create valid instances of SubscriptionLanguage and SubscriptionMode
        language_data = {"_id": str(uuid.uuid4()), "name": "English"}
        mode_data = {"_id": str(uuid.uuid4()), "name": "Online"}

        # Create SubscriptionLanguage
        language_serializer = SubscriptionLanguageSerializer(data=language_data)
        self.assertTrue(
            language_serializer.is_valid(),
            msg=f"Language serializer errors: {language_serializer.errors}"
        )
        self.language = language_serializer.save()
        self.assertIsNotNone(self.language, "Failed to create SubscriptionLanguage.")

        # Create SubscriptionMode
        mode_serializer = SubscriptionModeSerializer(data=mode_data)
        self.assertTrue(
            mode_serializer.is_valid(),
            msg=f"Mode serializer errors: {mode_serializer.errors}"
        )
        self.mode = mode_serializer.save()
        self.assertIsNotNone(self.mode, "Failed to create SubscriptionMode.")

        # Create a valid SubscriptionPlan
        plan_data = {
            "_id": str(uuid.uuid4()),
            "start_date": "2024-01-01",
            "subscription_price": 200.0,
            "subscription_language": self.language.pk,  # Pass pk here
            "subscription_mode": self.mode.pk,          # Pass pk here
            "duration_in_months": 6,
        }
        plan_serializer = SubscriptionPlanSerializer(data=plan_data)
        self.assertTrue(
            plan_serializer.is_valid(),
            msg=f"Plan serializer errors: {plan_serializer.errors}"
        )
        try:
            self.plan = plan_serializer.save()
        except Exception as e:
            self.plan = None
            print(f"Error creating SubscriptionPlan: {e}")

        self.assertIsNotNone(self.plan, "Failed to create SubscriptionPlan during setup.")

        # Valid data for serializer tests
        self.valid_data = {
            "_id": str(uuid.uuid4()),
            "version": "v1",
            "start_date": "2024-02-01",
            "subscription_price": 300.0,
            "subscription_language": self.language.pk,  # Pass pk here
            "subscription_mode": self.mode.pk,          # Pass pk here
            "duration_in_months": 12,
        }

    def tearDown(self):
        SubscriptionPlan.objects.all().delete()
        SubscriptionLanguage.objects.all().delete()
        SubscriptionMode.objects.all().delete()

    def test_valid_data(self):
        serializer = SubscriptionPlanSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        instance = serializer.save()
        self.assertEqual(instance.subscription_language, self.language)
        self.assertEqual(instance.subscription_mode, self.mode)
        self.assertEqual(instance.subscription_price, 300.0)

    def test_missing_required_field(self):
        # Missing 'subscription_language' and 'subscription_mode'
        invalid_data = {
            "_id": str(uuid.uuid4()),
            "version": "v1",
            "start_date": "2024-02-01",
            "subscription_price": 300.0,
        }
        serializer = SubscriptionPlanSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        self.assertIn("subscription_language", serializer.errors)
        self.assertIn("subscription_mode", serializer.errors)

    def test_partial_update(self):
        partial_data = {"subscription_price": 150.0}
        serializer = SubscriptionPlanSerializer(instance=self.plan, data=partial_data, partial=True)
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.subscription_price, 150.0)
        self.assertEqual(updated_instance.duration_in_months, self.plan.duration_in_months)

    def test_generate_version_same_price(self):
        data = {
            "_id": str(uuid.uuid4()),
            "version": "v1",
            "start_date": "2024-01-01",
            "subscription_price": 200.0,
            "subscription_language": self.language.pk,  # Use pk for serializers
            "subscription_mode": self.mode.pk,          # Use pk for serializers
            "duration_in_months": 6,
        }
        serializer = SubscriptionPlanSerializer(data=data)
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        new_plan = serializer.save()
        self.assertIsNotNone(new_plan, "Failed to create SubscriptionPlan.")
        self.assertEqual(new_plan.version, "v1")

    def test_generate_version_different_price(self):
        data = {
            "_id": str(uuid.uuid4()),
            "version": "v1",
            "start_date": "2024-01-01",
            "subscription_price": 250.0,  # Different price
            "subscription_language": self.language.pk,  # Use pk for serializers
            "subscription_mode": self.mode.pk,          # Use pk for serializers
            "duration_in_months": 6,
        }
        serializer = SubscriptionPlanSerializer(data=data)
        self.assertTrue(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        new_plan = serializer.save()
        self.assertIsNotNone(new_plan, "Failed to create SubscriptionPlan.")
        self.assertEqual(new_plan.version, "v2")

    def test_invalid_subscription_price(self):
        invalid_data = self.valid_data.copy()
        invalid_data["subscription_price"] = -50.0  # Invalid price
        serializer = SubscriptionPlanSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        self.assertIn("subscription_price", serializer.errors)

    def test_invalid_date_format(self):
        invalid_data = self.valid_data.copy()
        invalid_data["start_date"] = "invalid-date"  # Incorrect date format
        serializer = SubscriptionPlanSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        self.assertIn("start_date", serializer.errors)

    def test_edge_case_duration(self):
        edge_case_data = self.valid_data.copy()
        edge_case_data["duration_in_months"] = 0  # Edge case: zero months
        serializer = SubscriptionPlanSerializer(data=edge_case_data)
        self.assertFalse(serializer.is_valid(), msg=f"Serializer errors: {serializer.errors}")
        self.assertIn("duration_in_months", serializer.errors)
