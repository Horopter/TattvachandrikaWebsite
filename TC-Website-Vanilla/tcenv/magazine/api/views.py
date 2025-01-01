# Third-party libraries
import hashlib

# Rest Framework
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

# FPDF
from fpdf import FPDF
from django.http import HttpResponse

# Local app models
from .models import (
    AdminUser,
    MagazineSubscriber,
    PaymentMode,
    SubscriberCategory,
    SubscriberType,
    Subscription,
    SubscriptionLanguage,
    SubscriptionMode,
    SubscriptionPlan,
    UserToken,
)

# Local app serializers
from .serializers import (
    AdminUserSerializer,
    MagazineSubscriberSerializer,
    PaymentModeSerializer,
    SubscriberCategorySerializer,
    SubscriberTypeSerializer,
    SubscriptionLanguageSerializer,
    SubscriptionModeSerializer,
    SubscriptionPlanSerializer,
    SubscriptionSerializer,
)

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.data.get('token')  # Get the token from the request body
        print("Got called")
        if not token:
            return None  # No token provided, continue to other authentication methods

        # Validate the token
        user_token = UserToken.objects(token=token).first()
        if not user_token:
            raise AuthenticationFailed('Invalid token.')

        return (user_token.user, token)  # Return user and token if valid

class SubscriberCategoryViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriberCategorySerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return SubscriberCategory.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriberTypeViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriberTypeSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return SubscriberType.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriptionLanguageViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriptionLanguageSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return SubscriptionLanguage.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriptionModeViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriptionModeSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return SubscriptionMode.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriptionPlanSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return SubscriptionPlan.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class PaymentModeViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = PaymentModeSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return PaymentMode.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


class MagazineSubscriberViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = MagazineSubscriberSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return MagazineSubscriber.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    @action(detail=True, methods=['post'])
    def activate(self, request, _id=None):
        try:
            subscriber = self.get_object()
            subscriber.isDeleted = False
            subscriber.save()
            return Response({'status': 'subscriber activated'}, status=status.HTTP_200_OK)
        except MagazineSubscriber.DoesNotExist:
            raise NotFound('Subscriber not found')

    def perform_destroy(self, instance):
        instance.isDeleted = True
        instance.save()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def report(self, request):
        # Get the character limit from the request or use a default value
        char_limit = int(request.query_params.get('char_limit', 42))

        # Helper function to split an address into multiple lines based on character limit.
        def split_address(address, char_limit):
            lines = []
            while len(address) > char_limit:
                split_at = address[:char_limit].rfind(' ')
                if split_at == -1:  # If no space found, split at the char limit
                    split_at = char_limit
                lines.append(address[:split_at].strip())
                address = address[split_at:].strip()
            lines.append(address)
            return lines

        # Fetch and process all subscribers
        subscribers = self.get_queryset()
        report = []
        for subscriber in subscribers:
            address_lines = split_address(subscriber.address, char_limit)
            report.append({
                "Name": subscriber.name,
                "Address line 1": address_lines[0] if len(address_lines) > 0 else "",
                "Address line 2": address_lines[1] if len(address_lines) > 1 else "",
                "City": subscriber.city_town,
                "District": subscriber.district,
                "State": subscriber.state,
                "Pincode": subscriber.pincode,
                "Phone Number": subscriber.phone,
            })

        return Response(report, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def generate_report_dummy(self, request):
        """
        Generates a PDF report with 2 columns, 5 rows, clear boundaries, and adjusted layout using dummy data.
        """
        try:
            # Dummy subscriber data
            dummy_subscriber = {
                "Name": "John Doe " + "X" * 28,
                "Address line 1": "123 Elm Street " + "Y" * 25,
                "Address line 2": "Apartment 4B " + "Z" * 28,
                "City": "Springfield " + "A" * 14,
                "District": "Sangamon " + "B" * 17,
                "State": "Illinois " + "C" * 18,
                "Pincode": "62704 " + "D" * 20,
                "Phone Number": "123-456-7890 " + "E" * 25,
            }

            report_data = [dummy_subscriber] * 12  # Repeat the same subscriber 18 times

            char_limit = int(request.query_params.get('char_limit', 42))

            # Initialize FPDF
            pdf = FPDF()
            pdf.add_page()

            # Set base font size and other layout parameters
            base_font_size = 11
            pdf.set_font("Arial", size=base_font_size)

            # Layout parameters
            page_width = 210  # A4 page width in mm
            page_height = 297  # A4 page height in mm
            margin = 10  # Page margin
            usable_width = page_width - 2 * margin
            usable_height = page_height - 2 * margin

            # Calculate box and column dimensions
            column_width = usable_width / 2  # Two columns
            box_height = usable_height / 5  # Five rows per column

            # Draw table boundaries and add values
            for index, subscriber in enumerate(report_data):
                # Determine column and row positions for column-wise filling
                column = index % 2  # 0 = first column, 1 = second column
                row = (index // 2) % 5  # 5 rows per column

                # Start a new page after 10 entries (5 rows per column * 2 columns)
                if index > 0 and index % 10 == 0:
                    pdf.add_page()

                # Calculate position
                x_position = margin + (column * column_width)
                y_position = margin + (row * box_height)

                # Draw a rectangle for the boundary
                pdf.rect(x_position, y_position, column_width, box_height)

                # Handle None/null values
                def sanitize(value):
                    return str(value) if value not in [None, 'null', 'None', ""] else None

                # Write subscriber details inside the rectangle
                values = [
                    sanitize(subscriber.get("Name")),
                    sanitize(subscriber.get("Address line 1")),
                    sanitize(subscriber.get("Address line 2")),
                    sanitize(f"{subscriber.get('City', '')}, {subscriber.get('District', '')}".strip(", ")),
                    sanitize(f"{subscriber.get('State', '')}, {subscriber.get('Pincode', '')}".strip(", ")),
                    sanitize(subscriber.get("Phone Number")),
                ]
                current_y = y_position + 2  # Padding inside the rectangle
                pdf.set_xy(x_position + 2, current_y)  # Start writing with padding

                # Write the values, skipping empty ones
                for value in values:
                    if value:  # Skip empty strings or None
                        truncated_value = value[:char_limit-3] + "..." if len(value) > char_limit else value
                        pdf.cell(column_width - 4, 7, truncated_value, ln=True)  # Reduced line height
                        pdf.set_xy(x_position + 2, pdf.get_y())

            # Output PDF to response
            pdf_output = pdf.output(dest='S').encode('latin1')
            return HttpResponse(
                pdf_output,
                content_type="application/pdf",
                headers={"Content-Disposition": 'attachment; filename="subscriber_report.pdf"'},
            )

        except Exception as e:
            # Handle errors gracefully
            return Response({"error": str(e)}, status=500)

    @action(detail=False, methods=['get'])
    def generate_pdf_report(self, request):
        """
        Generates a PDF report with subscriber data fetched from the database, skipping empty strings.
        """
        try:
            # Fetch data from the report endpoint
            char_limit = int(request.query_params.get('char_limit', 42))
            report_data = self.report(request).data  # Use the existing `report` function to fetch data

            # Initialize FPDF
            pdf = FPDF()
            pdf.add_page()

            # Set base font size and other layout parameters
            base_font_size = 11
            pdf.set_font("Arial", size=base_font_size)

            # Layout parameters
            page_width = 210  # A4 page width in mm
            page_height = 297  # A4 page height in mm
            margin = 10  # Page margin
            usable_width = page_width - 2 * margin
            usable_height = page_height - 2 * margin

            # Calculate box and column dimensions
            column_width = usable_width / 2  # Two columns
            box_height = usable_height / 5  # Five rows per column

            # Draw table boundaries and add values
            for index, subscriber in enumerate(report_data):
                # Determine column and row positions for column-wise filling
                column = index % 2  # 0 = first column, 1 = second column
                row = (index // 2) % 5  # 5 rows per column

                # Start a new page after 10 entries (5 rows per column * 2 columns)
                if index > 0 and index % 10 == 0:
                    pdf.add_page()

                # Calculate position
                x_position = margin + (column * column_width)
                y_position = margin + (row * box_height)

                # Draw a rectangle for the boundary
                pdf.rect(x_position, y_position, column_width, box_height)

                # Handle None/null values
                def sanitize(value):
                    return str(value) if value not in [None, 'null', 'None', ""] else None

                # Write subscriber details inside the rectangle
                values = [
                    sanitize(subscriber.get("Name")),
                    sanitize(subscriber.get("Address line 1")),
                    sanitize(subscriber.get("Address line 2")),
                    sanitize(f"{subscriber.get('City', '')}, {subscriber.get('District', '')}".strip(", ")),
                    sanitize(f"{subscriber.get('State', '')}, {subscriber.get('Pincode', '')}".strip(", ")),
                    sanitize(subscriber.get("Phone Number")),
                ]
                current_y = y_position + 2  # Padding inside the rectangle
                pdf.set_xy(x_position + 2, current_y)  # Start writing with padding

                # Write the values, skipping empty ones
                for value in values:
                    if value:  # Skip empty strings or None
                        truncated_value = value[:char_limit-3] + "..." if len(value) > char_limit else value
                        pdf.cell(column_width - 4, 7, truncated_value, ln=True)  # Reduced line height
                        pdf.set_xy(x_position + 2, pdf.get_y())

            # Output PDF to response
            pdf_output = pdf.output(dest='S').encode('latin1')
            return HttpResponse(
                pdf_output,
                content_type="application/pdf",
                headers={"Content-Disposition": 'attachment; filename="subscriber_report.pdf"'},
            )

        except Exception as e:
            # Handle errors gracefully
            return Response({"error": str(e)}, status=500)


class SubscriptionViewSet(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = SubscriptionSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Subscription.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.get(**filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
        
    @action(detail=False, methods=['get'], url_path='by_subscriber/(?P<subscriber_id>[^/.]+)')
    def get_by_subscriber(self, request, subscriber_id=None):
        try:
            subscriptions = Subscription.objects.filter(subscriber=subscriber_id)
            serializer = self.get_serializer(subscriptions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subscription.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


class AdminUserViewSet(viewsets.ModelViewSet):
    serializer_class = AdminUserSerializer
    lookup_field = '_id'

    def get_queryset(self):
        """Return all admin users."""
        return AdminUser.objects.all()

    @action(detail=False, methods=['post'], url_path='signup')
    def signup(self, request):
        """Create a new admin user account."""
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        aadhaar = request.data.get('aadhaar')
        mobile = request.data.get('mobile')

        # Check for existing user
        if AdminUser.objects(username=username).first() or AdminUser.objects(email=email).first():
            return Response({"error": "Username or email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Hash the password before saving
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Create new admin user
        new_user = AdminUser(
            username=username,
            password=hashed_password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            aadhaar=aadhaar,
            mobile=mobile  
        )
        new_user.save()  # Save to MongoDB

        return Response(AdminUserSerializer(new_user).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='login', permission_classes=[AllowAny])
    def login(self, request):
        """Log in an admin user."""
        username = request.data.get('username')
        password = request.data.get('password')

        # Hash the password to compare
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        admin_user = AdminUser.objects(username=username, password=hashed_password).first()

        if admin_user:
            # Create a new token for the user
            token = UserToken.create_token(admin_user)  # Use the custom method to create a token

            # Update last login time
            admin_user.update_last_login()

            return Response({"token": token, "message": "Login successful!"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='logout', permission_classes=[AllowAny])
    def logout(self, request):
        """Log out the admin user."""
        token = request.data.get('token')  # Get the token from the request body

        if token:
            # Attempt to delete the token from the database
            token_entry = UserToken.objects(token=token).first()
            if token_entry:
                token_entry.delete()  # Token exists, so delete it
                return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid token."}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"error": "Token not provided."}, status=status.HTTP_400_BAD_REQUEST)
