# Nelson - Wheeler's Dental Anatomy, Physiology and Occlusion (Elsevier).
# Chapter list: 11th edition, from the publisher's table of contents (us.elsevierhealth.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Introduction to Dental Anatomy", "Dental anatomy covers tooth form, terms, and numbering. Teeth have a crown (covered by enamel) and root (covered by cementum), meeting at the cementoenamel junction (CEJ). Surfaces are mesial, distal, facial (labial/buccal), lingual, and occlusal or incisal. The Universal system numbers permanent teeth 1–32 starting with the maxillary right third molar. Crowns are divided into thirds.", ["Crown, root, CEJ", "Tooth surfaces", "Universal 1–32", "Thirds of the crown"]),
    ch(2, "Development and Eruption of the Teeth", "Teeth form from the dental lamina through bud, cap, and bell stages. Calcification, eruption, and root completion follow a schedule. Primary teeth begin erupting around 6 months (mandibular central incisors first); the first permanent molar erupts around age 6.", ["Bud, cap, bell", "Primary eruption ~6 months", "First permanent molar ~6 years", "Root completion after eruption"]),
    ch(3, "The Primary (Deciduous) Teeth", "There are 20 primary teeth (incisors, canines, molars; no premolars). They have thinner enamel, larger pulps, whiter color, constricted cervical areas, and flared, thin roots that make room for permanent tooth buds. Primary teeth guide permanent teeth into position.", ["20 teeth, no premolars", "Thin enamel, large pulps", "Flared roots", "Space maintainers"]),
    ch(4, "Forensics, Comparative Anatomy, Geometries, and Form and Function", "Dental anatomy helps identify people (forensic odontology) through dental records and bite marks. Comparative anatomy contrasts human teeth with other animals. Crown outlines follow geometric shapes (triangles, trapezoids, rhomboids) that relate to function.", ["Forensic identification", "Comparative anatomy", "Geometric crown outlines", "Form follows function"]),
    ch(5, "Orofacial Complex: Form and Function", "Teeth work with the jaws, TMJ, muscles, tongue, and lips for chewing, speech, and swallowing. Contours such as contact areas, embrasures, and height of contour protect the gingiva and direct food.", ["Contact areas", "Embrasures", "Height of contour", "Chewing, speech, swallowing"]),
    ch(6, "The Permanent Maxillary Incisors", "The maxillary central incisor is the widest anterior tooth, with a single conical root and lingual fossa, marginal ridges, and cingulum. The lateral incisor is smaller and more variable (may be peg-shaped or missing).", ["Central: widest anterior", "Lateral: most variable", "Cingulum and lingual fossa", "Single root"]),
    ch(7, "The Permanent Mandibular Incisors", "Mandibular incisors are the smallest permanent teeth, with narrow, symmetrical crowns (central) and roots that are flattened mesiodistally. The central incisor is usually the first permanent tooth to erupt with the first molar.", ["Smallest teeth", "Symmetrical central", "Flattened roots", "Erupt early"]),
    ch(8, "The Permanent Canines, Maxillary and Mandibular", "Canines are the cornerstones of the arch with a single cusp. The maxillary canine has the longest root of any tooth. Canines guide the jaw in lateral movements (canine guidance).", ["Longest root: maxillary canine", "Cornerstones of arch", "Single cusp", "Canine guidance"]),
    ch(9, "The Permanent Maxillary Premolars", "Maxillary premolars have two cusps (buccal and lingual). The maxillary first premolar usually has two roots (buccal and lingual) and a mesial crown concavity; the second premolar has one root and more equal cusps.", ["First premolar: two roots", "Mesial concavity", "Two cusps", "Second premolar: one root"]),
    ch(10, "The Permanent Mandibular Premolars", "The mandibular first premolar has a large buccal cusp and small lingual cusp (resembles a canine). The second premolar may have two or three cusps (Y-, U-, or H-shaped groove patterns). Both usually have one root.", ["First premolar resembles canine", "Second: 2 or 3 cusps", "Y, U, H patterns", "Single root"]),
    ch(11, "The Permanent Maxillary Molars", "Maxillary molars have three roots (mesiobuccal, distobuccal, palatal; the palatal is longest). The first molar has four cusps plus often a cusp of Carabelli and an oblique ridge. Second and third molars are smaller and more variable.", ["Three roots", "Palatal root longest", "Cusp of Carabelli", "Oblique ridge"]),
    ch(12, "The Permanent Mandibular Molars", "Mandibular molars have two roots (mesial and distal). The first molar has five cusps (three buccal, two lingual); the second molar has four. Third molars are most variable and often impacted.", ["Two roots", "First molar: five cusps", "Second molar: four cusps", "Third molars often impacted"]),
    ch(13, "Pulp Chambers and Canals", "The pulp chamber in the crown continues as root canals to the apical foramen. Pulp horns extend under cusps. Pulp size shrinks with age as secondary dentin forms. Knowledge of canal anatomy (e.g., the mesiobuccal root of maxillary molars often has two canals) guides endodontics.", ["Pulp horns under cusps", "Pulp shrinks with age", "Apical foramen", "MB root may have 2 canals"]),
    ch(14, "Dento-Osseous Structures, Blood Vessels and Nerves", "Teeth sit in alveolar bone supported by the periodontal ligament. Blood supply comes from the maxillary artery (alveolar branches). Nerve supply is from the trigeminal nerve: maxillary teeth from superior alveolar nerves, mandibular teeth from the inferior alveolar nerve.", ["Alveolar bone and PDL", "Maxillary artery", "Superior alveolar nerves", "Inferior alveolar nerve"]),
    ch(15, "The Temporomandibular Joints, Teeth, and Muscles and Their Functions", "The TMJ connects the mandibular condyle to the temporal bone with an articular disc. It allows rotation (hinge) and translation (gliding). Muscles of mastication include the masseter, temporalis, medial pterygoid (close) and lateral pterygoid (opens and protrudes).", ["Condyle and articular disc", "Rotation and translation", "Lateral pterygoid opens", "Masseter closes"]),
    ch(16, "Occlusion", "Occlusion is how teeth contact. Centric occlusion is maximum intercuspation; centric relation is the jaw position with condyles seated. Angle's classification: Class I (normal molar relation), Class II (mandible back), Class III (mandible forward). Overbite is vertical overlap; overjet is horizontal overlap.", ["Centric occlusion vs. relation", "Angle's Classes I–III", "Overbite = vertical", "Overjet = horizontal"]),
    ch(17, "Clinical Applications of Dental Anatomy, Physiology and Occlusion", "Dental anatomy guides restorations, crowns, and orthodontics. Restorations must recreate proper contours, contacts, and occlusion to protect the gingiva and function well.", ["Restore proper contours", "Contacts protect gingiva", "Occlusion in restorations", "Clinical relevance"]),
]

