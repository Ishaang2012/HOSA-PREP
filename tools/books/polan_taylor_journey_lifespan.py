# Polan & Taylor - Journey Across the Life Span: Human Development and Health Promotion (F.A. Davis).
# Chapter list supplied by the site owner (not verified against the publisher). Summaries are written for this site.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Healthy Lifestyles", "Health is physical, mental, and social well-being. Healthy lifestyles include balanced nutrition, physical activity, sleep, stress management, and avoiding tobacco and substance misuse. Health promotion and disease prevention occur at primary, secondary, and tertiary levels; Healthy People sets national goals.", ["Wellness dimensions", "Levels of prevention", "Healthy People goals", "Lifestyle risk factors"]),
    ch(2, "Communication", "Communication can be verbal or nonverbal. Therapeutic communication uses active listening, open-ended questions, empathy, and clarification. Barriers include jargon, distractions, language differences, and sensory impairments. Communication is adapted to each age group.", ["Verbal and nonverbal", "Active listening", "Open-ended questions", "Barriers to communication"]),
    ch(3, "Culture", "Culture is shared beliefs, values, and practices that shape health behaviors. Cultural competence means respecting differences, avoiding stereotyping and ethnocentrism, and using interpreters. Diet, religion, family roles, and views of illness vary by culture.", ["Cultural competence", "Ethnocentrism", "Stereotyping", "Interpreters"]),
    ch(4, "The Family", "Family structures include nuclear, extended, single-parent, blended, and others. Families provide support, socialization, and care. The family life cycle moves through stages, and stress such as illness affects the whole family.", ["Family structures", "Family functions", "Family life cycle", "Family stress"]),
    ch(5, "Theories of Growth and Development", "Growth is physical change; development is increasing skill. Major theories: Freud (psychosexual), Erikson (psychosocial), Piaget (cognitive), Kohlberg (moral), Maslow (needs). Development is orderly, proceeds head to toe (cephalocaudal) and center outward (proximodistal).", ["Growth vs. development", "Erikson's stages", "Piaget's stages", "Cephalocaudal and proximodistal"]),
    ch(6, "Prenatal Period to 1 Year", "Prenatal development includes germinal, embryonic, and fetal periods; teratogens can cause defects. Infants double birth weight by about 5–6 months and triple it by 1 year. Reflexes (rooting, Moro), motor milestones, trust vs. mistrust, immunizations, and safe sleep are key.", ["Prenatal periods", "Triple birth weight by 1 year", "Newborn reflexes", "Trust vs. mistrust"]),
    ch(7, "Toddlerhood", "Toddlers (1–3 years) walk, run, and develop language rapidly. Erikson's stage is autonomy vs. shame and doubt. Tantrums, toilet training, and safety (falls, poisoning, drowning) are major concerns.", ["Autonomy vs. shame", "Language explosion", "Toilet training", "Childproofing"]),
    ch(8, "Preschool", "Preschoolers (3–6 years) refine motor skills and are in Piaget's preoperational stage (egocentrism, magical thinking). Erikson's stage is initiative vs. guilt. Play, imagination, and school readiness develop.", ["Initiative vs. guilt", "Preoperational thinking", "Play", "School readiness"]),
    ch(9, "School Age", "School-age children (6–12) grow steadily and reach concrete operations (logic, conservation). Erikson's stage is industry vs. inferiority. Peers, school achievement, and self-esteem matter; concerns include bullying, obesity, and injuries.", ["Industry vs. inferiority", "Concrete operations", "Peer relationships", "Bullying and obesity"]),
    ch(10, "Puberty and Adolescence", "Puberty brings rapid physical and sexual maturation. Adolescents reach formal operations and seek identity (identity vs. role confusion). Risks include accidents, substance use, depression, and sexual health issues.", ["Puberty", "Identity vs. role confusion", "Formal operations", "Risk behaviors"]),
    ch(11, "Early Adulthood", "Young adults (about 20–40) are at peak physical health and focus on careers, relationships, and families. Erikson's stage is intimacy vs. isolation. Healthy habits now reduce later disease.", ["Intimacy vs. isolation", "Peak physical health", "Career and family", "Preventive habits"]),
    ch(12, "Middle Adulthood", "Middle adults (about 40–65) experience gradual physical changes, menopause, and increased chronic disease risk. Erikson's stage is generativity vs. stagnation. Many care for children and aging parents.", ["Generativity vs. stagnation", "Menopause", "Chronic disease screening", "Sandwich generation"]),
    ch(13, "Late Adulthood", "Older adults (65+) face changes in senses, bones, and organs; falls, polypharmacy, and dementia are concerns, though confusion isn't normal aging. Erikson's stage is integrity vs. despair. Theories of aging and promoting independence are emphasized.", ["Integrity vs. despair", "Fall prevention", "Polypharmacy", "Dementia is not normal aging"]),
    ch(14, "Death and Dying", "Responses to death vary by age and culture. Kübler-Ross described denial, anger, bargaining, depression, and acceptance. Hospice and palliative care focus on comfort; advance directives guide end-of-life wishes. Signs of approaching death and grief support are covered.", ["Stages of grief", "Hospice and palliative care", "Advance directives", "Grief support"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Screening tests like mammograms are:", "Secondary prevention", ["Primary prevention", "Tertiary prevention", "Treatment"], "Early detection."),
        (1, "Vaccines are an example of:", "Primary prevention", ["Secondary prevention", "Tertiary prevention", "Rehabilitation"], "Prevent disease before it starts."),
        (1, "The U.S. program setting national health goals is:", "Healthy People", ["Medicare", "MyPlate", "HIPAA"], "Updated every decade."),
        (2, "Body language and facial expressions are:", "Nonverbal communication", ["Verbal communication", "Written communication", "Jargon"], "Often louder than words."),
        (2, "'How are you feeling about your surgery?' is an:", "Open-ended question", ["Closed question", "Leading question", "Yes/no question"], "Invites discussion."),
        (2, "A barrier to communication is:", "Medical jargon", ["Active listening", "Eye contact", "Clarifying"], "Use plain language."),
        (3, "Believing one's own culture is superior is:", "Ethnocentrism", ["Cultural competence", "Acculturation", "Diversity"], "A barrier to care."),
        (3, "For a patient who speaks another language, use a:", "Trained interpreter", ["Family child", "Louder voice", "Gestures only"], "Ensures accuracy."),
        (3, "Assuming all members of a group behave alike is:", "Stereotyping", ["Cultural competence", "Empathy", "Respect"], "Avoid it."),
    ]),
    ((4, 5, 6), [
        (4, "A family that includes a stepparent is:", "Blended", ["Nuclear", "Extended", "Single-parent"], "Combines families."),
        (4, "When one member is ill, it:", "Affects the whole family", ["Affects only the patient", "Has no effect", "Always strengthens the family"], "Family-centered care."),
        (4, "Families teach children values and norms through:", "Socialization", ["Segregation", "Isolation", "Regression"], "A core family function."),
        (5, "Development that proceeds from head to toe is:", "Cephalocaudal", ["Proximodistal", "Random", "Distal-proximal"], "Head control comes first."),
        (5, "Piaget's theory describes:", "Cognitive development", ["Psychosexual stages", "Moral reasoning", "Needs hierarchy"], "How thinking develops."),
        (5, "Kohlberg's theory addresses:", "Moral development", ["Cognitive development", "Physical growth", "Attachment"], "Levels of moral reasoning."),
        (6, "Infants usually triple their birth weight by:", "1 year", ["3 months", "6 months", "2 years"], "Double by 5–6 months."),
        (6, "The startle reflex is the:", "Moro reflex", ["Rooting reflex", "Babinski reflex", "Grasp reflex"], "Disappears by about 4–6 months."),
        (6, "Major organs form during the:", "Embryonic period", ["Germinal period", "Fetal period", "Neonatal period"], "Weeks 3–8."),
    ]),
    ((7, 8, 9), [
        (7, "Erikson's stage for toddlers is:", "Autonomy vs. shame and doubt", ["Trust vs. mistrust", "Initiative vs. guilt", "Industry vs. inferiority"], "Toddlers seek independence."),
        (7, "A top safety concern for toddlers is:", "Poisoning and drowning", ["Retirement", "Peer pressure", "Driving"], "Childproof the home."),
        (7, "Temper tantrums in toddlers are:", "A normal part of seeking independence", ["Always a sign of illness", "Rare", "Signs of poor parenting always"], "Respond calmly and consistently."),
        (8, "Erikson's stage for preschoolers is:", "Initiative vs. guilt", ["Autonomy vs. shame", "Industry vs. inferiority", "Identity vs. role confusion"], "Taking initiative in play."),
        (8, "Preschoolers believing the moon follows them shows:", "Magical thinking", ["Abstract thinking", "Conservation", "Formal operations"], "Preoperational stage."),
        (8, "Preschoolers mainly learn through:", "Play", ["Lectures", "Reading only", "Work"], "Play is a child's work."),
        (9, "Erikson's stage for school-age children is:", "Industry vs. inferiority", ["Initiative vs. guilt", "Identity vs. role confusion", "Intimacy vs. isolation"], "Building competence."),
        (9, "Understanding that quantity doesn't change with shape is:", "Conservation", ["Egocentrism", "Object permanence", "Magical thinking"], "Concrete operations."),
        (9, "A common concern in school-age children is:", "Bullying", ["Menopause", "Retirement", "Teething"], "Affects self-esteem."),
    ]),
    ((10, 11, 12), [
        (10, "Erikson's stage for adolescents is:", "Identity vs. role confusion", ["Intimacy vs. isolation", "Industry vs. inferiority", "Integrity vs. despair"], "Who am I?"),
        (10, "Abstract thinking develops in Piaget's:", "Formal operational stage", ["Concrete operational stage", "Preoperational stage", "Sensorimotor stage"], "Adolescence."),
        (10, "A leading cause of death among adolescents is:", "Unintentional injuries", ["Heart disease", "Cancer", "Diabetes"], "Especially motor vehicle crashes."),
        (11, "Erikson's stage for early adulthood is:", "Intimacy vs. isolation", ["Generativity vs. stagnation", "Integrity vs. despair", "Identity vs. role confusion"], "Close relationships."),
        (11, "Physical abilities usually peak in:", "Early adulthood", ["Middle adulthood", "Late adulthood", "Adolescence only"], "Healthy habits pay off later."),
        (11, "A major focus of early adulthood is:", "Careers and relationships", ["Retirement", "Puberty", "Toilet training"], "Many start families."),
        (12, "Erikson's stage for middle adulthood is:", "Generativity vs. stagnation", ["Intimacy vs. isolation", "Integrity vs. despair", "Trust vs. mistrust"], "Contributing to others."),
        (12, "Adults caring for both children and aging parents are the:", "Sandwich generation", ["Silent generation", "Baby boomers", "Lost generation"], "High stress."),
        (12, "The end of menstrual periods in middle age is:", "Menopause", ["Menarche", "Puberty", "Ovulation"], "Around age 50."),
    ]),
    ((13, 14), [
        (13, "Erikson's final stage is:", "Integrity vs. despair", ["Generativity vs. stagnation", "Intimacy vs. isolation", "Trust vs. mistrust"], "Life review."),
        (13, "Which is NOT a normal part of aging?", "Dementia", ["Thinner skin", "Slower reaction time", "Presbyopia"], "Confusion needs evaluation."),
        (13, "Taking many medications at once is:", "Polypharmacy", ["Pharmacology", "Tolerance", "Adherence"], "Raises risk of interactions."),
        (13, "A major safety concern for older adults is:", "Falls", ["Sports injuries", "Sunburn only", "Peer pressure"], "Leading cause of injury."),
        (14, "The first stage of grief (Kübler-Ross) is:", "Denial", ["Anger", "Bargaining", "Acceptance"], "Then anger, bargaining, depression, acceptance."),
        (14, "Care focused on comfort for the terminally ill is:", "Hospice", ["Acute care", "Rehabilitation", "Surgery"], "Includes family support."),
        (14, "A document stating end-of-life wishes is an:", "Advance directive", ["Incident report", "Care plan", "Will for property"], "Includes living wills."),
        (14, "Young children often think death is:", "Temporary or reversible", ["Permanent and universal", "Impossible", "Only for animals"], "Understanding grows with age."),
        (14, "Support for people after a loss is:", "Bereavement support", ["Triage", "Rehabilitation", "Acute care"], "Helps with grief."),
    ]),
]

BOOK = {
    "titles": ["Journey Across the Lifespan: Human Development and Health Promotion"],
    "edition": "Edition not verified; chapter list supplied by the site owner",
    "source": "Chapter list supplied by the site owner",
    "chapters": C,
    "quizzes": Q,
}
