"""Medical Terminology chapter quizzes (one quiz per 3 chapters of a book).

Each question: (chapter, question, correct answer, [3 wrong answers], explanation).
Answer order and question order are shuffled with a fixed seed.
"""
import json, random, sys

# Book 0 = Ehrlich, Medical Terminology for Health Professions
EHRLICH_1_3 = [
    (1, 'In the combining form "gastr/o," the "o" is the:', "Combining vowel", ["Word root", "Suffix", "Prefix"], "A combining form is a word root plus a combining vowel, usually o."),
    (1, "When is the combining vowel usually dropped?", "When the suffix begins with a vowel", ["When the suffix begins with a consonant", "When two word roots are joined", "When the term has a prefix"], "Gastr/o + -itis = gastritis (vowel dropped). Gastr/o + -logy = gastrology (vowel kept)."),
    (1, "When defining a medical term, you usually start with the:", "Suffix", ["Prefix", "Word root", "Combining vowel"], "Define the suffix first, then the prefix, then the root(s): pericarditis = inflammation, around, heart."),
    (1, 'Which term is built correctly from "gastr/o" + "-itis"?', "Gastritis", ["Gastroitis", "Gastrotitis", "Gastritiis"], "The combining vowel is dropped because -itis begins with a vowel."),
    (1, "A disease named after a person, such as Alzheimer disease, is called an:", "Eponym", ["Acronym", "Homonym", "Synonym"], "An eponym is named after a person. An acronym is formed from initial letters, such as AIDS."),
    (2, "Which list shows the levels of body organization from simplest to most complex?", "Cells, tissues, organs, body systems", ["Tissues, cells, organs, body systems", "Cells, organs, tissues, body systems", "Organs, tissues, cells, body systems"], "Cells form tissues, tissues form organs, and organs work together as body systems."),
    (2, '"Distal" means:', "Farther from the point of attachment", ["Nearer the point of attachment", "Toward the midline", "Toward the back"], "Distal is the opposite of proximal. The hand is distal to the elbow."),
    (2, "The transverse plane divides the body into:", "Upper and lower parts", ["Left and right parts", "Front and back parts", "Equal left and right halves"], "Transverse = horizontal. Sagittal = left/right; frontal (coronal) = front/back; midsagittal = equal halves."),
    (2, "Which body cavity contains the heart and lungs?", "Thoracic cavity", ["Abdominal cavity", "Cranial cavity", "Pelvic cavity"], "The thoracic (chest) cavity is part of the ventral cavity and holds the heart and lungs."),
    (2, "Hemophilia is an example of a:", "Genetic (hereditary) disorder", ["Infectious disease", "Nutritional disorder", "Iatrogenic disorder"], "Hemophilia is an inherited blood-clotting disorder passed from parent to child."),
    (3, "Red bone marrow is responsible for:", "Making blood cells (hematopoiesis)", ["Storing fat", "Connecting bones to each other", "Producing synovial fluid"], "Red marrow makes blood cells; yellow marrow is mostly fat."),
    (3, "Which structure connects one bone to another bone?", "Ligament", ["Tendon", "Bursa", "Synovial membrane"], "Ligaments connect bone to bone. Tendons connect muscle to bone."),
    (3, '"Osteoporosis" is:', "Loss of bone density that makes bones fragile", ["Inflammation of bone and bone marrow", "Softening of bone from lack of vitamin D", "A degenerative joint disease"], "Osteomyelitis = bone and marrow inflammation; osteomalacia = softening; osteoarthritis = joint degeneration."),
    (3, "An open (compound) fracture is one in which:", "The broken bone pierces the skin", ["The bone is bent and only partly broken", "The bone is crushed into several pieces", "The bone stays in place under intact skin"], "Greenstick = bent and partly broken; comminuted = crushed; closed = skin intact."),
    (3, '"Arthroscopy" is:', "A visual examination of the inside of a joint", ["Surgical repair of a joint", "Surgical fusion of a joint", "Puncture of a joint to remove fluid"], "arthr/o (joint) + -scopy. Arthroplasty = repair, arthrodesis = fusion, arthrocentesis = fluid removal."),
]

def build(rows, seed):
    rng = random.Random(seed)
    rows = rows[:]
    rng.shuffle(rows)
    out = []
    for ch, q, right, wrong, expl in rows:
        assert len(wrong) == 3 and right not in wrong
        opts = [right] + wrong
        rng.shuffle(opts)
        out.append({"q": q, "options": opts, "answer": opts.index(right), "explanation": expl, "chapter": ch})
    return out

quizzes = {
    0: [{"chapters": [1, 2, 3], "questions": build(EHRLICH_1_3, 11)}],
}
for b, qz in quizzes.items():
    for z in qz:
        print("book", b, "chapters", z["chapters"], len(z["questions"]), "questions; answers:",
              "".join("ABCD"[q["answer"]] for q in z["questions"]))

js = ("// Medical Terminology chapter quizzes: one quiz per 3 chapters, keyed by the book's position\n"
      "// in this event's `books` list (data/events.js). 0 = Ehrlich, Medical Terminology for Health Professions.\n"
      "window.CONTENT = window.CONTENT || {};\n"
      "window.CONTENT[\"medical-terminology\"] = window.CONTENT[\"medical-terminology\"] || {};\n"
      "window.CONTENT[\"medical-terminology\"].quizzes = " + json.dumps(quizzes, indent=1, ensure_ascii=False) + ";\n")
open(sys.argv[1], "w", encoding="utf-8").write(js)
