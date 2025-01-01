from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework import serializers
from .models import MagazineSubscriber, Subscription, SubscriptionPlan, SubscriberCategory, SubscriberType, SubscriptionLanguage, SubscriptionMode, PaymentMode, AdminUser

class SubscriberCategorySerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)
    class Meta:
        model = SubscriberCategory
        fields = ('_id', 'name')

class SubscriberTypeSerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)
    class Meta:
        model = SubscriberType
        fields = ('_id', 'name')

class SubscriptionLanguageSerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)
    class Meta:
        model = SubscriptionLanguage
        fields = ('_id', 'name')

    def validate(self, data):
        id = data.get('_id')
        # Check for duplicate ID
        if SubscriptionLanguage.objects.filter(_id=id).count() > 0:
            raise serializers.ValidationError({"_id": f"A language with this ID already exists : {id}"})
        return data

class SubscriptionModeSerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)
    class Meta:
        model = SubscriptionMode
        fields = ('_id', 'name')

class SubscriptionPlanSerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)  # Explicitly include _id
    subscription_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)  # Ensure price is required and has valid decimal format
    duration_in_months = serializers.IntegerField(required=True, min_value=1)  # Ensure duration is required and greater than 0
    
    subscription_language = serializers.PrimaryKeyRelatedField(queryset=SubscriptionLanguage.objects.all())
    subscription_mode = serializers.PrimaryKeyRelatedField(queryset=SubscriptionMode.objects.all())

    class Meta:
        model = SubscriptionPlan
        fields = ('_id', 'version', 'name', 'start_date', 'subscription_price', 'subscription_language', 'subscription_mode', 'duration_in_months')

    def validate(self, data):
        # Check for valid duration_in_months
        duration = data.get('duration_in_months', None)
        if duration is None:
            if self.partial:  # Allow None for partial updates
                return data
            raise serializers.ValidationError("Duration in months is required.")
        
        if duration <= 0:
            raise serializers.ValidationError({"duration_in_months": f"Duration in months must be greater than zero. {data.get('duration_in_months', None)}"})
        
        # Check for valid subscription_price
        price = data.get('subscription_price', None)
        if price is None:
            if self.partial:  # Allow None for partial updates
                return data
            raise serializers.ValidationError("Price is required.")
        
        if price <= 0:
            raise serializers.ValidationError({"subscription_price": "Subscription price must be a positive number."})
        
        # Check for duplicate ID
        if SubscriptionPlan.objects.filter(_id=data.get('_id')).count() > 0:
            raise serializers.ValidationError({"_id": "A plan with this ID already exists."})
        
        return data


class PaymentModeSerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)
    class Meta:
        model = PaymentMode
        fields = ['_id', 'name']

    def validate(self, data):
        if 'name' not in data or not data['name']:
            raise serializers.ValidationError({'name': 'This field is required.'})
        return data
        
class SubscriptionSerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)
    subscription_plan = serializers.PrimaryKeyRelatedField(queryset=SubscriptionPlan.objects.all())
    payment_mode = serializers.PrimaryKeyRelatedField(queryset=PaymentMode.objects.all())

    class Meta:
        model = Subscription
        fields = '__all__'

    def validate(self, data):
        if 'subscription_plan' in data and isinstance(data['subscription_plan'], str):
            try:
                data['subscription_plan'] = SubscriptionPlan.objects.get(pk=data['subscription_plan'])
            except SubscriptionPlan.DoesNotExist:
                raise ValidationError({'subscription_plan': 'SubscriptionPlan matching query does not exist.'})
        if 'payment_mode' in data and isinstance(data['payment_mode'], str):
            try:
                data['payment_mode'] = PaymentMode.objects.get(pk=data['payment_mode'])
            except PaymentMode.DoesNotExist:
                raise ValidationError({'payment_mode': 'PaymentMode matching query does not exist.'})
        return data

class MagazineSubscriberSerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=SubscriberCategory.objects.all())
    stype = serializers.PrimaryKeyRelatedField(queryset=SubscriberType.objects.all())
    subscriptions = serializers.SerializerMethodField()
    
    def get_subscriptions(self, obj):
        subscriptions = Subscription.objects.filter(subscriber=obj)
        return SubscriptionSerializer(subscriptions, many=True).data

    class Meta:
        model = MagazineSubscriber
        fields = [
            '_id', 'name', 'registration_number', 'address', 'city_town',
            'state', 'pincode', 'phone', 'email', 'category', 'stype',
            'notes', 'hasActiveSubscriptions', 'isDeleted', 'subscriptions'
        ]

class AdminUserSerializer(DocumentSerializer):
    _id = serializers.CharField(required=True)
    class Meta:
        model = AdminUser
        fields = [
            '_id', 'username', 'email', 'first_name', 'last_name', 'aadhaar', 'mobile',
            'created_at', 'last_login', 'active'
        ]