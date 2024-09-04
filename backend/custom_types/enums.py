from enum import Enum


class Subject(Enum):
    """Define our currently available subjects
    """
    MATHEMATICS = 'Mathematics'
    PHYSICS = 'Physics'
    SCIENCES = 'Sciences'
    ENGLISH = 'English'


class SensoryPreferences(Enum):
    LOW_CONTRAST = 'Low contrast'
    HIGH_CONTRAST = 'High contrast'
    NO_SOUND_EFFECTS = 'No sound effects'
    BACKGROUND_MUSIC = 'Background music'


class CommunicationPreferences(Enum):
    VERBAL = 'Verbal'
    NON_VERBAL = 'Non-verbal'


class AttentionSpan(Enum):
    SHORT = 'Short'
    MODERATE = 'Moderate'
    LONG = 'Long'


class ReadingWritingSkills(Enum):
    EMERGING = 'Emerging'
    BASIC = 'Basic'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'


class MathSkills(Enum):
    EMERGING = 'Emerging'
    BASIC = 'Basic'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'


class TechComfortLevel(Enum):
    VERY_COMFORTABLE = 'Very comfortable'
    COMFORTABLE = 'Comfortable'
    NEEDS_ASSISTANCE = 'Needs assistance'
    UNCOMFORTABLE = 'Uncomfortable'


class ChildInterests(Enum):
    ANIMALS = 'Animals'
    SPACE_ASTRONOMY = 'Space & Astronomy'
    VEHICLES = 'Vehicles'
    NATURE_ENVIRONMENT = 'Nature & Environment'
    SUPERHEROES = 'Superheroes'
    SPORTS = 'Sports'
    FANTASY_FAIRY_TALES = 'Fantasy & Fairy tales'
