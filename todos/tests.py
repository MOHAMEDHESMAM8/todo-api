from django.test import TestCase
from .models import Todo


# Create your tests here.
class TODOModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="test title",
            body="body for the test"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "test title")
        self.assertEqual(str(self.todo), "test title")
        self.assertEqual(self.todo.body, "body for the test")
