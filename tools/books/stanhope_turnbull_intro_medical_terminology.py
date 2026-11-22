# Stanhope & Turnbull - Introduction to Medical Terminology (Goodheart-Willcox).
# Chapter list supplied by the site owner (not verified against the publisher). Summaries are written for this site.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Basic Word Structure (Prefixes, Suffixes, Combining Forms)", "Medical terms are built from a word root (core meaning), combining vowel (usually o), prefix (beginning), and suffix (ending). Analyze terms by reading the suffix first, then the prefix, then the root. Example: gastr/o/enter/itis = inflammation of the stomach and intestines.", ["Root, prefix, suffix", "Combining vowel o", "Read suffix first", "Combining forms"]),
    ch(2, "Body Structure, Color, and Oncology", "Body organization goes from cells to tissues, organs, and systems. Color prefixes include erythr/o (red), leuk/o (white), cyan/o (blue), melan/o (black), and xanth/o (yellow). Oncology terms include -oma (tumor), carcin/o (cancer), benign, malignant, and metastasis.", ["Cells to systems", "Color word parts", "-oma = tumor", "Benign vs. malignant"]),
    ch(3, "Directional Terms, Anatomic Planes, Regions, and Quadrants", "Directional terms include superior/inferior, anterior/posterior, medial/lateral, and proximal/distal. Planes divide the body: sagittal (left/right), frontal or coronal (front/back), transverse (top/bottom). The abdomen is divided into 4 quadrants or 9 regions.", ["Directional terms", "Body planes", "Four quadrants", "Nine regions"]),
    ch(4, "Integumentary System", "Skin word parts include derm/o and dermat/o (skin), cutane/o (skin), onych/o (nail), trich/o (hair), and kerat/o (hard). Terms include dermatitis, onychomycosis, alopecia, and burns classified by depth.", ["derm/o, cutane/o", "onych/o = nail", "trich/o = hair", "Burn depth"]),
    ch(5, "Respiratory System", "Word parts include pneum/o and pulmon/o (lung), bronch/o (bronchus), trache/o (trachea), laryng/o (larynx), rhin/o and nas/o (nose), and -pnea (breathing). Terms include dyspnea, apnea, bronchitis, and tracheostomy.", ["pneum/o, pulmon/o", "-pnea = breathing", "bronch/o, trache/o", "rhin/o = nose"]),
    ch(6, "Urinary System", "Word parts include nephr/o and ren/o (kidney), cyst/o and vesic/o (bladder), ur/o (urine), and ureter/o and urethr/o. Terms include nephritis, cystitis, hematuria, dysuria, and lithotripsy.", ["nephr/o, ren/o", "cyst/o = bladder", "-uria = urine condition", "Lithotripsy"]),
    ch(7, "Male Reproductive System", "Word parts include orchi/o and testicul/o (testis), prostat/o (prostate), vas/o (vessel/duct), and andr/o (male). Terms include orchitis, vasectomy, BPH, and prostatectomy.", ["orchi/o = testis", "prostat/o", "Vasectomy", "BPH"]),
    ch(8, "Female Reproductive System", "Word parts include gynec/o (woman), hyster/o and uter/o (uterus), oophor/o and ovari/o (ovary), salping/o (fallopian tube), mamm/o and mast/o (breast), and men/o (menstruation). Terms include hysterectomy, mammogram, and dysmenorrhea.", ["hyster/o = uterus", "oophor/o = ovary", "mamm/o, mast/o", "men/o = menstruation"]),
    ch(9, "Obstetrics and Neonatology", "Word parts include gravid/o (pregnancy), -para (to bear), nat/o (birth), and fet/o (fetus). Terms include gravida, para, prenatal, postpartum, neonate, and cesarean section.", ["Gravida vs. para", "nat/o = birth", "Prenatal and postpartum", "Neonate"]),
    ch(10, "Cardiovascular, Immune, and Lymphatic Systems and Blood", "Word parts include cardi/o (heart), angi/o and vas/o (vessel), arteri/o, phleb/o and ven/o (vein), hem/o and hemat/o (blood), lymph/o, and immun/o. Terms include tachycardia, anemia, leukemia, and lymphadenopathy.", ["cardi/o = heart", "angi/o = vessel", "hem/o = blood", "lymph/o, immun/o"]),
    ch(11, "Digestive System", "Word parts include gastr/o (stomach), enter/o (small intestine), col/o (colon), hepat/o (liver), cholecyst/o (gallbladder), and -emesis (vomiting). Terms include gastritis, hepatomegaly, cholecystectomy, and colonoscopy.", ["gastr/o = stomach", "hepat/o = liver", "col/o = colon", "-emesis = vomiting"]),
    ch(12, "Eye", "Word parts include ophthalm/o and ocul/o (eye), opt/o (vision), retin/o (retina), kerat/o (cornea), blephar/o (eyelid), and -opia (vision condition). Terms include myopia, presbyopia, cataract, and glaucoma.", ["ophthalm/o = eye", "blephar/o = eyelid", "-opia = vision", "Myopia and presbyopia"]),
    ch(13, "Ear", "Word parts include ot/o and aur/o (ear), audi/o (hearing), tympan/o and myring/o (eardrum), and -cusis (hearing). Terms include otitis media, presbycusis, tinnitus, and myringotomy.", ["ot/o = ear", "audi/o = hearing", "myring/o = eardrum", "Presbycusis"]),
    ch(14, "Musculoskeletal System", "Word parts include oste/o (bone), arthr/o (joint), my/o (muscle), chondr/o (cartilage), ten/o and tendin/o (tendon), and -malacia (softening). Terms include osteoporosis, arthritis, myalgia, and arthroscopy.", ["oste/o = bone", "arthr/o = joint", "my/o = muscle", "chondr/o = cartilage"]),
    ch(15, "Nervous System and Behavioral Health", "Word parts include neur/o (nerve), encephal/o (brain), cerebr/o (cerebrum), mening/o (meninges), myel/o (spinal cord), and psych/o (mind). Terms include meningitis, encephalopathy, hemiplegia, and psychosis.", ["neur/o = nerve", "encephal/o = brain", "myel/o = spinal cord", "psych/o = mind"]),
    ch(16, "Endocrine System", "Word parts include aden/o (gland), thyr/o (thyroid), adren/o (adrenal), pancreat/o (pancreas), gluc/o and glyc/o (sugar), and crin/o (secrete). Terms include hyperthyroidism, hypoglycemia, and diabetes mellitus.", ["aden/o = gland", "thyr/o = thyroid", "glyc/o = sugar", "crin/o = secrete"]),
]

