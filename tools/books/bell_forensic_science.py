# Bell - Forensic Science: An Introduction to Scientific and Investigative Techniques (CRC Press).
# Chapter list supplied by the site owner (not verified against the publisher; chapter numbering in the
# current 6th edition may differ). Summaries are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Justice and Science", "Forensic science applies science to legal questions. Forensic scientists must be objective and follow the scientific method. Courts decide admissibility of expert testimony using standards such as Frye (general acceptance) and Daubert (reliability, peer review, error rate).", ["Science in law", "Objectivity", "Frye standard", "Daubert standard"]),
    ch(2, "Evidence: Origins, Types, and Admissibility", "Evidence can be physical, biological, trace, or testimonial. Class evidence links to a group; individual evidence links to one source. Locard's exchange principle says every contact leaves a trace. Chain of custody documents evidence handling.", ["Class vs. individual evidence", "Locard's exchange principle", "Chain of custody", "Admissibility"]),
    ch(3, "Crime Scene Investigation", "Steps: secure the scene, document (notes, photos, sketches), search (spiral, grid, line, zone patterns), collect and package evidence properly (paper for biological items), and maintain chain of custody.", ["Secure the scene", "Photograph and sketch", "Search patterns", "Proper packaging"]),
    ch(4, "Bloodstain Pattern Analysis", "Bloodstain patterns reveal events. Passive drops, spatter (impact patterns), cast-off, transfer, and void patterns are analyzed. The angle of impact is estimated from stain shape (width ÷ length = sine of angle), and strings or software find the area of origin.", ["Spatter and cast-off", "Angle of impact", "Area of origin", "Transfer and void patterns"]),
    ch(5, "Death Investigation (Forensic Pathology)", "Forensic pathologists perform autopsies to determine cause, mechanism, and manner of death (natural, accident, suicide, homicide, undetermined). Time-of-death clues include rigor, livor, and algor mortis.", ["Cause vs. manner", "Autopsy", "Rigor, livor, algor mortis", "Medical examiner"]),
    ch(6, "Forensic Anthropology", "Forensic anthropologists analyze skeletal remains to estimate sex (pelvis, skull), age (growth plates, pubic symphysis), stature (long bones like the femur), and ancestry, and to identify trauma.", ["Sex from pelvis", "Age from growth plates", "Stature from femur", "Skeletal trauma"]),
    ch(7, "Forensic Entomology", "Insects colonize bodies in a predictable order. Blowfly life stages (egg, larva/maggot, pupa, adult) help estimate the postmortem interval, adjusted for temperature (accumulated degree hours).", ["Blowflies first", "Insect life cycle", "Postmortem interval", "Temperature effects"]),
    ch(8, "Forensic Odontology", "Forensic dentists identify people by comparing dental records and X-rays, estimate age from teeth, and analyze bite marks, though bite-mark evidence is now considered unreliable.", ["Dental records", "Age from teeth", "Bite marks", "Identification in disasters"]),
    ch(9, "Forensic Toxicology", "Toxicologists detect drugs, alcohol, and poisons in body fluids and tissues. Screening tests (immunoassays, color tests) are confirmed with GC-MS. Blood alcohol concentration and common poisons (cyanide, arsenic, carbon monoxide) are covered.", ["Screening vs. confirmation", "GC-MS", "Blood alcohol", "Common poisons"]),
    ch(10, "Forensic Serology and DNA Typing", "Serology identifies body fluids (presumptive tests like Kastle-Meyer and luminol for blood). DNA typing uses STRs and PCR; CODIS stores profiles. Mitochondrial DNA (maternal) and Y-STRs (paternal) help in special cases.", ["Presumptive vs. confirmatory", "STR and PCR", "CODIS", "mtDNA and Y-STR"]),
    ch(11, "Fingerprints and Other Friction Ridge Impressions", "Fingerprints are unique and permanent. Patterns are loops (most common), whorls, and arches; minutiae are used for matching. Prints are latent, patent, or plastic and developed with powders, ninhydrin, or superglue fuming. AFIS searches databases.", ["Loops, whorls, arches", "Minutiae", "Latent, patent, plastic", "AFIS"]),
    ch(12, "Firearms and Tool Marks", "Rifling in barrels leaves lands and grooves on bullets; firing pins and breech faces mark cartridge cases. Comparison microscopes match marks; NIBIN links cases. Gunshot residue and distance determination are also examined. Tools leave comparable marks too.", ["Rifling marks", "Comparison microscope", "NIBIN", "Gunshot residue"]),
    ch(13, "Trace Evidence: Hair, Fibers, Paint, and Glass", "Trace evidence transfers on contact. Hair (medulla, cuticle) can be compared and may yield DNA from roots; fibers are natural or synthetic; paint layers and glass refractive index and fracture patterns are compared.", ["Hair structure", "Natural vs. synthetic fibers", "Paint layers", "Glass refractive index"]),
    ch(14, "Questioned Documents", "Document examiners analyze handwriting, signatures, ink, paper, and printing to detect forgery, alteration, or authorship. Exemplars (known samples) are compared with questioned items.", ["Handwriting comparison", "Exemplars", "Ink and paper", "Alterations"]),
    ch(15, "Arson and Explosives Investigation", "Fire investigators find the origin (often the lowest point of burning with V-patterns) and cause, and detect accelerants with GC-MS. Explosives are low (burn) or high (detonate); residues are analyzed.", ["Point of origin", "V-patterns", "Accelerants", "Low vs. high explosives"]),
    ch(16, "Digital Forensics", "Digital forensics recovers data from computers, phones, and networks while preserving integrity with write blockers and hash values. Metadata and deleted files can be key evidence.", ["Write blockers", "Hash values", "Metadata", "Deleted file recovery"]),
    ch(17, "Forensic Psychology and Psychiatry", "Forensic psychologists evaluate competency to stand trial, insanity (M'Naghten rule), risk, and malingering, and study eyewitness memory, interrogation, and criminal profiling.", ["Competency to stand trial", "Insanity defense", "Eyewitness memory", "Criminal profiling"]),
]

