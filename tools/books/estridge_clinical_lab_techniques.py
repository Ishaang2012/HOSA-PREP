# Estridge & Reynolds - Basic Clinical Laboratory Techniques.
# Unit list: 6th edition (2012), from the publisher's table of contents on cengage.com. The book is organized in units.
# Summaries cover each unit's standard topics; they are written for this site, not copied from the book.

C = [
    (1, "The Clinical Laboratory", [
        "Clinical laboratories test blood, urine, and other specimens to help diagnose and monitor disease. Lab personnel include pathologists, medical laboratory scientists (MLS, bachelor's degree), medical laboratory technicians (MLT, associate degree), phlebotomists, and laboratory assistants. The Clinical Laboratory Improvement Amendments (CLIA) regulate labs; waived tests are simple, low-risk tests.",
        "Safety includes standard precautions, PPE, OSHA's Bloodborne Pathogens Standard, hepatitis B vaccination, sharps containers, chemical safety (Safety Data Sheets), fire safety, and biohazard disposal. Quality assurance and quality control (running controls of known values) ensure accurate results.",
        "Basic skills include using the microscope (oil immersion gives the highest magnification), pipettes, centrifuges, and lab math such as metric conversions, dilutions, and solution preparation. Specimen collection includes capillary puncture and venipuncture; tubes are drawn in a set order of draw.",
    ], ["CLIA regulates labs; waived tests are simple", "Quality control uses known values", "Oil immersion = highest magnification", "Follow the order of draw"]),
    (2, "Basic Hematology", [
        "Hematology studies blood cells. Blood contains plasma and formed elements: erythrocytes (red cells carrying oxygen on hemoglobin), leukocytes (white cells), and thrombocytes (platelets). Blood cells form in the bone marrow (hematopoiesis).",
        "Common tests include hemoglobin, hematocrit (the percentage of packed red cells), red and white cell counts, the differential count of white cell types (neutrophils, lymphocytes, monocytes, eosinophils, basophils), red cell indices (MCV, MCH, MCHC), and the erythrocyte sedimentation rate (ESR). Blood smears are made, stained with Wright's stain, and examined.",
        "Abnormal results can indicate anemia (low red cells or hemoglobin), polycythemia, infection (high neutrophils), allergies or parasites (high eosinophils), or leukemia. EDTA (lavender-top) tubes are used for most hematology tests.",
    ], ["Hematocrit = % red cells", "Differential counts white cell types", "Wright's stain for blood smears", "EDTA lavender top for CBC"]),
    (3, "Basic Hemostasis", [
        "Hemostasis is the process that stops bleeding. It includes vascular constriction, formation of a platelet plug, and coagulation, in which clotting factors produce fibrin threads that strengthen the clot. Fibrinolysis later dissolves the clot.",
        "Tests include platelet counts, bleeding time, prothrombin time (PT/INR, used to monitor warfarin), and activated partial thromboplastin time (aPTT, used to monitor heparin). Coagulation tests use light-blue-top tubes with sodium citrate that must be filled completely. Disorders include hemophilia and thrombocytopenia.",
    ], ["Vessel constriction, platelet plug, coagulation", "PT/INR monitors warfarin", "aPTT monitors heparin", "Light-blue top = sodium citrate"]),
    (4, "Basic Immunology and Immunohematology", [
        "Immunology studies the body's defenses. Antigens trigger the immune system to make antibodies. Antigen-antibody reactions are the basis of many tests, including agglutination (clumping), precipitation, and enzyme immunoassays (ELISA). Rapid tests detect strep, pregnancy (hCG), mononucleosis, and other conditions.",
        "Immunohematology (blood banking) includes ABO and Rh blood typing. People with type A have anti-B antibodies, type B have anti-A, type AB have neither (universal recipient), and type O have both (universal red cell donor). Crossmatching checks compatibility before transfusion. Rh-negative mothers carrying Rh-positive babies may receive RhoGAM.",
    ], ["Antigens trigger antibody production", "Agglutination = clumping", "Type O = universal donor; AB = universal recipient", "Crossmatch before transfusion"]),
    (5, "Urinalysis", [
        "A routine urinalysis has three parts. The physical exam checks color, clarity, volume, and specific gravity (concentration). The chemical exam uses reagent strips to test pH, protein, glucose, ketones, blood, bilirubin, urobilinogen, nitrite, and leukocyte esterase.",
        "The microscopic exam looks at urine sediment after centrifuging for cells (RBCs, WBCs, epithelial cells), casts, crystals, and microorganisms. A clean-catch midstream specimen reduces contamination, and specimens should be tested within about an hour or refrigerated. Glucose and ketones may suggest diabetes; nitrite and leukocytes suggest infection.",
    ], ["Physical, chemical, microscopic exam", "Specific gravity = concentration", "Clean-catch midstream specimen", "Nitrite + leukocytes suggest UTI"]),
    (6, "Basic Clinical Chemistry", [
        "Clinical chemistry measures chemicals in blood and body fluids, usually in serum or plasma. Common tests include glucose (diabetes), cholesterol and lipid panels (heart disease risk), blood urea nitrogen and creatinine (kidney function), liver enzymes, electrolytes, and hemoglobin A1c.",
        "Point-of-care testing such as glucose meters gives fast results. Accurate results depend on proper specimen handling, fasting when required, and quality control. Instruments such as spectrophotometers and chemistry analyzers measure many substances.",
    ], ["Serum vs. plasma", "Glucose and A1c for diabetes", "BUN and creatinine for kidneys", "Lipid panel for heart risk"]),
    (7, "Basic Clinical Microbiology", [
        "Microbiology identifies microorganisms that cause infection. Bacteria are classified by shape (cocci, bacilli, spirilla) and Gram stain reaction: Gram-positive bacteria stain purple and Gram-negative bacteria stain red or pink.",
        "Specimens are collected aseptically and cultured on media such as blood agar. Colonies are identified, and antibiotic susceptibility testing shows which drugs work. Rapid tests detect strep throat. Aseptic technique and biosafety protect workers and specimens.",
    ], ["Cocci, bacilli, spirilla", "Gram-positive purple; Gram-negative pink", "Culture on agar media", "Susceptibility testing picks antibiotics"]),
    (8, "Basic Parasitology", [
        "Parasites live on or in a host and harm it. Medical parasites include protozoa (such as Giardia and Plasmodium, which causes malaria), helminths (worms such as roundworms, pinworms, and tapeworms), and arthropods (lice, mites, ticks).",
        "Stool specimens are examined for ova and parasites (O&P); the cellophane tape test detects pinworm eggs; and blood smears detect malaria. Prevention includes hand hygiene, safe water and food, and controlling insects.",
    ], ["Protozoa, helminths, arthropods", "O&P exam on stool", "Tape test for pinworms", "Blood smears detect malaria"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Federal regulations for clinical labs come from:", "CLIA", ["HIPAA", "OBRA", "EMTALA"], "Clinical Laboratory Improvement Amendments."),
        (1, "Running samples of known value to check accuracy is:", "Quality control", ["Calibration only", "Phlebotomy", "Centrifugation"], "Controls must fall within set ranges."),
        (1, "Which microscope objective gives the highest magnification?", "Oil immersion", ["Low power", "High dry", "Scanning"], "It's usually 100x."),
        (1, "A medical laboratory technician (MLT) usually has a:", "Associate degree", ["Bachelor's degree", "Doctorate", "High school diploma only"], "MLS/MT usually have a bachelor's degree."),
        (2, "The hematocrit measures:", "The percentage of red blood cells in blood", ["White cell count", "Platelet count", "Clotting time"], "It's also called packed cell volume."),
        (2, "Which stain is used for blood smears?", "Wright's stain", ["Gram stain", "Acid-fast stain", "India ink"], "It shows cell types clearly."),
        (2, "Which tube is used for a complete blood count?", "Lavender top (EDTA)", ["Light blue top", "Red top", "Gray top"], "EDTA prevents clotting by binding calcium."),
        (2, "An increased eosinophil count may suggest:", "Allergies or parasites", ["Bacterial infection", "Anemia", "Dehydration"], "Neutrophils rise in bacterial infections."),
        (3, "The PT/INR test is used to monitor:", "Warfarin therapy", ["Heparin therapy", "Insulin therapy", "Antibiotic therapy"], "aPTT monitors heparin."),
        (3, "Coagulation tests use which tube?", "Light blue top (sodium citrate)", ["Lavender top", "Green top", "Gray top"], "It must be filled completely."),
    ]),
    ((4, 5, 6), [
        (4, "Clumping of cells in an antigen-antibody reaction is:", "Agglutination", ["Hemolysis", "Coagulation", "Precipitation"], "It's used in blood typing."),
        (4, "A person with type A blood has which antibodies?", "Anti-B", ["Anti-A", "Both anti-A and anti-B", "Neither"], "You make antibodies against antigens you don't have."),
        (4, "The universal red cell donor type is:", "O negative", ["AB positive", "A positive", "B negative"], "AB positive is the universal recipient."),
        (4, "Testing donor and recipient blood for compatibility is a:", "Crossmatch", ["Differential", "Culture", "Urinalysis"], "It prevents transfusion reactions."),
        (5, "Specific gravity of urine reflects its:", "Concentration", ["Color", "pH", "Bacteria count"], "Normal is about 1.005–1.030."),
        (5, "Which specimen reduces contamination for urinalysis?", "Clean-catch midstream", ["First drops of urine", "Specimen from the toilet", "24-hour sample left at room temperature"], "Clean first, then collect midstream."),
        (5, "Positive nitrite and leukocyte esterase suggest:", "A urinary tract infection", ["Diabetes", "Dehydration", "Liver disease"], "Bacteria convert nitrate to nitrite."),
        (5, "The three parts of a urinalysis are physical, chemical, and:", "Microscopic", ["Culture", "Genetic", "Radiologic"], "Sediment is examined under a microscope."),
        (6, "Which tests evaluate kidney function?", "BUN and creatinine", ["ALT and AST", "Cholesterol and triglycerides", "Hemoglobin and hematocrit"], "They're waste products filtered by the kidneys."),
        (6, "Hemoglobin A1c reflects average blood glucose over about:", "3 months", ["1 day", "1 week", "1 year"], "It's used to monitor diabetes."),
    ]),
    ((7, 8), [
        (7, "Gram-positive bacteria stain:", "Purple", ["Pink or red", "Green", "Yellow"], "Gram-negative bacteria stain pink or red."),
        (7, "Round bacteria are called:", "Cocci", ["Bacilli", "Spirilla", "Vibrios"], "Rod-shaped bacteria are bacilli."),
        (7, "Antibiotic susceptibility testing determines:", "Which antibiotics will work against the organism", ["The patient's blood type", "Viral load", "Glucose level"], "It guides treatment."),
        (7, "Blood agar is a type of:", "Culture medium", ["Stain", "Antibiotic", "Anticoagulant"], "Media support microbial growth."),
        (8, "Malaria is caused by a:", "Protozoan (Plasmodium)", ["Virus", "Bacterium", "Worm"], "It's spread by mosquitoes."),
        (8, "The cellophane tape test detects:", "Pinworm eggs", ["Malaria", "Tapeworms in blood", "Lice"], "Eggs are laid around the anus."),
        (8, "An O&P exam is performed on:", "Stool", ["Urine", "Blood", "Saliva"], "Ova and parasites."),
        (8, "Worms such as roundworms and tapeworms are called:", "Helminths", ["Protozoa", "Arthropods", "Fungi"], "Arthropods include lice and ticks."),
        (7, "Specimens for culture should be collected using:", "Aseptic technique", ["Any clean container", "Bare hands", "Reused swabs"], "Contamination can cause false results."),
    ]),
]

BOOK = {
    "titles": ["Basic Clinical Laboratory Techniques"],
    "edition": "6th edition (2012)",
    "source": "Cengage table of contents",
    "unit": "Unit",
    "chapters": C,
    "quizzes": Q,
}
