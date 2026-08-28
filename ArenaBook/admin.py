from django.contrib import admin
from .models import *

@admin.register(User)
class ShowUser(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "password", "profile_image", "UserImage", "date_joined"]
    search_fields = ["first_name", "last_name", "email"]

@admin.register(Country)
class ShowCountry(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(State)
class ShowState(admin.ModelAdmin):
    list_display = ["country", "name"]
    search_fields = ["country", "name"]

@admin.register(City)
class ShowCity(admin.ModelAdmin):
    list_display = ["state", "name"]
    search_fields = ["state", "name"]

@admin.register(User_Profile)
class ShowUser_Profile(admin.ModelAdmin):
    list_display = ["user", "address", "phone_number", "city", "state", "country"]

@admin.register(Sport_Category)
class ShowSport_Category(admin.ModelAdmin):
    list_display = ["name", "description", "sport_image"]
    search_fields = ["name"]

@admin.register(Turf)
class ShowTurf(admin.ModelAdmin):
    list_display = ["name", "description", "turf_images", "category", "address",
                    "city", "state", "country", "price_per_hour", "open_time", "close_time", "created_at"]
    search_fields = ["name", "description", "category", "state", "country"]

@admin.register(Turf_Image)
class ShowTurf_Images(admin.ModelAdmin):
    list_display = ["turf", "image"]
    search_fields = ["turf"]

@admin.register(Booking)
class ShowBooking(admin.ModelAdmin):
    list_display = ["user", "turf_name", "booking_date", "start_time", "end_time",
                    "total_amount", "status", "created_at"]
    list_filter = ["status", "created_at"]

@admin.register(Payment)
class ShowPayment(admin.ModelAdmin):
    list_display = ["booking", "name", "payment_date", "payment_method", "status"]
    search_fields = ["name", "booking", "payment_method", "status"]

@admin.register(Review)
class ShowReview(admin.ModelAdmin):
    list_display = ["user", "turf_name", "rating", "comment", "created_at"]
    search_fields = ["turf_name"]

@admin.register(Contact_Us)
class ShowContact_Us(admin.ModelAdmin):
    list_display = ["name", "email_address", "phone", "message", "created_at"]



