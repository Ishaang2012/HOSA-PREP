"""Build hosa-prep/data/events.js from the extracted 2026-27 HOSA guidelines.

Textbooks are hand-transcribed from each guideline's "Official References" section.
Only books/courses used to write the test questions are listed as textbooks; other
links (websites, webinars, skills-only references) go under `otherResources`.
"""
import json, re, sys

src, dest = sys.argv[1], sys.argv[2]
ex = json.load(open(src, encoding="utf-8"))

def B(title, author="", publisher="", note=""):
    return {k: v for k, v in dict(title=title, author=author, publisher=publisher, note=note).items() if v}

DHO = lambda note="": B("DHO: Health Science", "Simmers, Simmers-Nartker, Simmers-Kobelak & Morris", "Cengage Learning", note)
TABERS = B("Taber's Cyclopedic Medical Dictionary", "Venes (ed.)", "F.A. Davis")
STANHOPE = B("Introduction to Medical Terminology", "Stanhope & Turnbull", "Goodheart-Willcox")
RRONR_BRIEF = B("Robert's Rules of Order Newly Revised In Brief", "", "")

BOOKS = {
    "behavioral-health": [B("Discovering Psychology", "Cacioppo & Freberg", "Cengage Learning")],
    "biomedical-equipment-technician": [
        B("AAMI BMET 101", "AAMI Training", "", "Online course"),
        B("Medical Equipment Technician (MET) 100 Series", "College of Biomedical Equipment Training", "", "Online course")],
    "dental-terminology": [
        B("Dental Terminology", "Kindle & Dofka", "Cengage Learning"),
        B("Wheeler's Dental Anatomy, Physiology and Occlusion", "Nelson", "Elsevier")],
    "health-informatics": [
        B("Introduction to Healthcare Informatics", "Zhou & Clack", "AHIMA Press"),
        B("A Practical Approach to Analyzing Healthcare Data", "White", "AHIMA Press")],
    "healthcare-administration": [
        B("Shortell & Kaluzny's Health Care Management: Organization Design and Behavior", "Burns, Bradley & Weiner", "Cengage"),
        B("Introduction to Health Care Management", "Buchbinder", "Jones & Bartlett Learning")],
    "human-growth-development": [
        B("Journey Across the Lifespan: Human Development and Health Promotion", "Polan & Taylor", "F.A. Davis"),
        DHO(),
        B("Lifespan Development", "Kato", "Goodheart-Willcox")],
    "medical-law-ethics": [
        B("Medical Law, Ethics, & Bioethics for the Health Professions", "Tamparo", "F.A. Davis"),
        B("Healthcare Law and Ethics", "Fremgen", "Pearson"),
        B("Medical Law & Professional Ethics", "Ritter & Graham", "Goodheart-Willcox")],
    "medical-math": [
        DHO(),
        B("Dosage Calculations Made Easy", "Craig", "Wolters Kluwer"),
        B("Pharmacy Calculations: An Introduction for Pharmacy Technicians", "Rewald, Lorang & Schramm", "ASHP")],
    "medical-reading": [
        B("Crisis Averted: The Hidden Science of Fighting Outbreaks", "Caitlin Rivers"),
        B("Everything Is Tuberculosis: The History and Persistence of Our Deadliest Infection", "John Green"),
        B("Fragmented: A Doctor's Quest to Piece Together American Healthcare", "Ilana Yurkiewicz, MD"),
        B("The Next Patient: The Incredible World of Emergency Medicine", "J. Thomas Grant"),
        B("Grit: The Power of Passion and Perseverance", "Angela Duckworth")],
    "medical-spelling": [TABERS],
    "medical-terminology": [
        B("Medical Terminology for Health Professions", "Ehrlich", "Cengage Learning"),
        TABERS, STANHOPE,
        B("Dean Vaughn's Medical Terminology by Body Systems", "Dean Vaughn", "Peterson's Publishing", "Online course")],
    "nutrition": [
        B("Nutrition and Diet Therapy", "Roth", "Cengage Learning"),
        B("Nutrition and Wellness for Life", "West", "Goodheart-Willcox")],
    "pathophysiology": [
        B("iCEV Pathophysiology and Anatomy & Physiology Courses", "iCEV", "", "Online course"),
        B("Essentials of Human Diseases and Conditions", "Frazier", "Elsevier"),
        B("Human Diseases: A Systemic Approach", "Zelman et al.", "Pearson")],
    "pharmacology": [
        B("The Pharmacy Technician: A Comprehensive Approach", "Moini", "Cengage Learning"),
        B("Introductory Clinical Pharmacology", "Ford & Roach", "Wolters Kluwer"),
        B("Dean Vaughn's Pharmacology by Body System", "Dean Vaughn", "", "Online course")],
    "world-health-disparities": [B("Health Disparities in the US", "Barr", "Johns Hopkins University Press")],
    "biotechnology": [
        B("Biotechnology: A Laboratory Skills Course", "Brown", "Bio-Rad"),
        B("Biology: The Unity and Diversity of Life (AP)", "Starr & Taggart", "National Geographic Learning / Cengage")],
    "clinical-lab-science": [B("Basic Clinical Laboratory Techniques", "Estridge & Reynolds", "Cengage Learning")],
    "clinical-nursing": [
        B("Clinical Nursing Skills and Techniques", "Perry & Potter", "Elsevier / Mosby"),
        B("Textbook of Basic Nursing", "Rosdahl & Kowalski", "Wolters Kluwer")],
    "dental-science": [
        B("Dental Instruments: A Pocket Guide", "Boyd", "Saunders"),
        B("Modern Dental Assisting", "Robinson", "Elsevier")],
    "genetics": [B("Carolina Genetics: A Guidebook for the HOSA Genetics Written Test", "Carolina Biological", "")],
    "home-health-aide": [
        B("Homemaker Home Health Aide", "Balduzzi", "Cengage Learning"),
        B("Providing Home Care: A Textbook for Home Health Aides", "Leahy, Fuzy & Grafe", "Hartman Publishing")],
    "medical-assisting": [B("Medical Assisting: Administrative and Clinical Competencies", "Blesi, Wise & Kelley-Arney", "Cengage Learning")],
    "nursing-assisting": [
        B("Nursing Assisting: A Foundation in Caregiving", "Dugan", "Hartman Publishing"),
        B("The Nursing Assistant: Essentials of Holistic Care", "Roe", "Goodheart-Willcox")],
    "occupational-therapy": [
        B("Introduction to Occupational Therapy", "O'Brien & Conners", "Mosby"),
        B("Conditions in Occupational Therapy: Effect on Occupational Performance", "Atchison & Dirette", "Wolters Kluwer")],
    "patient-care-technician": [
        B("PCT Skills Builder Plus", "National Healthcareer Association", "", "Online course"),
        B("Certified Patient Care Technician/Assistant (CPCT/A) Online Study Guide", "National Healthcareer Association", "", "Online study guide")],
    "personal-care": [
        B("Nursing Assisting: A Foundation in Caregiving", "Dugan", "Hartman Publishing"),
        B("The Nursing Assistant: Essentials of Holistic Care", "Roe", "Goodheart-Willcox")],
    "pharmacy-science": [
        B("Manual for Pharmacy Technicians", "Bachenheimer & Phillips", "ASHP"),
        B("Understanding Pharmacology for Pharmacy Technicians", "Stuhan", "ASHP")],
    "phlebotomy": [
        B("Phlebotomy: A Competency Based Approach", "Booth & Mundt", "McGraw Hill"),
        B("Phlebotomy Essentials", "McCall", "Jones & Bartlett Learning")],
    "physical-therapy": [
        DHO(),
        B("Principles and Techniques of Patient Care", "Pierson & Fairchild", "Elsevier"),
        B("Introduction to Physical Therapy", "Pagliarulo", "Elsevier")],
    "physician-assistant": [B("Current Medical Diagnosis & Treatment", "Papadakis, Rabow, McQuaid, Nadler & Price", "McGraw Hill")],
    "respiratory-therapy": [
        B("Egan's Fundamentals of Respiratory Care", "Stoller, Heuer, Chatburn, Mireles-Cabodevila & Vines", "Elsevier"),
        DHO()],
    "sports-medicine": [
        B("Orthopedic Taping, Wrapping, Bracing, and Padding", "Beam", "F.A. Davis"),
        B("Introduction to Sports Medicine and Athletic Training", "France", "Cengage"),
        B("The Role of the Athletic Trainer in Sports Medicine", "Prentice", "McGraw Hill")],
    "surgical-technologist": [
        B("Surgical Technology for the Surgical Technologist: A Positive Care Approach", "Association of Surgical Technologists", "Cengage Learning", "Round One test focuses on chapters 1, 4, 7, 10, 11 and 16"),
        B("Surgical Instrumentation: An Interactive Approach", "Nemitz", "Saunders")],
    "veterinary-science": [B("Introduction to Veterinary Science", "Lawhead & Baker", "Cengage Learning")],
    "cert-skills": [
        B("CERT Basic Training (IS-317)", "FEMA", "", "Online course"),
        B("CERT Basic Training Participant Manual", "FEMA", ""),
        B("First Aid for Severe Trauma (FAST)", "American Red Cross", ""),
        B("SALT Mass Casualty Triage", "National Disaster Life Support Foundation", "", "Online course")],
    "cpr-first-aid": [
        B("Basic Life Support", "American Red Cross"),
        B("First Aid/CPR/AED", "American Red Cross"),
        B("Basic Life Support", "American Heart Association"),
        B("Heartsaver First Aid", "American Heart Association"),
        DHO()],
    "emergency-medical-technician": [
        B("Emergency Care and Transportation of the Sick and Injured", "Pollak (series ed.)", "Jones & Bartlett Learning"),
        B("BLS Provider Manual", "American Heart Association"),
        B("Emergency Care", "Limmer & O'Keefe", "Brady / Prentice Hall")],
    "epidemiology": [
        B("PH 101 Series", "CDC", "", "Online course"),
        B("ActivEpi", "", "", "Online course"),
        B("Morbidity and Mortality Weekly Report (MMWR)", "CDC", "", "Online reports")],
    "life-support-skills": [
        B("Basic Life Support", "American Red Cross"),
        B("First Aid/CPR/AED", "American Red Cross"),
        B("BLS Provider Manual", "American Heart Association"),
        B("Heartsaver First Aid", "American Heart Association"),
        DHO()],
    "healthy-living": [B("HOSA Healthy Living Course", "NASM", "", "Online course")],
    "organizational-leadership": [
        B("HOSA Handbook (Sections A, B and C)", "HOSA"),
        RRONR_BRIEF,
        B("First Fifty Years 1976–2026", "HOSA")],
    "biomedical-debate": [
        B("Breaking the Age Code", "Becca Levy", "William Morrow"),
        B("The Ethics of Health Care Rationing", "Bognar & Hirose", "Routledge")],
    "creative-problem-solving": [
        B("Organizational Behavior", "McShane & Von Glinow", "McGraw Hill"),
        B("Decision Making & Problem Solving", "Adair", "Kogan Page"),
        B("Solve It!", "Sternad", "Econcise Publishing"),
        B("Critical Thinking & Logic Mastery (3 Books in 1)", "Thinknetic")],
    "forensic-science": [
        B("Forensic Science Fundamentals", "Bertino & Bertino", "National Geographic Learning / Cengage"),
        B("Forensic Science", "Bell", "CRC Press")],
    "hosa-bowl": [
        DHO(),
        B("Body Structures and Functions", "Scott & Bell", "Cengage Learning"),
        TABERS, RRONR_BRIEF,
        B("First Fifty Years 1976–2026", "HOSA"),
        STANHOPE],
    "parliamentary-procedure": [
        B("Robert's Rules of Order Newly Revised", "", "Da Capo Press"),
        RRONR_BRIEF,
        B("Study Questions for NAP Membership Exam", "National Association of Parliamentarians")],
}

