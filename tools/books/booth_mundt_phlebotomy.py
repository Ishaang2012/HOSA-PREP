# Booth & Mundt - Phlebotomy: A Competency Based Approach.
# Chapter list: current edition, from McGraw Hill's product page table of contents (mheducation.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Phlebotomy and Healthcare", "Phlebotomy is the collection of blood for testing. Phlebotomists work in hospitals, clinics, labs, and blood donation centers and may be certified (for example, CPT through NHA or PBT through ASCP). The chapter covers the healthcare team, lab departments, professionalism, legal issues (consent, confidentiality under HIPAA, negligence), and quality patient care.", ["Phlebotomy = blood collection", "Certification through NHA, ASCP, AMT", "HIPAA protects patient information", "Consent before every draw"]),
    ch(2, "Safety and Preparedness", "Safety includes OSHA rules, the Bloodborne Pathogens Standard, needlestick prevention (safety devices, no recapping, sharps containers), chemical safety (Safety Data Sheets), fire safety (RACE and PASS), electrical safety, and emergency preparedness. Exposure incidents must be reported immediately.", ["Never recap used needles", "Sharps containers close at hand", "Report exposures immediately", "SDS for chemicals"]),
    ch(3, "Infection Control", "The chain of infection links agent, reservoir, portal of exit, mode of transmission, portal of entry, and susceptible host. Hand hygiene, standard precautions, transmission-based precautions (contact, droplet, airborne), and PPE break the chain. Proper glove use and disinfection prevent spreading pathogens between patients.", ["Hand hygiene breaks the chain", "Standard precautions for all patients", "Change gloves between patients", "Contact, droplet, airborne precautions"]),
    ch(4, "Medical Terminology and Abbreviations", "Phlebotomists use medical terms built from prefixes, roots, and suffixes (hemat/o = blood, phleb/o = vein, -tomy = cutting into, -emia = blood condition). Common abbreviations include CBC, BMP, PT/INR, stat, fasting, and NPO. Avoid error-prone abbreviations.", ["phleb/o = vein; -tomy = cut into", "hem/o, hemat/o = blood", "STAT = immediately", "CBC, BMP, PT/INR"]),
    ch(5, "Body Systems and Related Laboratory Tests", "Each body system has lab tests that assess it: kidney function (BUN, creatinine), liver (ALT, AST), endocrine (glucose, A1c, thyroid tests), musculoskeletal (calcium, uric acid), and others. Knowing which system a test evaluates helps phlebotomists understand orders and special handling.", ["BUN and creatinine = kidneys", "ALT and AST = liver", "Glucose and A1c = diabetes", "TSH = thyroid"]),
    ch(6, "The Cardiovascular System", "Blood is made of plasma and formed elements (red cells, white cells, platelets). Arteries carry blood away from the heart, veins return it, and capillaries connect them. The antecubital veins used most often are the median cubital (first choice), cephalic, and basilic (last choice, near the brachial artery and median nerve). Hemostasis involves vessel constriction, a platelet plug, and coagulation.", ["Median cubital = first choice vein", "Basilic is near the brachial artery and nerve", "Plasma has clotting factors; serum doesn't", "Hemostasis: vessel, platelets, coagulation"]),
    ch(7, "Patient and Specimen Requirements", "Patients must be identified with at least two identifiers before collection. Requisitions list the tests, timing, and special requirements such as fasting, timed draws, therapeutic drug monitoring (peak and trough), and basal state. Factors like posture, exercise, stress, and diurnal variation affect results.", ["Two patient identifiers", "Fasting and timed specimens", "Peak and trough timing", "Posture and exercise affect results"]),
    ch(8, "Blood Collection Equipment", "Equipment includes needles (higher gauge = smaller diameter; 21–22 gauge common), evacuated tube holders, syringes, butterfly (winged) sets, tourniquets, antiseptics (70% isopropyl alcohol), gauze, and bandages. Tube stopper colors indicate additives: light blue (sodium citrate), red or gold (clot activator/serum), green (heparin), lavender (EDTA), and gray (sodium fluoride and potassium oxalate).", ["Higher gauge = smaller needle", "Light blue = sodium citrate", "Lavender = EDTA; green = heparin", "Gray = sodium fluoride (glucose)"]),
    ch(9, "Venipuncture", "Steps include identifying the patient, explaining the procedure, hand hygiene, applying the tourniquet 3–4 inches above the site for no more than 1 minute, selecting and cleaning the site (let alcohol dry), anchoring the vein, inserting the needle bevel up at about 15–30 degrees, filling tubes in the correct order of draw, releasing the tourniquet, removing the needle, applying pressure, and labeling tubes at the bedside. The CLSI order of draw is: blood cultures, light blue, red/gold, green, lavender, gray.", ["Tourniquet no longer than 1 minute", "Bevel up, 15–30 degrees", "Order of draw: cultures, blue, red/gold, green, lavender, gray", "Label at the bedside"]),
    ch(10, "Dermal (Capillary) Puncture", "Capillary puncture is used for small samples, infants, and point-of-care tests. Sites include the side of the middle or ring finger for adults and the medial or lateral plantar heel for infants. Wipe away the first drop, avoid squeezing (which causes hemolysis and tissue fluid contamination), and follow the capillary order of draw (EDTA first, because platelets clump).", ["Wipe away the first drop", "Infant heel: medial or lateral plantar surface", "Don't squeeze (milk) the site", "EDTA collected first in capillary draws"]),
    ch(11, "Blood Specimen Handling", "Proper handling keeps results accurate. Some specimens need to be kept warm (cold agglutinins, at body temperature), chilled (ammonia, lactic acid), or protected from light (bilirubin). Tubes are inverted gently to mix additives, centrifuged as required, and transported promptly. Hemolysis, clotting, and wrong tubes cause rejected specimens.", ["Invert tubes gently; don't shake", "Bilirubin: protect from light", "Ammonia: on ice", "Hemolysis causes rejection"]),
    ch(12, "Quality Essentials", "Quality assurance covers the pre-analytical (collection), analytical (testing), and post-analytical (reporting) phases; most errors happen pre-analytically. Quality control, documentation, proficiency testing, and following CLSI standards and CLIA regulations keep testing reliable.", ["Most errors are pre-analytical", "Quality control checks accuracy", "CLIA regulates labs", "CLSI sets procedural standards"]),
    ch(13, "Special Phlebotomy Procedures", "Special procedures include blood cultures (strict aseptic technique, often two sets from different sites), glucose tolerance tests, timed and therapeutic drug monitoring specimens, blood bank specimens (careful labeling), blood donation, and collection from patients with special conditions such as IV lines (draw below the IV or from the other arm) or mastectomy (avoid the affected side).", ["Blood cultures: strict aseptic technique", "Avoid the arm with an IV or mastectomy", "Glucose tolerance test timing", "Blood bank labels must be exact"]),
    ch(14, "Collection of Non-Blood Specimens", "Phlebotomists may collect or process urine (random, clean-catch midstream, 24-hour, first morning), stool, throat and nasopharyngeal swabs, semen, sweat, and other specimens. Proper instructions, containers, labeling, and timing are essential. Chain-of-custody procedures apply to drug testing.", ["Clean-catch midstream urine", "First morning urine is most concentrated", "Chain of custody for drug tests", "Correct container and timing"]),
    ch(15, "Waived Testing", "CLIA-waived tests are simple, low-risk tests such as blood glucose, hemoglobin, urine dipstick, pregnancy, rapid strep, and some cholesterol and coagulation tests. They require following manufacturer instructions and running quality control.", ["CLIA-waived = simple, low risk", "Follow manufacturer instructions", "Run quality control", "Glucose and urine dipsticks"]),
    ch(16, "Practicing Professional Behavior", "Professional phlebotomists communicate clearly and with empathy, handle difficult patients calmly, respect cultural differences, maintain confidentiality, manage time and stress, and pursue continuing education and career growth.", ["Communicate with empathy", "Respect cultural differences", "Maintain confidentiality", "Continuing education"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Before drawing blood, the phlebotomist must obtain the patient's:", "Consent", ["Insurance card", "Medical history file", "Signature on a will"], "Patients can refuse."),
        (1, "HIPAA requires phlebotomists to:", "Protect patient information", ["Share results with family", "Post results publicly", "Skip identification"], "Confidentiality is a legal duty."),
        (2, "After using a needle, the phlebotomist should:", "Activate the safety device and discard it in a sharps container", ["Recap it with two hands", "Throw it in the trash", "Bend it"], "Never recap used needles."),
        (2, "Information about hazardous chemicals is found on:", "Safety Data Sheets", ["Requisitions", "Tube labels", "Patient charts"], "OSHA requires SDS."),
        (2, "A needlestick injury should be:", "Reported immediately", ["Ignored if small", "Reported at the end of the month", "Kept private"], "Follow-up testing may be needed."),
        (3, "The most important way to prevent infection is:", "Hand hygiene", ["Wearing a mask", "Using alcohol on the site", "Taking antibiotics"], "Clean hands before and after each patient."),
        (3, "Standard precautions are used for:", "All patients", ["Only patients with HIV", "Only children", "Only inpatients"], "Treat all blood as infectious."),
        (3, "Gloves should be changed:", "Between patients", ["Once a day", "Only if torn", "Every hour"], "This prevents cross-contamination."),
        (1, "Which is a phlebotomy certification?", "CPT or PBT", ["RN", "CNA", "EMT"], "Offered by NHA, ASCP, and others."),
        (3, "A patient with tuberculosis requires which precautions?", "Airborne", ["Contact", "Droplet", "None"], "Use an N95 respirator."),
    ]),
    ((4, 5, 6), [
        (4, "The combining form 'phleb/o' means:", "Vein", ["Artery", "Blood", "Heart"], "Phlebotomy = cutting into a vein."),
        (4, "'STAT' means:", "Immediately", ["Fasting", "Twice a day", "As needed"], "STAT specimens have top priority."),
        (5, "BUN and creatinine test the function of the:", "Kidneys", ["Liver", "Thyroid", "Heart"], "They're waste products filtered by the kidneys."),
        (5, "ALT and AST are tests of the:", "Liver", ["Kidneys", "Bones", "Lungs"], "They're liver enzymes."),
        (5, "Hemoglobin A1c is used to monitor:", "Diabetes", ["Thyroid disease", "Clotting", "Kidney stones"], "It reflects about 3 months of glucose."),
        (6, "The first-choice vein for venipuncture is the:", "Median cubital vein", ["Basilic vein", "Cephalic vein", "Jugular vein"], "It's large, well-anchored, and away from nerves."),
        (6, "The basilic vein is the last choice because it's near the:", "Brachial artery and median nerve", ["Heart", "Wrist bones", "Lymph nodes"], "Accidental puncture can cause injury."),
        (6, "The liquid part of blood that still contains clotting factors is:", "Plasma", ["Serum", "Hemoglobin", "Lymph"], "Serum is plasma without clotting factors."),
        (6, "Blood vessels that carry blood back to the heart are:", "Veins", ["Arteries", "Capillaries", "Arterioles"], "Venipuncture uses veins."),
        (4, "'CBC' stands for:", "Complete blood count", ["Cardiac blood count", "Clotting blood check", "Chemistry blood culture"], "It's drawn in a lavender (EDTA) tube."),
    ]),
    ((7, 8, 9), [
        (7, "Before collecting blood, patients must be identified using at least:", "Two identifiers", ["One identifier", "Room number only", "Their diagnosis"], "Name and date of birth are common."),
        (7, "A trough level for a drug is drawn:", "Just before the next dose", ["Right after the dose", "At any time", "The next day"], "It shows the lowest drug level."),
        (8, "Which needle gauge has the smallest diameter?", "25 gauge", ["18 gauge", "21 gauge", "16 gauge"], "Higher gauge = smaller needle."),
        (8, "A light-blue stopper contains:", "Sodium citrate", ["EDTA", "Heparin", "Sodium fluoride"], "It's used for coagulation tests."),
        (8, "A lavender stopper contains:", "EDTA", ["Sodium citrate", "Clot activator", "Heparin"], "It's used for CBCs."),
        (8, "A gray stopper is often used for:", "Glucose testing", ["Coagulation tests", "Blood bank", "CBCs"], "Sodium fluoride preserves glucose."),
        (9, "The tourniquet should stay on no longer than:", "1 minute", ["5 minutes", "10 minutes", "30 seconds is never enough"], "Longer causes hemoconcentration."),
        (9, "The needle is inserted with the bevel:", "Up", ["Down", "Sideways", "It doesn't matter"], "Use an angle of about 15–30 degrees."),
        (9, "Which tube is drawn first in the order of draw?", "Blood culture bottles", ["Lavender", "Gray", "Green"], "Then light blue, red/gold, green, lavender, gray."),
        (9, "Tubes should be labeled:", "At the bedside after collection", ["Before meeting the patient", "Back in the lab", "The next day"], "This prevents mislabeling."),
    ]),
    ((10, 11, 12), [
        (10, "In a capillary puncture, the first drop of blood should be:", "Wiped away", ["Collected", "Tested first", "Squeezed out hard"], "It contains tissue fluid."),
        (10, "The recommended site for infant heel sticks is the:", "Medial or lateral plantar surface of the heel", ["Back of the heel", "Center of the heel", "Toes"], "Avoid the bone at the back."),
        (10, "Squeezing (milking) the puncture site can cause:", "Hemolysis and tissue fluid contamination", ["Faster clotting", "More accurate results", "Less pain"], "Use gentle pressure."),
        (11, "Tubes with additives should be:", "Gently inverted", ["Shaken hard", "Left upright without mixing", "Frozen immediately"], "Shaking causes hemolysis."),
        (11, "A bilirubin specimen must be:", "Protected from light", ["Kept on ice", "Kept warm", "Shaken"], "Light breaks down bilirubin."),
        (11, "An ammonia specimen should be:", "Placed on ice", ["Kept at body temperature", "Left at room temperature for hours", "Exposed to light"], "Ammonia levels rise as cells metabolize."),
        (11, "Cold agglutinin specimens must be kept:", "At body temperature", ["On ice", "Frozen", "In sunlight"], "Cooling causes the antibodies to bind red cells."),
        (12, "Most laboratory errors occur in the:", "Pre-analytical phase", ["Analytical phase", "Post-analytical phase", "Billing phase"], "Collection and handling errors are common."),
        (12, "Federal rules for lab testing come from:", "CLIA", ["HIPAA", "OBRA", "EMTALA"], "Clinical Laboratory Improvement Amendments."),
        (12, "Running samples with known values to check accuracy is:", "Quality control", ["Calibration only", "Phlebotomy", "Centrifugation"], "Results must fall in set ranges."),
    ]),
    ((13, 14, 15), [
        (13, "Blood cultures require:", "Strict aseptic technique", ["No site cleaning", "Lavender tubes", "Collection after other tubes"], "Contamination causes false positives."),
        (13, "If a patient has an IV in one arm, blood should be drawn:", "From the other arm if possible", ["Above the IV", "From the IV line always", "From the same arm above the IV"], "IV fluid alters results."),
        (13, "After a mastectomy, blood should not be drawn from:", "The arm on the affected side", ["Either arm", "The other arm", "The hand"], "Lymph drainage may be impaired."),
        (14, "Which urine specimen is most concentrated?", "First morning", ["Random", "Postprandial", "Clean-catch afternoon"], "Urine concentrates overnight."),
        (14, "A clean-catch urine specimen is collected:", "Midstream after cleansing", ["From the first drops", "From the toilet", "From a bedpan"], "It reduces contamination."),
        (14, "Chain of custody is required for:", "Drug testing specimens", ["Routine CBCs", "Glucose tests", "Throat cultures"], "It documents every handler."),
        (15, "CLIA-waived tests are:", "Simple tests with low risk of error", ["The most complex tests", "Research tests", "Banned tests"], "Examples: glucose, urine dipstick."),
        (15, "When performing a waived test, you must:", "Follow the manufacturer's instructions", ["Change the procedure as you like", "Skip quality control", "Guess results"], "Instructions ensure accuracy."),
        (13, "A glucose tolerance test requires:", "Specimens drawn at timed intervals", ["A single random specimen", "No fasting", "Only urine"], "The patient drinks a glucose solution."),
        (15, "Which is a waived test?", "Urine pregnancy test", ["Blood culture identification", "Tissue biopsy", "Genetic sequencing"], "It's simple and quick."),
    ]),
    ((16,), [
        (16, "When a patient is anxious about a blood draw, the phlebotomist should:", "Explain the procedure calmly", ["Rush", "Ignore the patient", "Argue"], "Empathy reduces anxiety."),
        (16, "Respecting a patient's cultural beliefs is part of:", "Professional behavior", ["Quality control", "Order of draw", "Specimen handling"], "Ask about preferences."),
        (16, "Sharing a patient's test results with a friend violates:", "Confidentiality", ["Order of draw", "Aseptic technique", "Quality control"], "Protect privacy."),
        (16, "Continuing education helps phlebotomists:", "Keep skills and certification current", ["Avoid patients", "Skip safety rules", "Change careers only"], "Many certifications require it."),
        (16, "If a patient refuses a blood draw, the phlebotomist should:", "Respect the refusal and notify the nurse or supervisor", ["Draw anyway", "Restrain the patient", "Ignore it"], "Patients have the right to refuse."),
        (16, "Good time management in phlebotomy helps:", "Meet timed and STAT draw requirements", ["Avoid all patients", "Skip labeling", "Reduce safety"], "Timing affects results."),
        (16, "Handling a difficult patient calmly shows:", "Professionalism", ["Weakness", "Poor skills", "Rudeness"], "Stay polite and patient."),
        (16, "Effective communication includes:", "Clear explanations and active listening", ["Medical jargon", "Talking while walking away", "Ignoring questions"], "Patients feel respected."),
        (16, "Professional appearance for phlebotomists includes:", "Clean uniform and short nails", ["Long artificial nails", "Lots of jewelry", "Strong perfume"], "Long nails can tear gloves."),
    ]),
]

BOOK = {
    "titles": ["Phlebotomy: A Competency Based Approach"],
    "edition": "current edition",
    "source": "McGraw Hill product page table of contents",
    "chapters": C,
    "quizzes": Q,
}
