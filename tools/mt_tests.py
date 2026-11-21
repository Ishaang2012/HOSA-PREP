"""Medical Terminology practice tests: 3 levels x 50 questions.

Each level follows the 2026-27 HOSA test plan: Roots/Prefixes/Suffixes/Combining Forms 45% (23 Q),
and each of the 11 body-area topics 5% (2-3 Q each), for 50 questions total.

Each question: (topic, question, correct answer, [3 wrong answers], explanation).
Answer order and question order are shuffled with a fixed seed so the output is stable.
"""
import json, random, sys
from collections import Counter

WP, OV, SK, MU, RE, DI, CV, NE, EN, RP, IN, UR = (
    "Word parts", "Overview of body", "Skeletal", "Muscular", "Respiratory", "Digestive",
    "Cardiovascular & lymphatic", "Nervous/special senses", "Endocrine", "Reproductive", "Integumentary", "Urinary")

EASY = [
    (WP, 'What does the suffix "-itis" mean?', "Inflammation", ["Removal", "Study of", "Enlargement"], "-itis means inflammation, as in tonsillitis (inflammation of the tonsils)."),
    (WP, 'The combining form "cardi/o" refers to the:', "Heart", ["Lungs", "Kidney", "Liver"], "cardi/o = heart. Hepat/o = liver, nephr/o and ren/o = kidney, pulmon/o = lung."),
    (WP, 'Which prefix means "below" or "under"?', "sub-", ["hyper-", "epi-", "supra-"], "sub- means under (subcutaneous). hyper-, epi-, and supra- all mean above or excessive."),
    (WP, '"Gastr/o" refers to the:', "Stomach", ["Intestine", "Esophagus", "Gallbladder"], "gastr/o = stomach. enter/o = small intestine, esophag/o = esophagus, cholecyst/o = gallbladder."),
    (WP, 'What does "-ectomy" mean?', "Surgical removal", ["Incision", "Visual examination", "Surgical repair"], "-ectomy = surgical removal (appendectomy). -otomy is incision, -scopy is visual exam, -plasty is repair."),
    (WP, 'The suffix "-ology" means:', "Study of", ["Removal of", "Inflammation of", "Pain in"], "-ology = the study of, as in cardiology (study of the heart)."),
    (WP, 'The suffix "-algia" means:', "Pain", ["Swelling", "Hardening", "Bleeding"], "-algia = pain. Arthralgia is joint pain."),
    (WP, 'The prefix "tachy-" means:', "Fast", ["Slow", "Large", "Small"], "tachy- = fast (tachycardia). brady- = slow."),
    (WP, 'The prefix "hypo-" means:', "Below or deficient", ["Above or excessive", "Within", "Across"], "hypo- = below normal or deficient, as in hypoglycemia (low blood sugar)."),
    (WP, 'The suffix "-scopy" means:', "Visual examination", ["Surgical repair", "Process of recording", "Incision"], "-scopy = visual examination with an instrument, as in endoscopy."),
    (WP, 'The prefix "inter-" means:', "Between", ["Within", "Around", "Through"], "inter- = between. Intercostal means between the ribs. intra- means within."),
    (WP, 'The suffix "-emia" means:', "Blood condition", ["Urine condition", "Tumor", "Hernia"], "-emia = blood condition, as in anemia or hyperglycemia."),
    (WP, 'The prefix "neo-" means:', "New", ["Old", "Many", "Few"], "neo- = new. A neonate is a newborn."),
    (WP, 'The suffix "-plasty" means:', "Surgical repair", ["Surgical puncture", "Crushing", "Dilation"], "-plasty = surgical repair, as in rhinoplasty (repair of the nose)."),
    (WP, 'The prefix "poly-" means:', "Many", ["One", "Half", "None"], "poly- = many or much. Polyuria is excessive urination."),
    (WP, 'The suffix "-oma" means:', "Tumor", ["Softening", "Narrowing", "Rupture"], "-oma = tumor or mass, as in lipoma (fatty tumor)."),
    (WP, 'The prefix "bi-" means:', "Two", ["Half", "Three", "Above"], "bi- = two (bilateral = both sides). hemi- and semi- mean half; tri- means three."),
    (WP, 'The suffix "-otomy" means:', "Cutting into (incision)", ["Removal", "Making a new opening", "Fixation"], "-otomy = incision. -ectomy is removal; -ostomy is making a new opening; -pexy is fixation."),
    (WP, 'The prefix "macro-" means:', "Large", ["Small", "Few", "Bad"], "macro- = large (macrocyte). micro- = small."),
    (WP, 'The prefix "micro-" means:', "Small", ["Large", "Fast", "Outside"], "micro- = small, as in microscope."),
    (WP, 'The suffix "-pathy" means:', "Disease", ["Treatment", "Specialist", "Measurement"], "-pathy = disease, as in neuropathy (disease of the nerves)."),
    (WP, 'The suffix "-logist" means:', "Specialist who studies and treats", ["Study of", "Instrument", "Process"], "-logist = specialist (cardiologist). -logy is the study itself."),
    (WP, 'The prefix "ab-" means:', "Away from", ["Toward", "Around", "Beneath"], "ab- = away from (abduction). ad- = toward (adduction)."),
    (OV, "Which of these is the smallest level of body organization?", "Cell", ["Tissue", "Organ", "Body system"], "Cells form tissues, tissues form organs, and organs form body systems."),
    (OV, "In the anatomical position, the palms face:", "Forward", ["Backward", "Inward toward the thighs", "Upward"], "Anatomical position: standing upright, facing forward, arms at the sides, palms facing forward."),
    (OV, 'The directional term "superior" means:', "Toward the head or upper part", ["Toward the feet", "Toward the front", "Toward the side"], "Superior = above or toward the head; inferior = below or toward the feet."),
    (SK, 'The combining form "oste/o" means:', "Bone", ["Joint", "Cartilage", "Muscle"], "oste/o = bone (osteoporosis). arthr/o = joint, chondr/o = cartilage, my/o = muscle."),
    (SK, 'The combining form "arthr/o" means:', "Joint", ["Bone marrow", "Tendon", "Spine"], "arthr/o = joint, as in arthritis (inflammation of a joint)."),
    (MU, 'The combining form "my/o" means:', "Muscle", ["Marrow", "Nerve", "Fat"], "my/o = muscle (myalgia = muscle pain). myel/o = marrow or spinal cord."),
    (MU, "Which structure connects muscle to bone?", "Tendon", ["Ligament", "Cartilage", "Bursa"], "Tendons connect muscle to bone. Ligaments connect bone to bone."),
    (RE, 'The combining forms "pneum/o" and "pulmon/o" refer to the:', "Lungs", ["Heart", "Liver", "Stomach"], "pneum/o and pulmon/o = lung (pneumonia, pulmonary)."),
    (RE, 'The combining form "rhin/o" means:', "Nose", ["Throat", "Ear", "Mouth"], "rhin/o = nose (rhinitis). pharyng/o = throat, ot/o = ear, or/o = mouth."),
    (RE, '"Apnea" means:', "Absence of breathing", ["Difficult breathing", "Rapid breathing", "Normal breathing"], "a- (without) + -pnea (breathing). Normal breathing is eupnea; difficult breathing is dyspnea."),
    (DI, 'The combining form "hepat/o" means:', "Liver", ["Kidney", "Spleen", "Pancreas"], "hepat/o = liver (hepatitis). nephr/o = kidney, splen/o = spleen, pancreat/o = pancreas."),
    (DI, 'The combining forms "or/o" and "stomat/o" refer to the:', "Mouth", ["Teeth", "Tongue", "Lips"], "or/o and stomat/o = mouth. dent/o = teeth, gloss/o = tongue, cheil/o = lips."),
    (DI, 'The combining form "col/o" refers to the:', "Colon (large intestine)", ["Small intestine", "Rectum", "Esophagus"], "col/o = colon. enter/o = small intestine, rect/o = rectum, esophag/o = esophagus."),
    (CV, 'The combining form "angi/o" means:', "Vessel", ["Heart muscle", "Valve", "Blood"], "angi/o = vessel (angiogram). hem/o = blood, valv/o = valve."),
    (CV, "Which vessels carry blood away from the heart?", "Arteries", ["Veins", "Venules", "Lymphatic vessels"], "Arteries carry blood away from the heart; veins return blood to it."),
    (CV, "Which organ is part of the lymphatic system?", "Spleen", ["Liver", "Pancreas", "Gallbladder"], "The spleen, lymph nodes, thymus, and tonsils are lymphatic organs."),
    (NE, 'The combining form "neur/o" means:', "Nerve", ["Brain", "Spinal cord", "Muscle"], "neur/o = nerve. encephal/o = brain, myel/o = spinal cord."),
    (NE, 'The combining form "encephal/o" means:', "Brain", ["Skull", "Head", "Nerve"], "encephal/o = brain (encephalitis). crani/o = skull, cephal/o = head."),
    (NE, 'The combining form "ophthalm/o" means:', "Eye", ["Ear", "Nose", "Mouth"], "ophthalm/o = eye (ophthalmologist). ot/o = ear."),
    (EN, 'Which gland is often called the "master gland"?', "Pituitary", ["Thyroid", "Adrenal", "Pineal"], "The pituitary gland secretes hormones that control many other endocrine glands."),
    (EN, 'The combining form "glyc/o" means:', "Sugar (glucose)", ["Fat", "Protein", "Salt"], "glyc/o = sugar, as in hyperglycemia. lip/o = fat."),
    (RP, 'The combining forms "hyster/o" and "uter/o" refer to the:', "Uterus", ["Ovary", "Breast", "Vagina"], "hyster/o and uter/o = uterus. oophor/o = ovary, mamm/o = breast, colp/o = vagina."),
    (RP, 'The combining forms "orchi/o" and "test/o" refer to the:', "Testis", ["Prostate", "Penis", "Sperm"], "orchi/o, orchid/o, and test/o = testis. prostat/o = prostate, spermat/o = sperm."),
    (IN, 'The combining forms "derm/o" and "dermat/o" mean:', "Skin", ["Hair", "Nail", "Sweat"], "derm/o and dermat/o = skin. trich/o = hair, onych/o = nail, hidr/o = sweat."),
    (IN, 'The combining form "onych/o" means:', "Nail", ["Hair", "Gland", "Skin"], "onych/o = nail, as in onychomycosis (fungal nail infection)."),
    (UR, 'The combining forms "nephr/o" and "ren/o" refer to the:', "Kidney", ["Bladder", "Ureter", "Urethra"], "nephr/o and ren/o = kidney. cyst/o = bladder."),
    (UR, 'In urinary terms, "cyst/o" refers to the:', "Urinary bladder", ["Kidney", "Urethra", "Prostate"], "cyst/o = urinary bladder (cystitis). It can also mean a sac or cyst."),
]

