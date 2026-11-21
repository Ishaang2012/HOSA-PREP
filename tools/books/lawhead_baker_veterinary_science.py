# Lawhead & Baker - Introduction to Veterinary Science.
# Chapter list: 3rd edition (2017), from the publisher's table of contents on cengage.com.
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

C = [
    (1, "Basic Cell Biology", [
        "Cells are the basic units of life. Animal cells have a cell membrane (controls what enters and leaves), cytoplasm, and a nucleus containing DNA. Organelles include mitochondria (energy), ribosomes (protein synthesis), endoplasmic reticulum, Golgi apparatus (packaging), and lysosomes (digestion). Protein synthesis uses transcription (DNA to mRNA) and translation (mRNA to protein).",
        "Mitosis produces two identical body cells for growth and repair; uncontrolled mitosis leads to cancer. Meiosis produces gametes (sperm and eggs) with half the chromosome number for sexual reproduction.",
    ], ["Mitochondria = energy; ribosomes = protein", "Transcription DNA→mRNA; translation mRNA→protein", "Mitosis = identical body cells", "Meiosis = gametes"]),
    (2, "Tissue Types and Functions", [
        "The four basic tissues are epithelial (covers and lines surfaces, forms glands), connective (supports and binds, including bone, cartilage, blood, and adipose), muscle (skeletal, smooth, and cardiac), and nervous (neurons and supporting glial cells).",
        "Epithelial tissue is classified by cell shape (squamous, cuboidal, columnar) and layers (simple or stratified). Knowing tissues helps veterinary staff understand wound healing and disease.",
    ], ["Epithelial, connective, muscle, nervous", "Squamous, cuboidal, columnar", "Blood and bone are connective tissue", "Cardiac muscle only in the heart"]),
    (3, "The Musculoskeletal System", [
        "The skeleton supports and protects the body, stores minerals, and makes blood cells. The axial skeleton includes the skull, spine, and ribs; the appendicular skeleton includes the limbs. Long bones have a diaphysis (shaft), epiphyses (ends), and growth plates where bones lengthen. Joint types include fibrous, cartilaginous, and synovial joints.",
        "Muscles attach to bones by tendons and move them through flexion, extension, abduction, and adduction. Species differ in skeletal structure, such as the number of toes and vertebrae. Common problems include fractures, arthritis, and hip dysplasia in dogs.",
    ], ["Axial vs. appendicular skeleton", "Growth plates lengthen bones", "Tendons attach muscle to bone", "Hip dysplasia common in large dogs"]),
    (4, "The Circulatory System", [
        "Blood carries oxygen, nutrients, hormones, and wastes. It contains plasma, red blood cells (oxygen), white blood cells (immunity), and platelets (clotting). The mammalian heart has four chambers; blood flows through the right side to the lungs and the left side to the body.",
        "Arteries carry blood away from the heart, veins return it, and capillaries exchange materials. Veterinary staff assess heart rate, heart sounds with a stethoscope, blood pressure, and electrocardiograms. Heartworm disease, spread by mosquitoes, damages the heart and lungs of dogs and cats.",
    ], ["Four-chambered mammalian heart", "Red cells carry oxygen", "Arteries away, veins back", "Heartworm spread by mosquitoes"]),
    (5, "The Respiratory System", [
        "The respiratory tract runs from the nostrils through the pharynx, larynx, trachea, and bronchi to the alveoli, where gas exchange occurs. The diaphragm contracts to pull air into the lungs.",
        "Respiratory rate varies by species and size. Birds have air sacs and a very efficient one-way airflow system. Common respiratory problems include pneumonia, kennel cough, feline upper respiratory infections, and heaves in horses.",
    ], ["Alveoli = gas exchange", "Diaphragm drives breathing", "Birds have air sacs", "Kennel cough = canine respiratory infection"]),
    (6, "The Renal System", [
        "The kidneys filter blood to remove wastes, balance water and electrolytes, regulate blood pressure, and make hormones. The nephron is the working unit: the glomerulus filters blood and the tubules reabsorb water and nutrients. Urine passes through the ureters to the bladder and out the urethra.",
        "Urinalysis checks specific gravity, pH, protein, glucose, and sediment. Blood tests such as BUN and creatinine assess kidney function. Common problems include kidney disease in older cats, bladder stones, and urinary tract infections.",
    ], ["Nephron = functional unit", "BUN and creatinine measure kidney function", "Urinalysis checks specific gravity and sediment", "Chronic kidney disease common in older cats"]),
    (7, "The Digestive System", [
        "Digestion breaks food into nutrients for absorption. Monogastric animals (dogs, cats, pigs, humans) have one simple stomach. Ruminants (cattle, sheep, goats) have four compartments: rumen, reticulum, omasum, and abomasum (the true stomach); microbes in the rumen ferment plant material and the animal chews cud.",
        "Horses and rabbits are hindgut fermenters with a large cecum. Carnivores have short digestive tracts; herbivores have long ones. Digestive problems include bloat, colic in horses, and gastric dilatation-volvulus in deep-chested dogs.",
    ], ["Monogastric = one stomach", "Ruminant: rumen, reticulum, omasum, abomasum", "Horses = hindgut fermenters", "Colic in horses; bloat in ruminants"]),
    (8, "The Reproductive System", [
        "Males produce sperm in the testes and testosterone; females produce eggs in the ovaries and estrogen and progesterone. Estrous cycles vary by species and determine when females are fertile (in heat).",
        "Gestation lengths differ: about 63 days for dogs and cats, 114 days for pigs, 283 for cattle, and about 340 for horses. Parturition is the birth process. Spaying (ovariohysterectomy) and neutering (castration) control reproduction and prevent some diseases.",
    ], ["Estrous cycle = heat cycle", "Dog/cat gestation ≈ 63 days", "Parturition = giving birth", "Spay = ovariohysterectomy; neuter = castration"]),
    (9, "The Nervous System", [
        "The nervous system detects changes and coordinates responses. The central nervous system is the brain and spinal cord; the peripheral nervous system is the nerves. The autonomic nervous system controls involuntary functions through sympathetic (fight or flight) and parasympathetic (rest and digest) branches.",
        "Neurons send signals using electrical impulses and neurotransmitters. Neurological exams check reflexes, gait, and consciousness. Problems include seizures, rabies, intervertebral disc disease in dachshunds, and spinal injuries.",
    ], ["CNS = brain + spinal cord", "Sympathetic = fight or flight", "Rabies attacks the nervous system", "Disc disease common in dachshunds"]),
    (10, "The Endocrine System", [
        "Endocrine glands release hormones into the blood to regulate growth, metabolism, reproduction, and stress. The pituitary gland, controlled by the hypothalamus, directs other glands. Other glands include the thyroid, parathyroids, adrenals, pancreas, and gonads.",
        "Common endocrine diseases include diabetes mellitus (dogs and cats), hyperthyroidism (common in older cats), hypothyroidism (common in dogs), and Cushing's disease (hyperadrenocorticism) in dogs.",
    ], ["Pituitary = master gland", "Hyperthyroidism common in older cats", "Hypothyroidism common in dogs", "Cushing's = too much cortisol"]),
    (11, "The Immune System", [
        "The immune system defends against pathogens. Innate immunity includes skin, mucous membranes, inflammation, and phagocytes. Adaptive immunity uses B cells (antibodies) and T cells and creates memory.",
        "Active immunity comes from infection or vaccination; passive immunity comes from receiving antibodies, such as newborns absorbing them from colostrum (first milk). Vaccination schedules protect animals from diseases like distemper, parvovirus, and rabies. Allergies and autoimmune diseases are immune system disorders.",
    ], ["Innate vs. adaptive immunity", "B cells make antibodies", "Colostrum gives passive immunity", "Vaccines produce active immunity"]),
    (12, "Basic Nutrients", [
        "Animals need six nutrient classes: water (most important), carbohydrates, fats, proteins, vitamins, and minerals. Energy comes mainly from carbohydrates and fats. Proteins provide amino acids for growth and repair; cats need taurine, an essential amino acid for them.",
        "Feed labels list guaranteed analysis (protein, fat, fiber, moisture). Diets are formulated for life stage and species. Malnutrition, obesity, and toxicities (such as chocolate or grapes in dogs) are nutritional concerns.",
    ], ["Water = most important nutrient", "Cats require taurine", "Guaranteed analysis on feed labels", "Chocolate and grapes are toxic to dogs"]),
    (13, "Species Comparison", [
        "Nutritional needs vary by species. Carnivores like cats need animal-based protein; omnivores like dogs and pigs eat varied diets; herbivores like horses, cattle, and rabbits digest plant fiber.",
        "Ruminants rely on rumen microbes; horses need high-fiber forage and frequent small meals; poultry have a crop and gizzard. Diets must also match production goals such as growth, milk production, or work.",
    ], ["Cats are obligate carnivores", "Herbivores digest fiber", "Poultry have a crop and gizzard", "Horses need forage and small, frequent meals"]),
    (14, "Principles of Infectious Disease", [
        "Infectious diseases are caused by pathogens: bacteria, viruses, fungi, protozoa, and parasites. Disease spreads by direct contact, indirect contact (fomites), airborne droplets, vectors (insects and ticks), and contaminated food or water.",
        "Parasites can be internal (roundworms, tapeworms, heartworms) or external (fleas, ticks, mites). The host's immune status, the pathogen's virulence, and the environment determine whether disease develops.",
    ], ["Pathogens: bacteria, viruses, fungi, protozoa, parasites", "Fomite = contaminated object", "Vector = living carrier like a tick", "Internal vs. external parasites"]),
    (15, "Disease Prevention", [
        "Preventing disease is better than treating it. Methods include vaccination, parasite control, sanitation and disinfection, quarantine and isolation of sick or new animals, biosecurity on farms, good nutrition, and reducing stress.",
        "Regular wellness exams, herd health programs, and record keeping help catch problems early. Proper cleaning of kennels and equipment breaks the chain of infection.",
    ], ["Vaccination and parasite control", "Quarantine new animals", "Biosecurity protects herds", "Sanitation breaks the chain of infection"]),
    (16, "Classification of Diseases", [
        "Diseases can be classified as infectious or noninfectious. Noninfectious causes include genetic (inherited) disorders, nutritional deficiencies, toxins, trauma, metabolic problems, and cancer.",
        "Diseases are also described as acute (sudden) or chronic (long-lasting), and clinical (with signs) or subclinical (without signs). Understanding the cause guides treatment.",
    ], ["Infectious vs. noninfectious", "Acute = sudden; chronic = long-lasting", "Subclinical = no visible signs", "Genetic, nutritional, toxic causes"]),
    (17, "Zoonoses", [
        "Zoonoses are diseases that spread between animals and humans. Examples include rabies, ringworm (a fungus), salmonellosis, leptospirosis, toxoplasmosis (from cat feces; dangerous in pregnancy), Lyme disease (from ticks), avian influenza, and brucellosis.",
        "Veterinary workers prevent zoonoses with handwashing, PPE, vaccination (including rabies pre-exposure vaccines for staff), and safe handling. Public health officials and veterinarians work together under the One Health concept.",
    ], ["Zoonosis = animal-to-human disease", "Rabies, ringworm, salmonella, leptospirosis", "Toxoplasmosis risk in pregnancy", "One Health links human and animal health"]),
    (18, "Diagnosis of Disease", [
        "Diagnosis begins with the history and physical exam, including temperature, pulse, respiration, body condition, and mucous membrane color and capillary refill time. Normal values differ by species.",
        "Diagnostic tests include blood counts and chemistry, urinalysis, fecal exams (flotation for parasite eggs), skin scrapings, cultures, radiographs, ultrasound, and necropsy (animal autopsy).",
    ], ["TPR and mucous membranes", "Capillary refill < 2 seconds", "Fecal flotation finds parasite eggs", "Necropsy = animal autopsy"]),
    (19, "Principles of Surgery", [
        "Veterinary surgery requires aseptic technique: sterilized instruments, surgical scrubbing, sterile gowns and gloves, and proper patient prep (clipping and scrubbing the site). Anesthesia includes preanesthetic exams, induction, monitoring, and recovery.",
        "Common procedures include spays, neuters, and wound repair. Surgical instruments include scalpels, scissors, forceps, hemostats, needle holders, and retractors. Sutures close wounds; postoperative care prevents infection.",
    ], ["Aseptic technique prevents infection", "Monitor patients under anesthesia", "Hemostats clamp vessels", "Needle holders grasp suture needles"]),
    (20, "Safety", [
        "Veterinary workers face bites, scratches, kicks, zoonoses, chemical hazards, radiation, anesthetic gases, and sharps injuries. Proper restraint techniques protect both animals and staff.",
        "Safety measures include PPE, Safety Data Sheets, lead aprons for radiography, safe sharps disposal, proper lifting, and understanding animal behavior. Large animals require special handling to avoid kicks and crushing.",
    ], ["Proper restraint prevents bites", "Lead aprons for X-rays", "SDS for chemicals", "Stay out of large animals' kick zones"]),
    (21, "Careers and Decision Making in Veterinary Science", [
        "Veterinary careers include veterinarian (DVM, about 4 years of veterinary school after college), veterinary technician (associate degree and credentialing exam, the VTNE), veterinary assistant, animal caretaker, groomer, and researcher. Specialties include surgery, internal medicine, and exotic animal medicine.",
        "Professionalism, ethics, communication with clients, and decision making about animal welfare and euthanasia are important. Career planning includes education, experience such as volunteering, and continuing education.",
    ], ["DVM = veterinarian degree", "Vet techs pass the VTNE", "Communication with clients matters", "Animal welfare and ethics"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Which organelle produces energy for the cell?", "Mitochondrion", ["Ribosome", "Golgi apparatus", "Nucleus"], "Ribosomes make proteins."),
        (1, "Meiosis produces:", "Gametes with half the chromosome number", ["Two identical body cells", "Muscle cells", "Blood cells"], "Mitosis produces identical body cells."),
        (1, "Uncontrolled cell division can lead to:", "Cancer", ["Immunity", "Digestion", "Respiration"], "Normal mitosis is tightly regulated."),
        (2, "Blood is classified as which type of tissue?", "Connective", ["Epithelial", "Muscle", "Nervous"], "Bone, cartilage, and fat are also connective tissue."),
        (2, "Flat, thin epithelial cells are called:", "Squamous", ["Cuboidal", "Columnar", "Stratified"], "Stratified means multiple layers."),
        (2, "Cardiac muscle is found:", "Only in the heart", ["In blood vessels", "Attached to bones", "In the stomach"], "Smooth muscle lines organs and vessels."),
        (3, "The skull, spine, and ribs make up the:", "Axial skeleton", ["Appendicular skeleton", "Visceral skeleton", "Pelvic girdle"], "The limbs form the appendicular skeleton."),
        (3, "Bones grow in length at the:", "Growth plates", ["Diaphysis", "Periosteum", "Marrow cavity"], "Growth plates close at maturity."),
        (3, "Which condition is common in large-breed dogs?", "Hip dysplasia", ["Heaves", "Milk fever", "Laminitis"], "It's an abnormal hip joint."),
        (3, "Tendons connect:", "Muscle to bone", ["Bone to bone", "Muscle to muscle", "Skin to bone"], "Ligaments connect bone to bone."),
    ]),
    ((4, 5, 6), [
        (4, "Which blood component carries oxygen?", "Red blood cells", ["White blood cells", "Platelets", "Plasma proteins only"], "Hemoglobin binds oxygen."),
        (4, "Heartworm disease is spread by:", "Mosquitoes", ["Fleas", "Ticks", "Contaminated water"], "Monthly preventives protect pets."),
        (4, "Blood vessels that carry blood away from the heart are:", "Arteries", ["Veins", "Capillaries", "Lymphatics"], "Veins return blood to the heart."),
        (5, "Gas exchange in the lungs occurs in the:", "Alveoli", ["Trachea", "Bronchi", "Larynx"], "Alveoli are surrounded by capillaries."),
        (5, "Which animals have air sacs that allow one-way airflow?", "Birds", ["Dogs", "Horses", "Cattle"], "Avian respiration is very efficient."),
        (5, "Kennel cough is a:", "Contagious respiratory disease of dogs", ["Heart disease of cats", "Digestive disease of horses", "Skin disease of cattle"], "It spreads where dogs are housed together."),
        (6, "The functional unit of the kidney is the:", "Nephron", ["Ureter", "Alveolus", "Neuron"], "The glomerulus filters blood."),
        (6, "Which blood tests assess kidney function?", "BUN and creatinine", ["Glucose and insulin", "T4 and TSH", "PCV and total protein only"], "Both rise when kidneys fail."),
        (6, "Chronic kidney disease is especially common in:", "Older cats", ["Young puppies", "Cattle", "Birds"], "Diet and fluids help manage it."),
        (4, "Platelets are needed for:", "Blood clotting", ["Carrying oxygen", "Fighting infection", "Digesting food"], "They plug damaged vessels."),
    ]),
    ((7, 8, 9), [
        (7, "The true stomach of a ruminant is the:", "Abomasum", ["Rumen", "Reticulum", "Omasum"], "It secretes digestive acid like a monogastric stomach."),
        (7, "Which animal is a hindgut fermenter?", "Horse", ["Cow", "Dog", "Cat"], "Horses ferment fiber in a large cecum."),
        (7, "Colic in horses refers to:", "Abdominal pain", ["A skin disease", "A hoof infection", "A breathing problem"], "It can be life-threatening."),
        (8, "The approximate gestation length for dogs and cats is:", "63 days", ["114 days", "283 days", "340 days"], "Pigs ≈ 114, cattle ≈ 283, horses ≈ 340 days."),
        (8, "Spaying a female animal is called an:", "Ovariohysterectomy", ["Orchiectomy", "Cesarean section", "Laparotomy"], "Castration is the male procedure."),
        (8, "The birth process is called:", "Parturition", ["Gestation", "Ovulation", "Estrus"], "Estrus is 'heat.'"),
        (9, "Which disease attacks the nervous system and is fatal once signs appear?", "Rabies", ["Parvovirus", "Ringworm", "Heartworm"], "Rabies vaccination is required by law in many places."),
        (9, "The 'fight or flight' response is controlled by the:", "Sympathetic nervous system", ["Parasympathetic nervous system", "Somatic nervous system", "Spinal cord only"], "The parasympathetic system calms the body."),
        (9, "Intervertebral disc disease is common in:", "Dachshunds", ["Persian cats", "Horses", "Chickens"], "Long backs make the discs vulnerable."),
        (7, "Animals that chew cud are:", "Ruminants", ["Monogastrics", "Carnivores", "Hindgut fermenters"], "Cattle, sheep, and goats are ruminants."),
    ]),
    ((10, 11, 12), [
        (10, "Hyperthyroidism is most common in:", "Older cats", ["Young dogs", "Horses", "Cattle"], "Signs include weight loss with a big appetite."),
        (10, "Cushing's disease results from too much:", "Cortisol", ["Insulin", "Thyroid hormone", "Estrogen"], "It's also called hyperadrenocorticism."),
        (10, "The gland that controls many other endocrine glands is the:", "Pituitary", ["Pancreas", "Thyroid", "Adrenal"], "It's regulated by the hypothalamus."),
        (11, "Newborn animals get passive immunity from:", "Colostrum", ["Vaccines", "Water", "Grain"], "Colostrum is the first milk, rich in antibodies."),
        (11, "Antibodies are made by:", "B cells", ["T cells", "Red blood cells", "Platelets"], "T cells attack infected cells directly."),
        (11, "Vaccination produces:", "Active immunity", ["Passive immunity", "Autoimmunity", "Allergy"], "The body makes its own antibodies."),
        (12, "The most important nutrient is:", "Water", ["Protein", "Fat", "Vitamins"], "Animals die faster without water than without food."),
        (12, "Cats require which amino acid in their diet?", "Taurine", ["Glycine", "Alanine", "Serine"], "Deficiency causes heart and eye problems."),
        (12, "The protein, fat, fiber, and moisture on a feed label are the:", "Guaranteed analysis", ["Ingredient list", "Feeding directions", "Calorie statement"], "It lists minimums and maximums."),
        (12, "Which food is toxic to dogs?", "Chocolate", ["Cooked chicken", "Carrots", "Rice"], "Theobromine in chocolate is toxic."),
    ]),
    ((13, 14, 15), [
        (13, "Cats are classified as:", "Obligate carnivores", ["Herbivores", "Omnivores", "Ruminants"], "They need animal-based nutrients."),
        (13, "Which digestive structure is found in poultry?", "Gizzard", ["Rumen", "Abomasum", "Cecum only"], "The gizzard grinds food."),
        (13, "Horses should be fed:", "High-fiber forage in small, frequent meals", ["One large grain meal a day", "Meat-based diets", "Only water"], "Large grain meals can cause colic."),
        (14, "A contaminated object that spreads disease is a:", "Fomite", ["Vector", "Host", "Reservoir only"], "Examples: food bowls, leashes, clothing."),
        (14, "A tick that spreads disease is an example of a:", "Vector", ["Fomite", "Toxin", "Antibody"], "Vectors are living carriers."),
        (14, "Which is an external parasite?", "Flea", ["Roundworm", "Tapeworm", "Heartworm"], "The others live inside the body."),
        (15, "Keeping new animals separate before adding them to a herd is:", "Quarantine", ["Vaccination", "Necropsy", "Castration"], "It prevents spreading disease."),
        (15, "Biosecurity refers to:", "Practices that keep disease out of a farm or facility", ["Animal identification tags", "Feeding programs", "Breeding records"], "Examples include disinfecting boots and limiting visitors."),
        (15, "Sanitation and disinfection help by:", "Breaking the chain of infection", ["Increasing appetite", "Building muscle", "Speeding growth"], "They remove pathogens from the environment."),
        (14, "Roundworms and tapeworms are:", "Internal parasites", ["External parasites", "Viruses", "Fungi"], "Fecal exams detect their eggs."),
    ]),
    ((16, 17, 18), [
        (16, "A disease that appears suddenly and runs a short course is:", "Acute", ["Chronic", "Subclinical", "Congenital"], "Chronic diseases last a long time."),
        (16, "A disease with no visible signs is:", "Subclinical", ["Acute", "Clinical", "Infectious"], "Testing may be needed to detect it."),
        (16, "Which is a noninfectious cause of disease?", "Nutritional deficiency", ["Bacteria", "Viruses", "Fungi"], "Genetics, toxins, and trauma are other examples."),
        (17, "A disease that spreads between animals and humans is a:", "Zoonosis", ["Toxicosis", "Neoplasm", "Allergy"], "Rabies is a classic example."),
        (17, "Ringworm is caused by a:", "Fungus", ["Worm", "Virus", "Bacterium"], "It's a skin infection, not a worm."),
        (17, "Toxoplasmosis, spread through cat feces, is especially dangerous for:", "Pregnant people", ["Veterinarians only", "Dogs", "Horses"], "It can harm the unborn baby."),
        (18, "Normal capillary refill time is under about:", "2 seconds", ["10 seconds", "30 seconds", "1 minute"], "Slow refill suggests poor circulation."),
        (18, "Fecal flotation is used to find:", "Parasite eggs", ["Broken bones", "Heart murmurs", "Blood type"], "Eggs float to the top of the solution."),
        (18, "An autopsy on an animal is called a:", "Necropsy", ["Biopsy", "Laparotomy", "Endoscopy"], "It helps find the cause of death."),
        (17, "The idea that human, animal, and environmental health are connected is called:", "One Health", ["Biosecurity", "Herd immunity", "Zoonosis"], "Vets and public health officials work together."),
    ]),
    ((19, 20, 21), [
        (19, "Sterile technique used during surgery to prevent infection is:", "Aseptic technique", ["Restraint", "Triage", "Quarantine"], "It includes scrubbing, sterile gowns, and sterile instruments."),
        (19, "Which instrument clamps blood vessels to control bleeding?", "Hemostat", ["Scalpel", "Retractor", "Needle holder"], "Needle holders grasp suture needles."),
        (19, "During anesthesia, the patient must be:", "Continuously monitored", ["Left alone", "Fed", "Kept standing"], "Monitor heart rate, breathing, and oxygen."),
        (20, "What protects staff from radiation when taking X-rays?", "Lead aprons and gloves", ["Latex gloves", "Surgical masks", "Safety goggles only"], "Staff should also stay out of the beam."),
        (20, "Proper animal restraint helps prevent:", "Bites and injuries to staff and animals", ["Infections only", "Dehydration", "Weight gain"], "Use the least restraint needed."),
        (20, "Information about chemical hazards is found in:", "Safety Data Sheets", ["Medical records", "Feed labels", "Vaccine certificates"], "OSHA requires SDS for chemicals."),
        (21, "The degree earned by veterinarians is the:", "DVM", ["MD", "RVT", "PhD only"], "Doctor of Veterinary Medicine."),
        (21, "Veterinary technicians usually must pass the:", "VTNE", ["NCLEX", "MCAT", "USMLE"], "Veterinary Technician National Examination."),
        (21, "Which is part of professionalism in veterinary careers?", "Clear, compassionate communication with clients", ["Sharing client information publicly", "Ignoring animal welfare", "Avoiding continuing education"], "Client trust is essential."),
        (19, "Before surgery, the incision site is:", "Clipped and scrubbed", ["Left as is", "Covered in food", "Bandaged tightly"], "This reduces bacteria on the skin."),
    ]),
]

BOOK = {
    "titles": ["Introduction to Veterinary Science"],
    "edition": "3rd edition (2017)",
    "source": "Cengage table of contents",
    "chapters": C,
    "quizzes": Q,
}
