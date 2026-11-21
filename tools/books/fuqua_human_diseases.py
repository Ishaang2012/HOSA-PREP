# Frazier & Fuqua - Essentials of Human Diseases and Conditions.
# Chapter list: 8th edition, from the publisher's table of contents (us.elsevierhealth.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Mechanisms of Disease, Diagnosis, and Treatment", "Disease is a change in body structure or function. Causes include genetic factors, infection, inflammation, trauma, nutritional imbalance, immune problems, and neoplasms (benign or malignant). Terms: etiology (cause), pathogenesis (development), signs (objective), symptoms (subjective), acute vs. chronic, diagnosis, prognosis, and idiopathic (unknown cause). Treatment can be curative or palliative.", ["Etiology = cause; prognosis = outcome", "Signs objective; symptoms subjective", "Acute vs. chronic", "Idiopathic = unknown cause"]),
    ch(2, "Developmental, Congenital, and Childhood Diseases and Disorders", "Congenital conditions are present at birth and may be genetic (Down syndrome/trisomy 21, cystic fibrosis, sickle cell anemia, PKU) or caused by prenatal factors (fetal alcohol syndrome). Others include spina bifida, cleft lip and palate, and congenital heart defects. Childhood diseases include infections (measles, mumps, chickenpox, pertussis) prevented by vaccines, ADHD, and autism spectrum disorder.", ["Down syndrome = trisomy 21", "Cystic fibrosis and sickle cell are genetic", "Spina bifida = neural tube defect", "Vaccines prevent childhood infections"]),
    ch(3, "Immunologic Diseases and Conditions", "The immune system defends the body. Immunodeficiency disorders include HIV/AIDS. Hypersensitivity reactions include allergies and anaphylaxis (treated with epinephrine). Autoimmune diseases occur when the body attacks itself: systemic lupus erythematosus, rheumatoid arthritis, multiple sclerosis, and others.", ["HIV causes AIDS", "Anaphylaxis → epinephrine", "Autoimmune = body attacks itself", "Lupus is autoimmune"]),
    ch(4, "Diseases and Conditions of the Endocrine System", "Endocrine disorders involve hormone excess or deficiency. Examples: pituitary (gigantism, acromegaly, diabetes insipidus), thyroid (hypothyroidism, hyperthyroidism/Graves disease, goiter), parathyroid, adrenal (Cushing syndrome, Addison disease), and pancreas (diabetes mellitus type 1, type 2, gestational).", ["Graves disease = hyperthyroidism", "Cushing = excess cortisol; Addison = deficiency", "Diabetes insipidus = ADH problem", "Type 1 vs. type 2 diabetes"]),
    ch(5, "Diseases and Disorders of the Eye and Ear", "Eye disorders include refractive errors (myopia, hyperopia, astigmatism, presbyopia), cataracts, glaucoma, macular degeneration, conjunctivitis, and retinal detachment. Ear disorders include otitis media, otitis externa, Ménière disease, tinnitus, and conductive and sensorineural hearing loss.", ["Glaucoma = increased eye pressure", "Cataract = cloudy lens", "Otitis media = middle ear infection", "Conductive vs. sensorineural hearing loss"]),
    ch(6, "Diseases and Conditions of the Integumentary System", "Skin conditions include dermatitis, eczema, psoriasis, acne, urticaria, infections (impetigo, cellulitis, fungal infections, herpes zoster), parasites (lice, scabies), pressure injuries, burns, and skin cancers (basal cell, squamous cell, and malignant melanoma).", ["Psoriasis: silvery plaques", "Impetigo: contagious bacterial infection", "Melanoma is most dangerous", "Shingles = herpes zoster"]),
    ch(7, "Diseases and Conditions of the Musculoskeletal System", "Musculoskeletal conditions include osteoporosis, osteoarthritis, rheumatoid arthritis, gout, fractures, sprains and strains, scoliosis, kyphosis, lordosis, carpal tunnel syndrome, bursitis, tendinitis, muscular dystrophy, and bone tumors.", ["Osteoporosis = low bone density", "Gout = uric acid crystals", "Scoliosis = lateral curvature", "Carpal tunnel = median nerve compression"]),
    ch(8, "Diseases and Conditions of the Digestive System", "Digestive disorders include GERD, peptic ulcers (often H. pylori), gastroenteritis, appendicitis, hernias, inflammatory bowel disease (Crohn's disease, ulcerative colitis), irritable bowel syndrome, diverticulitis, hepatitis, cirrhosis, gallstones, pancreatitis, and colorectal cancer.", ["H. pylori causes many ulcers", "Crohn's vs. ulcerative colitis", "Cirrhosis = liver scarring", "Cholelithiasis = gallstones"]),
    ch(9, "Diseases and Conditions of the Respiratory System", "Respiratory disorders include the common cold, influenza, pneumonia, tuberculosis, asthma, COPD (chronic bronchitis and emphysema), cystic fibrosis, pulmonary embolism, pneumothorax, and lung cancer (most often caused by smoking).", ["COPD = bronchitis + emphysema", "TB spread by airborne droplets", "Pulmonary embolism = clot in lung", "Smoking causes most lung cancer"]),
    ch(10, "Diseases and Conditions of the Circulatory System", "Circulatory disorders include coronary artery disease, angina, myocardial infarction, heart failure, arrhythmias, hypertension, atherosclerosis, aneurysms, varicose veins, deep vein thrombosis, and blood disorders such as anemias (iron-deficiency, pernicious, sickle cell) and leukemia.", ["MI = heart attack", "Atherosclerosis = plaque buildup", "DVT can cause pulmonary embolism", "Leukemia = cancer of white blood cells"]),
    ch(11, "Diseases and Conditions of the Urinary System", "Urinary disorders include urinary tract infections, cystitis, pyelonephritis, glomerulonephritis, kidney stones (nephrolithiasis), acute and chronic kidney failure, polycystic kidney disease, urinary incontinence, and bladder cancer.", ["Cystitis = bladder infection", "Pyelonephritis = kidney infection", "Nephrolithiasis = kidney stones", "Chronic kidney failure may need dialysis"]),
    ch(12, "Diseases and Conditions of the Reproductive System", "Reproductive disorders include benign prostatic hyperplasia, prostate and testicular cancer, endometriosis, uterine fibroids, ovarian cysts, cervical and breast cancer, infertility, pregnancy complications (ectopic pregnancy, preeclampsia), and sexually transmitted infections (chlamydia, gonorrhea, syphilis, HPV, herpes).", ["BPH = enlarged prostate", "Endometriosis = tissue outside the uterus", "HPV can cause cervical cancer", "Ectopic pregnancy is an emergency"]),
    ch(13, "Neurologic Diseases and Conditions", "Neurologic disorders include headaches and migraines, epilepsy, stroke (CVA) and TIA, meningitis, encephalitis, Parkinson disease, Alzheimer disease, multiple sclerosis, amyotrophic lateral sclerosis (ALS), Bell's palsy, spinal cord injuries, and concussions.", ["Stroke = interrupted blood flow to the brain", "Parkinson: dopamine loss, tremors", "MS: myelin damage", "Meningitis: inflamed meninges"]),
    ch(14, "Mental Disorders", "Mental disorders, diagnosed using the DSM, include anxiety disorders, depression, bipolar disorder, schizophrenia, obsessive-compulsive disorder, PTSD, personality disorders, eating disorders (anorexia, bulimia), substance use disorders, and neurodevelopmental disorders such as ADHD and autism.", ["DSM used for diagnosis", "Bipolar = mania + depression", "Schizophrenia: hallucinations, delusions", "PTSD follows trauma"]),
    ch(15, "Disorders and Conditions Resulting From Trauma", "Trauma causes injuries such as fractures, head injuries, spinal cord injuries, burns, wounds, crush injuries, and environmental injuries (heat stroke, hypothermia, frostbite). Physical and psychological trauma, including abuse, may need long-term care.", ["Burns: superficial to full thickness", "Heat stroke is an emergency", "Head and spinal cord injuries", "Hypothermia and frostbite"]),
]

