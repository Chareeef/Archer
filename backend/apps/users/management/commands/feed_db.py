import random
from django.core.management.base import BaseCommand
from apps.users.models import Student, Parent, Educator
from apps.curriculum.models import Lesson
from custom_types import enums


class Command(BaseCommand):
    help = 'Feed the database with mock data for students, parents, educators, and lessons.'

    def handle(self, *args, **options):
        self.stdout.write("Deleting old data...")
        self._clear_old_data()

        self.stdout.write("Creating new data...")
        self._create_parents()
        self._create_students()
        self._create_educators()
        self._create_lessons()

        self.stdout.write(self.style.SUCCESS('Database feeding completed successfully!'))

    def _clear_old_data(self):
        Student.objects.all().delete()
        Parent.objects.all().delete()
        Educator.objects.all().delete()
        Lesson.objects.all().delete()

    def _create_parents(self):
        self.parents = []
        for i in range(5):
            parent = Parent.objects.create_user(
                email=f'parent{i}@example.com',
                first_name=f'ParentFirstName{i}',
                last_name=f'ParentLastName{i}',
                number_of_children=random.randint(1, 3),
                password='parent123'
            )
            self.parents.append(parent)

    def _create_students(self):
        self.students = []
        for i in range(10):
            student = Student.objects.create_user(
                email=f'student{i}@example.com',
                first_name=f'StudentFirstName{i}',
                last_name=f'StudentLastName{i}',
                age=random.randint(7, 18),
                grade_level=random.randint(6, 12),
                parent_id=random.choice(self.parents),
                sensory_preference=random.choice(list(enums.SensoryPreferences)),
                communication_preference=random.choice(list(enums.CommunicationPreferences)),
                attention_span=random.choice(list(enums.AttentionSpan)),
                reading_writing_skills=random.choice(list(enums.ReadingWritingSkills)),
                math_skills=random.choice(list(enums.MathSkills)),
                technology_comfort=random.choice(list(enums.TechComfortLevel)),
                interests=random.choice(list(enums.ChildInterests)),
                password='student123'
            )
            self.students.append(student)

    def _create_educators(self):
        self.educators = []
        subjects = [enums.Subject.READING_WRITING, enums.Subject.MATHEMATICS, enums.Subject.SCIENCE]
        for subject in subjects:
            educator = Educator.objects.create_user(
                email=f'educator_joe_{subject.value}@example.com',
                first_name='Joe',
                last_name=f'{subject.value}',
                subject=subject,
                password='educator123'
            )
            self.educators.append(educator)

    def _create_lessons(self):
        lessons_data = {
            enums.Subject.MATHEMATICS: [
                {"title": "Basic Algebra", "text": "# Algebra\nThis is an introduction to algebra."},
                {"title": "Geometry Basics", "text": "# Geometry\nLet's explore the basics of geometry."},
                {"title": "Calculus Intro", "text": "# Calculus\nIntroduction to calculus and derivatives."},
            ],
            enums.Subject.SCIENCE: [
                {"title": "Science Principles", "text": "# Science\nAn introduction to classical mechanics."},
                {"title": "Biology Overview", "text": "# Biology\nBasics of cell structure and functions."},
                {"title": "Chemistry Essentials", "text": "# Chemistry\nUnderstanding the periodic table."},
            ],
            enums.Subject.READING_WRITING: [
                {"title": "Grammar Basics", "text": "# Grammar\nLet's dive into sentence structure."},
            {
                "title": "Understanding English Grammar",
                "text": (
                    "# Understanding English Grammar\n"
                    "## Lesson Overview\n"
                    "In this lesson, we will explore different aspects of English grammar, such as **sentence structure**, "
                    "the use of **nouns, verbs, and adjectives**, and how to form coherent paragraphs.\n"

                    "### What is a Sentence?\n"
                    "A sentence is a group of words that expresses a complete thought. It usually contains a subject (the person, place, or thing being talked about) "
                    "and a predicate (what is being said about the subject).\n"

                    "For example:\n"
                    "- The cat (subject) is sleeping (predicate).\n"
                    "- **Important:** Sentences should always begin with a capital letter and end with a punctuation mark, such as a period.\n"

                    "### Types of Sentences\n"
                    "There are four main types of sentences:\n"
                    "1. **Declarative:** States a fact or opinion. E.g., *She likes to read.*\n"
                    "2. **Interrogative:** Asks a question. E.g., *Do you like ice cream?*\n"
                    "3. **Imperative:** Gives a command. E.g., *Please close the door.*\n"
                    "4. **Exclamatory:** Expresses strong emotion. E.g., *Wow, that was amazing!*\n"

                    "### Using Nouns, Verbs, and Adjectives\n"
                    "1. **Nouns** are names of people, places, or things. E.g., *cat, city, book.*\n"
                    "2. **Verbs** show action or state of being. E.g., *run, jump, is.*\n"
                    "3. **Adjectives** describe nouns. E.g., *beautiful, quick, tall.*\n"

                    "### Paragraph Writing\n"
                    "A paragraph is a group of sentences that focus on one idea. A well-written paragraph includes:\n"
                    "- A **topic sentence** that introduces the main idea.\n"
                    "- **Supporting sentences** that provide details or examples.\n"
                    "- A **concluding sentence** that summarizes the paragraph.\n"

                    "### Summary\n"
                    "By understanding sentence structure and how to use nouns, verbs, and adjectives correctly, you can form better paragraphs and improve your writing skills.\n"

                    "---\n"
                    "## Homework Assignment\n"
                    "Write a paragraph using at least three different types of sentences (declarative, interrogative, and exclamatory). "
                    "Try to include **nouns**, **verbs**, and **adjectives** in your writing."
                )
            },
                {"title": "Creative Writing", "text": "# Writing\nTips for improving your creative writing."},
                {"title": "Reading Comprehension", "text": "# Reading\nStrategies to enhance understanding of texts."},
            ]
        }

        for educator in self.educators:
            subject_lessons = lessons_data[educator.subject]
            for lesson_data in subject_lessons:
                Lesson.objects.create(
                    subject=educator.subject,
                    educator_id=educator,
                    grade_level=random.randint(7, 12),
                    title=lesson_data['title'],
                    text=lesson_data['text'],
                    video_link="https://example.com/video"
                )

            for lesson_data in subject_lessons:
                Lesson.objects.create(
                    subject=educator.subject,
                    educator_id=educator,
                    grade_level=6,
                    title=lesson_data['title'],
                    text=lesson_data['text'],
                    video_link="https://example.com/video"
                )