Q = [
    ((1, 2, 3), [
        (1, "The core meaning of a medical term is the:", "Word root", ["Prefix", "Suffix", "Combining vowel"], "Foundation of the term."),
        (1, "The most common combining vowel is:", "o", ["a", "e", "i"], "E.g., cardi/o."),
        (1, "When analyzing a term, start with the:", "Suffix", ["Prefix", "Root", "Middle"], "Then prefix, then root."),
        (2, "erythr/o means:", "Red", ["White", "Blue", "Black"], "Erythrocyte = red blood cell."),
        (2, "The suffix -oma means:", "Tumor", ["Inflammation", "Removal", "Pain"], "E.g., carcinoma."),
        (2, "Spread of cancer to distant sites is:", "Metastasis", ["Remission", "Biopsy", "Benign growth"], "Malignant tumors spread."),
        (3, "The plane dividing the body into left and right is:", "Sagittal", ["Frontal", "Transverse", "Coronal"], "Midsagittal = equal halves."),
        (3, "Farther from the point of attachment is:", "Distal", ["Proximal", "Medial", "Superior"], "Fingers are distal to the elbow."),
        (3, "The abdomen can be divided into how many quadrants?", "Four", ["Two", "Six", "Nine"], "Or nine regions."),
    ]),
    ((4, 5, 6), [
        (4, "onych/o refers to the:", "Nail", ["Hair", "Skin", "Sweat gland"], "Onychomycosis = nail fungus."),
        (4, "trich/o refers to:", "Hair", ["Nail", "Skin", "Fat"], "Trichology."),
        (4, "Hair loss is:", "Alopecia", ["Pruritus", "Erythema", "Urticaria"], "Pruritus = itching."),
        (5, "-pnea means:", "Breathing", ["Lung", "Air sac", "Voice"], "Dyspnea, apnea."),
        (5, "rhin/o refers to the:", "Nose", ["Throat", "Lung", "Larynx"], "Rhinitis."),
        (5, "An incision into the trachea is a:", "Tracheotomy", ["Tracheitis", "Bronchoscopy", "Laryngectomy"], "-otomy = cutting into."),
        (6, "nephr/o means:", "Kidney", ["Bladder", "Urethra", "Ureter"], "Nephritis."),
        (6, "Blood in the urine is:", "Hematuria", ["Dysuria", "Polyuria", "Anuria"], "-uria = urine condition."),
        (6, "Crushing kidney stones is:", "Lithotripsy", ["Lithotomy", "Nephrectomy", "Cystoscopy"], "-tripsy = crushing."),
    ]),
    ((7, 8, 9), [
        (7, "orchi/o refers to the:", "Testis", ["Prostate", "Penis", "Bladder"], "Orchitis."),
        (7, "Cutting and sealing the vas deferens is a:", "Vasectomy", ["Prostatectomy", "Orchiectomy", "Circumcision"], "Male sterilization."),
        (7, "BPH stands for:", "Benign prostatic hyperplasia", ["Bilateral prostate hernia", "Blood pressure high", "Benign penile hyperplasia"], "Enlarged prostate."),
        (8, "hyster/o refers to the:", "Uterus", ["Ovary", "Breast", "Vagina"], "Hysterectomy."),
        (8, "oophor/o refers to the:", "Ovary", ["Uterus", "Fallopian tube", "Breast"], "Oophorectomy."),
        (8, "Painful menstruation is:", "Dysmenorrhea", ["Amenorrhea", "Menorrhagia", "Menarche"], "dys- = painful."),
        (9, "A woman's number of pregnancies is her:", "Gravida", ["Para", "Parity only", "Natal"], "Para = births."),
        (9, "After childbirth is:", "Postpartum", ["Prenatal", "Antepartum", "Intrapartum"], "post- = after."),
        (9, "A newborn up to 4 weeks old is a:", "Neonate", ["Infant only", "Toddler", "Fetus"], "neo- = new."),
    ]),
    ((10, 11, 12), [
        (10, "angi/o means:", "Vessel", ["Heart", "Blood", "Lymph"], "Angiogram."),
        (10, "A fast heart rate is:", "Tachycardia", ["Bradycardia", "Arrhythmia", "Cardiomegaly"], "tachy- = fast."),
        (10, "Cancer of white blood cells is:", "Leukemia", ["Anemia", "Lymphoma only", "Hemophilia"], "leuk/o = white."),
        (11, "hepat/o refers to the:", "Liver", ["Gallbladder", "Pancreas", "Stomach"], "Hepatitis."),
        (11, "Removal of the gallbladder is:", "Cholecystectomy", ["Colectomy", "Gastrectomy", "Appendectomy"], "cholecyst/o = gallbladder."),
        (11, "-emesis means:", "Vomiting", ["Digestion", "Swallowing", "Bleeding"], "Hematemesis."),
        (12, "blephar/o refers to the:", "Eyelid", ["Cornea", "Retina", "Iris"], "Blepharitis."),
        (12, "Nearsightedness is:", "Myopia", ["Hyperopia", "Presbyopia", "Diplopia"], "-opia = vision."),
        (12, "Age-related loss of near vision is:", "Presbyopia", ["Myopia", "Glaucoma", "Cataract"], "presby- = old age."),
    ]),
    ((13, 14), [
        (13, "ot/o refers to the:", "Ear", ["Eye", "Nose", "Throat"], "Otitis."),
        (13, "Age-related hearing loss is:", "Presbycusis", ["Tinnitus", "Otitis", "Vertigo"], "-cusis = hearing."),
        (13, "Ringing in the ears is:", "Tinnitus", ["Vertigo", "Otalgia", "Otorrhea"], "Common symptom."),
        (13, "Incision into the eardrum is a:", "Myringotomy", ["Otoplasty", "Tympanitis", "Audiometry"], "myring/o = eardrum."),
        (14, "oste/o means:", "Bone", ["Joint", "Muscle", "Cartilage"], "Osteoporosis."),
        (14, "arthr/o means:", "Joint", ["Bone", "Muscle", "Tendon"], "Arthritis."),
        (14, "Muscle pain is:", "Myalgia", ["Arthralgia", "Ostealgia", "Neuralgia"], "my/o = muscle."),
        (14, "chondr/o refers to:", "Cartilage", ["Bone", "Tendon", "Ligament"], "Chondromalacia."),
        (14, "Softening of bone is:", "Osteomalacia", ["Osteoporosis", "Osteitis", "Osteoma"], "-malacia = softening."),
    ]),
    ((15, 16), [
        (15, "encephal/o refers to the:", "Brain", ["Spinal cord", "Nerve", "Skull"], "Encephalitis."),
        (15, "myel/o can refer to the:", "Spinal cord (or bone marrow)", ["Brain", "Muscle", "Nerve"], "Myelitis."),
        (15, "Inflammation of the meninges is:", "Meningitis", ["Encephalitis", "Neuritis", "Myelitis"], "Membranes around brain and cord."),
        (15, "Paralysis of one side of the body is:", "Hemiplegia", ["Paraplegia", "Quadriplegia", "Paresis"], "hemi- = half."),
        (15, "psych/o refers to the:", "Mind", ["Brain tissue", "Nerve", "Skull"], "Psychology."),
        (16, "aden/o means:", "Gland", ["Sugar", "Thyroid", "Kidney"], "Adenoma."),
        (16, "Low blood sugar is:", "Hypoglycemia", ["Hyperglycemia", "Glycosuria", "Polydipsia"], "glyc/o = sugar."),
        (16, "An overactive thyroid is:", "Hyperthyroidism", ["Hypothyroidism", "Thyroiditis", "Goiter only"], "hyper- = excessive."),
        (16, "crin/o means:", "To secrete", ["Gland", "Sugar", "Blood"], "Endocrine = secrete within."),
    ]),
]

BOOK = {
    "titles": ["Introduction to Medical Terminology"],
    "edition": "Edition not verified; chapter list supplied by the site owner",
    "source": "Chapter list supplied by the site owner",
    "chapters": C,
    "quizzes": Q,
}