MEDIUM = [
    (DI, 'A patient with "hepatomegaly" has:', "Enlargement of the liver", ["Inflammation of the liver", "Pain in the liver", "Removal of part of the liver"], "hepat/o (liver) + -megaly (enlargement)."),
    (OV, "Which term describes a position closer to the point of attachment of a limb?", "Proximal", ["Distal", "Lateral", "Inferior"], "Proximal means nearer the point of attachment or origin; distal means farther away."),
    (CV, '"Bradycardia" means:', "Slow heart rate", ["Fast heart rate", "Irregular heart rhythm", "Absent heartbeat"], "brady- (slow) + card/i (heart) + -ia (condition). A fast heart rate is tachycardia."),
    (OV, "Which plane divides the body into anterior and posterior portions?", "Frontal (coronal)", ["Sagittal", "Transverse", "Midsagittal"], "The frontal (coronal) plane separates front from back. Sagittal planes divide left from right."),
    (WP, 'The suffix "-ostomy" means:', "Creating a new opening", ["Cutting into", "Removal", "Suturing"], "-ostomy = surgically creating an opening (colostomy). -otomy is cutting into; -rrhaphy is suturing."),
    (WP, 'Which suffix means "surgical puncture to remove fluid"?', "-centesis", ["-stomy", "-pexy", "-tripsy"], "-centesis = surgical puncture to remove fluid, as in amniocentesis."),
    (WP, 'In "bronchiectasis," the suffix "-ectasis" means:', "Dilation or stretching", ["Narrowing", "Hardening", "Discharge"], "-ectasis = dilation. Bronchiectasis is permanent widening of the bronchi."),
    (WP, 'The suffix "-stenosis" means:', "Narrowing", ["Rupture", "Paralysis", "Flow"], "-stenosis = abnormal narrowing, as in aortic stenosis."),
    (WP, 'The suffix "-sclerosis" means:', "Hardening", ["Softening", "Drooping", "Prolapse"], "-sclerosis = hardening (arteriosclerosis). -malacia = softening."),
    (WP, 'The suffix "-plegia" means:', "Paralysis", ["Weakness", "Pain", "Seizure"], "-plegia = paralysis (hemiplegia). -paresis = partial paralysis or weakness."),
    (WP, '"Hemiparesis" means:', "Weakness of one side of the body", ["Paralysis of one side of the body", "Loss of sensation on one side", "Pain on one side"], "hemi- (half) + -paresis (slight paralysis or weakness). Full paralysis would be hemiplegia."),
    (WP, 'The prefix "epi-" means:', "Upon or above", ["Under", "Within", "Between"], "epi- = upon or above, as in epidermis (the layer on top of the dermis)."),
    (WP, 'The prefix "endo-" means:', "Within", ["Outside", "Around", "Through"], "endo- = within (endoscopy). exo- and ecto- mean outside."),
    (WP, 'The suffix "-rrhea" means:', "Flow or discharge", ["Bursting forth", "Suture", "Hernia"], "-rrhea = flow or discharge (diarrhea). -rrhagia = bursting forth; -rrhaphy = suture."),
    (WP, 'The suffix "-cele" means:', "Hernia or protrusion", ["Cell", "Cavity", "Tumor"], "-cele = hernia or protrusion, as in cystocele (bladder protruding into the vagina)."),
    (WP, 'The prefix "dys-" means:', "Bad, painful, or difficult", ["Absent", "Excessive", "Normal"], "dys- = bad, painful, or difficult (dyspnea, dysuria)."),
    (WP, 'Which term means "pertaining to under the tongue"?', "Sublingual", ["Intralingual", "Supralingual", "Retrolingual"], "sub- (under) + lingu/o (tongue) + -al (pertaining to)."),
    (WP, 'The suffix "-lysis" means:', "Breakdown, destruction, or separation", ["Formation", "Hardening", "Fixation"], "-lysis = breakdown or separation, as in hemolysis (destruction of red blood cells)."),
    (WP, 'The suffix "-genesis" means:', "Formation or creation", ["Destruction", "Measurement", "Hardening"], "-genesis = formation or origin, as in osteogenesis (bone formation)."),
    (WP, 'The suffix "-ptosis" means:', "Drooping or prolapse", ["Rupture", "Narrowing", "Fixation"], "-ptosis = drooping, as in blepharoptosis (drooping eyelid)."),
    (WP, 'The suffix "-osis" generally means:', "Abnormal condition", ["Inflammation", "Removal", "Surgical repair"], "-osis = abnormal condition (cyanosis, nephrosis)."),
    (WP, 'The prefix "retro-" means:', "Behind or backward", ["Before", "After", "Across"], "retro- = behind or backward, as in retroperitoneal (behind the peritoneum)."),
    (WP, 'The suffix "-tripsy" means:', "Crushing", ["Cutting", "Suturing", "Fixation"], "-tripsy = crushing, as in lithotripsy (crushing a stone)."),
    (WP, 'The prefix "contra-" means:', "Against or opposite", ["With", "Beside", "Before"], "contra- = against, as in contraindication."),
    (WP, 'The suffix "-desis" means:', "Binding or surgical fusion", ["Separation", "Drooping", "Dissolving"], "-desis = binding or fusion. Arthrodesis is surgical fusion of a joint."),
    (WP, "Inflammation of the bone and bone marrow is called:", "Osteomyelitis", ["Osteitis", "Myelitis", "Osteoarthritis"], "oste/o (bone) + myel/o (bone marrow) + -itis (inflammation)."),
    (WP, 'The suffix "-trophy" means:', "Development or nourishment", ["Tumor", "Measurement", "Pain"], "-trophy = development or nourishment. Atrophy is wasting; hypertrophy is overdevelopment."),
    (OV, "Which body cavity contains the brain and spinal cord?", "Dorsal cavity", ["Ventral cavity", "Thoracic cavity", "Pelvic cavity"], "The dorsal cavity holds the cranial cavity (brain) and spinal cavity (spinal cord)."),
    (SK, "The bones of the fingers and toes are called:", "Phalanges", ["Carpals", "Tarsals", "Metacarpals"], "Phalanges are finger and toe bones. Carpals = wrist, tarsals = ankle, metacarpals = hand."),
    (SK, "An abnormal sideways (lateral) curvature of the spine is:", "Scoliosis", ["Kyphosis", "Lordosis", "Spondylosis"], "Scoliosis = lateral curve. Kyphosis = hunchback; lordosis = swayback."),
    (MU, "Moving a limb away from the midline of the body is called:", "Abduction", ["Adduction", "Flexion", "Rotation"], "ab- (away from) + duct (to lead). Adduction moves a limb toward the midline."),
    (MU, "Myasthenia gravis is characterized by:", "Muscle weakness", ["Muscle wasting from disuse", "Inflammation of muscles", "Muscle rigidity"], "my/o (muscle) + -asthenia (weakness). It is an autoimmune disorder at the neuromuscular junction."),
    (RE, '"Dyspnea" means:', "Difficult or labored breathing", ["Absence of breathing", "Rapid breathing", "Coughing up blood"], "dys- (difficult) + -pnea (breathing)."),
    (RE, '"Hemoptysis" means:', "Coughing up blood from the respiratory tract", ["Vomiting blood", "Nosebleed", "Blood in the chest cavity"], "Hematemesis = vomiting blood, epistaxis = nosebleed, hemothorax = blood in the chest cavity."),
    (RE, "Which structure covers the larynx during swallowing?", "Epiglottis", ["Uvula", "Glottis", "Pharynx"], "The epiglottis closes over the larynx so food goes into the esophagus."),
    (DI, '"Dysphagia" means:', "Difficulty swallowing", ["Difficulty speaking", "Indigestion", "Loss of appetite"], "-phagia = swallowing. Dysphasia = difficulty speaking; dyspepsia = indigestion."),
    (DI, "The first part of the small intestine is the:", "Duodenum", ["Jejunum", "Ileum", "Cecum"], "Small intestine order: duodenum, jejunum, ileum. The cecum is the start of the large intestine."),
    (CV, 'The "myocardium" is the:', "Muscle layer of the heart", ["Inner lining of the heart", "Sac surrounding the heart", "Heart valve"], "my/o (muscle) + cardi (heart) + -um. Endocardium = inner lining; pericardium = outer sac."),
    (CV, '"Lymphadenitis" means:', "Inflammation of the lymph nodes", ["Tumor of the lymph nodes", "Swelling from lymph fluid", "Disease of lymph vessels"], "lymphaden/o (lymph node) + -itis. Swelling from lymph fluid is lymphedema."),
    (NE, "Which part of the brain coordinates balance and muscle movement?", "Cerebellum", ["Cerebrum", "Medulla oblongata", "Hypothalamus"], "The cerebellum coordinates voluntary movement and balance."),
    (NE, '"Otitis media" is inflammation of the:', "Middle ear", ["Outer ear", "Inner ear", "Eardrum only"], "ot/o (ear) + -itis; media = middle. Otitis externa is outer-ear inflammation."),
    (NE, 'A "cataract" is:', "Clouding of the lens of the eye", ["Increased pressure inside the eye", "Inflammation of the conjunctiva", "Detachment of the retina"], "Glaucoma = increased intraocular pressure; conjunctivitis = inflamed conjunctiva."),
    (EN, "Hyperthyroidism results from:", "Overproduction of thyroid hormones", ["Underproduction of thyroid hormones", "Enlarged parathyroid glands", "Low blood calcium"], "hyper- (excessive) + thyroid + -ism (condition)."),
    (EN, "Which pancreatic hormone lowers blood glucose?", "Insulin", ["Glucagon", "Cortisol", "Thyroxine"], "Insulin lowers blood glucose; glucagon raises it."),
    (RP, '"Oophorectomy" is the surgical removal of:', "An ovary", ["A fallopian tube", "The uterus", "A breast"], "oophor/o = ovary. Salpingectomy = tube, hysterectomy = uterus, mastectomy = breast."),
    (RP, "Benign prostatic hyperplasia (BPH) is:", "Non-cancerous enlargement of the prostate", ["Cancer of the prostate", "Inflammation of the prostate", "Removal of the prostate"], "hyper- (excessive) + -plasia (formation). Inflammation is prostatitis."),
    (IN, '"Erythema" means:', "Redness of the skin", ["Yellowing of the skin", "Bluish discoloration", "Lack of pigment"], "erythr/o = red. Jaundice = yellow, cyanosis = blue, albinism = lack of pigment."),
    (IN, "A second-degree burn is also called a:", "Partial-thickness burn", ["Superficial burn", "Full-thickness burn", "Subdermal burn"], "First-degree = superficial, second-degree = partial-thickness, third-degree = full-thickness."),
    (UR, '"Hematuria" means:', "Blood in the urine", ["Pus in the urine", "Painful urination", "Excessive urination"], "hemat/o (blood) + -uria (urine). Pyuria = pus, dysuria = painful, polyuria = excessive."),
    (UR, "Which tubes carry urine from the kidneys to the bladder?", "Ureters", ["Urethras", "Nephrons", "Renal pelves"], "Two ureters run from the kidneys to the bladder; the urethra carries urine out of the body."),
]

