# McCall - Phlebotomy Essentials (Jones & Bartlett Learning).
# Chapter list: 7th edition (enhanced), from the publisher's sample front matter (samples.jblearning.com).
# The 8th edition keeps 14 chapters ending with arterial puncture. Summaries are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Phlebotomy: Past and Present and the Healthcare Setting", "Phlebotomy began with ancient bloodletting; today phlebotomists collect blood for testing. The healthcare setting includes hospitals, clinics, and labs; the clinical laboratory has areas like hematology, chemistry, microbiology, and blood bank. Phlebotomists need professionalism, communication skills, and certification (e.g., CPT, PBT).", ["Bloodletting history", "Clinical lab departments", "Professionalism", "Certification"]),
    ch(2, "Quality Assurance and Legal Issues in Healthcare", "Quality assurance ensures accurate results through standards, quality control, and documentation. Legal issues include informed consent, patient confidentiality (HIPAA), negligence, malpractice, and assault and battery. Organizations like CLSI and The Joint Commission set standards.", ["Quality control", "Informed consent", "HIPAA", "Negligence and malpractice"]),
    ch(3, "Infection Control, Safety, First Aid, and Personal Wellness", "Infection control breaks the chain of infection with hand hygiene, standard precautions, and PPE. Safety includes biohazard, electrical, fire, radiation, and chemical safety. Phlebotomists must know first aid for fainting and how to handle needlestick exposures.", ["Chain of infection", "Hand hygiene", "PPE", "Needlestick protocol"]),
    ch(4, "Medical Terminology", "Medical terms are built from prefixes, roots, combining vowels, and suffixes. Phlebotomists use common lab abbreviations and terms like hematology (blood study) and venipuncture (vein puncture).", ["Word parts", "Lab abbreviations", "phleb/o = vein", "-tomy = cutting"]),
    ch(5, "Human Anatomy and Physiology Review", "A review of body systems, organization, and planes, with attention to how each system relates to laboratory tests.", ["Body systems", "Anatomical position", "Homeostasis", "Tests by system"]),
    ch(6, "The Circulatory System", "The circulatory system includes the heart, blood vessels, and blood. Antecubital veins (median cubital, cephalic, basilic) are used for venipuncture. Blood contains plasma and formed elements; hemostasis stops bleeding. Serum lacks fibrinogen; plasma contains it.", ["Antecubital veins", "Median cubital first choice", "Serum vs. plasma", "Hemostasis"]),
    ch(7, "Blood Collection Equipment, Additives, and Order of Draw", "Equipment includes needles (gauge), tube holders, evacuated tubes, tourniquets, and antiseptics. Tube color indicates additive: light blue (citrate), red/gold (clot activator/gel), green (heparin), lavender (EDTA), gray (fluoride/oxalate). The order of draw prevents additive carryover.", ["Tube colors and additives", "Order of draw", "Needle gauge", "Additive carryover"]),
    ch(8, "Venipuncture Procedures", "Steps: review the requisition, identify the patient with two identifiers, hand hygiene, apply the tourniquet (no more than 1 minute), select and clean the site, anchor the vein, insert bevel up at 30° or less, fill tubes in order, release the tourniquet, remove the needle, apply pressure, and label at the bedside.", ["Two patient identifiers", "Tourniquet ≤ 1 minute", "Bevel up, ≤ 30°", "Label at bedside"]),
    ch(9, "Preexamination/Preanalytical Considerations", "Most lab errors occur before testing. Factors include patient preparation (fasting), posture, exercise, diurnal variation, hemolysis, hemoconcentration, and drawing above an IV. Complications include hematoma, nerve injury, and syncope.", ["Most errors are preanalytical", "Hemolysis", "Hemoconcentration", "Avoid drawing above an IV"]),
    ch(10, "Capillary Puncture Equipment, Principles and Procedures", "Capillary (skin) puncture uses lancets and microcollection tubes. Sites are the fingertip in adults and the heel in infants (medial or lateral plantar surface). Wipe away the first drop, avoid squeezing, and follow the capillary order of draw.", ["Heel stick in infants", "Wipe first drop", "Don't milk the site", "Capillary order of draw"]),
    ch(11, "Special Collections and Point-of-Care Testing", "Special collections include blood cultures, glucose tolerance tests, therapeutic drug monitoring (peak and trough), blood alcohol, and chain-of-custody specimens. Point-of-care testing (glucose, coagulation) happens at the bedside.", ["Blood cultures", "Peak and trough", "Chain of custody", "Point-of-care testing"]),
    ch(12, "Computers and Specimen Handling and Processing", "Lab information systems track orders and results. Specimens may need to be kept warm, chilled, or protected from light, and transported promptly. Processing includes centrifuging and aliquoting.", ["Lab information system", "Chill, warm, or protect from light", "Centrifuging", "Prompt transport"]),
    ch(13, "Urine and Other Nonblood Specimens and Tests", "Nonblood specimens include urine (random, first morning, midstream clean-catch, 24-hour), stool, throat swabs, sputum, semen, and cerebrospinal fluid. Proper collection and labeling are essential.", ["Clean-catch urine", "24-hour urine", "Throat swab", "Proper labeling"]),
    ch(14, "Arterial Puncture Procedures", "Arterial blood gases measure oxygen, carbon dioxide, and pH. The radial artery is preferred; perform the modified Allen test first to check collateral circulation. Specimens are collected anaerobically in heparinized syringes and need firm pressure afterward.", ["ABGs", "Radial artery preferred", "Modified Allen test", "Anaerobic collection"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Historically, bloodletting was used to:", "Treat illness by removing blood", ["Test blood sugar", "Type blood", "Grow bacteria"], "Phlebotomy's roots."),
        (1, "A common phlebotomy certification is the:", "CPT or PBT", ["RN", "MD", "CNA only"], "From NHA or ASCP."),
        (1, "The lab department that studies blood cells is:", "Hematology", ["Microbiology", "Chemistry", "Urinalysis"], "CBCs are done here."),
        (2, "Keeping patient information private is required by:", "HIPAA", ["OSHA", "CLIA", "EMTALA"], "Health privacy law."),
        (2, "Drawing blood without consent could be:", "Assault and battery", ["Malpractice insurance", "Quality control", "Delegation"], "Always get consent."),
        (2, "Testing known samples to check accuracy is:", "Quality control", ["Chain of custody", "Phlebotomy", "Hemostasis"], "Part of quality assurance."),
        (3, "The most important infection control measure is:", "Hand hygiene", ["Gloves", "Masks", "Gowns"], "Before and after each patient."),
        (3, "After a needlestick, you should first:", "Wash the site and report it", ["Ignore it", "Squeeze it and wait", "Finish the shift"], "Follow exposure protocol."),
        (3, "If a patient faints during a draw, you should:", "Remove the needle and tourniquet, lower the head", ["Keep drawing", "Leave the room", "Give food"], "Protect the patient."),
    ]),
    ((4, 5, 6), [
        (4, "The combining form phleb/o means:", "Vein", ["Blood", "Artery", "Heart"], "Phlebotomy = vein incision."),
        (4, "The suffix -emia means:", "Blood condition", ["Inflammation", "Removal", "Pain"], "E.g., anemia."),
        (4, "The prefix hyper- means:", "Excessive", ["Below", "Slow", "Within"], "E.g., hyperglycemia."),
        (5, "The body's stable internal balance is:", "Homeostasis", ["Metabolism", "Hemostasis", "Anabolism"], "Lab tests reflect it."),
        (5, "Standing upright facing forward, palms forward, is:", "Anatomical position", ["Supine", "Prone", "Fowler's"], "Reference position."),
        (5, "Kidney function is assessed with tests like:", "BUN and creatinine", ["Troponin", "TSH", "A1c"], "Urinary system."),
        (6, "The first-choice vein for venipuncture is the:", "Median cubital", ["Basilic", "Cephalic", "Femoral"], "Large and well anchored."),
        (6, "The liquid from clotted blood is:", "Serum", ["Plasma", "Whole blood", "Buffy coat"], "No fibrinogen."),
        (6, "The process that stops bleeding is:", "Hemostasis", ["Homeostasis", "Hemolysis", "Hematopoiesis"], "Vessel spasm, platelets, clotting."),
    ]),
    ((7, 8, 9), [
        (7, "A lavender tube contains:", "EDTA", ["Heparin", "Sodium citrate", "Sodium fluoride"], "Used for CBCs."),
        (7, "A light blue tube is used for:", "Coagulation tests", ["CBC", "Glucose", "Chemistry panels"], "Contains citrate."),
        (7, "The order of draw prevents:", "Additive carryover", ["Hemolysis", "Fainting", "Bruising"], "Contamination between tubes."),
        (8, "The tourniquet should stay on no longer than:", "1 minute", ["5 minutes", "3 minutes", "10 minutes"], "Prevents hemoconcentration."),
        (8, "The needle is inserted:", "Bevel up at 30 degrees or less", ["Bevel down", "At 90 degrees", "At 60 degrees"], "Shallow angle."),
        (8, "Tubes should be labeled:", "At the bedside after the draw", ["Before seeing the patient", "In the lab later", "By the patient"], "Prevents mix-ups."),
        (9, "Most laboratory errors occur in the:", "Preanalytical phase", ["Analytical phase", "Postanalytical phase", "Billing phase"], "Before testing."),
        (9, "Breakdown of red blood cells in a sample is:", "Hemolysis", ["Hemoconcentration", "Hemostasis", "Lipemia"], "Can alter results."),
        (9, "Blood should not be drawn:", "Above an IV site", ["From the median cubital", "From the nondominant arm", "With a tourniquet"], "IV fluid dilutes the sample."),
    ]),
    ((10, 11, 12), [
        (10, "In infants, capillary puncture is usually done on the:", "Heel", ["Finger", "Earlobe", "Toe"], "Medial or lateral plantar surface."),
        (10, "The first drop of blood in a capillary puncture is usually:", "Wiped away", ["Collected first", "Used for glucose only", "Squeezed out hard"], "May contain tissue fluid."),
        (10, "Squeezing (milking) a capillary site can cause:", "Hemolysis and tissue fluid contamination", ["Better results", "Faster clotting only", "No effect"], "Use gentle pressure."),
        (11, "Blood cultures are collected to detect:", "Bacteria in the blood", ["Glucose levels", "Blood type", "Hormones"], "Strict skin antisepsis."),
        (11, "Drug levels drawn at the highest and lowest points are:", "Peak and trough", ["Fasting and random", "Arterial and venous", "Serum and plasma"], "Therapeutic drug monitoring."),
        (11, "Documented handling of a legal specimen is:", "Chain of custody", ["Quality control", "Requisition", "Aliquoting"], "For drug or alcohol testing."),
        (12, "Some specimens, like bilirubin, must be:", "Protected from light", ["Frozen immediately", "Shaken", "Left uncapped"], "Light breaks it down."),
        (12, "Spinning samples to separate serum or plasma is:", "Centrifuging", ["Aliquoting", "Labeling", "Accessioning"], "Balance the centrifuge."),
        (12, "A portion of a specimen transferred to another tube is an:", "Aliquot", ["Requisition", "Additive", "Artifact"], "For separate tests."),
    ]),
    ((13, 14), [
        (13, "A midstream urine specimen after cleaning is a:", "Clean-catch specimen", ["Random specimen", "24-hour specimen", "First morning specimen"], "Used for cultures."),
        (13, "For a 24-hour urine collection, the first morning void is:", "Discarded", ["Kept", "Sent separately", "Frozen"], "Collection starts after."),
        (13, "The most concentrated urine sample is the:", "First morning specimen", ["Random specimen", "Afternoon specimen", "Post-meal specimen"], "Good for pregnancy tests."),
        (14, "Arterial blood gases measure oxygen, carbon dioxide, and:", "pH", ["Glucose", "Cholesterol", "Hemoglobin A1c"], "ABGs."),
        (14, "The preferred site for arterial puncture is the:", "Radial artery", ["Femoral artery", "Brachial vein", "Carotid artery"], "Collateral circulation."),
        (14, "Before a radial puncture, perform the:", "Modified Allen test", ["Romberg test", "Lachman test", "Tourniquet test"], "Checks ulnar circulation."),
        (14, "ABG samples must be collected:", "Anaerobically, without air bubbles", ["In an open tube", "With a tourniquet for 3 minutes", "Into a red tube"], "Air changes results."),
        (13, "A throat swab is often collected to test for:", "Strep throat", ["Diabetes", "Anemia", "Kidney stones"], "Swab tonsils and the back of the throat."),
        (14, "After an arterial puncture, apply firm pressure for at least:", "3–5 minutes", ["10 seconds", "30 seconds", "None"], "Longer if on blood thinners."),
    ]),
]

BOOK = {
    "titles": ["Phlebotomy Essentials"],
    "edition": "7th edition (enhanced); the 8th edition also has 14 chapters",
    "source": "Jones & Bartlett sample front matter",
    "chapters": C,
    "quizzes": Q,
}
