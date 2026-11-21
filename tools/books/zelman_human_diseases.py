# Zelman et al. - Human Diseases: A Systemic Approach (Pearson).
# Chapter list: 8th edition, from the publisher's table of contents (pearson.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Introduction to Disease", "Disease disrupts homeostasis. Key terms: etiology (cause), pathogenesis (development), signs (objective) and symptoms (subjective), syndrome (group of signs and symptoms), acute vs. chronic, diagnosis, prognosis, morbidity (illness rate), and mortality (death rate). Risk factors include age, genetics, lifestyle, and environment.", ["Etiology and pathogenesis", "Signs vs. symptoms", "Morbidity vs. mortality", "Risk factors"]),
    ch(2, "Immunity, Inflammation, and Immune Disorders", "Inflammation's cardinal signs are redness, heat, swelling, pain, and loss of function. Innate immunity is nonspecific; adaptive immunity uses B and T cells. Disorders include hypersensitivity (allergies, anaphylaxis), autoimmune diseases (lupus, rheumatoid arthritis), and immunodeficiencies (HIV/AIDS).", ["Five signs of inflammation", "Innate vs. adaptive", "Anaphylaxis", "Autoimmune diseases"]),
    ch(3, "Infectious Diseases and Infection Control", "Pathogens include bacteria, viruses, fungi, protozoa, helminths, and prions. The chain of infection is broken by hand hygiene, standard precautions, vaccines, and sterilization. Antibiotics treat bacteria, not viruses; overuse leads to resistance (MRSA).", ["Types of pathogens", "Chain of infection", "Antibiotics don't treat viruses", "Antibiotic resistance"]),
    ch(4, "Neoplasms", "Neoplasms are benign (slow, encapsulated, non-spreading) or malignant (invasive, can metastasize). Carcinomas arise from epithelial tissue; sarcomas from connective tissue. Cancers are graded and staged (TNM). Warning signs include unusual bleeding, lumps, and changes in moles. Treatment includes surgery, chemotherapy, radiation, and immunotherapy.", ["Benign vs. malignant", "Carcinoma vs. sarcoma", "Metastasis", "TNM staging"]),
    ch(5, "Heredity and Disease", "Genetic diseases can be autosomal dominant (Huntington disease), autosomal recessive (cystic fibrosis, sickle cell, PKU, Tay-Sachs), sex-linked (hemophilia, Duchenne muscular dystrophy), or chromosomal (Down syndrome, Turner, Klinefelter). Genetic testing and counseling help families.", ["Autosomal dominant vs. recessive", "X-linked disorders", "Chromosomal disorders", "Genetic counseling"]),
    ch(6, "Diseases and Disorders of the Cardiovascular System", "Cardiovascular diseases include hypertension, atherosclerosis, coronary artery disease, angina, myocardial infarction, heart failure, arrhythmias, valve diseases, aneurysms, and peripheral vascular disease. Risk factors include smoking, high cholesterol, diabetes, obesity, and inactivity.", ["Atherosclerosis", "MI = heart attack", "Heart failure", "Modifiable risk factors"]),
    ch(7, "Diseases and Disorders of the Blood", "Blood disorders include anemias (iron-deficiency, pernicious/B12, aplastic, sickle cell), polycythemia, leukemias, lymphomas, and clotting disorders (hemophilia, thrombocytopenia).", ["Iron-deficiency anemia", "Pernicious anemia = B12", "Leukemia", "Hemophilia"]),
    ch(8, "Diseases and Disorders of the Respiratory System", "Respiratory disorders include upper respiratory infections, influenza, pneumonia, tuberculosis, asthma, COPD (emphysema and chronic bronchitis), cystic fibrosis, lung cancer, pulmonary embolism, and pneumothorax.", ["COPD", "Asthma", "Tuberculosis", "Lung cancer and smoking"]),
    ch(9, "Diseases and Disorders of the Digestive System", "Digestive disorders include GERD, peptic ulcers (H. pylori), gastroenteritis, appendicitis, IBD (Crohn's, ulcerative colitis), IBS, diverticular disease, hepatitis, cirrhosis, gallstones, pancreatitis, and colorectal cancer.", ["H. pylori ulcers", "Crohn's vs. ulcerative colitis", "Hepatitis and cirrhosis", "Colorectal cancer screening"]),
    ch(10, "Diseases and Disorders of the Urinary System", "Urinary disorders include UTIs (cystitis, pyelonephritis), glomerulonephritis, kidney stones, polycystic kidney disease, and acute and chronic kidney failure (dialysis or transplant).", ["Cystitis vs. pyelonephritis", "Kidney stones", "Glomerulonephritis", "Dialysis"]),
    ch(11, "Diseases and Disorders of the Reproductive System", "Reproductive disorders include BPH and prostate cancer, testicular cancer, endometriosis, fibroids, PCOS, menstrual disorders, breast and cervical cancer, infertility, and STIs such as chlamydia, gonorrhea, syphilis, herpes, and HPV.", ["BPH", "Endometriosis", "HPV and cervical cancer", "STIs"]),
    ch(12, "Diseases and Disorders of the Endocrine System", "Endocrine disorders involve too much or too little hormone: gigantism and acromegaly, diabetes insipidus, hypo- and hyperthyroidism, Cushing syndrome, Addison disease, and diabetes mellitus (type 1, type 2, gestational).", ["Diabetes mellitus types", "Hypo- vs. hyperthyroidism", "Cushing vs. Addison", "Acromegaly"]),
    ch(13, "Diseases and Disorders of the Nervous System", "Nervous system disorders include stroke (ischemic and hemorrhagic) and TIA, epilepsy, meningitis, encephalitis, Parkinson disease, Alzheimer disease, multiple sclerosis, ALS, traumatic brain and spinal cord injuries, and headaches.", ["Ischemic vs. hemorrhagic stroke", "Epilepsy", "Parkinson and Alzheimer", "MS and ALS"]),
    ch(14, "Diseases and Disorders of the Special Senses", "Eye disorders include refractive errors, cataracts, glaucoma, macular degeneration, and conjunctivitis. Ear disorders include otitis media and externa, hearing loss (conductive and sensorineural), tinnitus, and Ménière disease.", ["Cataract and glaucoma", "Macular degeneration", "Otitis media", "Types of hearing loss"]),
    ch(15, "Mental Illness and Cognitive Disorders", "Mental illnesses include anxiety disorders, mood disorders (depression, bipolar), schizophrenia, personality disorders, eating disorders, substance use disorders, and ADHD. Cognitive disorders include delirium (sudden, reversible) and dementia (gradual, progressive).", ["Depression and bipolar", "Schizophrenia", "Delirium vs. dementia", "Substance use disorders"]),
    ch(16, "Diseases and Disorders of the Bones, Joints, and Muscles", "Musculoskeletal disorders include fractures, osteoporosis, osteoarthritis, rheumatoid arthritis, gout, scoliosis, osteomyelitis, sprains and strains, muscular dystrophy, and fibromyalgia.", ["Osteoporosis", "Osteoarthritis vs. rheumatoid arthritis", "Gout", "Muscular dystrophy"]),
    ch(17, "Diseases and Disorders of the Skin", "Skin disorders include dermatitis, eczema, psoriasis, acne, infections (impetigo, cellulitis, fungal infections, warts, herpes zoster), parasites (lice, scabies), burns, pressure injuries, and skin cancers (basal cell, squamous cell, melanoma).", ["Psoriasis", "Impetigo", "Melanoma (ABCDE)", "Scabies and lice"]),
]