Q = [
    ((1, 2, 3), [
        (1, "The line where enamel meets cementum is the:", "Cementoenamel junction", ["Apex", "Cingulum", "Furcation"], "CEJ."),
        (1, "In the Universal system, tooth #1 is the:", "Maxillary right third molar", ["Maxillary left third molar", "Mandibular right third molar", "Maxillary right central"], "Numbering goes around clockwise."),
        (1, "The tooth surface facing the tongue is:", "Lingual", ["Facial", "Mesial", "Distal"], "Facial faces the lips or cheeks."),
        (2, "The first primary teeth to erupt are usually the:", "Mandibular central incisors", ["Maxillary canines", "First molars", "Second molars"], "Around 6 months."),
        (2, "The first permanent molar erupts around age:", "6", ["2", "12", "18"], "'Six-year molar.'"),
        (2, "Tooth development stages include bud, cap, and:", "Bell", ["Crown", "Root", "Pulp"], "Then apposition and maturation."),
        (3, "The primary dentition has how many teeth?", "20", ["32", "28", "24"], "No premolars."),
        (3, "Compared to permanent teeth, primary teeth have:", "Larger pulps and thinner enamel", ["Smaller pulps", "Thicker enamel", "Longer roots"], "Decay spreads faster."),
        (3, "Primary molar roots are flared to make room for:", "Permanent tooth buds", ["Blood vessels", "Nerves", "Bone"], "Premolars develop between them."),
    ]),
    ((4, 5, 6), [
        (4, "Using teeth to identify people is:", "Forensic odontology", ["Orthodontics", "Endodontics", "Periodontics"], "Dental records and bite marks."),
        (4, "From the proximal view, anterior crowns are shaped like:", "Triangles (wedges)", ["Circles", "Squares", "Hexagons"], "Suited for cutting."),
        (5, "The spaces next to contact areas are:", "Embrasures", ["Fossae", "Grooves", "Ridges"], "Allow food to escape."),
        (5, "The greatest bulge of a tooth surface is the:", "Height of contour", ["Cingulum", "Marginal ridge", "Apex"], "Protects the gingiva."),
        (5, "Proper contact areas help:", "Protect the gingiva from food", ["Whiten teeth", "Lengthen roots", "Prevent eruption"], "Prevent food impaction."),
        (6, "The widest anterior tooth is the:", "Maxillary central incisor", ["Mandibular central incisor", "Maxillary lateral incisor", "Mandibular canine"], "Mesiodistally."),
        (6, "The most variable incisor, sometimes peg-shaped, is the:", "Maxillary lateral incisor", ["Maxillary central", "Mandibular central", "Mandibular lateral"], "May be missing."),
        (6, "The bulge on the lingual cervical third of anterior teeth is the:", "Cingulum", ["Marginal ridge", "Cusp", "Fossa"], "Lingual surface feature."),
        (4, "Posterior crowns from the proximal view are shaped like:", "Trapezoids or rhomboids", ["Triangles", "Circles", "Stars"], "Suited for grinding."),
    ]),
    ((7, 8, 9), [
        (7, "The smallest permanent teeth are the:", "Mandibular incisors", ["Maxillary incisors", "Canines", "Premolars"], "Especially the central."),
        (7, "The most symmetrical incisor is the:", "Mandibular central incisor", ["Maxillary central", "Maxillary lateral", "Mandibular lateral"], "Mesial and distal halves alike."),
        (7, "Mandibular incisor roots are flattened:", "Mesiodistally", ["Faciolingually", "Not at all", "Occlusally"], "Narrow side to side."),
        (8, "The tooth with the longest root is the:", "Maxillary canine", ["Maxillary central", "Mandibular first molar", "Mandibular canine"], "Very stable."),
        (8, "Canines are called the:", "Cornerstones of the arch", ["Grinding teeth", "Baby teeth", "Wisdom teeth"], "At the arch corners."),
        (8, "During side-to-side movement, canines often guide the jaw. This is:", "Canine guidance", ["Group function", "Centric relation", "Overjet"], "Protects posterior teeth."),
        (9, "The maxillary first premolar usually has:", "Two roots", ["One root", "Three roots", "Four roots"], "Buccal and lingual."),
        (9, "A depression on the mesial crown of the maxillary first premolar is the:", "Mesial concavity", ["Cingulum", "Cusp of Carabelli", "Oblique ridge"], "Hard to restore."),
        (9, "Maxillary premolars typically have how many cusps?", "Two", ["One", "Three", "Five"], "Buccal and lingual."),
    ]),
    ((10, 11, 12), [
        (10, "The mandibular first premolar resembles a:", "Canine", ["Molar", "Incisor", "Primary tooth"], "Large buccal cusp."),
        (10, "The mandibular second premolar may have groove patterns described as:", "Y, U, or H", ["A, B, C", "X, O", "I, L"], "Two or three cusps."),
        (10, "Mandibular premolars usually have:", "One root", ["Two roots", "Three roots", "No roots"], "Single conical root."),
        (11, "Maxillary molars usually have how many roots?", "Three", ["One", "Two", "Four"], "MB, DB, palatal."),
        (11, "The longest root of the maxillary first molar is the:", "Palatal (lingual) root", ["Mesiobuccal", "Distobuccal", "Mesial"], "Points toward the palate."),
        (11, "An extra cusp on the lingual of the maxillary first molar is the:", "Cusp of Carabelli", ["Cingulum", "Tubercle of Zuckerkandl", "Oblique ridge"], "Fifth cusp."),
        (12, "Mandibular molars usually have how many roots?", "Two", ["One", "Three", "Four"], "Mesial and distal."),
        (12, "The mandibular first molar has how many cusps?", "Five", ["Three", "Four", "Six"], "Three buccal, two lingual."),
        (12, "The molars most often impacted are the:", "Third molars", ["First molars", "Second molars", "Premolars"], "Wisdom teeth."),
    ]),
    ((13, 14, 15), [
        (13, "Extensions of the pulp under cusps are:", "Pulp horns", ["Canals", "Foramina", "Fossae"], "Risk during cavity prep."),
        (13, "With age, the pulp chamber:", "Gets smaller", ["Gets larger", "Stays the same", "Disappears immediately"], "Secondary dentin forms."),
        (13, "The opening at the root tip is the:", "Apical foramen", ["Furcation", "CEJ", "Pulp horn"], "Vessels and nerves enter."),
        (14, "Mandibular teeth are supplied by the:", "Inferior alveolar nerve", ["Superior alveolar nerves", "Facial nerve", "Vagus nerve"], "Branch of V3."),
        (14, "The tissue that attaches teeth to alveolar bone is the:", "Periodontal ligament", ["Enamel", "Gingiva", "Pulp"], "Absorbs force."),
        (14, "Teeth get their blood supply mainly from the:", "Maxillary artery", ["Carotid sinus", "Subclavian artery", "Aorta directly"], "Alveolar branches."),
        (15, "The muscle that opens the jaw and moves it forward is the:", "Lateral pterygoid", ["Masseter", "Temporalis", "Medial pterygoid"], "Others close the jaw."),
        (15, "The TMJ disc sits between the condyle and the:", "Temporal bone", ["Maxilla", "Zygoma", "Hyoid"], "Articular eminence."),
        (15, "The TMJ performs hinge movement and:", "Gliding (translation)", ["Rotation only", "No movement", "Twisting only"], "Combination joint."),
    ]),
    ((16, 17), [
        (16, "Vertical overlap of anterior teeth is:", "Overbite", ["Overjet", "Crossbite", "Open bite"], "Overjet is horizontal."),
        (16, "In Angle's Class III malocclusion, the mandible is:", "Forward (prognathic)", ["Back", "Normal", "Missing"], "Underbite."),
        (16, "Maximum intercuspation of teeth is:", "Centric occlusion", ["Centric relation", "Rest position", "Protrusion"], "Teeth fit together fully."),
        (16, "Angle's Class I describes:", "Normal molar relationship", ["Mandible back", "Mandible forward", "Open bite"], "Crowding may still occur."),
        (17, "Restorations must recreate proper contours to:", "Protect the gingiva and function well", ["Look shiny only", "Be easy to make", "Cost less"], "Contours matter."),
        (17, "Open contacts in restorations can cause:", "Food impaction", ["Stronger teeth", "Whiter teeth", "Faster eruption"], "Leads to gum problems."),
        (16, "Horizontal overlap of anterior teeth is:", "Overjet", ["Overbite", "Crossbite", "Centric relation"], "Measured in mm."),
        (17, "High spots on a new restoration can cause:", "Occlusal problems and pain", ["Better chewing", "No effect", "Whitening"], "Check with articulating paper."),
        (16, "The jaw position with condyles fully seated is:", "Centric relation", ["Centric occlusion", "Overjet", "Rest position"], "Reproducible reference."),
    ]),
]

BOOK = {
    "titles": ["Wheeler's Dental Anatomy, Physiology and Occlusion"],
    "edition": "11th edition",
    "source": "Elsevier table of contents",
    "chapters": C,
    "quizzes": Q,
}
