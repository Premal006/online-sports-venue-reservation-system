from django.db import models
from django.utils.safestring import mark_safe


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile', null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def UserImage(self):
        if self.profile_image:
            return mark_safe('<img src="{}" width="100px">'.format(self.profile_image.url))
        return "No Image"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class User_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Sport_Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sport_image = models.ImageField(upload_to='sport_categories', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sport_Category"
        verbose_name_plural = "Sport_Categories"


class Turf(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    turf_images = models.ImageField(upload_to='turfs', null=True, blank=True)
    category = models.ForeignKey(Sport_Category, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    price_per_hour = models.IntegerField()
    open_time = models.CharField(max_length=100)
    close_time = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Turf_Image(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='turf_images', null=True, blank=True)

    def __str__(self):
        return f"{self.turf.name} Image"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf_name = models.ForeignKey(Turf, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    status = models.CharField(max_length= 100, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])
    created_at = models.DateField(auto_now_add=True)



class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=100, choices=[('credit_card', 'Credit_Card'), ('debit_card', 'Debit_Card'), ('paypal', 'Paypal'), ('other', 'Other')])
    status = models.CharField(max_length=100, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf_name = models.ForeignKey(Turf, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class Contact_Us(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


