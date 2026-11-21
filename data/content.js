/*
 * Study content, keyed by event id (see data/events.js).
 *
 * Shape of one event:
 * {
 *   summaries: {
 *     <bookIndex>: [ { number, title, summary: [ "paragraph", ... ], keyPoints: [ "..." ] } ]
 *   },                     // bookIndex = position of the book in that event's `books` list
 *   tests: {             // usually in its own file: data/tests/<event-id>.js
 *     easy:   [ { q, options: [..4], answer: <index>, explanation, topic } ],
 *     medium: [ ... ],     // each level must have exactly the event's testQuestions (50)
 *     hard:   [ ... ],     // before the site opens it
 *   },
 *   flashcards: [
 *     { section: "Prefixes", description: "...", cards: [ { front, back } ] }
 *   ]
 * }
 *
 * Events or books with no entry here show a "coming soon" state.
 */
window.CONTENT = {
  "medical-terminology": {
    // Chapter summaries, keyed by the book's position in this event's `books` list (data/events.js).
    // 0 = Ehrlich, Medical Terminology for Health Professions
    summaries: {
      0: [
          {
            number: 1,
            title: "Introduction to Medical Terminology",
            summary: [
              "Medical terms are built from a small set of word parts: the word root (the core meaning, usually a body part), the combining form (root + combining vowel, usually \"o\"), prefixes (placed before the root to modify meaning), and suffixes (placed after the root to indicate a procedure, condition, or disease).",
              "To define a term, start with the suffix, then the prefix, then the root. For example, pericarditis = -itis (inflammation) + peri- (around) + card (heart): inflammation of the tissue around the heart.",
              "The combining vowel is kept when the suffix starts with a consonant (cardiology) and dropped when it starts with a vowel (carditis). It is usually kept between two roots (gastroenterology).",
            ],
            keyPoints: [
              "Word root + combining vowel = combining form",
              "Read definitions suffix → prefix → root",
              "Most terms have Greek or Latin origins",
            ],
          },
          {
            number: 2,
            title: "The Human Body in Health and Disease",
            summary: [
              "The body is organized from smallest to largest: cells → tissues → organs → body systems → whole organism. The four main tissue types are epithelial, connective, muscle, and nervous.",
              "Directional terms describe location relative to anatomical position (standing, facing forward, palms forward). Key pairs: superior/inferior, anterior (ventral)/posterior (dorsal), medial/lateral, proximal/distal, superficial/deep.",
              "Body planes divide the body for imaging and description: the sagittal plane (left/right), the frontal or coronal plane (front/back), and the transverse plane (upper/lower).",
            ],
            keyPoints: [
              "Proximal/distal are used for limbs",
              "Midsagittal plane = equal left and right halves",
              "Dorsal and ventral are the two main body cavities",
            ],
          },
          {
            number: 3,
            title: "The Skeletal System",
            summary: [
              "The skeleton supports and protects the body, stores minerals (especially calcium), and makes blood cells in the red bone marrow (hematopoiesis). Combining forms include oste/o (bone), arthr/o (joint), chondr/o (cartilage), and myel/o (bone marrow or spinal cord).",
              "Common conditions include osteoporosis (loss of bone density), osteoarthritis (degenerative joint disease), and fractures, such as closed, open (compound), comminuted, and greenstick.",
            ],
            keyPoints: [
              "Ligaments connect bone to bone",
              "Osteoporosis increases fracture risk",
              "Arthroscopy = visual exam of a joint's interior",
            ],
          },
          {
            number: 5,
            title: "The Cardiovascular System",
            summary: [
              "The heart pumps blood through two circuits: pulmonary (to the lungs for oxygen) and systemic (to the rest of the body). Blood flows right atrium → tricuspid valve → right ventricle → pulmonary valve → lungs → left atrium → mitral (bicuspid) valve → left ventricle → aortic valve → aorta.",
              "Combining forms include cardi/o (heart), angi/o and vas/o (vessel), arteri/o (artery), phleb/o and ven/o (vein), and hem/o or hemat/o (blood).",
              "Key conditions: hypertension (high blood pressure), myocardial infarction (heart attack, tissue death from blocked blood flow), atherosclerosis (plaque in the arteries), and arrhythmia (irregular heartbeat).",
            ],
            keyPoints: [
              "Arteries carry blood away from the heart",
              "The left ventricle has the thickest wall",
              "The SA node is the heart's natural pacemaker",
            ],
          },
      ],
    },

    // Practice tests: data/tests/medical-terminology.js. Flashcards: data/flashcards/medical-terminology.js
  },
};