Q = [
    ((1, 2, 3), [
        (1, "The standard requiring general acceptance in the scientific community is:", "Frye", ["Daubert", "Miranda", "Locard"], "Older standard."),
        (1, "The Daubert standard considers testing, peer review, and:", "Known error rates", ["Popularity", "Cost", "Speed"], "Judge as gatekeeper."),
        (1, "Forensic scientists must remain:", "Objective", ["On the prosecution's side", "On the defense's side", "Silent"], "Follow the evidence."),
        (2, "'Every contact leaves a trace' is:", "Locard's exchange principle", ["Frye standard", "Daubert rule", "Chain of custody"], "Basis of trace evidence."),
        (2, "Evidence that can be linked to a single source is:", "Individual evidence", ["Class evidence", "Circumstantial evidence", "Testimonial evidence"], "E.g., DNA."),
        (2, "Documenting everyone who handled evidence is the:", "Chain of custody", ["Search warrant", "Autopsy report", "Exemplar"], "Keeps it admissible."),
        (3, "The first priority at a crime scene is to:", "Secure the scene", ["Collect evidence", "Interview witnesses", "Leave"], "Prevent contamination."),
        (3, "Wet biological evidence should be packaged in:", "Paper", ["Plastic", "Glass jars sealed", "Metal cans"], "Prevents mold."),
        (3, "A search moving in widening circles is a:", "Spiral search", ["Grid search", "Line search", "Zone search"], "Good for small scenes."),
    ]),
    ((4, 5, 6), [
        (4, "The angle of impact is estimated from a stain's:", "Width-to-length ratio", ["Color", "Smell", "Temperature"], "Sine of the angle."),
        (4, "Blood flung from a swinging object creates:", "Cast-off", ["Passive drops", "Transfer", "Void"], "Shows motion."),
        (4, "An empty area in a spatter pattern is a:", "Void", ["Transfer", "Cast-off", "Pool"], "Something blocked the blood."),
        (5, "The five manners of death include natural, accident, suicide, homicide, and:", "Undetermined", ["Disease", "Trauma", "Poisoning"], "Manner vs. cause."),
        (5, "Stiffening of muscles after death is:", "Rigor mortis", ["Livor mortis", "Algor mortis", "Putrefaction"], "Peaks ~12 hours."),
        (5, "Pooling of blood after death is:", "Livor mortis", ["Rigor mortis", "Algor mortis", "Adipocere"], "Lividity."),
        (6, "The best bone for determining sex is the:", "Pelvis", ["Femur", "Skull only", "Rib"], "Wider subpubic angle in females."),
        (6, "Stature is estimated from long bones such as the:", "Femur", ["Pelvis", "Skull", "Vertebra"], "Regression formulas."),
        (6, "Unfused growth plates indicate a:", "Younger person", ["Older adult", "Female", "Male"], "Fuse with age."),
    ]),
    ((7, 8, 9), [
        (7, "The first insects to arrive at a body are usually:", "Blowflies", ["Beetles", "Ants", "Moths"], "Within minutes to hours."),
        (7, "Insects help estimate the:", "Postmortem interval", ["Cause of death", "Manner of death", "Identity"], "Time since death."),
        (7, "Insect development speed depends mainly on:", "Temperature", ["Humidity only", "Light only", "Body size"], "Accumulated degree hours."),
        (8, "Forensic odontologists identify people by comparing:", "Dental records and X-rays", ["Fingerprints", "Shoe prints", "Handwriting"], "Useful in disasters."),
        (8, "Bite-mark evidence is now considered:", "Unreliable for individual identification", ["Perfectly accurate", "Better than DNA", "Always admissible"], "Many wrongful convictions."),
        (8, "Teeth can estimate a person's:", "Age", ["Height", "Blood type", "Eye color"], "Development and wear."),
        (9, "Preliminary drug screens are confirmed with:", "GC-MS", ["Color tests", "Smell", "Visual inspection"], "Gold standard."),
        (9, "Cherry-red lividity suggests poisoning by:", "Carbon monoxide", ["Arsenic", "Cyanide only", "Lead"], "Carboxyhemoglobin."),
        (9, "A bitter almond odor suggests:", "Cyanide", ["Arsenic", "Strychnine", "Carbon monoxide"], "Not everyone can smell it."),
    ]),
    ((10, 11, 12), [
        (10, "A presumptive test for blood is:", "Kastle-Meyer", ["Marquis", "Duquenois-Levine", "Scott test"], "Phenolphthalein turns pink."),
        (10, "The national DNA database is:", "CODIS", ["AFIS", "NIBIN", "IAFIS only"], "Stores STR profiles."),
        (10, "DNA passed only from mother to child is:", "Mitochondrial DNA", ["Y-STR DNA", "Nuclear DNA", "Autosomal STRs"], "Useful for degraded remains."),
        (11, "The most common fingerprint pattern is the:", "Loop", ["Whorl", "Arch", "Tented arch"], "About 60–65%."),
        (11, "Invisible prints that must be developed are:", "Latent prints", ["Patent prints", "Plastic prints", "Partial prints"], "Powder, ninhydrin, superglue."),
        (11, "The fingerprint database search system is:", "AFIS", ["CODIS", "NIBIN", "NCIC"], "Automated Fingerprint Identification System."),
        (12, "Spiral grooves in a gun barrel are:", "Rifling", ["Striations only", "Breech marks", "Firing pins"], "Leave lands and grooves on bullets."),
        (12, "Bullets are compared using a:", "Comparison microscope", ["Spectrophotometer", "Centrifuge", "Thermocycler"], "Side-by-side view."),
        (12, "The national ballistic imaging network is:", "NIBIN", ["CODIS", "AFIS", "NCIC"], "Links firearm cases."),
    ]),
    ((13, 14, 15), [
        (13, "The central core of a hair is the:", "Medulla", ["Cuticle", "Cortex", "Root"], "Pattern helps identify species."),
        (13, "Glass samples are compared using:", "Refractive index", ["Color only", "Weight only", "Smell"], "How light bends."),
        (13, "Polyester and nylon are:", "Synthetic fibers", ["Natural fibers", "Animal fibers", "Plant fibers"], "Man-made."),
        (14, "Known writing samples used for comparison are:", "Exemplars", ["Questioned documents", "Forgeries", "Indentations"], "Collected or requested."),
        (14, "Document examiners look for:", "Forgery or alteration", ["Fingerprints only", "DNA only", "Gunshot residue"], "Handwriting, ink, paper."),
        (14, "Comparing ink can reveal:", "Additions or alterations", ["The writer's height", "The writer's blood type", "Nothing"], "Different inks."),
        (15, "Fire investigators often find the point of origin at the:", "Lowest point of burning with V-patterns", ["Highest point", "Doorway always", "Roof"], "Fire rises."),
        (15, "Accelerants are identified using:", "GC-MS", ["Luminol", "Ninhydrin", "Kastle-Meyer"], "Detects hydrocarbons."),
        (15, "Explosives that detonate with a shock wave are:", "High explosives", ["Low explosives", "Accelerants", "Propellants only"], "E.g., TNT."),
    ]),
    ((16, 17), [
        (16, "A device that prevents changes to digital evidence is a:", "Write blocker", ["Firewall", "Hash value", "Router"], "Preserves integrity."),
        (16, "A unique digital fingerprint of data is a:", "Hash value", ["Metadata", "Cookie", "IP address"], "Proves data unchanged."),
        (16, "Data about data, like creation dates, is:", "Metadata", ["Malware", "Encryption", "Cache"], "Often key evidence."),
        (17, "Whether a defendant understands the trial is:", "Competency to stand trial", ["Insanity", "Malingering", "Profiling"], "About the present."),
        (17, "The rule asking if a defendant knew right from wrong is:", "M'Naghten", ["Miranda", "Daubert", "Frye"], "Insanity defense."),
        (17, "Faking symptoms for gain is:", "Malingering", ["Competency", "Psychosis", "Profiling"], "Forensic psychologists assess it."),
        (17, "Eyewitness memory can be altered by:", "Misleading information after the event", ["Nothing", "Sleep only", "DNA testing"], "Misinformation effect."),
        (16, "Deleted files can often be:", "Recovered", ["Never recovered", "Only printed", "Only emailed"], "Data remains until overwritten."),
        (17, "Inferring offender traits from crime scene behavior is:", "Criminal profiling", ["DNA typing", "Ballistics", "Serology"], "Behavioral analysis."),
    ]),
]

BOOK = {
    "titles": ["Forensic Science"],
    "edition": "Edition not verified; chapter list supplied by the site owner (numbering may differ in the 6th edition)",
    "source": "Chapter list supplied by the site owner",
    "chapters": C,
    "quizzes": Q,
}
