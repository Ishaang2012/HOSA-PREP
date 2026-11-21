# Bertino & Bertino - Forensic Science: Fundamentals & Investigations.
# Chapter list: 3rd edition (2021), from National Geographic Learning's product data (ngl.cengage.com).
# A 4th edition (2027) exists, but its chapter list was not published online.
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

C = [
    (1, "Forensic Science and Observation", [
        "Forensic science applies science to questions of law. Early contributors include Mathieu Orfila (toxicology), Alphonse Bertillon (body measurements), Francis Galton (fingerprints), and Edmond Locard, whose exchange principle states that every contact leaves a trace.",
        "Good observation is the foundation of forensic work, yet human perception is unreliable: people notice what they expect, and eyewitness memory can be influenced by stress, bias, and leading questions. Investigators observe systematically and document findings with notes, sketches, and photographs.",
    ], ["Locard: every contact leaves a trace", "Orfila = father of toxicology", "Eyewitness memory is unreliable", "Document observations carefully"]),
    (2, "Crime Scene Investigation and Evidence Collection", [
        "The crime scene is secured first, then documented with notes, photographs, and sketches. Search patterns include line (strip), grid, spiral, and zone searches. Evidence can be physical, biological, or trace, and can be direct or circumstantial.",
        "Evidence is collected and packaged properly: biological evidence in paper (to prevent mold) and other items in sealed containers. The chain of custody records everyone who handles the evidence so it is admissible in court. Class evidence narrows to a group; individual evidence points to one source.",
    ], ["Secure, document, search, collect", "Grid, spiral, line, zone searches", "Chain of custody keeps evidence admissible", "Class vs. individual evidence"]),
    (3, "Hair Analysis", [
        "Hair is common trace evidence. A hair has a root, shaft, and tip, and three layers: the cuticle (scales), cortex (pigment), and medulla (center). Medulla patterns and scale patterns help distinguish human from animal hair.",
        "Hair can suggest body region, race, treatments such as dyeing, and sometimes drug use. Hair alone is class evidence unless the root has tissue for nuclear DNA; hair shafts can provide mitochondrial DNA.",
    ], ["Cuticle, cortex, medulla", "Medulla and scale patterns separate human and animal hair", "Root tissue can give nuclear DNA", "Hair shaft = mitochondrial DNA"]),
    (4, "Fiber Analysis", [
        "Fibers transfer easily between people and places. Natural fibers come from animals (wool, silk), plants (cotton, linen), and minerals; synthetic fibers include nylon, polyester, rayon, and acrylic.",
        "Fibers are compared by color, shape, microscopic features, burn tests, and chemical tests. Fiber evidence is usually class evidence but can link suspects, victims, and scenes, especially with unusual fibers.",
    ], ["Natural vs. synthetic fibers", "Cotton = plant; wool and silk = animal", "Burn and microscope tests", "Usually class evidence"]),
    (5, "Forensic Botany", [
        "Forensic botany uses plants as evidence. Pollen and spores are tiny, durable, and specific to locations and seasons, so they can link a person or object to a place (forensic palynology).",
        "Plant material such as leaves, seeds, wood, and stomach contents can help establish location or time of death. Plant growth through remains can indicate how long a body has been in a location.",
    ], ["Palynology = study of pollen and spores", "Pollen can link a suspect to a location", "Plants help estimate time and place", "Stomach contents can be evidence"]),
    (6, "Fingerprint Analysis", [
        "Fingerprints are unique, even between identical twins, and stay the same throughout life. The three main patterns are loops (most common), whorls, and arches. Minutiae (ridge endings, bifurcations, dots) are compared to make an identification.",
        "Prints can be patent (visible), plastic (impressed in soft material), or latent (invisible). Latent prints are developed with powders, ninhydrin (on paper), cyanoacrylate (superglue) fuming (on nonporous surfaces), and other methods. AFIS is the automated fingerprint database.",
    ], ["Loops, whorls, arches", "Patent, plastic, latent prints", "Ninhydrin on paper; superglue fuming on nonporous", "AFIS = fingerprint database"]),
    (7, "DNA Profiling", [
        "DNA is found in the nuclei of cells in blood, saliva, semen, skin, and hair roots. Mitochondrial DNA is inherited from the mother and useful for degraded samples. Except for identical twins, each person's DNA is unique.",
        "DNA profiling uses PCR to copy small samples and analyzes short tandem repeats (STRs). Gel or capillary electrophoresis separates DNA fragments by size. CODIS is the FBI's DNA database. DNA evidence has also helped free wrongly convicted people.",
    ], ["STRs used for profiling", "PCR copies DNA", "Electrophoresis separates by size", "CODIS = DNA database"]),
    (8, "Blood and Blood Spatter", [
        "Presumptive tests such as Kastle-Meyer (phenolphthalein) and luminol indicate possible blood; confirmatory and precipitin tests show if it's human. ABO and Rh blood typing is class evidence.",
        "Bloodstain pattern analysis studies drops and spatter to determine the direction, angle of impact, and point of origin. The angle of impact is found from the stain's width-to-length ratio (sin θ = width ÷ length). Patterns include passive drops, transfer, cast-off, and impact spatter.",
    ], ["Kastle-Meyer and luminol are presumptive", "Precipitin test: human or animal", "Angle: sin θ = width ÷ length", "Cast-off from swinging objects"]),
    (9, "Forensic Toxicology", [
        "Forensic toxicology detects drugs and poisons in the body. Samples include blood, urine, hair, and organs. Poisons include heavy metals (arsenic, lead), carbon monoxide, cyanide, and overdoses of medications or illegal drugs.",
        "Presumptive color tests screen for drugs, and gas chromatography-mass spectrometry (GC-MS) confirms them. Drug classes include stimulants, depressants, hallucinogens, and narcotics. Blood alcohol concentration is important in traffic cases.",
    ], ["GC-MS confirms drugs", "Hair can show long-term drug use", "Carbon monoxide gives cherry-red color", "Blood alcohol concentration in DUI cases"]),
    (10, "Handwriting Analysis, Forgery, and Counterfeiting", [
        "Document examiners compare questioned documents with known samples (exemplars). Handwriting characteristics include letter form, line quality, spacing, size, slant, and pen pressure. Forgery is making or altering documents to deceive.",
        "Investigators also analyze inks and paper (using chromatography and UV light) and detect counterfeit currency through security features such as watermarks, security threads, color-shifting ink, and microprinting.",
    ], ["Exemplar = known sample", "Line quality and slant compared", "Chromatography separates inks", "Watermarks and security threads detect counterfeits"]),
    (11, "Forensic Entomology", [
        "Forensic entomology uses insects to estimate the postmortem interval (time since death). Blowflies often arrive within minutes to hours and lay eggs; their life cycle goes egg, larva (maggot), pupa, and adult.",
        "Temperature strongly affects development, so investigators use accumulated degree hours. The insect species present can also show if a body was moved or if drugs were present.",
    ], ["Insects estimate postmortem interval", "Blowflies arrive first", "Egg, larva, pupa, adult", "Temperature affects development speed"]),
    (12, "Death: Manner, Mechanism, Cause", [
        "The cause of death is the injury or disease that started the chain of events (such as a gunshot wound); the mechanism is the physiological change that caused death (such as blood loss); and the manner is natural, accidental, suicide, homicide, or undetermined.",
        "Time of death is estimated using livor mortis (blood pooling), rigor mortis (muscle stiffening, peaking around 12 hours), algor mortis (body cooling), stomach contents, decomposition, and insects. Autopsies are performed by medical examiners or pathologists.",
    ], ["Manner: natural, accident, suicide, homicide, undetermined", "Livor = pooling; rigor = stiffening; algor = cooling", "Cause starts the chain; mechanism is the body change", "Medical examiner performs autopsy"]),
    (13, "Soil Examination", [
        "Soil differs from place to place in color, texture, minerals, and organic matter, so it can link people or objects to locations. Soil components include sand, silt, and clay.",
        "Examiners compare soil samples using color charts, density gradient tubes, pH, microscopy, and particle size. Samples should be collected from the scene and from control areas.",
    ], ["Sand, silt, clay", "Color, texture, minerals compared", "Density gradient tubes separate particles", "Collect control samples"]),
    (14, "Forensic Anthropology", [
        "Forensic anthropologists study skeletal remains to determine sex, age, ancestry, stature, and trauma. The pelvis is the best indicator of sex (wider in females); the skull also helps.",
        "Age is estimated from growth plate fusion, teeth, and bone changes. Height is estimated from long bones such as the femur. Marks on bones can show trauma or disease. Facial reconstruction and DNA help identify individuals.",
    ], ["Pelvis = best indicator of sex", "Growth plates and teeth estimate age", "Femur estimates height", "Bones show trauma and disease"]),
    (15, "Glass Evidence", [
        "Glass fragments transfer to clothing and can link suspects to scenes. Glass is compared by color, thickness, density, and refractive index (how much it bends light).",
        "Fracture patterns reveal the direction and order of impacts: radial fractures spread outward from the impact, and concentric fractures form circles around it. A later fracture stops at an earlier one.",
    ], ["Refractive index compares glass", "Radial and concentric fractures", "A later crack stops at an earlier one", "Density helps identify glass"]),
    (16, "Casts and Impressions", [
        "Impression evidence includes shoeprints, tire tracks, tool marks, and bite marks. Impressions can be two-dimensional (prints on surfaces) or three-dimensional (in mud or snow).",
        "Impressions are photographed with a scale and cast with materials like dental stone. Shoeprints show tread design (class) and wear or damage (individual characteristics). Tire tracks can show vehicle type and direction.",
    ], ["2D prints vs. 3D impressions", "Photograph with a scale, then cast", "Wear patterns are individual characteristics", "Dental stone for casting"]),
    (17, "Tool Marks", [
        "Tool marks are impressions or scratches left by tools such as screwdrivers, crowbars, and cutters. Each tool develops unique imperfections from manufacturing and use.",
        "Examiners compare marks from the scene with test marks made by a suspect tool using comparison microscopes. Tool marks can be impressed, sliding (striated), or cutting marks.",
    ], ["Tools leave unique marks", "Impressed, sliding, cutting marks", "Comparison microscope", "Test marks from suspect tools"]),
    (18, "Firearms and Ballistics", [
        "Ballistics studies bullets and firearms. Rifling inside a gun barrel (lands and grooves) leaves marks on bullets; firing pins, breech faces, and ejectors leave marks on cartridge cases. These marks can link a bullet to a specific gun.",
        "NIBIN is the national database of ballistic images. Gunshot residue testing can show if someone fired a gun recently, and the shape and range of wounds help reconstruct shootings. Trajectory analysis determines the bullet's path.",
    ], ["Lands and grooves mark bullets", "Cartridge cases show firing pin marks", "NIBIN = ballistic image database", "Gunshot residue shows recent firing"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Locard's exchange principle states that:", "Every contact leaves a trace", ["Fingerprints never change", "DNA is unique", "Eyewitnesses are reliable"], "Evidence transfers when people touch places and things."),
        (1, "Who is considered the father of forensic toxicology?", "Mathieu Orfila", ["Edmond Locard", "Francis Galton", "Alphonse Bertillon"], "Orfila studied poisons in the 1800s."),
        (1, "Eyewitness accounts can be unreliable because:", "Memory can be affected by stress and suggestion", ["People always lie", "Memory never fades", "Courts don't allow them"], "Leading questions can change memories."),
        (2, "Biological evidence should be packaged in:", "Paper bags", ["Sealed plastic bags", "Glass jars filled with water", "Metal cans"], "Plastic traps moisture and promotes mold."),
        (2, "The record of everyone who handled a piece of evidence is the:", "Chain of custody", ["Search pattern", "Crime scene sketch", "Autopsy report"], "It keeps evidence admissible in court."),
        (2, "Evidence that narrows to a group but not one source is:", "Class evidence", ["Individual evidence", "Direct evidence", "Testimonial evidence"], "Blood type is class evidence."),
        (2, "Which search pattern spirals inward or outward from a point?", "Spiral", ["Grid", "Line", "Zone"], "Grid searches cover the area twice."),
        (3, "The pigment in a hair is found mostly in the:", "Cortex", ["Cuticle", "Medulla", "Root only"], "The cuticle is the scaly outer layer."),
        (3, "Nuclear DNA can be obtained from a hair only if:", "The root has tissue attached", ["The hair is dyed", "The hair is long", "The hair is from an animal"], "Hair shafts give mitochondrial DNA."),
        (3, "Comparing the medulla helps distinguish:", "Human hair from animal hair", ["Male from female hair", "Young from old hair", "Wet from dry hair"], "Animal medullas are usually wider."),
    ]),
    ((4, 5, 6), [
        (4, "Which is a natural plant fiber?", "Cotton", ["Nylon", "Polyester", "Acrylic"], "Wool and silk are natural animal fibers."),
        (4, "Fiber evidence is usually:", "Class evidence", ["Individual evidence", "Never admissible", "DNA evidence"], "Unusual fibers can still be strong links."),
        (4, "Which test helps tell natural from synthetic fibers?", "Burn test", ["Fingerprint powder", "Luminol test", "Precipitin test"], "Synthetics melt; natural fibers burn differently."),
        (5, "The study of pollen and spores is:", "Palynology", ["Entomology", "Toxicology", "Odontology"], "Pollen can link someone to a location."),
        (5, "Pollen is useful evidence because it is:", "Durable and specific to locations and seasons", ["Always visible", "Identical everywhere", "Easily destroyed"], "It survives for a long time."),
        (6, "The most common fingerprint pattern is the:", "Loop", ["Whorl", "Arch", "Delta"], "Loops make up about 60–65% of prints."),
        (6, "Invisible fingerprints that must be developed are:", "Latent prints", ["Patent prints", "Plastic prints", "Rolled prints"], "Patent prints are visible; plastic prints are impressions."),
        (6, "Superglue (cyanoacrylate) fuming is used to develop prints on:", "Nonporous surfaces", ["Paper only", "Wet fabric", "Soil"], "Ninhydrin works well on paper."),
        (6, "AFIS is a database of:", "Fingerprints", ["DNA profiles", "Bullets", "Shoeprints"], "Automated Fingerprint Identification System."),
        (6, "Ridge endings and bifurcations used to compare prints are called:", "Minutiae", ["Deltas", "Cores", "Patterns"], "Examiners compare many minutiae points."),
    ]),
    ((7, 8, 9), [
        (7, "DNA profiling commonly analyzes:", "Short tandem repeats (STRs)", ["Blood types", "Hair color genes", "Fingerprint ridges"], "STRs vary greatly between people."),
        (7, "PCR is used to:", "Make many copies of a small DNA sample", ["Separate DNA by size", "Store DNA profiles", "Stain DNA"], "Electrophoresis separates the fragments."),
        (7, "Mitochondrial DNA is inherited from:", "The mother", ["The father", "Both parents equally", "Neither parent"], "It's useful for degraded samples."),
        (7, "The FBI's DNA database is called:", "CODIS", ["AFIS", "NIBIN", "NCIC"], "Combined DNA Index System."),
        (8, "The Kastle-Meyer test is a:", "Presumptive test for blood", ["Confirmatory DNA test", "Fingerprint test", "Drug test"], "It turns pink with possible blood."),
        (8, "Which test shows whether blood is human?", "Precipitin test", ["Luminol test", "Kastle-Meyer test", "Ninhydrin test"], "It uses antibodies against human proteins."),
        (8, "Spatter flung from a swinging object is:", "Cast-off", ["Passive drop", "Transfer stain", "Pool"], "It forms a linear trail."),
        (8, "A bloodstain's angle of impact is found using:", "Width ÷ length (sin θ)", ["Length × width", "Stain color", "Stain temperature"], "Rounder stains mean steeper angles."),
        (9, "Which method confirms the identity of a drug?", "GC-MS", ["Color test", "Smell test", "Microscope only"], "Gas chromatography-mass spectrometry."),
        (9, "Which sample can show drug use over months?", "Hair", ["Urine", "Saliva", "Sweat"], "Drugs are deposited as hair grows."),
    ]),
    ((10, 11, 12), [
        (10, "A known handwriting sample used for comparison is an:", "Exemplar", ["Forgery", "Counterfeit", "Watermark"], "Questioned documents are compared to exemplars."),
        (10, "Inks can be separated and compared using:", "Chromatography", ["Fingerprint powder", "Luminol", "X-rays"], "Different inks separate into different pigments."),
        (10, "Which is a security feature of real currency?", "Watermark", ["Glossy finish", "Bright colors only", "Thick paper only"], "Security threads and color-shifting ink are others."),
        (11, "Forensic entomology mainly helps estimate:", "Time since death", ["Cause of death", "Blood type", "Height of the victim"], "This is the postmortem interval."),
        (11, "Which insects usually arrive first at a body?", "Blowflies", ["Beetles", "Ants", "Wasps"], "They can arrive within minutes."),
        (11, "Insect development speeds up when:", "Temperatures are warmer", ["Temperatures are colder", "It is dark", "It is raining"], "Investigators use accumulated degree hours."),
        (12, "Which is NOT a manner of death?", "Blood loss", ["Homicide", "Accident", "Natural"], "Blood loss is a mechanism of death."),
        (12, "Pooling of blood after death is:", "Livor mortis", ["Rigor mortis", "Algor mortis", "Decomposition"], "Rigor = stiffening; algor = cooling."),
        (12, "Rigor mortis usually peaks about:", "12 hours after death", ["1 hour after death", "3 days after death", "1 week after death"], "It then gradually disappears."),
        (12, "A gunshot wound that leads to death is the:", "Cause of death", ["Manner of death", "Mechanism of death", "Time of death"], "The mechanism might be blood loss."),
    ]),
    ((13, 14, 15), [
        (13, "The three main mineral particle sizes in soil are:", "Sand, silt, and clay", ["Gravel, rock, and dust", "Humus, peat, and loam", "Iron, copper, and zinc"], "Sand is largest and clay is smallest."),
        (13, "Density gradient tubes are used to:", "Separate and compare soil particles", ["Type blood", "Develop fingerprints", "Measure bullets"], "Particles settle at different levels."),
        (13, "When collecting soil evidence, investigators should also collect:", "Control samples from nearby areas", ["Only one sample", "No samples", "Air samples"], "Controls show normal variation."),
        (14, "The best bone for determining sex is the:", "Pelvis", ["Femur", "Skull", "Rib"], "The female pelvis is wider."),
        (14, "The femur can be used to estimate:", "Height", ["Blood type", "Eye color", "Time of death"], "Long bones correlate with stature."),
        (14, "Fusion of growth plates helps estimate:", "Age", ["Sex", "Ancestry", "Cause of death"], "Growth plates close at predictable ages."),
        (15, "Glass is compared using its refractive index, which measures:", "How much it bends light", ["Its weight", "Its color only", "Its temperature"], "Density is also compared."),
        (15, "Fractures that spread outward from the point of impact are:", "Radial fractures", ["Concentric fractures", "Spiral fractures", "Stress fractures"], "Concentric fractures form circles."),
        (15, "When determining the order of bullet holes in glass:", "A later fracture stops at an earlier one", ["The first fracture stops at the second", "All fractures cross", "Order can't be determined"], "This is a key rule of glass analysis."),
        (14, "Forensic anthropologists study:", "Skeletal remains", ["Insects", "Fingerprints", "Handwriting"], "They estimate sex, age, ancestry, and stature."),
    ]),
    ((16, 17, 18), [
        (16, "A footprint left in mud is a:", "Three-dimensional impression", ["Two-dimensional print", "Latent print", "Tool mark"], "It can be cast with dental stone."),
        (16, "Before casting an impression, investigators should:", "Photograph it with a scale", ["Wash it out", "Walk on it", "Cover it with sand"], "Photos preserve details."),
        (16, "Wear patterns on a shoe sole are:", "Individual characteristics", ["Class characteristics", "Irrelevant", "Manufacturing defects only"], "Tread design is a class characteristic."),
        (17, "Tool marks can be unique because:", "Each tool has its own imperfections", ["All tools are identical", "Tools never wear", "Marks always look the same"], "Use and manufacturing create unique features."),
        (17, "Scratches made by a tool sliding across a surface are:", "Striated (sliding) marks", ["Impressed marks", "Latent prints", "Cast marks"], "Impressed marks are pressed into the surface."),
        (17, "Examiners compare tool marks using a:", "Comparison microscope", ["Thermometer", "Spectrometer only", "Metal detector"], "It shows two samples side by side."),
        (18, "Raised and lowered spiral ridges inside a gun barrel are:", "Lands and grooves", ["Firing pins", "Breech faces", "Ejectors"], "They spin the bullet and mark it."),
        (18, "The national database of ballistic images is:", "NIBIN", ["CODIS", "AFIS", "NCIC"], "National Integrated Ballistic Information Network."),
        (18, "Gunshot residue testing can show that a person:", "Recently fired a gun", ["Owns a gun", "Was shot", "Bought ammunition"], "Residue settles on hands and clothing."),
        (18, "Marks on a cartridge case can come from the:", "Firing pin and breech face", ["Rifling only", "Barrel length", "Bullet weight"], "Ejector marks are also left."),
    ]),
]

BOOK = {
    "titles": ["Forensic Science Fundamentals"],
    "edition": "3rd edition (2021)",
    "source": "National Geographic Learning table of contents; the 4th edition's list wasn't available",
    "chapters": C,
    "quizzes": Q,
}
