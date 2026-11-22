# Prentice - The Role of the Athletic Trainer in Sports Medicine: An Introduction for the Secondary School Student (McGraw Hill).
# Unit list from the publisher's "Contents in Brief" (mheducation.com). Summaries are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Investigating the Field of Sports Medicine", "Sports medicine is a team approach to caring for active people. The team includes the team physician, certified athletic trainer, coach, physical therapist, and others. Athletic trainers are licensed health care professionals certified by the BOC; the NATA is their professional association.", ["Sports medicine team", "Athletic trainer role", "BOC certification", "NATA"]),
    ch(2, "Understanding the Concepts of Athletic Health Care Administration", "Administration includes designing the athletic training facility, managing budgets and supplies, keeping records (injury reports, treatment logs), pre-participation exams, and emergency action plans.", ["Facility design", "Record keeping", "Pre-participation exam", "Emergency action plan"]),
    ch(3, "Analyzing Legal, Ethical, and Insurance Considerations in Sports Medicine", "Legal concepts include negligence, standard of care, scope of practice, informed consent, and confidentiality (HIPAA/FERPA). Ethics guide professional behavior (NATA Code of Ethics). Insurance covers athletes' injuries and protects professionals.", ["Negligence", "Scope of practice", "Confidentiality", "NATA Code of Ethics"]),
    ch(4, "Understanding the Basics of Training and Conditioning Techniques for Preventing Injuries", "Conditioning prevents injury through strength, flexibility, cardiorespiratory endurance, and proper warm-up and cool-down. Principles include overload, progression, and specificity (SAID).", ["Warm-up and cool-down", "Overload and progression", "SAID principle", "Flexibility"]),
    ch(5, "Assessing Environmental Factors that Lead to Injury", "Heat illness (heat cramps, exhaustion, exertional heat stroke), cold injuries (hypothermia, frostbite), lightning safety, and air quality all affect athletes. Heat acclimatization and hydration prevent problems.", ["Heat illness", "Heat acclimatization", "Lightning safety", "Cold injuries"]),
    ch(6, "Understanding Sports Nutrition and Dietary Supplements", "Athletes need carbohydrates for fuel, protein for repair, fats, vitamins, minerals, and water. Pre-event meals and hydration matter. Many supplements are unregulated and some contain banned substances.", ["Carbohydrates fuel", "Hydration", "Pre-event meals", "Supplement risks"]),
    ch(7, "Understanding Basic Taping, Wrapping and Bracing for Injuries", "Taping, wrapping, and bracing support and protect joints. Common techniques include the ankle closed basket weave and elastic compression wraps. Check circulation after application.", ["Ankle taping", "Elastic wraps", "Braces", "Check circulation"]),
    ch(8, "Determining Appropriate Emergency Injury Management", "Emergency care starts with scene safety and the primary survey (airway, breathing, circulation). Know CPR and AED use, spinal injury management, shock care, and the emergency action plan.", ["Primary survey", "CPR and AED", "Spinal injury precautions", "Emergency action plan"]),
    ch(9, "Recognizing and Preventing the Spread of Blood Borne Pathogens and Wound Care", "Bloodborne pathogens like HIV and hepatitis B spread through blood. Universal/standard precautions, gloves, and proper disposal prevent spread. Wounds (abrasions, lacerations, punctures) are cleaned and covered.", ["Standard precautions", "Hepatitis B and HIV", "Biohazard disposal", "Wound care"]),
    ch(10, "Investigating the Psychological Aspects of Injury", "Injured athletes may experience grief, anxiety, and depression. Support, goal setting, and imagery help recovery. Watch for signs of mental health concerns and refer as needed.", ["Emotional response to injury", "Goal setting", "Imagery", "Referral"]),
    ch(11, "Introduction to Rehabilitation and Modalities", "Rehabilitation restores range of motion, strength, and function before return to play. Modalities include cryotherapy, thermotherapy, electrical stimulation, and ultrasound.", ["Rehab phases", "Cryotherapy", "Thermotherapy", "Return to play"]),
    ch(12, "Basic Pharmacology and Substance Abuse", "Athletic trainers understand common medications (NSAIDs, analgesics, inhalers) and their effects. Substance abuse includes performance-enhancing drugs (anabolic steroids), stimulants, alcohol, and recreational drugs; drug testing deters use.", ["NSAIDs", "Anabolic steroids", "Drug testing", "Substance abuse"]),
    ch(13, "Fundamental Concepts of Evaluation", "Injury evaluation uses HOPS: history, observation, palpation, and special tests, plus range of motion and strength testing. Accurate evaluation guides treatment and referral.", ["HOPS", "Range of motion", "Special tests", "Referral"]),
    ch(14, "Identifying Basic Tissue Responses and Common Injuries", "Tissue injuries include sprains (ligaments), strains (muscles/tendons), contusions, fractures, and dislocations. Healing follows inflammation, repair, and remodeling phases.", ["Sprains vs. strains", "Fractures", "Healing phases", "Inflammation"]),
    ch(15, "Anatomy of the Human Body", "Athletic trainers need knowledge of bones, muscles, joints, and anatomical terms to evaluate injuries and communicate with the sports medicine team.", ["Anatomical terms", "Major bones", "Major muscles", "Joint types"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Who usually makes the final return-to-play decision?", "The team physician", ["The coach", "The athlete", "The parent"], "Medical authority."),
        (1, "Athletic trainers are certified by the:", "BOC", ["NATA", "AMA", "OSHA"], "Board of Certification."),
        (1, "The professional association for athletic trainers is the:", "NATA", ["BOC", "APTA", "AOTA"], "National Athletic Trainers' Association."),
        (2, "A written plan for emergencies at each venue is an:", "Emergency action plan", ["Injury report", "Budget", "Treatment log"], "Rehearse it."),
        (2, "Screening athletes before the season is the:", "Pre-participation exam", ["Return-to-play test", "Drug test", "Combine"], "Medical history is key."),
        (2, "Documentation of each treatment given is a:", "Treatment log", ["Waiver", "Budget", "Schedule"], "Part of record keeping."),
        (3, "Failure to act as a reasonable professional would is:", "Negligence", ["Assault", "Libel", "Fraud"], "Breach of standard of care."),
        (3, "Student health information in schools may be protected by:", "FERPA", ["OSHA", "EMTALA", "CLIA"], "Plus HIPAA in some settings."),
        (3, "Athletic trainers' ethical standards are set by the:", "NATA Code of Ethics", ["DSM", "AMA only", "School board"], "Professional ethics."),
    ]),
    ((4, 5, 6), [
        (4, "Training should match the demands of the sport, according to the:", "SAID principle", ["RICE principle", "HOPS principle", "FITT only"], "Specific adaptation."),
        (4, "Gradually increasing training load is:", "Progression", ["Reversibility", "Specificity", "Recovery"], "Prevents overload injuries."),
        (4, "A warm-up before activity:", "Raises muscle temperature and prepares the body", ["Causes fatigue", "Replaces conditioning", "Is unnecessary"], "Prevents injury."),
        (5, "Hot skin and confusion during practice suggest:", "Exertional heat stroke", ["Heat cramps", "Hypothermia", "Dehydration only"], "Emergency: cold-water immersion."),
        (5, "Gradually adjusting to exercise in heat is:", "Heat acclimatization", ["Hydration", "Overload", "Tapering"], "Over 10–14 days."),
        (5, "Outdoor activity should stop when:", "Lightning or thunder is detected nearby", ["It's cloudy", "It's windy", "It's sunny"], "30-minute rule."),
        (6, "The main fuel for athletic performance is:", "Carbohydrates", ["Protein", "Vitamins", "Minerals"], "Stored as glycogen."),
        (6, "Protein's main role for athletes is:", "Muscle repair", ["Main energy source", "Hydration", "Vision"], "Building tissue."),
        (6, "A risk of dietary supplements is:", "Contamination with banned substances", ["Guaranteed safety", "FDA approval before sale", "No side effects"], "Loosely regulated."),
    ]),
    ((7, 8, 9), [
        (7, "A common ankle taping technique is the:", "Closed basket weave", ["Figure-8 elbow", "Spica", "Buddy tape"], "Supports against inversion."),
        (7, "After taping or wrapping, always check:", "Circulation", ["Blood sugar", "Vision", "Hearing"], "Too tight cuts off blood flow."),
        (7, "Elastic wraps are often used for:", "Compression", ["Cooling only", "Heating", "Immobilizing fractures"], "Reduce swelling."),
        (8, "The primary survey checks:", "Airway, breathing, and circulation", ["Range of motion", "Strength", "Reflexes"], "Life threats first."),
        (8, "For a suspected spinal injury, you should:", "Stabilize the head and neck and call EMS", ["Help them stand", "Remove the helmet first", "Have them walk"], "Don't move them."),
        (8, "For sudden cardiac arrest, use:", "CPR and an AED", ["Ice", "Tape", "A splint"], "Early defibrillation."),
        (9, "Hepatitis B and HIV are:", "Bloodborne pathogens", ["Airborne diseases", "Foodborne illnesses", "Genetic disorders"], "Spread through blood."),
        (9, "When handling blood, wear:", "Gloves", ["Nothing special", "Sunglasses only", "A hat"], "Standard precautions."),
        (9, "A scrape of the outer skin layer is an:", "Abrasion", ["Laceration", "Puncture", "Avulsion"], "Clean and cover."),
    ]),
    ((10, 11, 12), [
        (10, "Injured athletes commonly feel:", "Grief, frustration, or anxiety", ["Nothing", "Only relief", "Only happiness"], "Normal emotional responses."),
        (10, "Mentally rehearsing successful performance is:", "Imagery", ["Goal setting", "Relaxation only", "Taping"], "Aids recovery."),
        (10, "Signs of depression after injury should be:", "Referred to a professional", ["Ignored", "Kept secret", "Treated with medication by the AT"], "Refer appropriately."),
        (11, "Cold therapy after an acute injury helps:", "Reduce pain and swelling", ["Increase swelling", "Warm the tissue", "Loosen muscles"], "Cryotherapy."),
        (11, "Heat therapy is generally used for:", "Chronic conditions, not new injuries", ["New swollen injuries", "Bleeding", "Fractures"], "Increases blood flow."),
        (11, "Athletes return to play after regaining:", "Full motion, strength, and function", ["Only pain relief", "Only motion", "Permission from teammates"], "Functional testing."),
        (12, "Ibuprofen is a(n):", "NSAID", ["Steroid", "Opioid", "Antibiotic"], "Reduces pain and inflammation."),
        (12, "A risk of anabolic steroids is:", "Liver damage and aggression", ["Better heart health", "Weight loss only", "No risks"], "Banned in sports."),
        (12, "Drug testing in sports aims to:", "Deter performance-enhancing drug use", ["Diagnose infections", "Measure fitness", "Check blood type"], "Fair competition."),
    ]),
    ((13, 14, 15), [
        (13, "HOPS stands for history, observation, palpation, and:", "Special tests", ["Splinting", "Surgery", "Stretching"], "Injury evaluation."),
        (13, "The most important part of an injury evaluation is often the:", "History", ["Palpation", "Observation", "X-ray"], "How it happened."),
        (13, "Measuring how far a joint moves is assessing:", "Range of motion", ["Strength", "Balance", "Endurance"], "Often with a goniometer."),
        (14, "A sprain is an injury to a:", "Ligament", ["Muscle", "Tendon", "Bone"], "Strains affect muscles or tendons."),
        (14, "A bruise is a:", "Contusion", ["Fracture", "Dislocation", "Strain"], "Bleeding under the skin."),
        (14, "Healing phases are inflammation, repair, and:", "Remodeling", ["Infection", "Atrophy", "Necrosis"], "Tissue matures."),
        (15, "The longest bone in the body is the:", "Femur", ["Tibia", "Humerus", "Fibula"], "Thigh bone."),
        (15, "Muscles attach to bones by:", "Tendons", ["Ligaments", "Cartilage", "Bursae"], "Ligaments connect bones."),
        (15, "Moving a limb away from the midline is:", "Abduction", ["Adduction", "Flexion", "Extension"], "Anatomical movement term."),
    ]),
]

BOOK = {
    "titles": ["The Role of the Athletic Trainer in Sports Medicine"],
    "edition": "Current edition (unit list from the publisher's Contents in Brief)",
    "source": "McGraw Hill contents in brief",
    "unit": "Unit",
    "chapters": C,
    "quizzes": Q,
}
