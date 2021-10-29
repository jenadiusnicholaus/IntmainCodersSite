from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import datetime
from django.utils import timezone

from authentication.models import UserProfile
from intmaincoders import settings


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(max_length=200, null=True),

    class Mata:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Courses(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_instructor = models.ForeignKey('CourseInstructor', on_delete=models.CASCADE,
                                          related_name='course_instructor', null=True)
    image = models.FileField(upload_to='course_files', null=True)
    likes = models.ForeignKey('Likes', on_delete=models.CASCADE, null=True, related_name='couse_likes')
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=0.00, )
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title


class CourseInstructor(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    profession = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    social_link1 = models.URLField()
    social_link2 = models.URLField()
    social_link3 = models.URLField()
    social_link4 = models.URLField()

    class Meta:
        verbose_name_plural = 'Course Instructor'

    def __str__(self):
        return f'{self.user.user.firstname}  .  {self.user.user.middlename[0]} . {self.user.user.lastname}'

    def getInstructorProfilePicture(self):
        return str(self.user.image.url)

    def getFullname(self):
        return f'{self.user.user.firstname}  .  {self.user.user.middlename[0]} . {self.user.user.lastname}'


class SchedulingDay(models.Model):
    day_number = models.CharField(max_length=200, null=True)
    working_date = models.DateTimeField(default=timezone.now, null=True)
    scheduling_class = models.ManyToManyField(
        'SchedulingClass',
        related_name='list_of_class_per_day'
    )

    class Meta:
        verbose_name_plural = 'Scheduling Days'

    def __str__(self):
        return f' Day {str(self.day_number)} - {self.working_date}'


class SchedulingClass(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    starting_date = models.DateField(default=timezone.now)
    starting_time = models.TimeField(default=timezone.now)
    ending_date = models.DateField(default=timezone.now)
    ending_time = models.TimeField(default=timezone.now)
    class_capacity = models.IntegerField(default=30)

    class Meta:
        verbose_name_plural = 'Scheduling class'

    def __str__(self):
        return f' Class for {str(self.course)}'

    def getUserId(self):

        for i in self.user.all():
            return i.id

    def getTotalBooking(self):
        totalBookings = 0
        for b in self.user.all():
            totalBookings += 1
        return totalBookings


class Likes(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name_plural = 'course likes'

    def __str__(self):

        for u in self.user.all():
            return 'course likes '

    def getTotalLikes(self):
        likes = 0
        for like in self.user.all():
            likes += 1
        return str(likes)


class Events(models.Model):
    image = models.FileField(upload_to='event_files', null=True)
    title = models.CharField(max_length=200, null=True)
    staring_date = models.DateField(default=timezone.now)
    starting_time = models.TimeField(default=timezone.now)
    ending_date = models.DateField(default=timezone.now)
    ending_time = models.TimeField(default=timezone.now)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title
