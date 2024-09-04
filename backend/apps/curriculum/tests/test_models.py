from django.test import TestCase
from apps.users.models import Educator
from custom_types.enums import Subject
from ..models import Lesson
from django.core.exceptions import ValidationError


class LessonModelTest(TestCase):
    """Test suite for the Lesson model."""

    def setUp(self):
        """Set up a test Educator instance."""
        self.educator = Educator.objects.create_user(
            email='educator@example.com',
            password='password123',
            first_name='Edu',
            last_name='Cator',
            subject='Mathematics'
        )

    def tearDown(self):
        """Clean up the database after each test."""
        Lesson.objects.all().delete()
        Educator.objects.all().delete()

    def test_create_lesson(self):
        """Test creating a Lesson instance with all fields."""
        lesson = Lesson.objects.create(
            subject=Subject.ENGLISH,
            educator_id=self.educator,
            grade_level=10,
            title="Introduction to English Literature",
            text="This is a lesson about English Literature.",
            video_link="http://example.com/video"
        )
        self.assertEqual(lesson.subject, Subject.ENGLISH)
        self.assertEqual(lesson.educator_id, self.educator)
        self.assertEqual(lesson.grade_level, 10)
        self.assertEqual(lesson.title, "Introduction to English Literature")
        self.assertEqual(
            lesson.text,
            "This is a lesson about English Literature.")
        self.assertEqual(lesson.video_link, "http://example.com/video")

    def test_create_lesson_without_video_link(self):
        """Test creating a Lesson instance without a video link."""
        lesson = Lesson.objects.create(
            subject=Subject.MATHEMATICS,
            educator_id=self.educator,
            grade_level=9,
            title="Introduction to Algebra",
            text="This is a lesson about Algebra."
        )
        self.assertEqual(lesson.subject, Subject.MATHEMATICS)
        self.assertEqual(lesson.educator_id, self.educator)
        self.assertEqual(lesson.grade_level, 9)
        self.assertEqual(lesson.title, "Introduction to Algebra")
        self.assertEqual(lesson.text, "This is a lesson about Algebra.")
        self.assertIsNone(lesson.video_link)

    def test_create_lesson_without_educator(self):
        """Test creating a Lesson instance without an educator."""
        lesson = Lesson.objects.create(
            subject=Subject.PHYSICS,
            grade_level=11,
            title="Introduction to Quantum Mechanics",
            text="This is a lesson about Quantum Mechanics.",
            video_link="http://example.com/video"
        )
        self.assertEqual(lesson.subject, Subject.PHYSICS)
        self.assertIsNone(lesson.educator_id)
        self.assertEqual(lesson.grade_level, 11)
        self.assertEqual(lesson.title, "Introduction to Quantum Mechanics")
        self.assertEqual(
            lesson.text,
            "This is a lesson about Quantum Mechanics.")
        self.assertEqual(lesson.video_link, "http://example.com/video")

    def test_invalid_subject(self):
        """Test that an invalid subject raises a ValidationError."""
        with self.assertRaises(ValidationError):
            lesson = Lesson(
                subject="History",  # Invalid subject
                educator_id=self.educator,
                grade_level=10,
                title="Introduction to History",
                text="This is a lesson about History.",
                video_link="http://example.com/video"
            )

    def test_valid_subjects(self):
        """Test creating Lesson instances with all valid subjects."""
        valid_subjects = [
            Subject.ENGLISH,
            Subject.MATHEMATICS,
            Subject.PHYSICS,
            Subject.SCIENCES]

        for subject in valid_subjects:
            lesson = Lesson.objects.create(
                subject=subject,
                educator_id=self.educator,
                grade_level=10,
                title=f"Introduction to {subject}",
                text=f"This is a lesson about {subject}.",
                video_link="http://example.com/video"
            )
            self.assertEqual(lesson.subject, subject)