HARD = [
    (DI, '"Cholecystolithiasis" refers to:', "Stones in the gallbladder", ["Inflammation of the bile duct", "Removal of the gallbladder", "Stones in the kidney"], "cholecyst/o (gallbladder) + lith (stone) + -iasis (abnormal condition)."),
    (UR, 'Which term means "surgical fixation of a kidney"?', "Nephropexy", ["Nephrolysis", "Nephroptosis", "Nephrorrhaphy"], "-pexy = surgical fixation. -lysis = separation, -ptosis = drooping, -rrhaphy = suture."),
    (CV, "Which valve does blood pass through immediately before entering the left ventricle?", "Mitral (bicuspid) valve", ["Tricuspid valve", "Pulmonary valve", "Aortic valve"], "Left atrium → mitral (bicuspid) valve → left ventricle → aortic valve → aorta."),
    (NE, '"Myelogram" is best defined as:', "An X-ray record of the spinal cord", ["A recording of muscle activity", "Inflammation of bone marrow", "A tumor of muscle tissue"], "myel/o can mean spinal cord or bone marrow; -gram is the record. Muscle is my/o."),
    (WP, "Which pair is correctly matched?", "-malacia : softening", ["-rrhea : bursting forth", "-rrhagia : flow or discharge", "-stenosis : dilation"], "-malacia = softening. -rrhea = flow, -rrhagia = bursting forth, -stenosis = narrowing, -ectasis = dilation."),
    (WP, 'In "pericardiocentesis," which word part names the procedure?', "-centesis", ["peri-", "cardi/o", "-o-"], "-centesis (surgical puncture to remove fluid) is the procedure; peri- and cardi/o give the location."),
    (WP, "Which term contains a prefix meaning \"half\"?", "Hemiplegia", ["Hematoma", "Hemolysis", "Hepatitis"], "hemi- = half. In hematoma and hemolysis, hem/o and hemat/o mean blood."),
    (WP, "Which term describes the side of the body opposite the affected side?", "Contralateral", ["Ipsilateral", "Bilateral", "Unilateral"], "contra- (opposite) + later/o (side). Ipsilateral means the same side."),
    (WP, 'The suffix "-rrhaphy" means:', "Suturing", ["Bursting forth", "Discharge", "Rupture"], "-rrhaphy = surgical suturing, as in herniorrhaphy."),
    (WP, 'The suffix "-rrhexis" means:', "Rupture", ["Suture", "Flow", "Hemorrhage"], "-rrhexis = rupture, as in hysterorrhexis (rupture of the uterus)."),
    (WP, 'Which suffix means "process of recording"?', "-graphy", ["-gram", "-graph", "-meter"], "-graphy = the process; -gram = the record; -graph = the recording instrument; -meter = measuring instrument."),
    (WP, 'Which prefix means "all"?', "pan-", ["poly-", "multi-", "hyper-"], "pan- = all (pandemic). poly- and multi- mean many."),
    (WP, 'The combining form "phren/o" can mean the mind or the:', "Diaphragm", ["Pharynx", "Pleura", "Pericardium"], "phren/o = diaphragm or mind (phrenic nerve, schizophrenia)."),
    (WP, 'Which pair of combining forms both mean "vein"?', "phleb/o and ven/o", ["angi/o and vas/o", "arteri/o and aort/o", "lymph/o and lymphaden/o"], "phleb/o and ven/o = vein. angi/o and vas/o = vessel."),
    (WP, "An abnormal fear of open or public places is:", "Agoraphobia", ["Claustrophobia", "Acrophobia", "Xenophobia"], "agora (marketplace) + -phobia. Claustrophobia = closed spaces; acrophobia = heights."),
    (WP, 'The prefix "meta-" means:', "Change or beyond", ["Middle", "Small", "Before"], "meta- = change or beyond, as in metastasis (spread of cancer beyond its origin)."),
    (WP, "Which term means \"formation of blood cells\"?", "Hematopoiesis", ["Hemolysis", "Hemostasis", "Hematemesis"], "-poiesis = formation. Hemolysis = destruction; hemostasis = stopping bleeding; hematemesis = vomiting blood."),
    (WP, 'The suffix "-stasis" means:', "Stopping or controlling", ["Flowing", "Dissolving", "Spreading"], "-stasis = stopping or standing still, as in hemostasis."),
    (WP, "Which term means \"enlargement of the heart\"?", "Cardiomegaly", ["Cardiomyopathy", "Cardiomalacia", "Cardiorrhexis"], "-megaly = enlargement. -pathy = disease, -malacia = softening, -rrhexis = rupture."),
    (WP, "A condition that is present at birth is described as:", "Congenital", ["Idiopathic", "Iatrogenic", "Acquired"], "Congenital = present at birth. Idiopathic = unknown cause; iatrogenic = caused by treatment."),
    (WP, "An iatrogenic illness is one that is:", "Caused by medical treatment", ["Of unknown cause", "Present at birth", "Acquired in a hospital"], "iatr/o = physician or treatment. A hospital-acquired infection is nosocomial."),
    (WP, 'Which suffix means "eating or swallowing"?', "-phagia", ["-phasia", "-plasia", "-phobia"], "-phagia = eating or swallowing. -phasia = speech; -plasia = formation."),
    (WP, 'The suffix "-plasia" means:', "Formation or development", ["Surgical repair", "Paralysis", "Speech"], "-plasia = formation (dysplasia, hyperplasia). -plasty = surgical repair."),
    (WP, 'Which term contains a combining form meaning "stone"?', "Lithotripsy", ["Lipectomy", "Lymphoma", "Leukocyte"], "lith/o = stone. lip/o = fat, lymph/o = lymph, leuk/o = white."),
    (WP, 'Which combining form means "yellow"?', "xanth/o", ["cyan/o", "chlor/o", "erythr/o"], "xanth/o = yellow. cyan/o = blue, chlor/o = green, erythr/o = red."),
    (WP, 'Which term means "within a vein"?', "Intravenous", ["Intervenous", "Perivenous", "Transvenous"], "intra- = within; inter- = between; peri- = around; trans- = across."),
    (WP, 'What is the plural of "diagnosis"?', "Diagnoses", ["Diagnosises", "Diagnosae", "Diagnosi"], "Words ending in -is form the plural by changing -is to -es."),
    (OV, "The area at the back of the knee is the:", "Popliteal region", ["Antecubital region", "Inguinal region", "Gluteal region"], "Popliteal = back of the knee; antecubital = front of the elbow; inguinal = groin."),
    (OV, "Which abdominal region lies directly above the umbilical region?", "Epigastric", ["Hypogastric", "Right hypochondriac", "Left lumbar"], "epi- (above) + gastr/o. The hypogastric region lies below the umbilical region."),
    (OV, "Which tissue type covers body surfaces and lines body cavities?", "Epithelial", ["Connective", "Muscle", "Nervous"], "Epithelial tissue forms the skin's outer layer and lines cavities and organs."),
    (SK, "Which bone is NOT part of the axial skeleton?", "Scapula", ["Sternum", "Vertebrae", "Ribs"], "The scapula is part of the pectoral girdle, which belongs to the appendicular skeleton."),
    (SK, "A comminuted fracture is one in which the bone is:", "Splintered or crushed into several pieces", ["Broken through the skin", "Bent and partly broken, as in children", "Driven into another fragment"], "Open (compound) = through the skin; greenstick = bent and partly broken; impacted = driven together."),
    (MU, '"Dorsiflexion" is:', "Bending the foot upward toward the leg", ["Pointing the toes downward", "Turning the sole inward", "Turning the palm upward"], "Plantar flexion points the toes down; inversion turns the sole inward; supination turns the palm up."),
    (MU, "Rhabdomyolysis is the breakdown of:", "Skeletal (striated) muscle", ["Smooth muscle", "Cardiac muscle only", "Tendons"], "rhabd/o = striated; my/o = muscle; -lysis = breakdown. leiomy/o = smooth muscle."),
    (RE, "A surgically created opening into the trachea, with a tube inserted to keep the airway open, is a:", "Tracheostomy", ["Tracheotomy", "Tracheoplasty", "Tracheorrhaphy"], "-ostomy creates a lasting opening (stoma). -otomy is only the incision itself."),
    (RE, '"Atelectasis" is:', "A collapsed or incompletely expanded lung", ["Air in the pleural cavity", "Fluid in the alveoli", "Dilation of the bronchi"], "Pneumothorax = air in the pleural cavity; pulmonary edema = fluid; bronchiectasis = dilated bronchi."),
    (RE, "The exchange of oxygen and carbon dioxide in the lungs takes place in the:", "Alveoli", ["Bronchioles", "Trachea", "Pleura"], "Gas exchange happens across the thin walls of the alveoli and surrounding capillaries."),
    (DI, '"Cheilosis" is a disorder of the:', "Lips", ["Gums", "Tongue", "Cheeks"], "cheil/o = lip. gingiv/o = gums, gloss/o = tongue, bucc/o = cheek."),
    (DI, 'An "anastomosis" is:', "A surgical connection between two hollow structures", ["An abnormal passage between two organs", "An abnormal narrowing", "A complete blockage"], "An anastomosis joins two hollow structures. An abnormal passage is a fistula."),
    (CV, "Which term describes the contraction phase of the heartbeat?", "Systole", ["Diastole", "Fibrillation", "Bradycardia"], "Systole = contraction; diastole = relaxation."),
    (CV, 'A "hemangioma" is:', "A benign tumor made of blood vessels", ["A blood clot", "Bleeding from a vessel", "Hardening of a vessel"], "hem/o (blood) + angi/o (vessel) + -oma (tumor). A clot is a thrombus."),
    (NE, "From outermost to innermost, the meninges are the:", "Dura mater, arachnoid membrane, pia mater", ["Pia mater, arachnoid membrane, dura mater", "Arachnoid membrane, dura mater, pia mater", "Dura mater, pia mater, arachnoid membrane"], "Dura (tough, outer), arachnoid (middle), pia (delicate, on the brain surface)."),
    (NE, '"Presbyopia" is:', "Age-related loss of the ability to focus on near objects", ["Nearsightedness", "Farsightedness present from birth", "Age-related hearing loss"], "presby/o = old age; -opia = vision. Age-related hearing loss is presbycusis."),
    (EN, "Which gland secretes epinephrine?", "Adrenal medulla", ["Adrenal cortex", "Thyroid", "Pituitary"], "The adrenal medulla secretes epinephrine; the adrenal cortex secretes cortisol and aldosterone."),
    (EN, "Acromegaly is caused by:", "Too much growth hormone in adulthood", ["Too little thyroid hormone in infancy", "Too much cortisol", "Too little insulin"], "acr/o (extremities) + -megaly. Excess cortisol causes Cushing syndrome."),
    (RP, '"Salpingo-oophorectomy" is the removal of:', "A fallopian tube and an ovary", ["The uterus and cervix", "Both breasts", "The ovaries only"], "salping/o = fallopian tube; oophor/o = ovary; -ectomy = removal."),
    (RP, '"Cryptorchidism" is:', "An undescended testicle", ["Absence of sperm", "Inflammation of a testis", "Twisting of the spermatic cord"], "crypt/o = hidden; orchid/o = testis. Orchitis = inflammation; testicular torsion = twisting."),
    (IN, "Which layer of the skin has no blood vessels?", "Epidermis", ["Dermis", "Subcutaneous layer", "Hypodermis"], "The epidermis is avascular; it gets nutrients from the dermis below."),
    (IN, '"Onychomycosis" is:', "A fungal infection of the nails", ["An ingrown nail", "Inflammation around the nail", "Softening of the nails"], "onych/o (nail) + myc/o (fungus) + -osis. Paronychia = infection around the nail."),
    (UR, "Which term means excessive urination at night?", "Nocturia", ["Polyuria", "Enuresis", "Oliguria"], "noct/i (night) + -uria. Polyuria = excessive amount; enuresis = bedwetting; oliguria = scanty urine."),
]