# Short, readable format labels
def fmt(v):
    r = v["round1"]
    if r.startswith("50 Q test"):
        mins = re.search(r"\((\d+) minutes\)", r)
        return f"50-question test ({mins.group(1)} min)" if mins else "50-question test"
    fixes = {
        "Research, Interview &": "Research, interview & presentation",
        "Written policy letter in 60": "Written policy letter (60 min)",
        "Digital upload of portfolio": "Photo portfolio",
        "Digital upload of Resume": "Resume upload, then interview",
        "Digital upload of research": "Research paper, then speech",
        "Digital outline & picture of": "Career display",
        "Digital upload of poster,": "Research poster",
        "Digital: Portfolio": "Portfolio",
        "Portfolio pre-judged": "Portfolio",
        "Portfolio (pre-judged)": "Portfolio",
        "Digital outline pre-judged": "Innovation outline, then presentation",
        "PSA video pre-judged": "PSA video",
        "Trailer Video (pre-judged)": "Trailer video, then presentation",
        "Digital Social Media": "Social media campaign",
        "Speech (5 minutes)": "5-minute speech",
        "5 minute Speech": "5-minute speech",
    }
    return fixes.get(r, r)

def team(v):
    t = v["team"]
    if t.lower().startswith("solo"): return "Individual"
    m = re.search(r"(\d+(?:-\d+)?) competitors", t)
    return f"Team of {m.group(1).replace('-', '–')}" if m else t

