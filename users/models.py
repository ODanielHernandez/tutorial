from django.db import models


class StudentStatusType(models.IntegerChoices):
    PENDING = (0, "pending")
    ACTIVE = (1, "active",)
    REJECTED = (2, "rejected")
    APPLIED = (3, "applied")
    CANCELLED = (4, "cancelled")
    DROPED = (5, "dropped")
    EXTERNAL = (6, "external")



class User(models.Model):
    class GenderType(models.IntegerChoices):
        MALE = (1, "male")
        FEMALE = (2, "female")
        OTHER = (3, "other")

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(verbose_name="Birth date", null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    campus = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GenderType.choices, default=GenderType.MALE)
    photo = models.FileField(upload_to="users/images/", null=True)

    def __str__(self):
        return f"{self.name} {self.email}"


class Student(models.Model):

    class SemesterType(models.IntegerChoices):
        FIRST = (1, "First Semester")
        SECOND = (2, "Second Semester")
        THIRD = (3, "Third Semester")
        FOURTH = (4, "Fourth Semester")
        FIFTH = (5, "Fifth Semester")
        SIXTH = (6, "Sixth Semester")
        SEVENTH = (7, "Seventh Semester")
        EIGHTH = (8, "Eighth Semester")
        EXTRA = (9, "extra")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    semester = models.IntegerField(
        choices=SemesterType.choices,
        default=SemesterType.FIRST,
        verbose_name="semester",
    )
    grades = models.FloatField(default=0.0)
    admission_date = models.DateField(auto_now=True, verbose_name="Admission date")
    graduation_date = models.DateField(
        null=True, blank=True, verbose_name="Graduation date"
    )
    status = models.IntegerField(
        choices=StudentStatusType.choices,
        default=StudentStatusType.PENDING,
        verbose_name="status",
    )

    def __str__(self):
        return self.user.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