Q = [
    ((1, 2, 3), [
        (1, "The study of a disease's cause is:", "Etiology", ["Prognosis", "Pathogenesis", "Epidemiology only"], "Pathogenesis is how it develops."),
        (1, "A group of signs and symptoms occurring together is a:", "Syndrome", ["Diagnosis", "Prognosis", "Sign"], "Example: Down syndrome."),
        (1, "The rate of illness in a population is:", "Morbidity", ["Mortality", "Prognosis", "Etiology"], "Mortality is the death rate."),
        (2, "Which is a cardinal sign of inflammation?", "Swelling", ["Pallor", "Cold skin", "Numbness"], "Redness, heat, swelling, pain, loss of function."),
        (2, "Lupus and rheumatoid arthritis are:", "Autoimmune diseases", ["Immunodeficiencies", "Infections", "Cancers"], "Body attacks itself."),
        (2, "A severe, life-threatening allergic reaction is:", "Anaphylaxis", ["Urticaria only", "Rhinitis", "Dermatitis"], "Treat with epinephrine."),
        (3, "Antibiotics are effective against:", "Bacteria", ["Viruses", "Prions", "All pathogens"], "Not viruses."),
        (3, "MRSA is an example of:", "Antibiotic resistance", ["A virus", "A fungal infection", "An autoimmune disease"], "From overuse of antibiotics."),
        (3, "Infectious proteins that cause brain diseases are:", "Prions", ["Viruses", "Fungi", "Protozoa"], "E.g., Creutzfeldt-Jakob disease."),
    ]),
    ((4, 5, 6), [
        (4, "The spread of cancer to distant sites is:", "Metastasis", ["Hyperplasia", "Remission", "Dysplasia"], "Through blood or lymph."),
        (4, "Cancer arising from epithelial tissue is a:", "Carcinoma", ["Sarcoma", "Lymphoma", "Leukemia"], "Sarcomas arise from connective tissue."),
        (4, "A benign tumor is usually:", "Encapsulated and non-spreading", ["Invasive", "Metastatic", "Always fatal"], "Slow-growing."),
        (5, "Cystic fibrosis is inherited as:", "Autosomal recessive", ["Autosomal dominant", "X-linked", "Chromosomal"], "Two copies needed."),
        (5, "Huntington disease is inherited as:", "Autosomal dominant", ["Autosomal recessive", "X-linked recessive", "Mitochondrial"], "One copy causes disease."),
        (5, "A female with only one X chromosome has:", "Turner syndrome", ["Klinefelter syndrome", "Down syndrome", "Fragile X"], "45,X."),
        (6, "Plaque buildup in artery walls is:", "Atherosclerosis", ["Aneurysm", "Arrhythmia", "Anemia"], "Leads to CAD and stroke."),
        (6, "Death of heart muscle from blocked blood flow is a:", "Myocardial infarction", ["Angina", "Arrhythmia", "Cardiomyopathy"], "Heart attack."),
        (6, "A modifiable cardiovascular risk factor is:", "Smoking", ["Age", "Genetics", "Sex"], "Can be changed."),
    ]),
    ((7, 8, 9), [
        (7, "Anemia caused by lack of vitamin B12 absorption is:", "Pernicious anemia", ["Iron-deficiency anemia", "Aplastic anemia", "Sickle cell anemia"], "Lacks intrinsic factor."),
        (7, "The most common anemia worldwide is:", "Iron-deficiency anemia", ["Aplastic anemia", "Pernicious anemia", "Hemolytic anemia"], "Common in women and children."),
        (7, "A low platelet count is:", "Thrombocytopenia", ["Leukopenia", "Polycythemia", "Anemia"], "Causes bleeding."),
        (8, "Emphysema and chronic bronchitis together are:", "COPD", ["Asthma", "Pneumonia", "TB"], "Mostly from smoking."),
        (8, "Tuberculosis is caused by:", "A bacterium", ["A virus", "A fungus", "A prion"], "Mycobacterium tuberculosis."),
        (8, "Reversible airway narrowing with wheezing is:", "Asthma", ["Emphysema", "Lung cancer", "TB"], "Triggered by allergens or exercise."),
        (9, "Most peptic ulcers are caused by:", "H. pylori", ["Spicy food", "Viruses", "Stress only"], "Treated with antibiotics."),
        (9, "IBD that can affect any part of the GI tract is:", "Crohn's disease", ["Ulcerative colitis", "IBS", "GERD"], "UC affects only the colon."),
        (9, "Scarring of the liver is:", "Cirrhosis", ["Hepatitis", "Cholecystitis", "Pancreatitis"], "Often from alcohol."),
    ]),
    ((10, 11, 12), [
        (10, "A bladder infection is:", "Cystitis", ["Pyelonephritis", "Nephritis", "Urethritis"], "More common in women."),
        (10, "Kidney stones are called:", "Renal calculi", ["Cysts", "Polyps", "Casts"], "Nephrolithiasis."),
        (10, "Chronic kidney failure may require:", "Dialysis or transplant", ["Antibiotics only", "Surgery on the bladder", "Bed rest"], "End-stage renal disease."),
        (11, "Uterine tissue growing outside the uterus is:", "Endometriosis", ["Fibroids", "PCOS", "Ovarian cancer"], "Causes pain and infertility."),
        (11, "An enlarged prostate that isn't cancer is:", "BPH", ["Prostatitis", "Orchitis", "Epididymitis"], "Benign prostatic hyperplasia."),
        (11, "Which STI causes most cervical cancer?", "HPV", ["Chlamydia", "Syphilis", "Gonorrhea"], "Vaccine available."),
        (12, "Too much cortisol causes:", "Cushing syndrome", ["Addison disease", "Graves disease", "Acromegaly"], "Moon face, weight gain."),
        (12, "Excess growth hormone in adults causes:", "Acromegaly", ["Gigantism", "Dwarfism", "Cretinism"], "Gigantism in children."),
        (12, "Type 2 diabetes is mainly caused by:", "Insulin resistance", ["No insulin production", "Too much ADH", "Thyroid failure"], "Linked to obesity."),
    ]),
    ((13, 14, 15), [
        (13, "A stroke caused by a blocked artery is:", "Ischemic", ["Hemorrhagic", "Transient", "Embolic only"], "Most common type."),
        (13, "A 'mini-stroke' with symptoms that resolve is a:", "TIA", ["CVA", "Seizure", "Migraine"], "Transient ischemic attack."),
        (13, "Progressive loss of motor neurons is:", "ALS", ["MS", "Parkinson disease", "Epilepsy"], "Lou Gehrig's disease."),
        (14, "Clouding of the lens is a:", "Cataract", ["Glaucoma", "Macular degeneration", "Myopia"], "Treated with surgery."),
        (14, "Loss of central vision in older adults is often due to:", "Macular degeneration", ["Cataracts", "Myopia", "Conjunctivitis"], "Affects the macula."),
        (14, "Hearing loss from inner ear or nerve damage is:", "Sensorineural", ["Conductive", "Mixed only", "Temporary"], "Often permanent."),
        (15, "Sudden, reversible confusion is:", "Delirium", ["Dementia", "Schizophrenia", "Depression"], "Often from infection or drugs."),
        (15, "Alternating mania and depression occurs in:", "Bipolar disorder", ["Schizophrenia", "Anxiety disorder", "OCD"], "Mood disorder."),
        (15, "Hallucinations and delusions suggest:", "Schizophrenia", ["Phobia", "ADHD", "Insomnia"], "Psychotic disorder."),
    ]),
    ((16, 17), [
        (16, "Wear-and-tear joint disease is:", "Osteoarthritis", ["Rheumatoid arthritis", "Gout", "Lupus"], "Degenerative."),
        (16, "An autoimmune disease causing symmetrical joint inflammation is:", "Rheumatoid arthritis", ["Osteoarthritis", "Gout", "Osteoporosis"], "Morning stiffness."),
        (16, "Infection of bone is:", "Osteomyelitis", ["Osteoporosis", "Osteoarthritis", "Osteosarcoma"], "Treated with antibiotics."),
        (16, "Uric acid crystals in joints cause:", "Gout", ["Osteoarthritis", "Bursitis", "Lupus"], "Big toe pain."),
        (17, "The deadliest skin cancer is:", "Melanoma", ["Basal cell carcinoma", "Squamous cell carcinoma", "Actinic keratosis"], "ABCDE warning signs."),
        (17, "A highly contagious bacterial skin infection with honey-colored crusts is:", "Impetigo", ["Psoriasis", "Eczema", "Scabies"], "Common in children."),
        (17, "Scabies is caused by:", "Mites", ["Lice", "Bacteria", "Fungi"], "Intense itching."),
        (17, "Chronic red, scaly plaques are typical of:", "Psoriasis", ["Acne", "Impetigo", "Warts"], "Autoimmune."),
        (17, "Shingles is caused by reactivation of the:", "Varicella-zoster virus", ["Herpes simplex", "HPV", "Staph"], "Chickenpox virus."),
    ]),
]

BOOK = {
    "titles": ["Human Diseases: A Systemic Approach"],
    "edition": "8th edition",
    "source": "Pearson table of contents",
    "chapters": C,
    "quizzes": Q,
}