def plan(v):
    rows = []
    for it in v["testplan"]:
        t = it["t"]
        if it.get("intro") or re.match(r"^(The (written )?test|The test plan|Includes both)", t, re.I) and "%" not in t.split("is:")[-1]:
            continue
        # inline ○ sub-items (some PDFs put them on one line)
        subs = list(it["sub"])
        if "○" in t:
            parts = [p.strip() for p in t.split("○")]
            t, subs = parts[0], [p for p in parts[1:] if p] + subs
        t = re.sub(r"\s*At the International Leadership Conference.*$", "", t)
        t = re.sub(r"\s*The test will include.*$", "", t)
        m = re.match(r"^(.*?)[\s:–-]*\(?(\d+)\s*%\)?\s*:?\s*$", t)
        topic, pct = (m.group(1).strip(" -–:"), int(m.group(2))) if m else (t.strip(), None)
        # sub-items that carry their own % (Body Systems) become their own rows
        if subs and all(re.search(r"\d+\s*%", s) for s in subs):
            for s in subs:
                sm = re.match(r"^(.*?)[\s–-]*(\d+)\s*%", s)
                rows.append({"topic": f"{topic.rstrip(':')}: {sm.group(1).strip(' -–')}", "pct": int(sm.group(2))})
            continue
        if topic.startswith("(Safety"): continue
        if topic.startswith("The remaining categories"):
            topic = "Other: " + ", ".join(subs); subs = []
        row = {"topic": topic, "pct": pct}
        if subs: row["sub"] = subs
        rows.append(row)
    return rows

