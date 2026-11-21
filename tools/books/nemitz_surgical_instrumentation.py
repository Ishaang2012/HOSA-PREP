# Nemitz - Surgical Instrumentation: An Interactive Approach (Saunders/Elsevier).
# Chapter list: 5th edition (same chapters as the 4th), from the publisher's table of contents (us.elsevierhealth.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Introduction to Surgical Instruments", "Instruments are made mostly of stainless steel (some titanium or tungsten carbide). Parts include the jaws/tips, box lock, shanks, ratchets, and finger rings. Instrument categories are cutting/dissecting, grasping/holding, clamping/occluding, retracting/exposing, dilating, suctioning, and probing. Many are named for their inventors.", ["Stainless steel", "Box lock, ratchet, finger rings", "Instrument categories", "Named after inventors"]),
    ch(2, "Basic Sterilization", "Instruments are cleaned (manual and ultrasonic), inspected, assembled, packaged, and sterilized. Methods include steam (most common), ethylene oxide, hydrogen peroxide gas plasma, and immediate-use steam sterilization. Chemical indicators show exposure; biological indicators confirm sterility. Instruments are opened with ratchets unlocked during sterilization.", ["Clean before sterilizing", "Steam most common", "Biological indicators confirm sterility", "Open box locks"]),
    ch(3, "Basic Instruments", "A basic set includes scalpel handles (#3 holds blades #10, #11, #15; #4 holds #20-series), scissors (Mayo for heavy tissue and sutures; Metzenbaum for delicate tissue), forceps (Adson, DeBakey, Russian), hemostats (Kelly, mosquito, Crile), needle holders, towel clips, and retractors (Army-Navy, Richardson, Weitlaner).", ["#3 handle: #10, #11, #15 blades", "Mayo vs. Metzenbaum scissors", "Kelly and mosquito hemostats", "Army-Navy retractor"]),
    ch(4, "General Instruments", "General surgery sets include Allis (grasp tissue), Babcock (atraumatic for bowel), Kocher/Ochsner (heavy tissue with teeth), Balfour (self-retaining abdominal retractor), Deaver, malleable retractors, Yankauer (tonsil suction), and Poole suction (abdominal).", ["Allis grasps tissue", "Babcock is atraumatic", "Balfour self-retaining", "Yankauer and Poole suction"]),
    ch(5, "Laparoscopic Instruments", "Minimally invasive surgery uses trocars (ports), a Veress needle (creates pneumoperitoneum with CO2), laparoscopes (often 0° or 30°), graspers, scissors, clip appliers, and electrosurgical tools. Benefits include smaller incisions and faster recovery.", ["Veress needle → CO2", "Trocars", "0° and 30° scopes", "Faster recovery"]),
    ch(6, "Robotic Instruments", "Robotic-assisted surgery uses a surgeon console, patient-side cart, and instrument arms with wristed instruments for precise movement. Instruments have limited lives and need special cleaning.", ["Surgeon console", "Wristed instruments", "Limited instrument life", "Precision"]),
    ch(7, "Obstetrics and Gynecologic Instruments", "OB/GYN instruments include the weighted vaginal speculum, Graves speculum, tenaculum (grasps cervix), uterine sounds (measure uterine depth), dilators (Hegar, Pratt), curettes, Heaney clamps, and instruments for cesarean section.", ["Tenaculum grasps cervix", "Uterine sound measures depth", "Hegar dilators", "Heaney clamps"]),
    ch(8, "Genitourinary Instruments", "GU instruments include cystoscopes, urethral sounds and dilators, catheters, kidney stone forceps (Randall), and Satinsky and Mayo instruments for open procedures.", ["Cystoscope", "Urethral dilators", "Randall stone forceps", "Catheters"]),
    ch(9, "Ophthalmic Instruments", "Eye instruments are very small and delicate: lid speculum, castroviejo needle holders and calipers, fine forceps, micro scissors, and phaco handpieces for cataract surgery. They're handled with great care.", ["Lid speculum", "Castroviejo instruments", "Phacoemulsification", "Delicate handling"]),
    ch(10, "Otorhinolaryngology Instruments", "ENT instruments include nasal speculums, ear specula, myringotomy knives, tonsil instruments (tonsil snare, Hurd dissector, tonsil hemostats), adenoid curettes, and mouth gags (Crowe-Davis, McIvor).", ["Myringotomy knife", "Tonsil snare", "Crowe-Davis mouth gag", "Nasal speculum"]),
    ch(11, "Oral Instruments", "Oral surgery instruments include molt mouth gags, periosteal elevators, dental elevators, extraction forceps, rongeurs, and bone files.", ["Molt mouth gag", "Dental elevators", "Extraction forceps", "Rongeurs"]),
    ch(12, "Plastic and Reconstructive Instruments", "Plastic surgery uses fine instruments: skin hooks, Senn retractors, Adson forceps, Webster needle holders, iris scissors, and dermatomes (harvest skin grafts).", ["Skin hooks", "Senn retractor", "Dermatome for skin grafts", "Fine instruments"]),
    ch(13, "Orthopedic Instruments", "Orthopedic instruments include bone hooks, bone-holding forceps (Lane, Lowman), periosteal elevators, rongeurs, osteotomes and mallets, curettes, power drills and saws, and implants such as plates, screws, and rods.", ["Osteotome and mallet", "Bone-holding forceps", "Power drills and saws", "Plates and screws"]),
    ch(14, "Neurosurgical Instruments", "Neurosurgery uses cranial drills (perforators), Kerrison and Leksell rongeurs, Penfield dissectors, bipolar electrosurgery, brain retractors, and Frazier suction tips.", ["Kerrison rongeur", "Penfield dissector", "Frazier suction", "Cranial drills"]),
    ch(15, "Cardiovascular Thoracic Instruments", "Cardiothoracic instruments include rib spreaders (Finochietto), sternal saws, vascular clamps (DeBakey, Satinsky), Potts scissors, and bulldog clamps. Vascular clamps are atraumatic to protect vessels.", ["Finochietto rib spreader", "Sternal saw", "DeBakey vascular clamps", "Bulldog clamps"]),
    ch(16, "Basic Operating Room Supplies and Equipment", "OR supplies include sutures and needles, sponges (lap sponges, Raytec), drains, dressings, electrosurgical units (ESU), suction, and staplers. Counts of sponges, sharps, and instruments prevent retained items.", ["Sponge and sharps counts", "Electrosurgical unit", "Sutures and needles", "Drains"]),
    ch(17, "Surgical Setups", "Setting up the sterile field includes organizing the back table and Mayo stand in a standard order, performing counts, and anticipating the surgeon's needs for each procedure.", ["Back table setup", "Mayo stand", "Counts", "Anticipate needs"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Most surgical instruments are made of:", "Stainless steel", ["Plastic", "Aluminum", "Copper"], "Durable and corrosion resistant."),
        (1, "The joint where an instrument's two halves connect is the:", "Box lock", ["Ratchet", "Shank", "Finger ring"], "Inspect for debris."),
        (1, "Instruments that hold tissue aside are:", "Retractors", ["Clamps", "Scissors", "Probes"], "Retracting/exposing."),
        (2, "Before sterilization, ratcheted instruments should be:", "Opened (unlocked)", ["Closed tightly", "Taped shut", "Oiled heavily"], "Steam must reach all surfaces."),
        (2, "The most common sterilization method is:", "Steam", ["Ethylene oxide", "Boiling", "Alcohol soak"], "Autoclave."),
        (2, "Sterility is confirmed by:", "Biological indicators", ["Chemical indicators", "Tape color", "Package look"], "Spore tests."),
        (3, "Which scissors are for delicate tissue?", "Metzenbaum", ["Mayo", "Bandage scissors", "Wire cutters"], "Mayo cut heavy tissue and sutures."),
        (3, "A #15 blade fits on a:", "#3 knife handle", ["#4 handle", "#7 handle only", "Needle holder"], "#4 holds #20-series blades."),
        (3, "A small, delicate hemostat is a:", "Mosquito", ["Kocher", "Allis", "Babcock"], "For small vessels."),
    ]),
    ((4, 5, 6), [
        (4, "An atraumatic clamp used to grasp bowel is the:", "Babcock", ["Kocher", "Allis", "Towel clip"], "Smooth, rounded jaws."),
        (4, "A self-retaining abdominal retractor is the:", "Balfour", ["Army-Navy", "Deaver", "Senn"], "Holds the abdomen open."),
        (4, "A suction tip often used in the mouth and throat is the:", "Yankauer", ["Poole", "Frazier", "Veress"], "Tonsil suction."),
        (5, "The needle used to create pneumoperitoneum is the:", "Veress needle", ["Trocar", "Hypodermic needle", "Keith needle"], "Insufflates CO2."),
        (5, "The gas used to inflate the abdomen in laparoscopy is:", "Carbon dioxide", ["Oxygen", "Nitrogen", "Helium"], "Absorbed quickly."),
        (5, "Ports through which laparoscopic instruments pass are:", "Trocars", ["Retractors", "Speculums", "Drains"], "Different sizes."),
        (6, "In robotic surgery, the surgeon controls the instruments from a:", "Console", ["Back table", "Mayo stand", "Scrub sink"], "Away from the patient."),
        (6, "Robotic instruments often have:", "A limited number of uses", ["Unlimited lives", "No cleaning needs", "No moving parts"], "Tracked by the system."),
        (6, "A key benefit of robotic instruments is:", "Wristed, precise movement", ["Larger incisions", "Longer recovery", "Less accuracy"], "Mimics the wrist."),
    ]),
    ((7, 8, 9), [
        (7, "The instrument that grasps the cervix is the:", "Tenaculum", ["Speculum", "Sound", "Dilator"], "Has sharp tips."),
        (7, "Uterine depth is measured with a:", "Uterine sound", ["Tenaculum", "Curette", "Hegar dilator"], "Graduated markings."),
        (7, "Hegar and Pratt instruments are:", "Dilators", ["Retractors", "Clamps", "Scissors"], "Dilate the cervix."),
        (8, "The bladder is viewed with a:", "Cystoscope", ["Laparoscope", "Bronchoscope", "Otoscope"], "Through the urethra."),
        (8, "Kidney stones are removed in open surgery with:", "Randall stone forceps", ["Babcock clamps", "Allis clamps", "Kelly clamps"], "Curved jaws."),
        (8, "Urethral strictures may be widened with:", "Urethral dilators (sounds)", ["Rib spreaders", "Osteotomes", "Bone hooks"], "Graduated sizes."),
        (9, "Eyelids are held open during eye surgery with a:", "Lid speculum", ["Senn retractor", "Army-Navy", "Weitlaner"], "Spring-loaded."),
        (9, "Cataracts are often removed with:", "Phacoemulsification", ["Rongeurs", "Osteotomes", "Staplers"], "Ultrasonic breakup of the lens."),
        (9, "Ophthalmic instruments must be handled:", "With great care", ["Roughly", "In heavy trays stacked", "Without inspection"], "Tiny and delicate."),
    ]),
    ((10, 11, 12), [
        (10, "A small incision in the eardrum is made with a:", "Myringotomy knife", ["Scalpel #20", "Osteotome", "Kerrison"], "To place tubes."),
        (10, "A mouth gag used for tonsillectomy is the:", "Crowe-Davis", ["Molt", "Balfour", "Finochietto"], "Holds mouth open and tongue down."),
        (10, "The nose is examined with a:", "Nasal speculum", ["Otoscope only", "Laryngoscope", "Sound"], "Spreads nostrils."),
        (11, "A mouth gag used in oral surgery is the:", "Molt", ["Crowe-Davis", "Balfour", "Weitlaner"], "Ratcheted side gag."),
        (11, "Teeth are luxated with:", "Elevators", ["Rongeurs", "Bone files", "Hemostats"], "Before forceps."),
        (11, "Rough bone edges are smoothed with a:", "Bone file", ["Osteotome", "Elevator", "Curette"], "After extractions."),
        (12, "A dermatome is used to:", "Harvest skin grafts", ["Cut bone", "Clamp vessels", "Retract tissue"], "Takes thin skin layers."),
        (12, "Small, sharp hooks used to retract skin edges are:", "Skin hooks", ["Towel clips", "Bone hooks", "Allis clamps"], "Fine retraction."),
        (12, "A small handheld retractor with a rake end is the:", "Senn retractor", ["Balfour", "Deaver", "Richardson"], "Double-ended."),
    ]),
    ((13, 14, 15), [
        (13, "Bone is cut or shaped with an osteotome and:", "Mallet", ["Scalpel", "Needle holder", "Hemostat"], "Struck to cut."),
        (13, "Fractured bone ends are held with:", "Bone-holding forceps", ["Babcocks", "Mosquitoes", "Skin hooks"], "Like Lane or Lowman."),
        (13, "Fractures are often fixed with plates and:", "Screws", ["Staples only", "Sutures only", "Glue only"], "Internal fixation."),
        (14, "A rongeur used in spine surgery to remove bone is the:", "Kerrison", ["Leksell only", "Babcock", "Allis"], "Bites lamina."),
        (14, "A suction tip commonly used in neurosurgery is the:", "Frazier", ["Poole", "Yankauer", "Veress"], "Fine, angled."),
        (14, "A dissector often used in neurosurgery is the:", "Penfield", ["Kocher", "Mayo", "Balfour"], "Numbered 1–5."),
        (15, "Ribs are spread apart with a:", "Finochietto retractor", ["Balfour", "Weitlaner", "Army-Navy"], "Thoracotomy."),
        (15, "Vascular clamps are designed to be:", "Atraumatic", ["Sharp-toothed", "Heavy crushing", "Disposable only"], "Protect vessels."),
        (15, "Small spring clamps for vessels are:", "Bulldog clamps", ["Towel clips", "Allis clamps", "Kochers"], "Temporary occlusion."),
    ]),
    ((16, 17), [
        (16, "Counts of sponges, sharps, and instruments prevent:", "Retained surgical items", ["Infection only", "Bleeding", "Delays"], "Done before, during, and after."),
        (16, "The device that cuts and coagulates tissue with electric current is the:", "Electrosurgical unit", ["Suction", "Stapler", "Dermatome"], "ESU or Bovie."),
        (16, "Large abdominal sponges are called:", "Lap sponges", ["Peanuts", "Cotton balls", "Raytec 4x4s"], "Laparotomy sponges."),
        (17, "The small tray placed over the patient for frequently used instruments is the:", "Mayo stand", ["Back table", "Kick bucket", "Ring stand"], "Within easy reach."),
        (17, "A good surgical technologist tries to:", "Anticipate the surgeon's needs", ["Wait to be asked every time", "Leave the field", "Rearrange randomly"], "Know the procedure."),
        (17, "The back table is organized:", "In a standard, consistent order", ["Randomly", "By color only", "By price"], "Speeds counts and setup."),
        (16, "Tubes placed to remove fluid from a wound are:", "Drains", ["Sutures", "Staples", "Sponges"], "Like Jackson-Pratt."),
        (17, "Counts are performed:", "Before, during, and at closure", ["Only at the end", "Never", "Only if requested"], "Required by policy."),
        (16, "Sutures attached to needles without an eye are:", "Swaged (atraumatic)", ["Eyed", "French-eye only", "Free ties"], "Less tissue damage."),
    ]),
]

BOOK = {
    "titles": ["Surgical Instrumentation: An Interactive Approach"],
    "edition": "5th edition",
    "source": "Elsevier table of contents",
    "chapters": C,
    "quizzes": Q,
}