Q = [
    ((1, 2, 3), [
        (1, "The cause of a disease is its:", "Etiology", ["Prognosis", "Pathogenesis", "Diagnosis"], "Prognosis is the expected outcome."),
        (1, "A disease with an unknown cause is:", "Idiopathic", ["Iatrogenic", "Congenital", "Acute"], "Iatrogenic means caused by treatment."),
        (1, "Treatment that relieves symptoms without curing is:", "Palliative", ["Curative", "Preventive", "Diagnostic"], "Hospice care is palliative."),
        (2, "Down syndrome is caused by:", "Trisomy 21", ["A missing X chromosome", "Infection", "Lack of folic acid only"], "An extra copy of chromosome 21."),
        (2, "Spina bifida is a:", "Neural tube defect", ["Heart defect", "Blood disorder", "Skin condition"], "Folic acid helps prevent it."),
        (2, "Which childhood disease is prevented by the MMR vaccine?", "Measles", ["Pertussis", "Chickenpox only", "Polio"], "MMR = measles, mumps, rubella."),
        (3, "When the immune system attacks the body's own tissues, it's an:", "Autoimmune disease", ["Immunodeficiency", "Allergy only", "Infection"], "Lupus and rheumatoid arthritis are examples."),
        (3, "Anaphylaxis is treated first with:", "Epinephrine", ["Antibiotics", "Insulin", "Aspirin"], "It's a life-threatening allergic reaction."),
        (3, "AIDS is caused by:", "HIV", ["Hepatitis B", "Influenza", "Bacteria"], "HIV attacks CD4 T cells."),
    ]),
    ((4, 5, 6), [
        (4, "Graves disease causes:", "Hyperthyroidism", ["Hypothyroidism", "Diabetes", "Addison disease"], "Signs include weight loss and bulging eyes."),
        (4, "Too much cortisol causes:", "Cushing syndrome", ["Addison disease", "Diabetes insipidus", "Gigantism"], "Addison disease is too little."),
        (4, "Type 1 diabetes is caused by:", "Lack of insulin production", ["Insulin resistance", "Too much ADH", "An overactive thyroid"], "It's autoimmune."),
        (5, "Increased pressure inside the eye is:", "Glaucoma", ["Cataract", "Conjunctivitis", "Myopia"], "It can damage the optic nerve."),
        (5, "A middle ear infection is:", "Otitis media", ["Otitis externa", "Tinnitus", "Ménière disease"], "Common in children."),
        (5, "Clouding of the eye's lens is a:", "Cataract", ["Glaucoma", "Stye", "Detached retina"], "Treated with surgery."),
        (6, "The most dangerous skin cancer is:", "Malignant melanoma", ["Basal cell carcinoma", "Squamous cell carcinoma", "Actinic keratosis"], "Use the ABCDE rule."),
        (6, "Shingles is caused by the:", "Varicella-zoster virus", ["Herpes simplex type 1", "Staph bacteria", "A fungus"], "The chickenpox virus reactivates."),
        (6, "Thick, silvery-scaled plaques are typical of:", "Psoriasis", ["Eczema", "Impetigo", "Acne"], "It's autoimmune."),
    ]),
    ((7, 8, 9), [
        (7, "Loss of bone density that makes bones fragile is:", "Osteoporosis", ["Osteoarthritis", "Gout", "Scoliosis"], "Common in older women."),
        (7, "Gout is caused by:", "Uric acid crystals in joints", ["Bacteria", "Calcium loss", "Autoimmunity"], "Often affects the big toe."),
        (7, "Compression of the median nerve at the wrist is:", "Carpal tunnel syndrome", ["Bursitis", "Tendinitis", "Sciatica"], "Causes numbness in the fingers."),
        (8, "Many peptic ulcers are caused by:", "H. pylori bacteria", ["Spicy food alone", "Viruses", "Stress only"], "NSAIDs are another cause."),
        (8, "Scarring of the liver is:", "Cirrhosis", ["Hepatitis", "Cholecystitis", "Pancreatitis"], "Often from alcohol or hepatitis."),
        (8, "Inflammatory bowel diseases include Crohn's disease and:", "Ulcerative colitis", ["GERD", "Gastroenteritis", "Appendicitis"], "Both are chronic."),
        (9, "COPD includes emphysema and:", "Chronic bronchitis", ["Asthma", "Pneumonia", "Tuberculosis"], "Usually caused by smoking."),
        (9, "A blood clot in the lung's arteries is a:", "Pulmonary embolism", ["Pneumothorax", "Pleural effusion", "Atelectasis"], "Often from a DVT."),
        (9, "Tuberculosis spreads through:", "Airborne droplets", ["Contaminated food", "Mosquitoes", "Skin contact"], "It mainly affects the lungs."),
    ]),
    ((10, 11, 12), [
        (10, "A heart attack is a:", "Myocardial infarction", ["Angina", "Arrhythmia", "Aneurysm"], "Heart muscle dies from lack of blood."),
        (10, "Plaque buildup in arteries is:", "Atherosclerosis", ["Anemia", "Varicose veins", "Leukemia"], "It leads to heart disease and stroke."),
        (10, "Cancer of the blood-forming cells is:", "Leukemia", ["Lymphoma", "Anemia", "Hemophilia"], "Abnormal white cells crowd out normal cells."),
        (11, "A kidney infection is:", "Pyelonephritis", ["Cystitis", "Urethritis", "Nephrolithiasis"], "Cystitis is a bladder infection."),
        (11, "Kidney stones are called:", "Nephrolithiasis", ["Cholelithiasis", "Glomerulonephritis", "Hydronephrosis"], "Cholelithiasis = gallstones."),
        (11, "End-stage kidney failure may require:", "Dialysis or transplant", ["Antibiotics only", "Surgery on the bladder", "Nothing"], "Dialysis filters the blood."),
        (12, "An enlarged prostate that isn't cancer is:", "Benign prostatic hyperplasia", ["Prostatitis", "Prostate cancer", "Orchitis"], "It causes urinary symptoms."),
        (12, "Uterine lining tissue growing outside the uterus is:", "Endometriosis", ["Fibroids", "Ovarian cysts", "PID"], "It causes painful periods."),
        (12, "Which STI can cause cervical cancer?", "HPV", ["Chlamydia", "Gonorrhea", "Trichomoniasis"], "Vaccination prevents most cases."),
    ]),
    ((13, 14, 15), [
        (13, "A stroke is caused by:", "Interrupted blood flow to the brain", ["A heart infection", "A spinal fracture", "Low blood sugar"], "Also called a CVA."),
        (13, "Parkinson disease involves loss of neurons that make:", "Dopamine", ["Serotonin", "Insulin", "Adrenaline"], "Causes tremors and rigidity."),
        (13, "Multiple sclerosis damages the:", "Myelin sheath", ["Bones", "Heart valves", "Muscles directly"], "It's autoimmune."),
        (14, "Mental disorders are diagnosed using the:", "DSM", ["ICD-10-PCS", "CPT", "Braden Scale"], "Diagnostic and Statistical Manual."),
        (14, "Episodes of mania and depression are features of:", "Bipolar disorder", ["Schizophrenia", "OCD", "Anxiety disorder"], "Mood stabilizers are used."),
        (14, "Hallucinations and delusions are symptoms of:", "Schizophrenia", ["Phobia", "ADHD", "Anorexia"], "It's a psychotic disorder."),
        (15, "A full-thickness burn involves:", "All layers of skin", ["Only the epidermis", "Only redness", "Only the dermis"], "It may look white or charred."),
        (15, "A dangerously high body temperature with confusion after heat exposure is:", "Heat stroke", ["Heat cramps", "Hypothermia", "Frostbite"], "It's a medical emergency."),
        (15, "Freezing of body tissue from cold is:", "Frostbite", ["Hypothermia", "Heat exhaustion", "Burn"], "Hypothermia is low body temperature."),
    ]),
]

BOOK = {
    "titles": ["Essentials of Human Diseases and Conditions"],
    "edition": "8th edition",
    "source": "Elsevier table of contents",
    "chapters": C,
    "quizzes": Q,
}