events = []
for id_, v in ex.items():
    is_test = v["round1"].startswith("50 Q test")
    e = {
        "id": id_, "name": v["name"], "category": v["category"],
        "format": fmt(v), "team": team(v), "hasTest": is_test,
        "summary": v["summary"], "guideline": v["pdf"],
        "books": BOOKS.get(id_, []),
    }
    if is_test:
        qm = re.match(r"(\d+) Q test \((\d+) minutes\)", v["round1"])
        e["testQuestions"], e["testMinutes"] = int(qm.group(1)), int(qm.group(2))
        e["testPlan"] = plan(v)
    events.append(e)

missing = [e["id"] for e in events if e["hasTest"] and not e["books"]]
assert not missing, missing

header = """/*
 * HOSA event catalog, 2026-2027 school year.
 * Generated from the official HOSA Competitive Event Guidelines (hosa.org/guidelines).
 * Excludes Recognition events, Middle School-only events, and Academic Testing Center (ATC) exams.
 *
 * books     = references HOSA lists as used to write the test questions (shown under Chapter Summaries)
 * testPlan  = the official test plan (topic weightings) for events with a written test
 * testQuestions / testMinutes = length and time limit of the official Round One test
 */
window.CATEGORIES = [
  { id: "health-science", name: "Health Science", color: "#0ea5a4" },
  { id: "health-professions", name: "Health Professions", color: "#6366f1" },
  { id: "emergency-preparedness", name: "Emergency Preparedness", color: "#ef4444" },
  { id: "leadership", name: "Leadership", color: "#f59e0b" },
  { id: "teamwork", name: "Teamwork", color: "#8b5cf6" },
];

window.GUIDELINE_YEAR = "2026–2027";

window.EVENTS = """
open(dest, "w", encoding="utf-8").write(header + json.dumps(events, indent=2, ensure_ascii=False) + ";\n")

print(len(events), "events;", sum(e["hasTest"] for e in events), "with a written test")
for e in events:
    if e["hasTest"]:
        tot = sum(r["pct"] or 0 for r in e["testPlan"])
        print(f'{e["name"][:34]:34} books={len(e["books"])} plan={len(e["testPlan"])} total%={tot}')
