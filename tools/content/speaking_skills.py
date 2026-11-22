# Speaking Skills is the IEP version of Prepared Speaking with the same theme and rubric,
# so it uses the same flashcard deck plus its eligibility rules.
import importlib.util, os

_spec = importlib.util.spec_from_file_location("_prepared_speaking", os.path.join(os.path.dirname(__file__), "prepared_speaking.py"))
_m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m)

MIN_FLASHCARDS = _m.MIN_FLASHCARDS
FLASHCARDS = [s for s in _m.FLASHCARDS if s[0] != "Event Rules"] + [
    ("Event Rules", "Know them in advance.", [
        ("Speech length", "5 minutes max (new for 2026-27)."),
        ("Eligibility", "For members classified under IDEA with an IEP; Section 504 isn't eligible."),
        ("Accommodation form", "Submit it by your state deadline and digitally by May 15; missing it costs 35 points."),
        ("No props or visual aids", "Only notecards are allowed."),
        ("Same rubric as Prepared Speaking", "Content, organization, and delivery are scored."),
        ("Dress", "Business attire or the HOSA uniform."),
        ("No microphones", "Practice projecting your voice."),
    ]),
]
