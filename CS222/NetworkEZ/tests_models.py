from django.test import TestCase

from app.models import Student

class TestModel(TestCase):

    def setUp(self):
        Student.objects.create(email = "jalen.xing@gmail.com", major = "Computer Science" , hobbies ="tennis", classes = "CS357", social_media = "jalen_xing")
        Student.objects.create(email = "bob@gmail.com", major = "Statistics" , hobbies ="table tennis", classes = "CS222", social_media = "bob_joe")

    def testDatabase(self):
        getJalen = Student.objects.get(email = "jalen.xing@gmail.com")
        getBob = Student.objects.get(email = "bob@gmail.com")
        self.assertEqual(str(getJalen), "jalen.xing@gmail.com Computer Science tennis CS357 jalen_xing")
        self.assertEqual(str(getBob), "bob@gmail.com Statistics table tennis CS222 bob_joe")


    # def setUp(self):
    #     Student.objects.create(email = "jalen.xing@gmail.com", major = "Computer Science" , hobbies ="tennis", classes = "CS357", social_media = "jalen_xing")

    # def getEmail(self):
    #     getEmail = Student.objects.get(email = "jalen.xing@gmail.com")
    #     self.assertEqual(str(getEmail), "jalen.xing@gmail.com Computer Science tennis CS357 jalen_xing")