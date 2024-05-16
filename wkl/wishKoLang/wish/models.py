from django.db import models

# Create your models here.
class User(models.Model):
    # id auto generated
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture_link = models.TextField() # serialized image string
    email = models.CharField(max_length=255)
    birthday = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return str(self.id) + " | " + self.first_name + " " + self.last_name

class Wishlist(models.Model):
    # id auto generated
    title = models.CharField(max_length=255)
    owner = models.ForeignKey("User", on_delete=models.CASCADE, related_name="wishlist")

    def __str__(self):
        return str(self.id) + " | " + self.title + " by " + self.owner.first_name

class Item(models.Model):
    # id auto generated
    item_name = models.CharField(max_length=255)
    item_picture_link = models.TextField(blank=True) # serialized image string
    item_description = models.TextField(blank=True)
    wishlist = models.ForeignKey("Wishlist", on_delete=models.DO_NOTHING, related_name="item_in_wishlist")

    def __str__(self):
        return str(self.id) + " | " + self.item_name + " by " + self.wishlist.title

class Group(models.Model):
    # id auto generated
    group_name = models.CharField(max_length=255)
    profile_picture_link = models.TextField() # serialized image string
    def __str__(self):
        return str(self.id) + " | " + self.group_name

class Pair(models.Model):
    # id auto generated
    first_person = models.ForeignKey("User", on_delete=models.DO_NOTHING, related_name="first_person_pairs")
    second_person = models.ForeignKey("User", on_delete=models.DO_NOTHING, related_name="second_person_pairs")
    group = models.ForeignKey("Group", on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.id) + " | " + str(self.first_person.first_name) + " gifts " + str(self.second_person.first_name)

class Membership(models.Model):
    # id auto generated (not needed but comes by default)
    member = models.ForeignKey("User", on_delete=models.CASCADE)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " | " + self.member.first_name + " is a member of " + self.group.group_name

# Create your models here.




# class User(models.Model):
#     # id auto generated
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     profile_picture_link = models.TextField() # serialized image string
#     email = models.CharField(max_length=255)
#     birthday = models.DateField()

#     def __str__(self):
#         return str(self.id) + " | " + self.first_name + " " + self.last_name

# class Wishlist(models.Model):
#     # id auto generated
#     title = models.CharField(max_length=255)
#     owner = models.ForeignKey("User", on_delete=models.CASCADE, related_name="wishlist")

#     def __str__(self):
#         return str(self.id) + " | " + self.title + " by " + self.owner.first_name

# class Item(models.Model):
#     # id auto generated
#     item_name = models.CharField(max_length=255)
#     item_picture_link = models.TextField(blank=True) # serialized image string
#     item_description = models.TextField(blank=True)
#     wishlist = models.ForeignKey("Wishlist", on_delete=models.DO_NOTHING, related_name="item_in_wishlist")

#     def __str__(self):
#         return str(self.id) + " | " + self.item_name + " by " + self.wishlist.title

# class Group(models.Model):
#     # id auto generated
#     group_name = models.CharField(max_length=255)
#     profile_picture_link = models.TextField() # serialized image string
#     def __str__(self):
#         return str(self.id) + " | " + self.group_name

# class Pair(models.Model):
#     # id auto generated
#     first_person = models.ForeignKey("User", on_delete=models.DO_NOTHING, related_name="first_person_pairs")
#     second_person = models.ForeignKey("User", on_delete=models.DO_NOTHING, related_name="second_person_pairs")
#     group = models.ForeignKey("Group", on_delete=models.DO_NOTHING)
#     def __str__(self):
#         return str(self.id) + " | " + str(self.first_person.first_name) + " gifts " + str(self.second_person.first_name)

# class Membership(models.Model):
#     # id auto generated (not needed but comes by default)
#     member = models.ForeignKey("User", on_delete=models.CASCADE)
#     group = models.ForeignKey("Group", on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.id) + " | " + self.member.first_name + " is a member of " + self.group.group_name
    

# additional
class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    img_url = models.CharField(max_length = 150)

    def __str__(self):
        return str(self.id) + " | " + self.name

class Organization_Member(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    img_url = models.CharField(max_length = 150)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="categorizing", null=True, blank=True)

    def __str__(self):
        return str(self.id) + " | " + self.name
