# Pagliarulo - Introduction to Physical Therapy (Elsevier).
# Chapter list: 7th edition, from the publisher's table of contents (us.elsevierhealth.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "The Profession of Physical Therapy: Definition and Development", "Physical therapy helps people improve movement, reduce pain, and restore function. The profession grew from 'reconstruction aides' during World War I and expanded with the polio epidemics and later wars. Today physical therapists earn the Doctor of Physical Therapy (DPT) degree. The APTA's vision is to transform society by optimizing movement.", ["Reconstruction aides (WWI)", "Polio epidemics expanded PT", "DPT is entry-level degree", "Focus on movement"]),
    ch(2, "Characteristics and Roles of Physical Therapists", "Physical therapists examine, evaluate, diagnose, give a prognosis, and intervene (the patient/client management model). They work in hospitals, outpatient clinics, schools, home health, sports, and skilled nursing facilities. Many states allow direct access, letting patients see a PT without a physician referral. PTs follow the APTA Code of Ethics.", ["Examination → evaluation → diagnosis → prognosis → intervention", "Direct access", "Many practice settings", "Code of Ethics"]),
    ch(3, "The Physical Therapist Assistant", "Physical therapist assistants (PTAs) earn an associate degree from a CAPTE-accredited program and pass a licensing exam. PTAs carry out interventions under PT supervision but don't perform initial evaluations, change the plan of care independently, or discharge patients. Aides are unlicensed and do support tasks.", ["PTA: associate degree", "Works under PT supervision", "No initial evaluations", "CAPTE accredits programs"]),
    ch(4, "American Physical Therapy Association", "The APTA is the professional association for PTs, PTAs, and students. It develops the Code of Ethics, Standards of Practice, and Guide to Physical Therapist Practice, advocates for the profession, and supports research and specialist certification through ABPTS.", ["APTA = professional association", "Guide to PT Practice", "Advocacy", "ABPTS specialist certification"]),
    ch(5, "Laws, Regulations, and Policies", "State practice acts define PT scope of practice and licensure. Federal laws affecting PT include HIPAA (privacy), the ADA, IDEA (school-based therapy for children with disabilities), and Medicare rules. Documentation must meet legal requirements.", ["State practice acts", "HIPAA", "IDEA for school PT", "Medicare rules"]),
    ch(6, "Financing Health Care and Reimbursement (Payment) in Physical Therapist Practice", "PT services are paid by private insurance, Medicare (federal; age 65+), Medicaid (state-federal; low income), workers' compensation, and self-pay. Payment models include fee-for-service, managed care, and value-based payment. Accurate coding (CPT) and documentation support payment.", ["Medicare 65+", "Medicaid low income", "Workers' compensation", "Value-based payment"]),
    ch(7, "Effective Communication for Physical Therapists in the 21st Century", "Good communication includes active listening, cultural competence, health literacy, and clear documentation (often in SOAP format: subjective, objective, assessment, plan). PTs also communicate with the health care team and use telehealth.", ["SOAP notes", "Cultural competence", "Health literacy", "Active listening"]),
    ch(8, "Prevention, Health Promotion, and Wellness in Physical Therapist Practice", "PTs promote health through primary prevention (preventing disease), secondary prevention (early detection), and tertiary prevention (reducing disability). Physical activity guidelines recommend 150 minutes of moderate activity per week for adults. Fall prevention and screening are key roles.", ["Primary, secondary, tertiary prevention", "150 min/week activity", "Fall prevention", "Wellness screening"]),
    ch(9, "Physical Therapy for Musculoskeletal Conditions", "Musculoskeletal PT treats fractures, sprains, strains, arthritis, back pain, and post-surgical conditions such as joint replacements and ACL reconstruction. Interventions include therapeutic exercise, manual therapy, modalities, and patient education. Goals focus on pain, range of motion, strength, and function.", ["Therapeutic exercise", "Manual therapy", "Post-op rehab", "ROM and strength"]),
    ch(10, "Physical Therapy for Neuromuscular Conditions", "Neurologic PT treats stroke, spinal cord injury, traumatic brain injury, Parkinson disease, multiple sclerosis, and cerebral palsy. Treatment focuses on balance, gait training, motor control, and neuroplasticity—the brain's ability to reorganize.", ["Stroke rehab", "Neuroplasticity", "Balance and gait", "Spinal cord injury"]),
    ch(11, "Physical Therapy in Cardiovascular and Pulmonary Conditions", "Cardiopulmonary PT helps patients after heart attack, heart surgery, COPD, and other conditions. Cardiac rehabilitation and pulmonary rehabilitation improve endurance. PTs monitor heart rate, blood pressure, SpO2, and perceived exertion (Borg scale) during exercise.", ["Cardiac rehab", "Pulmonary rehab", "Monitor vital signs", "Borg scale"]),
    ch(12, "Physical Therapy for Integumentary Conditions", "Integumentary PT manages wounds, burns, and pressure injuries. Treatment includes wound cleaning, debridement, dressings, positioning to prevent contractures, and pressure relief. Pressure injuries are staged by depth.", ["Wound care", "Debridement", "Burn contracture prevention", "Pressure injury staging"]),
    ch(13, "Physical Therapy for Pediatric Conditions", "Pediatric PT helps children with developmental delays, cerebral palsy, Down syndrome, spina bifida, and torticollis. Therapy uses play and family-centered care and may occur in early intervention (birth–3) or schools under IDEA.", ["Developmental milestones", "Family-centered care", "Early intervention birth–3", "IDEA in schools"]),
    ch(14, "Physical Therapy for the Older Adult", "Geriatric PT addresses aging changes, falls, osteoporosis, arthritis, joint replacements, and dementia. Goals include maintaining independence and safety. Balance tests (such as the Berg Balance Scale and Timed Up and Go) assess fall risk.", ["Fall prevention", "Berg Balance Scale", "Timed Up and Go", "Maintain independence"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Early physical therapists in World War I were called:", "Reconstruction aides", ["Nurse assistants", "Orderlies", "Medics"], "They rehabilitated wounded soldiers."),
        (1, "The entry-level degree for physical therapists is the:", "DPT", ["Associate degree", "Bachelor's degree", "PhD only"], "Doctor of Physical Therapy."),
        (1, "Which epidemic greatly expanded physical therapy?", "Polio", ["Influenza", "Measles", "Smallpox"], "Many needed rehabilitation."),
        (2, "Seeing a PT without a physician referral is:", "Direct access", ["Managed care", "Telehealth", "Referral access"], "Allowed in all states with some limits."),
        (2, "The first step in patient/client management is:", "Examination", ["Intervention", "Discharge", "Prognosis"], "Then evaluation, diagnosis, prognosis, intervention."),
        (2, "Predicting the level of improvement is the:", "Prognosis", ["Diagnosis", "Evaluation", "Intervention"], "Includes expected time frame."),
        (3, "A physical therapist assistant may NOT:", "Perform the initial evaluation", ["Provide interventions", "Document treatment", "Teach exercises"], "Only the PT evaluates."),
        (3, "PTA programs are accredited by:", "CAPTE", ["APTA", "NBCOT", "ABPTS"], "Commission on Accreditation in Physical Therapy Education."),
        (3, "PTAs usually hold a(n):", "Associate degree", ["Doctorate", "Master's degree", "No degree"], "Plus a license."),
    ]),
    ((4, 5, 6), [
        (4, "The professional association for PTs is the:", "APTA", ["AOTA", "AMA", "ANA"], "American Physical Therapy Association."),
        (4, "Board certification for PT specialists is given by:", "ABPTS", ["CAPTE", "NBRC", "APTA House of Delegates"], "American Board of Physical Therapy Specialties."),
        (4, "The APTA document describing PT practice is the:", "Guide to Physical Therapist Practice", ["DSM", "ICD", "CPT manual"], "Defines practice patterns."),
        (5, "A PT's scope of practice is defined by the:", "State practice act", ["APTA", "Hospital", "Insurance company"], "Licensing laws."),
        (5, "Physical therapy in schools is required by:", "IDEA", ["HIPAA", "EMTALA", "OSHA"], "Individuals with Disabilities Education Act."),
        (5, "Patient privacy is protected by:", "HIPAA", ["IDEA", "ADA", "Medicare"], "Health information privacy."),
        (6, "Medicare mainly covers people:", "Age 65 and older", ["With low income only", "Under 18", "Injured at work"], "Also some people with disabilities."),
        (6, "Injuries on the job are usually paid by:", "Workers' compensation", ["Medicare", "Medicaid", "Self-pay"], "Employer insurance."),
        (6, "Payment based on outcomes and quality is:", "Value-based payment", ["Fee-for-service", "Self-pay", "Capitation only"], "Rewards results."),
    ]),
    ((7, 8, 9), [
        (7, "In a SOAP note, 'O' stands for:", "Objective", ["Observation", "Outcome", "Orders"], "Measurable findings."),
        (7, "What the patient reports goes in the:", "Subjective section", ["Objective section", "Assessment", "Plan"], "Symptoms and history."),
        (7, "Understanding a patient's ability to use health information is:", "Health literacy", ["Cultural competence", "Documentation", "Diagnosis"], "Adjust teaching to it."),
        (8, "Preventing disease before it occurs is:", "Primary prevention", ["Secondary prevention", "Tertiary prevention", "Rehabilitation"], "Like exercise programs."),
        (8, "Adults should get at least how much moderate activity per week?", "150 minutes", ["30 minutes", "60 minutes", "500 minutes"], "Physical activity guidelines."),
        (8, "Reducing disability from an existing condition is:", "Tertiary prevention", ["Primary prevention", "Secondary prevention", "Screening"], "Rehab is tertiary."),
        (9, "Hands-on techniques like joint mobilization are:", "Manual therapy", ["Modalities", "Gait training", "Bracing"], "Used for musculoskeletal conditions."),
        (9, "A common post-surgical PT patient is someone after:", "Total knee replacement", ["Cataract surgery", "Dental cleaning", "Appendectomy only"], "Rehab restores motion."),
        (9, "Musculoskeletal PT goals usually include improving:", "Range of motion and strength", ["Vision", "Hearing", "Blood sugar only"], "And reducing pain."),
    ]),
    ((10, 11, 12), [
        (10, "The brain's ability to reorganize after injury is:", "Neuroplasticity", ["Atrophy", "Spasticity", "Neuropathy"], "Basis of neuro rehab."),
        (10, "A common neurologic condition treated by PTs is:", "Stroke", ["Fractured wrist", "Sprained ankle", "Tennis elbow"], "Also SCI, TBI, MS."),
        (10, "Practicing walking is:", "Gait training", ["Manual therapy", "Debridement", "Cardiac rehab"], "Often with assistive devices."),
        (11, "A scale for rating exercise effort is the:", "Borg scale", ["Glasgow scale", "Apgar scale", "Braden scale"], "Rating of perceived exertion."),
        (11, "Programs after a heart attack to build endurance are:", "Cardiac rehabilitation", ["Pulmonary rehab", "Wound care", "Gait training"], "Supervised exercise."),
        (11, "During cardiopulmonary exercise, PTs monitor:", "Heart rate, BP, and SpO2", ["Only temperature", "Only weight", "Nothing"], "Ensure safety."),
        (12, "Removing dead tissue from a wound is:", "Debridement", ["Dressing", "Grafting", "Positioning"], "Promotes healing."),
        (12, "Burn patients are positioned to prevent:", "Contractures", ["Fractures", "Infections only", "Fever"], "Tightening of skin and joints."),
        (12, "Pressure injuries are classified by:", "Stage (depth)", ["Color only", "Size only", "Location only"], "Stage 1 to 4 plus unstageable."),
    ]),
    ((13, 14), [
        (13, "Early intervention serves children from:", "Birth to age 3", ["Ages 3–5", "Ages 5–12", "Ages 13–18"], "Under IDEA Part C."),
        (13, "Pediatric therapy often uses:", "Play", ["Weight machines only", "Lectures", "Bed rest"], "Engages children."),
        (13, "Care that involves parents in decisions is:", "Family-centered care", ["Provider-centered care", "Acute care", "Managed care"], "Family is key."),
        (13, "A tight neck muscle causing head tilt in infants is:", "Torticollis", ["Scoliosis", "Spina bifida", "Clubfoot"], "Treated with stretching."),
        (14, "A balance test for fall risk is the:", "Berg Balance Scale", ["Apgar", "Glasgow Coma Scale", "Borg scale"], "Scored 0–56."),
        (14, "The Timed Up and Go test measures:", "Mobility and fall risk", ["Heart rate", "Memory", "Vision"], "Stand, walk 3 m, return, sit."),
        (14, "A main goal of geriatric PT is:", "Maintaining independence and safety", ["Building bodybuilding muscle", "Running marathons", "Avoiding all activity"], "Function matters."),
        (14, "Older adults with weak bones from osteoporosis are at risk for:", "Fractures", ["Sprains only", "Burns", "Asthma"], "Especially hip fractures."),
        (13, "Cerebral palsy affects:", "Movement and muscle tone", ["Only vision", "Only hearing", "Only digestion"], "From early brain injury."),
    ]),
]

BOOK = {
    "titles": ["Introduction to Physical Therapy"],
    "edition": "7th edition",
    "source": "Elsevier table of contents",
    "chapters": C,
    "quizzes": Q,
}
