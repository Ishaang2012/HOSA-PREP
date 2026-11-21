/*
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

window.EVENTS = [
  {
    "id": "behavioral-health",
    "name": "Behavioral Health",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Behavioral Health allows members to gain knowledge and skills surrounding psychology, the mind, mental health, and substance use disorders. This competitive event consists of a written test. In the event of a tie, the tiebreaker essay will be judged. It aims to inspire members to learn about and promote mental health resilience and how to support those in recovery, their families, and the health community.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/BH-26-27.pdf",
    "books": [
      {
        "title": "Discovering Psychology",
        "author": "Cacioppo & Freberg",
        "publisher": "Cengage Learning"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "The Mind",
        "pct": 25,
        "sub": [
          "Biological",
          "Sensation",
          "Perception",
          "Consciousness",
          "Motivation",
          "Emotion",
          "Learning",
          "Memory"
        ]
      },
      {
        "topic": "Psychology and Behavioral Health Disorders, Treatments, Therapies & Services",
        "pct": 25,
        "sub": [
          "Autism",
          "ADHD",
          "Schizophrenia",
          "Bipolar",
          "Depression",
          "Anxiety",
          "OCD",
          "PTSD",
          "Personality Disorders",
          "Dissociative Disorders",
          "Eating Disorders"
        ]
      },
      {
        "topic": "Prevention, Identification, Recovery, and Management of Substance Abuse and Mental Illness",
        "pct": 25
      },
      {
        "topic": "Wellness, Stress, Coping",
        "pct": 15
      },
      {
        "topic": "Workforce/Careers and Laws, Regulations and Guidelines",
        "pct": 5
      },
      {
        "topic": "History and Health Systems Integration",
        "pct": 5
      }
    ]
  },
  {
    "id": "biomedical-equipment-technician",
    "name": "Biomedical Equipment Technician",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "The Biomedical Equipment Technician event aims to inspire members to learn more about Biomedical Equipment Technicians (BMETs) who ensure the functionality and safety of medical, imaging, and dental devices, including patient monitors, dental handpieces, surgical robots, ventilators, vacuum pumps, and imaging systems. This competitive event consists of a written test with a tiebreaker essay question. Through this event, competitors will learn how BMETs troubleshoot, maintain equipment, and ensure compliance within healthcare safety standards. BMETs combine technical expertise in electronics and mechanics with problem-solving skills to ensure medical devices operate reliably. They also communicate effectively with healthcare staff to provide training and support, contributing directly to patient care quality.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/BET-26-27-Sept09.pdf",
    "books": [
      {
        "title": "AAMI BMET 101",
        "author": "AAMI Training",
        "note": "Online course"
      },
      {
        "title": "Medical Equipment Technician (MET) 100 Series",
        "author": "College of Biomedical Equipment Training",
        "note": "Online course"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Anatomy & Physiology",
        "pct": 10
      },
      {
        "topic": "Medical Devices as Related to Public Safety",
        "pct": 22
      },
      {
        "topic": "Safety in Healthcare",
        "pct": 16
      },
      {
        "topic": "Fundamentals in Electricity and Electronics",
        "pct": 14
      },
      {
        "topic": "Reasoning",
        "pct": 24
      },
      {
        "topic": "Healthcare IT",
        "pct": 14
      }
    ]
  },
  {
    "id": "dental-terminology",
    "name": "Dental Terminology",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Dental terminology allows members to gain knowledge and skills regarding language common to all dental careers and specialties. This competitive event consists of a written test. In the event of a tie, the tiebreaker questions will be judged. It inspires members to learn about dental terminology, physiology, and pathophysiology.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/DT-26-27-.pdf",
    "books": [
      {
        "title": "Dental Terminology",
        "author": "Kindle & Dofka",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Wheeler's Dental Anatomy, Physiology and Occlusion",
        "author": "Nelson",
        "publisher": "Elsevier"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Comprehensive Dental Care and Dental Specialties",
        "pct": 30,
        "sub": [
          "General Dentistry",
          "Oral and Maxillofacial Surgery",
          "Cosmetic Dentistry",
          "Pediatric Dentistry",
          "Prosthodontics",
          "Endodontics, Orthodontics, & Periodontics",
          "Implant Dentistry",
          "Dental office laboratory and equipment"
        ]
      },
      {
        "topic": "Dental Instruments",
        "pct": 10
      },
      {
        "topic": "Pharmacology & Pain Management",
        "pct": 10
      },
      {
        "topic": "Emergency Care",
        "pct": 10
      },
      {
        "topic": "Tooth Restorations",
        "pct": 10
      },
      {
        "topic": "Head and Neck Anatomy",
        "pct": 10
      },
      {
        "topic": "Radiography",
        "pct": 10
      },
      {
        "topic": "Dental Laboratory Materials and Procedures",
        "pct": 10
      }
    ]
  },
  {
    "id": "health-informatics",
    "name": "Health Informatics",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "The Health Informatics test will assess knowledge and skills related to health information systems, analysis of healthcare data and information, and clinical research processes. This competitive event consists of a written test. In the event of a tie, the essay will be judged to break the tie. It aims to inspire members to learn more about this field.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/HI-26-27-FINAL-1-2.pdf",
    "books": [
      {
        "title": "Introduction to Healthcare Informatics",
        "author": "Zhou & Clack",
        "publisher": "AHIMA Press"
      },
      {
        "title": "A Practical Approach to Analyzing Healthcare Data",
        "author": "White",
        "publisher": "AHIMA Press"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "History, Careers, and Roles",
        "pct": 8
      },
      {
        "topic": "Information Systems in Healthcare",
        "pct": 12
      },
      {
        "topic": "Data Analytics",
        "pct": 28
      },
      {
        "topic": "Data Integrity and Quality",
        "pct": 8
      },
      {
        "topic": "Data Governance",
        "pct": 12
      },
      {
        "topic": "Health Information Privacy & Security",
        "pct": 12
      },
      {
        "topic": "Ethics",
        "pct": 4
      },
      {
        "topic": "Research Study and Design",
        "pct": 12
      },
      {
        "topic": "Emerging Technologies",
        "pct": 4
      }
    ]
  },
  {
    "id": "healthcare-administration",
    "name": "Healthcare Administration",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Healthcare Administration allows members to gain knowledge and skills regarding managing healthcare. This competitive event consists of a written test with a tiebreaker essay question. It aims to inspire members to learn about and prepare for a role in healthcare administration.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/HCA-26-27-FINAL-1.pdf",
    "books": [
      {
        "title": "Shortell & Kaluzny's Health Care Management: Organization Design and Behavior",
        "author": "Burns, Bradley & Weiner",
        "publisher": "Cengage"
      },
      {
        "title": "Introduction to Health Care Management",
        "author": "Buchbinder",
        "publisher": "Jones & Bartlett Learning"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Globalization of Health Care Delivery Systems and Challenges",
        "pct": 10
      },
      {
        "topic": "Leadership & Management Framework",
        "pct": 10
      },
      {
        "topic": "Organization Design & Coordination",
        "pct": 10
      },
      {
        "topic": "Motivating People and Conflict Management",
        "pct": 10
      },
      {
        "topic": "Teams & Team Effectiveness",
        "pct": 10
      },
      {
        "topic": "Communication",
        "pct": 10
      },
      {
        "topic": "Improving Quality",
        "pct": 10
      },
      {
        "topic": "Strategy & Achieving Mission",
        "pct": 10
      },
      {
        "topic": "Health Policy & Regulation",
        "pct": 10
      },
      {
        "topic": "Consumerism & Ethics",
        "pct": 10
      }
    ]
  },
  {
    "id": "human-growth-development",
    "name": "Human Growth and Development",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Human Growth & Development allows members to gain knowledge and skills regarding biophysical, mental/cognitive, social, and emotional development throughout the human lifespan. This competitive event consists of a written test. In the event of a tie, the essay will be judged to break the tie. It aims to inspire members to learn more about growth and development across the lifespan.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/HGD-26-27.pdf",
    "books": [
      {
        "title": "Journey Across the Lifespan: Human Development and Health Promotion",
        "author": "Polan & Taylor",
        "publisher": "F.A. Davis"
      },
      {
        "title": "DHO: Health Science",
        "author": "Simmers, Simmers-Nartker, Simmers-Kobelak & Morris",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Lifespan Development",
        "author": "Kato",
        "publisher": "Goodheart-Willcox"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Government, Cultural, and Family Influences",
        "pct": 20
      },
      {
        "topic": "Theories of Development",
        "pct": 16
      },
      {
        "topic": "Prenatal and Infancy",
        "pct": 12
      },
      {
        "topic": "Childhood and Adolescence",
        "pct": 22
      },
      {
        "topic": "Adulthood",
        "pct": 15
      },
      {
        "topic": "Geriatrics, End of Life, and Grief",
        "pct": 15
      }
    ]
  },
  {
    "id": "medical-law-ethics",
    "name": "Medical Law and Ethics",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Medical Law & Ethics allows members to gain knowledge and skills regarding U.S. medical law, ethics, and bioethics. This competitive event consists of a written test. In the event of a tie, the essay will be judged to break the tie. It aims to inspire members to learn about ethical and legal terms and how to analyze, synthesize, and evaluate information related to this field.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/MLE-26-27.pdf",
    "books": [
      {
        "title": "Medical Law, Ethics, & Bioethics for the Health Professions",
        "author": "Tamparo",
        "publisher": "F.A. Davis"
      },
      {
        "title": "Healthcare Law and Ethics",
        "author": "Fremgen",
        "publisher": "Pearson"
      },
      {
        "title": "Medical Law & Professional Ethics",
        "author": "Ritter & Graham",
        "publisher": "Goodheart-Willcox"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "The Basics: Medical Law, Ethics and Bioethics",
        "pct": 5
      },
      {
        "topic": "The Legal Environment",
        "pct": 35,
        "sub": [
          "State and Federal Regulations; Consent",
          "The Legal System; Professional Liability",
          "Law for Health Professionals; Public Duty"
        ]
      },
      {
        "topic": "The Health Care Environment",
        "pct": 35,
        "sub": [
          "Physician-Patient Relationships",
          "Medical Malpractice",
          "Medical Records",
          "Workplace Law and Ethics",
          "Cultural Perspective",
          "Patient Confidentiality",
          "Employment Practices"
        ]
      },
      {
        "topic": "Bioethical Issues",
        "pct": 25,
        "sub": [
          "Ethical and Bioethical Issues in Medicine",
          "Allocation of Scarce Resources",
          "Genetic Engineering",
          "Reproductive Issues",
          "End-of-Life Issues"
        ]
      }
    ]
  },
  {
    "id": "medical-math",
    "name": "Medical Math",
    "category": "health-science",
    "format": "50-question test (90 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Medical Math allows members to gain the knowledge and skills required to identify, solve, and apply mathematical principles. This competitive event consists of a written test. In the event of a tie, the tie-breaker questions will be judged to break the tie. It aims to inspire members to learn about the integration of mathematics in health care, including temperature, weights, and measures used in the health community.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/MM-26-27-Updated-10.17.pdf",
    "books": [
      {
        "title": "DHO: Health Science",
        "author": "Simmers, Simmers-Nartker, Simmers-Kobelak & Morris",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Dosage Calculations Made Easy",
        "author": "Craig",
        "publisher": "Wolters Kluwer"
      },
      {
        "title": "Pharmacy Calculations: An Introduction for Pharmacy Technicians",
        "author": "Rewald, Lorang & Schramm",
        "publisher": "ASHP"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 90,
    "testPlan": [
      {
        "topic": "Mathematical essentials",
        "pct": 5
      },
      {
        "topic": "Measurement and conversion problems",
        "pct": 30
      },
      {
        "topic": "Drug dosages and intravenous solutions",
        "pct": 35
      },
      {
        "topic": "Dilutions, solutions, and concentrations",
        "pct": 30
      }
    ]
  },
  {
    "id": "medical-reading",
    "name": "Medical Reading",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Medical Reading allows Secondary and Postsecondary/Collegiate members to improve their reading comprehension and understanding of particular topics related to leadership development and the health community. This competitive event shall be a written test of information and knowledge gained from reading the selected books for the current year. Competitors will apply, analyze, synthesize, and/or evaluate the reading material in a multiple-choice test. This event aims to inspire members to be proactive future health professionals and apply the knowledge gained from reading medical and leadership books.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/MR-26-27.pdf",
    "books": [
      {
        "title": "Crisis Averted: The Hidden Science of Fighting Outbreaks",
        "author": "Caitlin Rivers"
      },
      {
        "title": "Everything Is Tuberculosis: The History and Persistence of Our Deadliest Infection",
        "author": "John Green"
      },
      {
        "title": "Fragmented: A Doctor's Quest to Piece Together American Healthcare",
        "author": "Ilana Yurkiewicz, MD"
      },
      {
        "title": "The Next Patient: The Incredible World of Emergency Medicine",
        "author": "J. Thomas Grant"
      },
      {
        "title": "Grit: The Power of Passion and Perseverance",
        "author": "Angela Duckworth"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": []
  },
  {
    "id": "medical-spelling",
    "name": "Medical Spelling",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Medical Spelling allows HOSA members to gain knowledge and skills regarding the definitions and spelling of medical terms. This competitive event consists of two rounds: Round One is a written, multiple-choice test, and Round Two is a “spelldown” in which competitors spell terms in front of judges. This event aims to inspire members to become skilled in medical spelling.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/MS-26-27-FINAL-1.pdf",
    "books": [
      {
        "title": "Taber's Cyclopedic Medical Dictionary",
        "author": "Venes (ed.)",
        "publisher": "F.A. Davis"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": []
  },
  {
    "id": "medical-terminology",
    "name": "Medical Terminology",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Medical Terminology allows members to gain knowledge and skills regarding prefixes, suffixes, word roots, anatomy, physiology, pathophysiology, and occupations related to the health field. This competitive event consists of a written test with tiebreaker questions and aims to inspire members to learn about terms used in health professions and specialties.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/MT-26-27.pdf",
    "books": [
      {
        "title": "Medical Terminology for Health Professions",
        "author": "Ehrlich",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Taber's Cyclopedic Medical Dictionary",
        "author": "Venes (ed.)",
        "publisher": "F.A. Davis"
      },
      {
        "title": "Introduction to Medical Terminology",
        "author": "Stanhope & Turnbull",
        "publisher": "Goodheart-Willcox"
      },
      {
        "title": "Dean Vaughn's Medical Terminology by Body Systems",
        "author": "Dean Vaughn",
        "publisher": "Peterson's Publishing",
        "note": "Online course"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Roots, Prefixes, Suffixes, and Combining Forms",
        "pct": 45
      },
      {
        "topic": "Overview of Body",
        "pct": 5
      },
      {
        "topic": "Skeletal",
        "pct": 5
      },
      {
        "topic": "Muscular",
        "pct": 5
      },
      {
        "topic": "Respiratory",
        "pct": 5
      },
      {
        "topic": "Digestive",
        "pct": 5
      },
      {
        "topic": "Cardiovascular & Lymphatic",
        "pct": 5
      },
      {
        "topic": "Nervous/Special Senses",
        "pct": 5
      },
      {
        "topic": "Endocrine",
        "pct": 5
      },
      {
        "topic": "Reproductive",
        "pct": 5
      },
      {
        "topic": "Integumentary",
        "pct": 5
      },
      {
        "topic": "Urinary",
        "pct": 5
      }
    ]
  },
  {
    "id": "nutrition",
    "name": "Nutrition",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Nutrition allows HOSA members to explore and learn about the relationship between nutrition and wellness and assess knowledge common in this health field. This competitive event consists of a written test. In the event of a tie, the essay will be judged to break the tie. It aims to inspire members to become proactive future health professionals by applying and analyzing information related to nutrition and health.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Nut-26-27.pdf",
    "books": [
      {
        "title": "Nutrition and Diet Therapy",
        "author": "Roth",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Nutrition and Wellness for Life",
        "author": "West",
        "publisher": "Goodheart-Willcox"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Carbohydrates, fats and proteins",
        "pct": 15
      },
      {
        "topic": "Vitamins & minerals",
        "pct": 15
      },
      {
        "topic": "Water (Fluid & electrolyte balance)",
        "pct": 10
      },
      {
        "topic": "Nutrition through the life span",
        "pct": 15
      },
      {
        "topic": "Digestion, absorption, and metabolism",
        "pct": 10
      },
      {
        "topic": "Cultural patterns and food habits",
        "pct": 5
      },
      {
        "topic": "Food-related illnesses, intolerances, and allergies",
        "pct": 10
      },
      {
        "topic": "Medical nutrition therapy",
        "pct": 20,
        "sub": [
          "Diabetes",
          "Renal Disease",
          "Clients with special needs",
          "Cardiovascular disease",
          "Gastrointestinal disease",
          "Cancer"
        ]
      }
    ]
  },
  {
    "id": "pathophysiology",
    "name": "Pathophysiology",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Pathophysiology allows members to gain knowledge and skills regarding pathophysiology concepts. This competitive event consists of a written test. In the event of a tie, the essay will be judged to break the tie. This event aims to inspire members to learn about the anatomy and physiology of human diseases impacting the health community.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Patho-26-27-FINAL-1.pdf",
    "books": [
      {
        "title": "iCEV Pathophysiology and Anatomy & Physiology Courses",
        "author": "iCEV",
        "note": "Online course"
      },
      {
        "title": "Essentials of Human Diseases and Conditions",
        "author": "Frazier",
        "publisher": "Elsevier"
      },
      {
        "title": "Human Diseases: A Systemic Approach",
        "author": "Zelman et al.",
        "publisher": "Pearson"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Disease Process & Terminology (includes cancer & neoplasms)",
        "pct": 12
      },
      {
        "topic": "Body Systems: Integumentary",
        "pct": 8
      },
      {
        "topic": "Body Systems: Musculoskeletal",
        "pct": 10
      },
      {
        "topic": "Body Systems: Circulatory & Lymphatic",
        "pct": 12
      },
      {
        "topic": "Body Systems: Respiratory",
        "pct": 8
      },
      {
        "topic": "Body Systems: Digestive",
        "pct": 12
      },
      {
        "topic": "Body Systems: Endocrine",
        "pct": 8
      },
      {
        "topic": "Body Systems: Nervous & Senses",
        "pct": 10
      },
      {
        "topic": "Body Systems: Reproductive",
        "pct": 6
      },
      {
        "topic": "Body Systems: Urinary",
        "pct": 6
      },
      {
        "topic": "Body Systems: Mental Disorders",
        "pct": 8
      }
    ]
  },
  {
    "id": "pharmacology",
    "name": "Pharmacology",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Pharmacology provides HOSA members with the opportunity to gain knowledge and skills regarding the area of healthcare concerned with drug uses, effects, and modes of action. This competitive event consists of a written test. In the event of a tie, the essay will be judged to break the tie. It aims to inspire members to learn about drugs' actions on the body, proper administration, and adaptations for different patients and conditions.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Pharm-26-27.pdf",
    "books": [
      {
        "title": "The Pharmacy Technician: A Comprehensive Approach",
        "author": "Moini",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Introductory Clinical Pharmacology",
        "author": "Ford & Roach",
        "publisher": "Wolters Kluwer"
      },
      {
        "title": "Dean Vaughn's Pharmacology by Body System",
        "author": "Dean Vaughn",
        "note": "Online course"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Basic Concepts in Pharmacology",
        "pct": 15
      },
      {
        "topic": "Ethical and Legal Responsibilities",
        "pct": 10
      },
      {
        "topic": "Pediatrics and Geriatrics Adaptations",
        "pct": 10
      },
      {
        "topic": "Drug Names, Classifications, Actions, and Interactions",
        "pct": 30
      },
      {
        "topic": "Drug Administration",
        "pct": 20
      },
      {
        "topic": "Drug Measurement, Dosage, Conversions",
        "pct": 10
      },
      {
        "topic": "Technologies in Pharmacology",
        "pct": 5
      }
    ]
  },
  {
    "id": "world-health-disparities",
    "name": "World Health and Disparities",
    "category": "health-science",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "World Health and Disparities allows members to gain knowledge and skills regarding world health and disparities. This competitive event consists of a written test. In the event of a tie, the essay will be judged to break the tie. The event aims to increase competence in understanding world health and identifying and overcoming health disparities.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/WHD-26-27.pdf",
    "books": [
      {
        "title": "Health Disparities in the US",
        "author": "Barr",
        "publisher": "Johns Hopkins University Press"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "What is Health",
        "pct": 20
      },
      {
        "topic": "Health Disparities & Diversity",
        "pct": 40
      },
      {
        "topic": "Disparities in Treatment & Medical Decisions",
        "pct": 20
      },
      {
        "topic": "Reducing Health Disparities",
        "pct": 20
      }
    ]
  },
  {
    "id": "biotechnology",
    "name": "Biotechnology",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Biotechnology allows members to gain the knowledge and skills required for a laboratory setting using biotechnology. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors will advance to Round Two for the skills assessment. This event aims to inspire members to learn more about biotechnology careers.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/BT-26-27-FINAL-.pdf",
    "books": [
      {
        "title": "Biotechnology: A Laboratory Skills Course",
        "author": "Brown",
        "publisher": "Bio-Rad"
      },
      {
        "title": "Biology: The Unity and Diversity of Life (AP)",
        "author": "Starr & Taggart",
        "publisher": "National Geographic Learning / Cengage"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Biotechnology industry practices and careers",
        "pct": 4
      },
      {
        "topic": "Biotechnology in health",
        "pct": 4
      },
      {
        "topic": "Governmental regulation of biotechnology",
        "pct": 4
      },
      {
        "topic": "Basic laboratory skills",
        "pct": 14,
        "sub": [
          "PPE",
          "Preparing solutions (calculations, use of balance and other equipment)",
          "Pipetting"
        ]
      },
      {
        "topic": "Microbiology and cell culture",
        "pct": 12
      },
      {
        "topic": "DNA structure and analysis",
        "pct": 14
      },
      {
        "topic": "Bacterial transformation",
        "pct": 10
      },
      {
        "topic": "Polymerase chain reaction (PCR)",
        "pct": 14
      },
      {
        "topic": "Protein structure, function, and analysis",
        "pct": 14
      },
      {
        "topic": "Immunological applications",
        "pct": 10
      }
    ]
  },
  {
    "id": "clinical-lab-science",
    "name": "Clinical Lab Science",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Clinical Laboratory Science (Medical Laboratory Scientist) provides members with the opportunity to gain the knowledge and skills required for a traditional laboratory setting. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors advance to Round Two for the skills assessment. This event aims to inspire members to learn more about clinical/medical laboratory careers.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/CLS_MLS-26-27-FINAL-2-1.pdf",
    "books": [
      {
        "title": "Basic Clinical Laboratory Techniques",
        "author": "Estridge & Reynolds",
        "publisher": "Cengage Learning"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Clinical Lab Professions",
        "pct": 8
      },
      {
        "topic": "Biological Safety",
        "pct": 12
      },
      {
        "topic": "Laboratory Math",
        "pct": 6
      },
      {
        "topic": "Hematology & Hemostasis",
        "pct": 14
      },
      {
        "topic": "Immunology",
        "pct": 16
      },
      {
        "topic": "Urinalysis",
        "pct": 8
      },
      {
        "topic": "Clinical Chemistry",
        "pct": 14
      },
      {
        "topic": "Clinical Microbiology",
        "pct": 14
      },
      {
        "topic": "Parasitology",
        "pct": 8
      }
    ]
  },
  {
    "id": "clinical-nursing",
    "name": "Clinical Nursing",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Clinical Nursing provides members with the opportunity to gain the knowledge and skills required in the nursing field. This competitive event consists of two rounds. Round One will be a written, multiple-choice test and top-scoring competitors will advance to Round Two for the skills assessment. This event aims to inspire members to use critical thinking skills and be equipped with insight to treat patients in a clinical setting.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/CN-26-27-FINAL-2-1.pdf",
    "books": [
      {
        "title": "Clinical Nursing Skills and Techniques",
        "author": "Perry & Potter",
        "publisher": "Elsevier / Mosby"
      },
      {
        "title": "Textbook of Basic Nursing",
        "author": "Rosdahl & Kowalski",
        "publisher": "Wolters Kluwer"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Basic Care",
        "pct": 20
      },
      {
        "topic": "Clinical Care Through the Life Span",
        "pct": 20,
        "sub": [
          "Maternal / Newborn",
          "Pediatrics",
          "Adulthood and Gerontology",
          "Mental Health",
          "Home Care, Extended Care, Rehabilitation, Hospice"
        ]
      },
      {
        "topic": "Clinical Care for Systems Diseases and Disorders",
        "pct": 60,
        "sub": [
          "Structure and Function",
          "Signs and Symptoms",
          "Nursing Assessment and Diagnosis",
          "Pharmacology and Medication Management",
          "Nutrition, Fluid and Electrolyte Balance",
          "Medical and Surgical Treatments"
        ]
      }
    ]
  },
  {
    "id": "clinical-specialty",
    "name": "Clinical Specialty",
    "category": "health-professions",
    "format": "Portfolio",
    "team": "Individual",
    "hasTest": false,
    "summary": "Clinical Specialty allows members to gain knowledge and skills about a health career of their choosing. This competitive event consists of three items: developing a career portfolio, a video demonstration of a selected skill common to the chosen health career, and a live presentation to the judges. This event aims to inspire members to learn more about a health-related career and become skilled future health professionals.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/CS-26-27-Oct-26.pdf",
    "books": []
  },
  {
    "id": "dental-science",
    "name": "Dental Science",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Dental Science allows members to gain knowledge and skills required for dental careers. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors will advance to Round Two for the skills assessment. This event aims to inspire members to learn more about careers in the dental field.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/DS-26-27-Update.pdf",
    "books": [
      {
        "title": "Dental Instruments: A Pocket Guide",
        "author": "Boyd",
        "publisher": "Saunders"
      },
      {
        "title": "Modern Dental Assisting",
        "author": "Robinson",
        "publisher": "Elsevier"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "The Dental Team, Dental Specialties, and History",
        "pct": 10
      },
      {
        "topic": "DENTAL Anatomy and Physiology",
        "pct": 10
      },
      {
        "topic": "Dental Pathology",
        "pct": 10
      },
      {
        "topic": "Tooth Morphology",
        "pct": 10
      },
      {
        "topic": "Infection Control / Occupational Health and Safety",
        "pct": 10
      },
      {
        "topic": "Chairside Assisting/Instruments (Including Restorative and Laboratory Materials)",
        "pct": 30
      },
      {
        "topic": "Radiology",
        "pct": 10
      },
      {
        "topic": "Medical Emergencies in the Dental Office",
        "pct": 10
      }
    ]
  },
  {
    "id": "family-medicine-physician",
    "name": "Family Medicine Physician",
    "category": "health-professions",
    "format": "Research, interview & presentation",
    "team": "Individual",
    "hasTest": false,
    "summary": "The Family Medicine Physician competitive event allows HOSA members to gain knowledge about this career path through interviews, research, and a peer presentation. Competitors will conduct interviews to learn more about family medicine and share their findings with their peers through a presentation. Competitors will present their peer presentations to judges, showcasing what they have learned. This event aims to inspire members to learn about the dynamic field of Family Medicine and ensure patients from every community, everywhere, have access to a family physician.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/FMP-26-27-.pdf",
    "books": []
  },
  {
    "id": "genetics",
    "name": "Genetics",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Genetics provides HOSA Members the opportunity to gain the knowledge and skills required for a laboratory setting and to explore genetics-related careers. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors will advance to Round Two for the skills assessment. This event aims to inspire members to learn more about the careers available.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/11/Gen-26-27-11.17-1.pdf",
    "books": [
      {
        "title": "Carolina Genetics: A Guidebook for the HOSA Genetics Written Test",
        "author": "Carolina Biological"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Reproduction, Mitosis and Meiosis",
        "pct": 20
      },
      {
        "topic": "Classical Genetics",
        "pct": 20
      },
      {
        "topic": "Chromosomal Inheritance",
        "pct": 10
      },
      {
        "topic": "Experimental Design and Model Organisms",
        "pct": 15
      },
      {
        "topic": "Molecular Genetics",
        "pct": 15
      },
      {
        "topic": "Population Genetics",
        "pct": 10
      },
      {
        "topic": "Modern Applications and Careers in Genetics",
        "pct": 10
      }
    ]
  },
  {
    "id": "home-health-aide",
    "name": "Home Health Aide",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Home Health Aide allows members to gain the knowledge and skills required for supporting patients in their homes. This competitive event consists of two rounds. Round one is a written, multiple-choice test, and the top-scoring competitors will advance to Round Two for the skills assessment. This event aims to inspire members to be proactive future health professionals and equip them to serve patients in a home health setting.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/HHA-26-27-.pdf",
    "books": [
      {
        "title": "Homemaker Home Health Aide",
        "author": "Balduzzi",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Providing Home Care: A Textbook for Home Health Aides",
        "author": "Leahy, Fuzy & Grafe",
        "publisher": "Hartman Publishing"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Responsibilities and Legal/Ethical Issues",
        "pct": 10
      },
      {
        "topic": "Effective Communication",
        "pct": 6
      },
      {
        "topic": "Infection Control and Safety",
        "pct": 10
      },
      {
        "topic": "Body Systems and Common Disorders",
        "pct": 40
      },
      {
        "topic": "Caring for Special Populations",
        "pct": 24
      },
      {
        "topic": "Basic Healthcare Skills",
        "pct": 10
      }
    ]
  },
  {
    "id": "medical-assisting",
    "name": "Medical Assisting",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Medical Assisting provides members with the opportunity to gain the knowledge and skills required to assist in administrative and clinical tasks. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors advance to Round Two for the skills assessment. This event aims to inspire members to become allied health professionals who respond and assist efficiently in clinical settings.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/MA-26-27-9.29.pdf",
    "books": [
      {
        "title": "Medical Assisting: Administrative and Clinical Competencies",
        "author": "Blesi, Wise & Kelley-Arney",
        "publisher": "Cengage Learning"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Professionalism",
        "pct": 4
      },
      {
        "topic": "Communication Skills",
        "pct": 6
      },
      {
        "topic": "Anatomy & Physiology and Medical Terminology",
        "pct": 10
      },
      {
        "topic": "Legal and Ethical Issues",
        "pct": 10
      },
      {
        "topic": "Office Procedures",
        "pct": 10
      },
      {
        "topic": "Health Insurance and Coding",
        "pct": 10
      },
      {
        "topic": "Infection Control",
        "pct": 10
      },
      {
        "topic": "Collecting and Processing Specimens",
        "pct": 10
      },
      {
        "topic": "Diagnostic Testing",
        "pct": 10
      },
      {
        "topic": "Clinical Procedures and Equipment",
        "pct": 10
      },
      {
        "topic": "Physical Examinations",
        "pct": 10
      }
    ]
  },
  {
    "id": "nursing-assisting",
    "name": "Nursing Assisting",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Nursing Assisting allows members to gain knowledge and skills required for patient care in medical settings. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors will advance to Round Two for the skills assessment. This event aims to inspire members to learn more about the nursing field and how to provide quality care.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/NA-26-27-9.29.pdf",
    "books": [
      {
        "title": "Nursing Assisting: A Foundation in Caregiving",
        "author": "Dugan",
        "publisher": "Hartman Publishing"
      },
      {
        "title": "The Nursing Assistant: Essentials of Holistic Care",
        "author": "Roe",
        "publisher": "Goodheart-Willcox"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Nursing Assistant Roles and Responsibilities",
        "pct": 6
      },
      {
        "topic": "Anatomy and Physiology",
        "pct": 20
      },
      {
        "topic": "Infection Control/Safety",
        "pct": 14
      },
      {
        "topic": "Communication/Culture",
        "pct": 10
      },
      {
        "topic": "Providing and Reporting Care",
        "pct": 30
      },
      {
        "topic": "Disabilities and Disorders",
        "pct": 20
      }
    ]
  },
  {
    "id": "occupational-therapy",
    "name": "Occupational Therapy",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "The occupational therapy event enables members to acquire the knowledge and skills employed by occupational therapy professionals. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors will advance to Round Two for the skills assessment. This event aims to inspire members to learn more about careers in the occupational therapy field.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/OT-26-27-9.22.pdf",
    "books": [
      {
        "title": "Introduction to Occupational Therapy",
        "author": "O'Brien & Conners",
        "publisher": "Mosby"
      },
      {
        "title": "Conditions in Occupational Therapy: Effect on Occupational Performance",
        "author": "Atchison & Dirette",
        "publisher": "Wolters Kluwer"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Profession of OT",
        "pct": 10
      },
      {
        "topic": "Occupational Therapy Models of Practice",
        "pct": 10
      },
      {
        "topic": "Activity Analysis and Occupation-based Activities",
        "pct": 10
      },
      {
        "topic": "Occupational Therapy for Physical Conditions",
        "pct": 20
      },
      {
        "topic": "Occupational Therapy for Wellness and Mental Health",
        "pct": 20
      },
      {
        "topic": "Occupational Therapy Across the Lifespan: Children, Adults, Older Adults",
        "pct": 20
      },
      {
        "topic": "Ethical and Safety Considerations",
        "pct": 10
      }
    ]
  },
  {
    "id": "patient-care-technician",
    "name": "Patient Care Technician",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Patient Care Technician allows members to gain the knowledge and skills required for patient care in medical settings. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors advance to Round Two for the skills assessment. This event aims to inspire members to learn more about the field and how to provide quality patient care.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/PCT-26-27-FINAL-1.pdf",
    "books": [
      {
        "title": "PCT Skills Builder Plus",
        "author": "National Healthcareer Association",
        "note": "Online course"
      },
      {
        "title": "Certified Patient Care Technician/Assistant (CPCT/A) Online Study Guide",
        "author": "National Healthcareer Association",
        "note": "Online study guide"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Patient Care",
        "pct": 44
      },
      {
        "topic": "Compliance, Safety, & Professional Responsibility",
        "pct": 20
      },
      {
        "topic": "Infection Control",
        "pct": 12
      },
      {
        "topic": "Phlebotomy",
        "pct": 14
      },
      {
        "topic": "EKG",
        "pct": 10
      }
    ]
  },
  {
    "id": "personal-care",
    "name": "Personal Care",
    "category": "health-professions",
    "format": "Skill Assessment",
    "team": "Individual",
    "hasTest": false,
    "summary": "Personal Care allows members to gain the knowledge and skills required for patient care in medical settings. This competitive event consists of a skills assessment and aims to inspire members to learn more about the field of nursing and how to provide quality care. This event is specifically for HOSA members classified under IDEA.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/PC-26-27-FINAL-2.pdf",
    "books": [
      {
        "title": "Nursing Assisting: A Foundation in Caregiving",
        "author": "Dugan",
        "publisher": "Hartman Publishing"
      },
      {
        "title": "The Nursing Assistant: Essentials of Holistic Care",
        "author": "Roe",
        "publisher": "Goodheart-Willcox"
      }
    ]
  },
  {
    "id": "pharmacy-science",
    "name": "Pharmacy Science",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Pharmacy Science enables members to acquire the knowledge and skills necessary for careers in pharmacy. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors advance to Round Two for the skills assessment. This event aims to inspire members to learn more about the field of pharmacy, including careers and practices.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/Rx-26-27-Update.pdf",
    "books": [
      {
        "title": "Manual for Pharmacy Technicians",
        "author": "Bachenheimer & Phillips",
        "publisher": "ASHP"
      },
      {
        "title": "Understanding Pharmacology for Pharmacy Technicians",
        "author": "Stuhan",
        "publisher": "ASHP"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Pharmacy Practice History & Practice Settings",
        "pct": 4
      },
      {
        "topic": "Pharmacy Law & Ethics and Safety & Infection Control",
        "pct": 10
      },
      {
        "topic": "Pharmacy Terminology & Abbreviations",
        "pct": 10
      },
      {
        "topic": "Dosage Formulations & Administration Routes",
        "pct": 10
      },
      {
        "topic": "Sterile and Non-Sterile Compounding",
        "pct": 10
      },
      {
        "topic": "Concentration & Dilutions",
        "pct": 10
      },
      {
        "topic": "Disorders & Treatments",
        "pct": 46
      }
    ]
  },
  {
    "id": "phlebotomy",
    "name": "Phlebotomy",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "The phlebotomy event allows members to gain the knowledge and skills required in phlebotomy. This competitive event consists of two rounds. Round One will be a written, multiple-choice test and top-scoring competitors will advance to Round Two for the skills assessment. This event aims to inspire members to use critical thinking skills and be equipped with insight to treat patients in a clinical setting.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/PHL-26-27-9.29.pdf",
    "books": [
      {
        "title": "Phlebotomy: A Competency Based Approach",
        "author": "Booth & Mundt",
        "publisher": "McGraw Hill"
      },
      {
        "title": "Phlebotomy Essentials",
        "author": "McCall",
        "publisher": "Jones & Bartlett Learning"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Obtaining Blood Samples (including which tubes are used for specific tests)",
        "pct": 42
      },
      {
        "topic": "Specimen Collection & Processing",
        "pct": 16
      },
      {
        "topic": "Time Management & Assignment Organization",
        "pct": 8
      },
      {
        "topic": "Professional Communications",
        "pct": 4
      },
      {
        "topic": "Clerical Skills & Duties",
        "pct": 4
      },
      {
        "topic": "Safety Standards & Procedures",
        "pct": 10
      },
      {
        "topic": "Legal, Ethical, & Professional Considerations",
        "pct": 8
      },
      {
        "topic": "Terminology, Anatomy, & Physiology",
        "pct": 8
      }
    ]
  },
  {
    "id": "physical-therapy",
    "name": "Physical Therapy",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Physical therapy as a profession helps people improve movement, reduce pain, restore function, and enhance their quality of life through evidence-based care and education. This competitive event consists of two rounds. Round One is a written, multiple-choice test and top-scoring competitors advance to Round Two for the skills assessment. This event aims to inspire HOSA members to learn more about the concepts and techniques of physical therapy.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/PT-26-27-9.30-1.pdf",
    "books": [
      {
        "title": "DHO: Health Science",
        "author": "Simmers, Simmers-Nartker, Simmers-Kobelak & Morris",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Principles and Techniques of Patient Care",
        "author": "Pierson & Fairchild",
        "publisher": "Elsevier"
      },
      {
        "title": "Introduction to Physical Therapy",
        "author": "Pagliarulo",
        "publisher": "Elsevier"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Profession of PT",
        "pct": 14
      },
      {
        "topic": "Legal and Ethical Considerations",
        "pct": 10
      },
      {
        "topic": "Physical Therapy for Musculoskeletal Conditions",
        "pct": 16
      },
      {
        "topic": "Physical Therapy for Neuromuscular Conditions",
        "pct": 16
      },
      {
        "topic": "Physical Therapy for Cardiopulmonary Conditions",
        "pct": 14
      },
      {
        "topic": "Physical Therapy for Integumentary Conditions",
        "pct": 14
      },
      {
        "topic": "Physical Therapy for Pediatrics and Older Adults",
        "pct": 16
      }
    ]
  },
  {
    "id": "physician-assistant",
    "name": "Physician Assistant – Medical Case Challenge",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Team of 2",
    "hasTest": true,
    "summary": "The Physician Assistant (PA) competitive event allows HOSA members to gain knowledge and assessment techniques needed for a career in the PA profession. This event consists of two rounds, and each team consists of two people. Round One will consist of a written multiple-choice test, and the score will be used to determine which teams qualify for Round Two. In Round Two teams will review case documentation to determine a diagnosis and develop an appropriate treatment plan for the patient.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/PA-26-27-FINAL-1-1.pdf",
    "books": [
      {
        "title": "Current Medical Diagnosis & Treatment",
        "author": "Papadakis, Rabow, McQuaid, Nadler & Price",
        "publisher": "McGraw Hill"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Disease Process & Terminology (includes cancer & neoplasms)",
        "pct": 10
      },
      {
        "topic": "Body Systems: Integumentary",
        "pct": 4
      },
      {
        "topic": "Body Systems: Musculoskeletal",
        "pct": 6
      },
      {
        "topic": "Body Systems: Circulatory & Lymphatic",
        "pct": 10
      },
      {
        "topic": "Body Systems: Respiratory",
        "pct": 6
      },
      {
        "topic": "Body Systems: Digestive",
        "pct": 10
      },
      {
        "topic": "Body Systems: Endocrine",
        "pct": 6
      },
      {
        "topic": "Body Systems: Nervous & Senses",
        "pct": 8
      },
      {
        "topic": "Body Systems: Reproductive",
        "pct": 4
      },
      {
        "topic": "Body Systems: Urinary",
        "pct": 4
      },
      {
        "topic": "Body Systems: Mental Disorders",
        "pct": 6
      },
      {
        "topic": "Patient Assessment",
        "pct": 12
      },
      {
        "topic": "Diagnosis",
        "pct": 14
      }
    ]
  },
  {
    "id": "respiratory-therapy",
    "name": "Respiratory Therapy",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "The respiratory therapy event allows individuals to gain the knowledge and skills required in respiratory therapy.. This competitive event consists of two rounds. Round One is a written, multiple-choice test and top-scoring competitors advance to Round Two for the skills assessment. This event aims to inspire HOSA members to learn more about respiratory careers, use critical thinking skills, and become allied health professionals who can respond and assist efficiently in clinical settings.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/RT-26-27-10.8.pdf",
    "books": [
      {
        "title": "Egan's Fundamentals of Respiratory Care",
        "author": "Stoller, Heuer, Chatburn, Mireles-Cabodevila & Vines",
        "publisher": "Elsevier"
      },
      {
        "title": "DHO: Health Science",
        "author": "Simmers, Simmers-Nartker, Simmers-Kobelak & Morris",
        "publisher": "Cengage Learning"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Foundations of Respiratory Care",
        "pct": 20
      },
      {
        "topic": "Applied anatomy & Physiology",
        "pct": 10
      },
      {
        "topic": "Assessment of Respiratory Disorder",
        "pct": 20
      },
      {
        "topic": "Cardiopulmonary Diseases",
        "pct": 20
      },
      {
        "topic": "Basic Therapeutics",
        "pct": 20
      },
      {
        "topic": "Patient Education and Long-Term Care",
        "pct": 10
      }
    ]
  },
  {
    "id": "sports-medicine",
    "name": "Sports Medicine",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Sports Medicine provides members with the opportunity to gain the knowledge and skills required for patient care in a sports medicine setting. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors advance to Round Two for the skills assessment. This event aims to inspire members to learn more about injury prevention, therapeutic intervention, and immediate care.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/SM-26-27-FINAL.pdf",
    "books": [
      {
        "title": "Orthopedic Taping, Wrapping, Bracing, and Padding",
        "author": "Beam",
        "publisher": "F.A. Davis"
      },
      {
        "title": "Introduction to Sports Medicine and Athletic Training",
        "author": "France",
        "publisher": "Cengage"
      },
      {
        "title": "The Role of the Athletic Trainer in Sports Medicine",
        "author": "Prentice",
        "publisher": "McGraw Hill"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Injury / Illness Prevention and Wellness Promotion",
        "pct": 30
      },
      {
        "topic": "Examination, Evaluation, and Assessment",
        "pct": 30
      },
      {
        "topic": "Immediate and Emergency Care",
        "pct": 16
      },
      {
        "topic": "Therapeutic Intervention",
        "pct": 16
      },
      {
        "topic": "Healthcare Administration and Professional Responsibilities",
        "pct": 8
      }
    ]
  },
  {
    "id": "surgical-technologist",
    "name": "Surgical Technologist",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "The Surgical Technologist event allows members to gain essential knowledge and skills required for the field of Surgical Technology. This competitive event consists of two rounds. Competitors will take a written test for Round One. Top-scoring competitors will advance to Round Two for a clinical skills assessment. This event aims to inspire members to learn more about Surgical Technologist careers, enhance critical thinking skills, and prepare to become allied health professionals capable of effectively assisting in surgical settings.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/ST-26-27-FINAL-1-1.pdf",
    "books": [
      {
        "title": "Surgical Technology for the Surgical Technologist: A Positive Care Approach",
        "author": "Association of Surgical Technologists",
        "publisher": "Cengage Learning",
        "note": "Round One test focuses on chapters 1, 4, 7, 10, 11 and 16"
      },
      {
        "title": "Surgical Instrumentation: An Interactive Approach",
        "author": "Nemitz",
        "publisher": "Saunders"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Profession of CST",
        "pct": 10
      },
      {
        "topic": "Physical Environment and Safety Standards",
        "pct": 10
      },
      {
        "topic": "Surgical Asepsis and Sterility",
        "pct": 20
      },
      {
        "topic": "Instrumentation, Equipment, and Supplies",
        "pct": 30
      },
      {
        "topic": "Hemostasis, Wound Healing, and Wound Closure",
        "pct": 10
      },
      {
        "topic": "Surgical Anatomy & Physiology",
        "pct": 20
      }
    ]
  },
  {
    "id": "veterinary-science",
    "name": "Veterinary Science",
    "category": "health-professions",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Veterinary Science allows members to gain the knowledge and skills required for diagnosing and treating animals. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors advance to Round Two for the skills assessment. This event aims to inspire members to learn more about the field of veterinary care.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/11/VS-26-27-Nov-8.pdf",
    "books": [
      {
        "title": "Introduction to Veterinary Science",
        "author": "Lawhead & Baker",
        "publisher": "Cengage Learning"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Anatomy and Physiology",
        "pct": 24
      },
      {
        "topic": "Basic Nutrients",
        "pct": 10
      },
      {
        "topic": "Animal Behavior",
        "pct": 6
      },
      {
        "topic": "Diseases/Disease Prevention",
        "pct": 14
      },
      {
        "topic": "Zoonoses",
        "pct": 6
      },
      {
        "topic": "Clinical Practice",
        "pct": 10
      },
      {
        "topic": "Emergency Care/First Aid",
        "pct": 12
      },
      {
        "topic": "Principles of Surgery",
        "pct": 12
      },
      {
        "topic": "Ethical, Legal, and Safety",
        "pct": 6
      }
    ]
  },
  {
    "id": "cert-skills",
    "name": "CERT Skills",
    "category": "emergency-preparedness",
    "format": "50-question test (60 min)",
    "team": "Team of 2",
    "hasTest": true,
    "summary": "CERT Skills allows members to gain knowledge and skills required for disaster preparedness and response. This competitive event consists of two rounds, and each team consists of two (2) people. Round One is a written, 50 multiple-choice question test, and the top-scoring teams will advance to Round Two for the skills assessment. This event aims to inspire members to be proactive future health professionals who respond efficiently to complex community hazards in the absence of emergency services.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/CERT-26-27-FINAL-1.pdf",
    "books": [
      {
        "title": "CERT Basic Training (IS-317)",
        "author": "FEMA",
        "note": "Online course"
      },
      {
        "title": "CERT Basic Training Participant Manual",
        "author": "FEMA"
      },
      {
        "title": "First Aid for Severe Trauma (FAST)",
        "author": "American Red Cross"
      },
      {
        "title": "SALT Mass Casualty Triage",
        "author": "National Disaster Life Support Foundation",
        "note": "Online course"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Disaster Preparedness",
        "pct": 15
      },
      {
        "topic": "CERT Organization",
        "pct": 5
      },
      {
        "topic": "Life Threatening Interventions and SALT Triage",
        "pct": 30
      },
      {
        "topic": "Medical Operations",
        "pct": 20
      },
      {
        "topic": "Disaster Psychology",
        "pct": 5
      },
      {
        "topic": "Fire Safety",
        "pct": 5
      },
      {
        "topic": "Light Search and Rescue Operations",
        "pct": 15
      },
      {
        "topic": "Terrorism",
        "pct": 5
      }
    ]
  },
  {
    "id": "cpr-first-aid",
    "name": "CPR/First Aid",
    "category": "emergency-preparedness",
    "format": "50-question test (60 min)",
    "team": "Team of 2",
    "hasTest": true,
    "summary": "CPR/First Aid enables members to acquire essential skills and knowledge required for team-based first aid and basic life support. This competitive event consists of two rounds, with each team comprising two people. Round One is a written exam with 50 multiple-choice questions, and teams with the highest scores proceed to Round Two, which involves a skills assessment. The goal of this event is to encourage members to become proactive future health professionals who are capable of administering life-saving measures.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/CPR_FA-26-27-FINAL-update.pdf",
    "books": [
      {
        "title": "Basic Life Support",
        "author": "American Red Cross"
      },
      {
        "title": "First Aid/CPR/AED",
        "author": "American Red Cross"
      },
      {
        "title": "Basic Life Support",
        "author": "American Heart Association"
      },
      {
        "title": "Heartsaver First Aid",
        "author": "American Heart Association"
      },
      {
        "title": "DHO: Health Science",
        "author": "Simmers, Simmers-Nartker, Simmers-Kobelak & Morris",
        "publisher": "Cengage Learning"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Basic Life Support",
        "pct": 40,
        "sub": [
          "General Concepts",
          "BLS/CPR for Adults, Children and Infants",
          "AED for Adults, Children and Infants",
          "CPR with Advanced Airway",
          "Mouth-to-Mouth/Rescue Breathing",
          "Relief of Choking"
        ]
      },
      {
        "topic": "First Aid",
        "pct": 60,
        "sub": [
          "Basic",
          "Medical Emergencies",
          "Injury Emergencies",
          "Environmental Emergencies"
        ]
      }
    ]
  },
  {
    "id": "emergency-medical-technician",
    "name": "Emergency Medical Technician",
    "category": "emergency-preparedness",
    "format": "50-question test (60 min)",
    "team": "Team of 2",
    "hasTest": true,
    "summary": "Emergency Medical Technician allows HOSA members to gain the knowledge and skills required for emergency medical care. This competitive event consists of two rounds, and each team consists of two (2) people. Round One is a written, 50-question multiple-choice test, and the top-scoring teams will advance to Round Two for the skills assessment. The primary goal of this event is to motivate members to pursue careers as proactive healthcare professionals, equipping them with resilience, physical strength, and adept problem-solving abilities necessary for delivering immediate emergency care.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/EMT-26-27-Update.pdf",
    "books": [
      {
        "title": "Emergency Care and Transportation of the Sick and Injured",
        "author": "Pollak (series ed.)",
        "publisher": "Jones & Bartlett Learning"
      },
      {
        "title": "BLS Provider Manual",
        "author": "American Heart Association"
      },
      {
        "title": "Emergency Care",
        "author": "Limmer & O'Keefe",
        "publisher": "Brady / Prentice Hall"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Patient Assessment",
        "pct": 20
      },
      {
        "topic": "Basic Life Support",
        "pct": 20
      },
      {
        "topic": "Trauma",
        "pct": 16
      },
      {
        "topic": "Medical Emergencies",
        "pct": 14
      },
      {
        "topic": "Pediatrics and Childbirth",
        "pct": 16
      },
      {
        "topic": "Environmental Emergencies",
        "pct": 10
      },
      {
        "topic": "Special Situations",
        "pct": 4
      }
    ]
  },
  {
    "id": "epidemiology",
    "name": "Epidemiology",
    "category": "emergency-preparedness",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Epidemiology allows members to gain knowledge about health and disease in populations. This competitive event consists of a written exam of concepts related to the study of epidemiology. In the event of a tie, the essay will be judged to break the tie. Competitors must recognize, identify, define, interpret, and apply these concepts in a multiple-choice test. The event aims to motivate members to become proactive future health professionals, enhancing their scientific literacy and offering valuable insights into careers in public health.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/EPI-26-27-9.29.pdf",
    "books": [
      {
        "title": "PH 101 Series",
        "author": "CDC",
        "note": "Online course"
      },
      {
        "title": "ActivEpi",
        "note": "Online course"
      },
      {
        "title": "Morbidity and Mortality Weekly Report (MMWR)",
        "author": "CDC",
        "note": "Online reports"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Introduction to Epidemiology",
        "pct": 30,
        "sub": [
          "Basic concept",
          "Types of case studies",
          "Measuring health and disease",
          "Causation",
          "Surveillance"
        ]
      },
      {
        "topic": "World and Government Response to Infectious Diseases",
        "pct": 20,
        "sub": [
          "WHO Infectious Diseases",
          "CDC Activities",
          "Government Responses"
        ]
      },
      {
        "topic": "CDC: Morbidity and Mortality Weekly Report",
        "pct": 50,
        "sub": [
          "Case studies, investigations, surveillance summaries, scientific information recommendations"
        ]
      }
    ]
  },
  {
    "id": "life-support-skills",
    "name": "Life Support Skills",
    "category": "emergency-preparedness",
    "format": "Skill Assessment",
    "team": "Individual",
    "hasTest": false,
    "summary": "Life Support Skills allows HOSA members to gain knowledge and skills required for basic life support. This competitive event consists of evaluating members' performance through a skills assessment. This event aims to inspire members to be proactive future health professionals and be equipped with the skills to provide immediate, life-saving actions in the absence of emergency services. This event is specifically for HOSA members who are classified under IDEA.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/LSS-26-27-Update-9.30.pdf",
    "books": [
      {
        "title": "Basic Life Support",
        "author": "American Red Cross"
      },
      {
        "title": "First Aid/CPR/AED",
        "author": "American Red Cross"
      },
      {
        "title": "BLS Provider Manual",
        "author": "American Heart Association"
      },
      {
        "title": "Heartsaver First Aid",
        "author": "American Heart Association"
      },
      {
        "title": "DHO: Health Science",
        "author": "Simmers, Simmers-Nartker, Simmers-Kobelak & Morris",
        "publisher": "Cengage Learning"
      }
    ]
  },
  {
    "id": "mental-health-promotion",
    "name": "Mental Health Promotion",
    "category": "emergency-preparedness",
    "format": "Social media campaign",
    "team": "Team of 2–6",
    "hasTest": false,
    "summary": "The Mental Health Promotion event provides HOSA members with an introduction to mental health topics with a grounding in prevention. The event is built on the understanding that “mental health IS health” and that we must think about taking car e of our mental health just as we do our physical health. This competitive event consists of a team of 2 to 6 members. Teams will create and publish a social media campaign for their peers centered on building and promoting protective factors around a selected mental health topic. This social media campaign will be pre-judged digitally prior to ILC. Teams will present their social media campaign and process to a panel of judges at ILC. This event aims to provide information on how to support someone struggling with their mental health and to inspire future health professionals to promote the importance of mental health in their schools and communities.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/MHP-26-27-Update-Oct-2026.pdf",
    "books": []
  },
  {
    "id": "mrc-partnership",
    "name": "MRC Partnership",
    "category": "emergency-preparedness",
    "format": "Portfolio",
    "team": "Team of 2–6",
    "hasTest": false,
    "summary": "MRC Partnership provides members with the opportunity to gain knowledge and skills required to initiate and maintain a partnership with their local/state Medical Reserve Corps units. This competitive event is designed for students to demonstrate the spirit and mission of both the MRC and HOSA in joint partnership activities. Each team consists of 2 to 6 competitors and teams will prepare a portfolio highlighting partnership activities that improve public health, increase emergency response capabilities, and strengthen the resiliency of local communities. This event aims to inspire members to engage with the Medical Reserve Corps and to learn more about community-based groups committed to strengthening public health.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/MRC-26-27.pdf",
    "books": []
  },
  {
    "id": "public-health",
    "name": "Public Health",
    "category": "emergency-preparedness",
    "format": "Trailer video, then presentation",
    "team": "Team of 2–6",
    "hasTest": false,
    "summary": "Public Health allows HOSA members to develop an effective, dynamic, and creative presentation informing the public about a significant public health issue. The team consists of 2-6 members. The event consists of two rounds. In Round One, the team creates a video “trailer” of their presentation with the goal of convincing a panel of judges of the need to view their full Round Two presentation. The video trailer should “wow” the judges. The highest-scoring teams will advance to Round Two, where a panel of judges will view the entire in-person presentation. The panel of judges for each round may be different, so bring your “A” game to both rounds.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/PH-26-27-9.5-FINAL.pdf",
    "books": []
  },
  {
    "id": "extemporaneous-writing-health-policy",
    "name": "Extemporaneous Writing – Health Policy",
    "category": "leadership",
    "format": "Written policy letter (60 min)",
    "team": "Individual",
    "hasTest": false,
    "summary": "Extemporaneous Writing—Health Policy allows HOSA members to gain the knowledge and skills to write an effective letter to a policymaker. On the day of the competition, competitors will receive a secret topic that outlines a relevant health policy or issue with supporting details. Competitors will draft their letters in 60 minutes to submit to judges. This event aims to inspire members to learn more about current health policy and feel empowered to make a difference by voicing their opinions on important health topics to applicable decision-makers to effect change.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/EWHP-26-27-FINAL-1.pdf",
    "books": []
  },
  {
    "id": "health-career-photography",
    "name": "Health Career Photography",
    "category": "leadership",
    "format": "Photo portfolio",
    "team": "Individual",
    "hasTest": false,
    "summary": "Health Career Photography provides HOSA members with the opportunity to gain knowledge about different health careers and analyze them through the medium of digital photography. Competitors will photograph three different health professionals performing an aspect of their job, edit the photos using computer software technology as needed, provide a written description of the career, and then present their three printed pictures to a panel of judges. This event aims to inspire members to use photography as a means to explore health careers.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/HCPhoto-26-27-8.16-FINAL.pdf",
    "books": []
  },
  {
    "id": "healthy-living",
    "name": "Healthy Living",
    "category": "leadership",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "Healthy Living provides HOSA members the opportunity to gain the knowledge and skills required to understand healthy living and its impact on health throughout the lifespan. This competitive event consists of two rounds. Round One is a written, multiple-choice test, and the top-scoring competitors will advance to Round Two for a presentation. In addition, each competitor will focus on one personal healthy living goal and document their efforts in a personalized portfolio. This event aims to inspire members to learn more about health literacy topics and to develop healthy habits for a lifetime.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Healthy-Living-26-27.pdf",
    "books": [
      {
        "title": "HOSA Healthy Living Course",
        "author": "NASM",
        "note": "Online course"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Nutrition",
        "pct": 25
      },
      {
        "topic": "Physical Activity",
        "pct": 25
      },
      {
        "topic": "Mental Health",
        "pct": 10
      },
      {
        "topic": "Wellness through the Lifespan",
        "pct": 20
      },
      {
        "topic": "Disease Prevention",
        "pct": 20
      }
    ]
  },
  {
    "id": "interviewing-skills",
    "name": "Interviewing Skills",
    "category": "leadership",
    "format": "Resume upload, then interview",
    "team": "Individual",
    "hasTest": false,
    "summary": "Interviewing Skills allows HOSA members to gain the knowledge and skills required to successfully apply and interview for employment and internship opportunities (for college, medical school, professional career, etc.). This competitive event requires competitors to prepare a personal statement and resume and then participate in a mock job interview with judges. This event aims to inspire members to learn more about applying and interviewing for health-related positions and experiences. This event is specifically for HOSA members who are classified under IDEA.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Interview-Skills-26-27.pdf",
    "books": []
  },
  {
    "id": "job-seeking-skills",
    "name": "Job Seeking Skills",
    "category": "leadership",
    "format": "Resume upload, then interview",
    "team": "Individual",
    "hasTest": false,
    "summary": "Job Seeking Skills allows HOSA members to gain the knowledge and skills required to apply and interview for employment and internship opportunities (for college, medical school, professional career, etc.). This competitive event requires competitors to prepare a personal statement and resume and then participate in a mock job interview with judges. This event aims to inspire members to learn more about applying and interviewing for health-related positions and experiences.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Job-Seeking-26-27.pdf",
    "books": []
  },
  {
    "id": "organizational-leadership",
    "name": "Organizational Leadership",
    "category": "leadership",
    "format": "50-question test (60 min)",
    "team": "Individual",
    "hasTest": true,
    "summary": "The purpose of the event is two-fold: 1) To assist Chartered Associations with selecting their Voting Delegates if a method does not already exist and 2) To encourage HOSA members to develop and apply their knowledge of the HOSA organization and Parliamentary Procedure to represent their Chartered Associations at the International Leadership Conference as an official Voting Delegate.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Org.-Leadership-26-27.pdf",
    "books": [
      {
        "title": "HOSA Handbook (Sections A, B and C)",
        "author": "HOSA"
      },
      {
        "title": "Robert's Rules of Order Newly Revised In Brief"
      },
      {
        "title": "First Fifty Years 1976–2026",
        "author": "HOSA"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Voting Delegate Role and Responsibilities",
        "pct": 24
      },
      {
        "topic": "Parliamentary Procedure",
        "pct": 24
      },
      {
        "topic": "HOSA Inc.",
        "pct": 16
      },
      {
        "topic": "Organizational Structure of HOSA",
        "pct": 12
      },
      {
        "topic": "History of HOSA",
        "pct": 12
      },
      {
        "topic": "Positions and Responsibilities of the Executive Council",
        "pct": 8
      },
      {
        "topic": "Membership",
        "pct": 4
      }
    ]
  },
  {
    "id": "prepared-speaking",
    "name": "Prepared Speaking",
    "category": "leadership",
    "format": "5-minute speech",
    "team": "Individual",
    "hasTest": false,
    "summary": "Prepared Speaking allows HOSA members to improve their knowledge and skills surrounding effective oral communication. This competitive event requires competitors to develop a speech about a selected national topic. The topic for the year aligns with the HOSA membership theme, which is announced at the conclusion of the previous annual International Leadership Conference.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Prepared-Speaking-26-27.pdf",
    "books": []
  },
  {
    "id": "researched-persuasive-writing-speaking",
    "name": "Researched Persuasive Writing and Speaking",
    "category": "leadership",
    "format": "Research paper, then speech",
    "team": "Individual",
    "hasTest": false,
    "summary": "Researched Persuasive Writing and Speaking allows HOSA members to gain the knowledge and skills required to research a health issue, prepare written documentation supporting a thesis, and present information orally. This competitive event requires competitors to develop a speech and written paper, either for or against the provided annual health topic.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/RPWS-26-27.pdf",
    "books": []
  },
  {
    "id": "speaking-skills",
    "name": "Speaking Skills",
    "category": "leadership",
    "format": "5-minute speech",
    "team": "Individual",
    "hasTest": false,
    "summary": "Speaking Skills allows HOSA members to improve their knowledge and skills surrounding effective oral communication. This competitive event requires competitors to develop a speech about a selected national topic. The topic for the year aligns to the HOSA membership theme, which is announced at the conclusion of the International Leadership Conference every year. This event is specifically for HOSA members classified under IDEA.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Speaking-Skills-26-27.pdf",
    "books": []
  },
  {
    "id": "biomedical-debate",
    "name": "Biomedical Debate",
    "category": "teamwork",
    "format": "50-question test (60 min)",
    "team": "Team of 3–4",
    "hasTest": true,
    "summary": "Biomedical Debate allows members to use debate as a platform for researching the pros and cons of a biomedical issue and showcasing what has been learned. This competitive event consists of two rounds, and each team consists of 3-4 people. Round One is a written test containing questions about the annual biomedical topic. The teams with the highest average score from the test will qualify for the Round Two debate(s). This event aims to inspire members to be proactive future healt h professionals by researching a given health topic, evaluating, discussing, and thinking critically about the issue, and refining verbal communication skills surrounding a complex biomedical issue. The annual debate topic will be selected yearly and announced in HOSA publications.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/11/BD-26-27-Revised-11.2.pdf",
    "books": [
      {
        "title": "Breaking the Age Code",
        "author": "Becca Levy",
        "publisher": "William Morrow"
      },
      {
        "title": "The Ethics of Health Care Rationing",
        "author": "Bognar & Hirose",
        "publisher": "Routledge"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": []
  },
  {
    "id": "community-awareness",
    "name": "Community Awareness",
    "category": "teamwork",
    "format": "Portfolio",
    "team": "Team of 2–6",
    "hasTest": false,
    "summary": "Community Awareness provides HOSA members with the opportunity to educate their own community about one health and/or safety-related issue of local, state, and/or national interest. Teams of 2-6 members plan a local community campaign surrounding a selected topic that will impact their community as a whole. Teams develop a portfolio that documents and explains this community campaign and activities. The team presents their community campaign to a panel of judges, using the portfolio to document their accomplishments. This event aims to inspire members to be proactive future health professionals and promote local community awareness of health-related issues.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Community-Awareness-26-27.pdf",
    "books": []
  },
  {
    "id": "creative-problem-solving",
    "name": "Creative Problem Solving",
    "category": "teamwork",
    "format": "50-question test (60 min)",
    "team": "Team of 2–6",
    "hasTest": true,
    "summary": "Creative Problem Solving allows members to analyze the problem-solving process and work as a team to apply their problem-solving skills in creating a solution to a hypothetical health or HOSA-related problem. This competitive event consists of two rounds, and each team consists of 2–6 people. Round One will consist of a written test, and the score will be used to qualify the team for Round Two. In Round Two, teams will be given a potential problem related to HOSA, the health community, or a specific health issue and have 15 minutes to analyze the problem. At the end of the preparation time, teams will have 10 minutes to present their solution to a panel of judges. This event aims to inspire members to be proactive future health professionals and utilize higher order thinking to solve complex challenges.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/CPS-26-27-8.31_Final.pdf",
    "books": [
      {
        "title": "Organizational Behavior",
        "author": "McShane & Von Glinow",
        "publisher": "McGraw Hill"
      },
      {
        "title": "Decision Making & Problem Solving",
        "author": "Adair",
        "publisher": "Kogan Page"
      },
      {
        "title": "Solve It!",
        "author": "Sternad",
        "publisher": "Econcise Publishing"
      },
      {
        "title": "Critical Thinking & Logic Mastery (3 Books in 1)",
        "author": "Thinknetic"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Critical & Effective Thinking",
        "pct": 26
      },
      {
        "topic": "Problem Solving Strategies & Skills",
        "pct": 24
      },
      {
        "topic": "Clarification of Problems & Generating Ideas",
        "pct": 10
      },
      {
        "topic": "Examining Constraints/Developing Alternatives",
        "pct": 20
      },
      {
        "topic": "Components of Logic",
        "pct": 20
      }
    ]
  },
  {
    "id": "forensic-science",
    "name": "Forensic Science",
    "category": "teamwork",
    "format": "50-question test (60 min)",
    "team": "Team of 2",
    "hasTest": true,
    "summary": "Forensic Science allows HOSA members to work as a team to apply their knowledge and skills in creating a solution to a forensic science-related problem. This competitive event consists of two rounds, and each team consists of two (2) people. Round One is a written test that evaluates the team’s understanding of forensic science. The test score from Round One will be used to qualify the team for Round Two. In Round Two, teams will be given a case study to analyze, including physical evidence and written information such as police reports and an autopsy. Teams may have time to view a “crime scene” and/or review resources to write their conclusions with supporting evidence. This event aims to inspire members to be proactive future health professionals and critically examine elements of a forensic case.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Forensic-Science-26-27.pdf",
    "books": [
      {
        "title": "Forensic Science Fundamentals",
        "author": "Bertino & Bertino",
        "publisher": "National Geographic Learning / Cengage"
      },
      {
        "title": "Forensic Science",
        "author": "Bell",
        "publisher": "CRC Press"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Forensic History and Careers",
        "pct": 10
      },
      {
        "topic": "Crime Scene and Death Investigation",
        "pct": 20
      },
      {
        "topic": "Forensic Toxicology and Pharmacology",
        "pct": 20
      },
      {
        "topic": "Forensic Anthropology",
        "pct": 10
      },
      {
        "topic": "Forensic Entomology",
        "pct": 10
      },
      {
        "topic": "Identification of Blood, Bloodstains, Biological Fluids and Stains",
        "pct": 10
      },
      {
        "topic": "Techniques of DNA Analysis",
        "pct": 10
      },
      {
        "topic": "Forensic Psychology and Psychiatry",
        "pct": 10
      }
    ]
  },
  {
    "id": "health-career-display",
    "name": "Health Career Display",
    "category": "teamwork",
    "format": "Career display",
    "team": "Team of 2",
    "hasTest": false,
    "summary": "Health Career Display allows members to research a career of interest, create a display board of associated career materials, and improve their presentation skills by communicating the career information to others. This competitive event consists of two rounds, and each team consists of two people. Round One is judging the plan/outline for the Health Career Display board. The top-scoring teams will advance to Round Two for the presentation. This event aims to inspire members to become future health professionals by exciting them about a career of their choosing.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Health-Career-Display-26-27.pdf",
    "books": []
  },
  {
    "id": "health-education",
    "name": "Health Education",
    "category": "teamwork",
    "format": "Portfolio",
    "team": "Team of 2–6",
    "hasTest": false,
    "summary": "Health Education provides members with the opportunity to gain knowledge and skills required to select a health-related concept or instructional objective, then prepare a lesson for a targeted group of learners, provide instruction, and evaluate results. This competitive event consists of a portfolio and presentation to judges and each team consists of 2-6 members. This event aims to inspire members to be proactive future health professionals by educating others on health-related concepts.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/11/HE-26-27-FINAL.pdf",
    "books": []
  },
  {
    "id": "hosa-bowl",
    "name": "HOSA Bowl",
    "category": "teamwork",
    "format": "50-question test (60 min)",
    "team": "Team of 4",
    "hasTest": true,
    "summary": "HOSA Bowl allows members to gain knowledge and skills on various topics and situations in health, current health topics, HOSA, and parliamentary procedure. This competitive event consists of two rounds, and each team consists of exactly four (4) members. Round One is a written test. Top-scoring teams advance to Round Two and compete by responding appropriately to items presented by a moderator in a “buzzer style” round. These items may be in the form of questions, incomplete statements, and/or definitions and may be multi-answer items. Winners will be determined by a series of elimination rounds as described in the event tournament bracket. This event aims to inspire members to be proactive future health professionals and motivate them to participate in teams while learning about health, HOSA, current health topics, and parliamentary procedure topics.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/HOSA-Bowl-26-27.pdf",
    "books": [
      {
        "title": "DHO: Health Science",
        "author": "Simmers, Simmers-Nartker, Simmers-Kobelak & Morris",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Body Structures and Functions",
        "author": "Scott & Bell",
        "publisher": "Cengage Learning"
      },
      {
        "title": "Taber's Cyclopedic Medical Dictionary",
        "author": "Venes (ed.)",
        "publisher": "F.A. Davis"
      },
      {
        "title": "Robert's Rules of Order Newly Revised In Brief"
      },
      {
        "title": "First Fifty Years 1976–2026",
        "author": "HOSA"
      },
      {
        "title": "Introduction to Medical Terminology",
        "author": "Stanhope & Turnbull",
        "publisher": "Goodheart-Willcox"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "HOSA Related Knowledge",
        "pct": 12
      },
      {
        "topic": "Parliamentary Procedure",
        "pct": 12
      },
      {
        "topic": "Anatomy and Physiology",
        "pct": 12
      },
      {
        "topic": "Medical Terminology",
        "pct": 12
      },
      {
        "topic": "Current Health Topics",
        "pct": 12
      },
      {
        "topic": "Other: History of Medicine, Healthcare Systems, Health Careers, Legal and Ethical Practices, Nutrition, Safety, Infection Control, Math Conversions",
        "pct": 40
      }
    ]
  },
  {
    "id": "medical-innovation",
    "name": "Medical Innovation",
    "category": "teamwork",
    "format": "Innovation outline, then presentation",
    "team": "Team of 2–4",
    "hasTest": false,
    "summary": "Medical Innovation provides HOSA members with the opportunity to gain knowledge and skills required to impact the future of health and/or the delivery of healthcare through the development of a new medical innovation.This competitive event consists of two rounds, and each team consists of 2-4 people. In Round One, judges will evaluate the medical innovation plan/ outline and the top scoring teams will advance to Round Two the oral presentation. This event aims to inspire members to be proactive future health professionals by sharing their unique medical innovation and outcomes with others.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/09/MI-26-27-9.25.pdf",
    "books": []
  },
  {
    "id": "parliamentary-procedure",
    "name": "Parliamentary Procedure",
    "category": "teamwork",
    "format": "50-question test (60 min)",
    "team": "Team of 5–8",
    "hasTest": true,
    "summary": "Parliamentary Procedure allows HOSA members to gain the knowledge and skills required to conduct a simulated business meeting by using parliamentary procedure. This competitive event consists of two rounds. Teams shall be composed of five (5) to eight (8) members with identified offices or representatives thereof (i.e., president, treasurer, committee chairman, member, etc.). Round One is a written test, and the top-scoring teams will advance to Round Two to conduct a demonstration meeting on a secret topic. The demonstrated meeting should show the participant’s knowledge of parliamentary procedure and should follow the agenda given. The secret topic will include four subsidiary and privileged motions commonly used during a business meeting. This event aims to inspire members to be proactive future health professionals by learning the importance of cooperation, fair decision-making, and competitive performance.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Parli-Pro-26-27.pdf",
    "books": [
      {
        "title": "Robert's Rules of Order Newly Revised",
        "publisher": "Da Capo Press"
      },
      {
        "title": "Robert's Rules of Order Newly Revised In Brief"
      },
      {
        "title": "Study Questions for NAP Membership Exam",
        "author": "National Association of Parliamentarians"
      }
    ],
    "testQuestions": 50,
    "testMinutes": 60,
    "testPlan": [
      {
        "topic": "Why Have Rules",
        "pct": null
      },
      {
        "topic": "What Happens at a Meeting?",
        "pct": null
      },
      {
        "topic": "Handling Motions",
        "pct": null
      },
      {
        "topic": "Debate",
        "pct": null
      },
      {
        "topic": "Amendments",
        "pct": null
      },
      {
        "topic": "Postponing and Referring to a Committee",
        "pct": null
      },
      {
        "topic": "How a group Can Change Its Mind",
        "pct": null
      },
      {
        "topic": "Voting and Elections",
        "pct": null
      },
      {
        "topic": "Bylaws and Other Rules and How to Use Them",
        "pct": null
      },
      {
        "topic": "How Rules are Enforced and Suspended",
        "pct": null
      },
      {
        "topic": "Table of Rules",
        "pct": null
      },
      {
        "topic": "Officers, Committee Chairman, or Member",
        "pct": null
      }
    ]
  },
  {
    "id": "public-service-announcement",
    "name": "Public Service Announcement",
    "category": "teamwork",
    "format": "PSA video",
    "team": "Team of 2–6",
    "hasTest": false,
    "summary": "Public Service Announcement (PSA) allows members to use technology to produce a video public service announcement informing the community about a significant health issue. This competitive event consists of two rounds, and each team consists of 2-6 people. All teams will show their PSA to a panel of judges and give a presentation about their creative process. This event aims to inspire members to be proactive future health professionals by producing a PSA to promote a health service organization, bring awareness to a health situation, or educate the public at large regarding health and well-being.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/10/PSA-26-27-10.6.pdf",
    "books": []
  },
  {
    "id": "research-poster",
    "name": "Research Poster",
    "category": "teamwork",
    "format": "Research poster",
    "team": "Team of 2–4",
    "hasTest": false,
    "summary": "Research Poster allows HOSA members to think critically about a health-related issue in their community, pose a research question surrounding the chosen topic, and conduct their own research on that topic. Each team will consist of 2-4 members, and they will develop a poster showcasing their findings. Round One will be an upload of their research poster which will be pre-judged virtually. The top teams from Round One will advance to Round Two where they will present their research to a panel of judges. Teams will be required to display their posters at ILC.",
    "guideline": "https://hosa.org/wp-content/uploads/2026/08/Research-Poster-26-27.pdf",
    "books": []
  }
];
