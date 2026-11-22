# Interviewing Skills is the IEP version of Job Seeking Skills with the same documents and interview,
# so it uses the same flashcard deck.
import importlib.util, os

_spec = importlib.util.spec_from_file_location("_job_seeking", os.path.join(os.path.dirname(__file__), "job_seeking_skills.py"))
_m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m)

MIN_FLASHCARDS = _m.MIN_FLASHCARDS
FLASHCARDS = [s for s in _m.FLASHCARDS if s[0] != "Round One Submission"] + [
    ("Round One Submission", "Formatting rules and the accommodation form.", [
        ("One PDF", "Personal statement and resume uploaded as one PDF by May 15."),
        ("Accommodation form", "Submit the IEP Verification & Accommodation Form by May 15 or lose 35 points."),
        ("Eligibility", "For members classified under IDEA with an IEP; Section 504 isn't eligible."),
    ]),
]
