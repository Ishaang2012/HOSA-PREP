# Beam - Orthopedic Taping, Wrapping, Bracing, & Padding (F.A. Davis).
# Chapter list: 4th edition (2021), from booksellers' published contents listings (13 chapters).
# Summaries are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Tapes, Wraps, Braces, and Pads", "Supplies include non-elastic white tape (support), elastic tape (allows movement), kinesiology tape, underwrap and pre-wrap, elastic wraps, braces (prophylactic, functional, rehabilitative), and pads (soft and hard). Each has specific uses and limits.", ["Non-elastic vs. elastic tape", "Underwrap", "Brace types", "Soft vs. hard pads"]),
    ch(2, "Facility Design for Taping, Wrapping, Bracing, and Padding", "A taping area needs proper table height, good lighting, ventilation, organized storage, and sanitation. Infection control and efficient workflow matter in busy athletic training rooms.", ["Table height", "Organized storage", "Sanitation", "Workflow"]),
    ch(3, "Foot and Toes", "Common conditions include arch strains, plantar fasciitis, turf toe, and blisters. Techniques include arch taping (X-arch), low-Dye taping, turf toe taping, and protective pads like donut pads.", ["Low-Dye taping", "Turf toe taping", "Arch support", "Blister care"]),
    ch(4, "Ankle", "Ankle sprains are usually inversion injuries. The closed basket weave with stirrups and horseshoes supports the ankle; heel locks add stability. Lace-up and stirrup braces are alternatives.", ["Inversion sprains", "Closed basket weave", "Heel locks", "Ankle braces"]),
    ch(5, "Lower Leg", "Lower leg conditions include shin splints (medial tibial stress syndrome), Achilles tendinopathy, and contusions. Techniques include shin splint taping, Achilles taping to limit dorsiflexion, and compression wraps.", ["Shin splints", "Achilles taping", "Compression wraps", "Contusion padding"]),
    ch(6, "Knee", "Knee conditions include MCL/LCL sprains, hyperextension, and patellofemoral pain. Collateral taping, hyperextension taping, patellar taping (McConnell), and knee braces provide support.", ["Collateral ligament taping", "Hyperextension taping", "McConnell taping", "Knee braces"]),
    ch(7, "Thigh, Hip, and Pelvis", "Conditions include quadriceps contusions, hamstring and groin strains, and hip pointers. Hip spica wraps support groin and hip flexor strains; pads protect contusions.", ["Quad contusion", "Hip spica wrap", "Groin strain", "Hip pointer padding"]),
    ch(8, "Shoulder and Upper Arm", "Conditions include AC sprains, glenohumeral instability, and contusions. Techniques include AC joint taping with a donut pad, shoulder spica wraps, and stabilizing braces.", ["AC joint taping", "Shoulder spica", "Instability braces", "Contusion pads"]),
    ch(9, "Elbow and Forearm", "Conditions include elbow hyperextension, collateral sprains, and lateral epicondylitis. Techniques include hyperextension taping, figure-8 wraps, and counterforce straps.", ["Hyperextension taping", "Figure-8 wrap", "Counterforce strap", "Epicondylitis"]),
    ch(10, "Wrist", "Wrist sprains and strains are supported with circular wrist taping, figure-8 techniques, and wrist braces to limit painful motion.", ["Circular wrist taping", "Figure-8", "Limit hyperextension", "Wrist braces"]),
    ch(11, "Hand, Fingers, and Thumb", "Conditions include finger sprains, thumb (UCL) sprains, and mallet finger. Techniques include buddy taping, thumb spica taping, and finger splints.", ["Buddy taping", "Thumb spica", "Mallet finger splint", "UCL sprain"]),
    ch(12, "Thorax, Abdomen, and Spine", "Rib contusions and fractures are protected with padding and rib belts; low back strains may use braces or supportive wraps. Serious injuries require referral.", ["Rib protection", "Flak jackets", "Low back support", "Referral for serious injury"]),
    ch(13, "Protective Equipment and Padding", "Protective equipment includes helmets, mouthguards, shoulder pads, and custom pads made from thermoplastic or foam. Equipment must fit properly and meet sport rules and standards (e.g., NOCSAE for helmets).", ["Proper fit", "Mouthguards", "Custom pads", "NOCSAE standards"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Non-elastic white tape is used mainly for:", "Support and limiting motion", ["Compression only", "Allowing full motion", "Heating"], "Rigid support."),
        (1, "A thin foam layer under tape to protect skin is:", "Underwrap (pre-wrap)", ["Moleskin", "Gauze", "Kinesiology tape"], "Reduces irritation."),
        (1, "Braces used to prevent injury are:", "Prophylactic braces", ["Rehabilitative braces", "Functional braces only", "Casts"], "Worn before injury."),
        (2, "A taping area needs a table at:", "A comfortable working height", ["Floor level", "Any height", "Above the head"], "Protects the clinician's back."),
        (2, "Taping supplies should be:", "Organized and stored cleanly", ["Left on the floor", "Shared without cleaning", "Kept wet"], "Infection control."),
        (2, "Taping tables should be cleaned:", "Regularly with disinfectant", ["Never", "Once a year", "Only if visibly dirty"], "Prevents infection."),
        (3, "Heel pain worst with first morning steps suggests:", "Plantar fasciitis", ["Turf toe", "Ankle sprain", "Shin splints"], "Arch taping can help."),
        (3, "Sprain of the big toe from hyperextension is:", "Turf toe", ["Plantar fasciitis", "Bunion", "Hammer toe"], "Tape to limit extension."),
        (3, "A taping technique that supports the arch is:", "Low-Dye taping", ["Basket weave", "Spica", "Buddy taping"], "Arch support."),
    ]),
    ((4, 5, 6), [
        (4, "Most ankle sprains are:", "Inversion sprains", ["Eversion sprains", "High ankle sprains always", "Fractures"], "Foot rolls inward."),
        (4, "A common preventive ankle taping is the:", "Closed basket weave", ["Figure-8 elbow", "Thumb spica", "X-arch"], "Stirrups and horseshoes."),
        (4, "Heel locks are added to ankle taping for:", "Extra stability", ["Cooling", "Arch support", "Decoration"], "Limit heel motion."),
        (5, "Medial tibial stress syndrome is also called:", "Shin splints", ["Achilles rupture", "Turf toe", "Hip pointer"], "Pain along the tibia."),
        (5, "Achilles taping is used to limit:", "Dorsiflexion", ["Plantarflexion", "Inversion", "Eversion"], "Reduces tendon stretch."),
        (5, "Elastic wraps on the lower leg provide:", "Compression", ["Rigid immobilization", "Heat", "Traction"], "Reduce swelling."),
        (6, "Collateral knee taping supports the:", "MCL and LCL", ["ACL only", "Patella only", "Meniscus"], "Side ligaments."),
        (6, "Taping to correct patellar tracking is:", "McConnell taping", ["Low-Dye taping", "Basket weave", "Spica"], "Patellofemoral pain."),
        (6, "Taping that prevents the knee from straightening too far is:", "Hyperextension taping", ["Collateral taping", "Patellar taping", "Spica"], "Limits extension."),
    ]),
    ((7, 8, 9), [
        (7, "A wrap that supports groin and hip flexor strains is a:", "Hip spica", ["Figure-8 elbow", "Basket weave", "Buddy tape"], "Spica = figure-8 around a joint."),
        (7, "A bruise to the iliac crest is a:", "Hip pointer", ["Groin strain", "Quad contusion", "Hamstring strain"], "Pad for protection."),
        (7, "A deep thigh bruise in contact sports is a:", "Quadriceps contusion", ["Hamstring strain", "Hip pointer", "Shin splint"], "Pad and protect."),
        (8, "An AC sprain is often protected with taping and a:", "Donut pad", ["Arch pad", "Heel cup", "Mouthguard"], "Relieves pressure."),
        (8, "A wrap around the shoulder and chest is a:", "Shoulder spica", ["Hip spica", "Figure-8 wrist", "Buddy wrap"], "Supports the shoulder."),
        (8, "Athletes with shoulder instability may wear a:", "Stabilizing brace", ["Knee brace", "Wrist splint", "Arch support"], "Limits risky motion."),
        (9, "Tennis elbow is often treated with a:", "Counterforce strap", ["Knee brace", "Heel lift", "Mouthguard"], "Reduces tendon stress."),
        (9, "Taping to stop the elbow from straightening too far is:", "Hyperextension taping", ["Buddy taping", "Spica", "Circular taping"], "Limits extension."),
        (9, "A figure-8 elbow wrap provides:", "Compression and support", ["Rigid immobilization", "Heat", "Cooling"], "Around the joint."),
    ]),
    ((10, 11, 12, 13)[:3], [
        (10, "Simple wrist support uses:", "Circular wrist taping", ["Buddy taping", "Low-Dye", "Basket weave"], "Around the wrist."),
        (10, "Wrist taping often limits:", "Painful hyperextension", ["All finger motion", "Elbow motion", "Shoulder motion"], "Protects sprains."),
        (10, "A brace for wrist sprains limits:", "Painful wrist motion", ["Ankle motion", "Neck motion", "Breathing"], "Support during return."),
        (11, "Taping an injured finger to the next finger is:", "Buddy taping", ["Spica", "Basket weave", "Low-Dye"], "Splints with a neighbor."),
        (11, "A thumb UCL sprain is supported with:", "Thumb spica taping", ["Buddy taping", "Arch taping", "Hip spica"], "Limits thumb motion."),
        (11, "Inability to straighten the fingertip after a jammed finger is:", "Mallet finger", ["Boxer's fracture", "Trigger finger", "Turf toe"], "Splint in extension."),
        (12, "Rib injuries in contact sports are protected by:", "Rib padding or flak jackets", ["Mouthguards", "Knee braces", "Heel cups"], "Absorb impact."),
        (12, "Suspected rib fractures with breathing trouble require:", "Medical referral", ["Taping only", "Ignoring", "Ice only"], "Possible lung injury."),
        (12, "Low back strains may be supported with:", "Braces or wraps", ["Mouthguards", "Finger splints", "Ankle tape"], "Temporary support."),
    ]),
    ((13,), [
        (13, "Football helmets must meet standards set by:", "NOCSAE", ["OSHA", "FDA", "NATA"], "National Operating Committee on Standards for Athletic Equipment."),
        (13, "The most important factor for protective equipment is:", "Proper fit", ["Color", "Brand", "Price"], "Poor fit increases injury risk."),
        (13, "Mouthguards protect against:", "Dental injuries", ["Ankle sprains", "Heat illness", "Asthma"], "Also lip and jaw injuries."),
        (13, "Custom protective pads can be made from:", "Thermoplastic or foam", ["Paper", "Cotton only", "Glass"], "Molded to fit."),
        (13, "Hard pads should be covered with soft padding because:", "Hard surfaces can injure other players", ["It looks better", "It's cheaper", "Rules never mention it"], "Sport rules often require it."),
        (13, "Shoulder pads should be checked for:", "Fit and coverage", ["Color", "Smell only", "Weight only"], "Protect the AC joint and shoulder."),
        (13, "Damaged protective equipment should be:", "Repaired or replaced", ["Used anyway", "Taped over", "Ignored"], "Safety first."),
        (13, "Protective equipment rules vary by:", "Sport and governing body", ["Weather", "Team color", "Day of the week"], "Follow league rules."),
        (13, "Helmets should be reconditioned and recertified:", "Regularly per standards", ["Never", "Only when cracked", "Every 20 years"], "Maintains protection."),
    ]),
]

BOOK = {
    "titles": ["Orthopedic Taping, Wrapping, Bracing, and Padding"],
    "edition": "4th edition (2021)",
    "source": "Booksellers' published contents listings",
    "chapters": C,
    "quizzes": Q,
}