PLAN = {WP: 23, OV: 3, SK: 2, MU: 2, RE: 3, DI: 3, CV: 3, NE: 3, EN: 2, RP: 2, IN: 2, UR: 2}

def build(rows, seed):
    rng = random.Random(seed)
    assert len(rows) == 50, len(rows)
    assert Counter(r[0] for r in rows) == Counter(PLAN), Counter(r[0] for r in rows)
    assert len({r[1] for r in rows}) == 50, "duplicate question"
    rows = rows[:]
    rng.shuffle(rows)
    out = []
    for topic, q, right, wrong, expl in rows:
        assert len(wrong) == 3 and right not in wrong
        opts = [right] + wrong
        rng.shuffle(opts)
        out.append({"q": q, "options": opts, "answer": opts.index(right), "explanation": expl, "topic": topic})
    return out

tests = {"easy": build(EASY, 1), "medium": build(MEDIUM, 2), "hard": build(HARD, 3)}
all_q = [q["q"] for lvl in tests.values() for q in lvl]
assert len(set(all_q)) == len(all_q), "duplicate across levels"
for k, v in tests.items():
    print(k, len(v), "answer positions:", dict(sorted(Counter("ABCD"[q["answer"]] for q in v).items())))

js = ("// Medical Terminology practice tests: 50 questions each, matching the official Round One test.\n"
      "// Topics follow the 2026-27 test plan (word parts 45%, each body area 5%).\n"
      "window.CONTENT = window.CONTENT || {};\n"
      "window.CONTENT[\"medical-terminology\"] = window.CONTENT[\"medical-terminology\"] || {};\n"
      "window.CONTENT[\"medical-terminology\"].tests = " + json.dumps(tests, indent=1, ensure_ascii=False) + ";\n")
open(sys.argv[1], "w", encoding="utf-8").write(js)
