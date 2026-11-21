# Kato - Lifespan Development (Goodheart-Willcox).
# Chapter list: 3rd edition (2024), from the publisher's table of contents (g-w.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "An Introduction to Lifespan Development", "Lifespan development studies how people grow and change from conception to death in physical, cognitive, social, and emotional areas. Development is lifelong, multidirectional, and shaped by heredity (nature) and environment (nurture). Researchers use observation, case studies, surveys, and longitudinal and cross-sectional studies.", ["Physical, cognitive, social-emotional domains", "Nature and nurture interact", "Development is lifelong", "Longitudinal vs. cross-sectional studies"]),
    ch(2, "How and Why People Develop and Learn", "Major theories include Piaget's cognitive stages (sensorimotor, preoperational, concrete operational, formal operational), Erikson's eight psychosocial stages, Vygotsky's sociocultural theory (zone of proximal development, scaffolding), Kohlberg's moral development, Bronfenbrenner's ecological systems, Maslow's hierarchy of needs, and behaviorist and social learning theories (Skinner, Bandura).", ["Piaget's four cognitive stages", "Erikson's eight psychosocial stages", "Vygotsky: zone of proximal development", "Kohlberg: moral reasoning levels"]),
    ch(3, "Family Trends Today", "Families take many forms: nuclear, single-parent, blended, extended, and others. Trends include delayed marriage, smaller families, dual-income households, and multigenerational living. Families provide care, socialization, and support, and parenting styles (authoritative, authoritarian, permissive, uninvolved) affect child development.", ["Many family structures", "Authoritative parenting = warmth + limits", "Families socialize children", "Multigenerational households"]),
    ch(4, "Pregnancy and Birth", "Prenatal development has three periods: germinal (first 2 weeks), embryonic (weeks 3–8, organs form), and fetal (week 9 to birth). Teratogens such as alcohol, tobacco, drugs, and some infections can cause birth defects. Prenatal care, good nutrition (including folic acid), and avoiding harmful substances support healthy outcomes. Labor has three stages, and newborns are assessed with the Apgar score.", ["Germinal, embryonic, fetal periods", "Organs form in the embryonic period", "Teratogens cause birth defects", "Apgar score assesses newborns"]),
    ch(5, "Infancy: Newborn to Age 1", "Infants grow faster than at any other time and develop reflexes, motor skills (rolling, sitting, crawling), and senses. Cognitively they are in Piaget's sensorimotor stage and develop object permanence. Socially, they form attachments to caregivers; Erikson's stage is trust vs. mistrust. Safe sleep on the back reduces SIDS risk.", ["Fastest growth period", "Object permanence develops", "Trust vs. mistrust", "Back to sleep reduces SIDS"]),
    ch(6, "Toddlerhood: Ages 1 through 2", "Toddlers learn to walk, talk, and do things for themselves. Language grows rapidly, and they begin symbolic play. Erikson's stage is autonomy vs. shame and doubt; tantrums and saying 'no' are normal as toddlers seek independence. Toilet training and safety (childproofing) are key concerns.", ["Walking and rapid language growth", "Autonomy vs. shame and doubt", "Tantrums are normal", "Childproof for safety"]),
    ch(7, "Early Childhood: Ages 3 through 5", "Preschoolers refine motor skills and are in Piaget's preoperational stage (egocentrism, symbolic thinking, lack of conservation). Play is how they learn. Erikson's stage is initiative vs. guilt. School readiness, social skills, and guidance through positive discipline are emphasized.", ["Preoperational stage; egocentrism", "Play is learning", "Initiative vs. guilt", "Positive discipline"]),
    ch(8, "Middle Childhood: Ages 6 through 10", "School-age children grow steadily and develop concrete operational thinking (logic about real objects, conservation). Erikson's stage is industry vs. inferiority. Friendships, self-esteem, and academic skills grow. Concerns include bullying, childhood obesity, and learning differences.", ["Concrete operational stage", "Industry vs. inferiority", "Friendships and self-esteem", "Bullying and obesity concerns"]),
    ch(9, "Adolescence: Ages 11 through 19", "Puberty brings rapid physical and sexual maturation. Cognitively, teens reach formal operational thinking (abstract reasoning). Erikson's stage is identity vs. role confusion. Peer influence grows; risks include substance use, risky driving, and mental health challenges. The prefrontal cortex is still developing.", ["Puberty", "Formal operational thinking", "Identity vs. role confusion", "Prefrontal cortex still maturing"]),
    ch(10, "Early Adulthood: Ages 20 through 39", "Young adults are at peak physical condition and focus on education, careers, relationships, and often starting families. Erikson's stage is intimacy vs. isolation. Healthy habits formed now affect later health.", ["Peak physical condition", "Intimacy vs. isolation", "Career and relationships", "Healthy habits matter"]),
    ch(11, "Middle Adulthood: Ages 40 through 65", "Middle adults experience gradual physical changes such as declining vision, menopause, and slower metabolism. Erikson's stage is generativity vs. stagnation: contributing to the next generation through work, parenting, and mentoring. Many care for both children and aging parents (the 'sandwich generation').", ["Generativity vs. stagnation", "Menopause and physical changes", "Sandwich generation", "Mentoring and contributing"]),
    ch(12, "Older Adulthood: Ages 66 Plus", "Older adults experience physical changes (thinner skin, weaker bones, sensory losses) but many stay healthy and independent. Erikson's final stage is integrity vs. despair, reflecting on one's life. Issues include retirement, loss of loved ones, dementia (not a normal part of aging), and end-of-life decisions. Kübler-Ross described stages of grief.", ["Integrity vs. despair", "Dementia is not normal aging", "Retirement and loss", "Stages of grief"]),
    ch(13, "Child and Adult Care Resources for Families", "Families use resources such as child care centers, family child care homes, preschools, after-school programs, adult day services, assisted living, and nursing homes. Choosing quality care involves licensing, staff training, ratios, and safety.", ["Child care options", "Adult day services and assisted living", "Check licensing and ratios", "Quality and safety matter"]),
    ch(14, "Providing for Individual and Family Needs", "Families meet needs for food, shelter, health care, education, and emotional support while managing time, money, and stress. Community resources and support networks help families facing challenges such as illness, disability, or financial hardship.", ["Meet basic and emotional needs", "Manage time and money", "Community resources help", "Support networks reduce stress"]),
    ch(15, "Preparing for Careers", "Career preparation includes self-assessment of interests and skills, education and training, résumés, interviews, and workplace skills such as communication, teamwork, and professionalism.", ["Self-assessment", "Résumés and interviews", "Soft skills matter", "Education and training"]),
    ch(16, "Career Paths Education and Training", "Careers in education and training include teachers, early childhood educators, counselors, and trainers. They require knowledge of development and learning and the appropriate degrees or certifications.", ["Teachers and early childhood educators", "Counselors and trainers", "Degrees and certification", "Apply developmental knowledge"]),
    ch(17, "Career Paths in Human Services", "Human services careers include social workers, family counselors, child life specialists, and gerontology workers who help people at every life stage.", ["Social work and counseling", "Child life specialists", "Gerontology careers", "Helping across the lifespan"]),
]

Q = [
    ((1, 2, 3), [
        (1, "The debate about heredity versus environment is called:", "Nature vs. nurture", ["Mind vs. body", "Stage vs. continuous", "Theory vs. practice"], "Both interact in development."),
        (1, "A study that follows the same people over many years is:", "Longitudinal", ["Cross-sectional", "Case study", "Survey"], "Cross-sectional compares different ages at one time."),
        (2, "Piaget's stage for infants is:", "Sensorimotor", ["Preoperational", "Concrete operational", "Formal operational"], "Infants learn through senses and movement."),
        (2, "Vygotsky's 'zone of proximal development' is:", "What a learner can do with help", ["What a learner can do alone", "The brain's language center", "A stage of puberty"], "Scaffolding supports learning in this zone."),
        (2, "Kohlberg is known for his theory of:", "Moral development", ["Cognitive development", "Attachment", "Hierarchy of needs"], "He described levels of moral reasoning."),
        (2, "Maslow said people must meet which needs first?", "Physiological needs", ["Esteem needs", "Self-actualization", "Love and belonging"], "Food, water, and rest come first."),
        (3, "A parenting style combining warmth with clear limits is:", "Authoritative", ["Authoritarian", "Permissive", "Uninvolved"], "It's linked to the best outcomes."),
        (3, "A family that includes a stepparent and stepchildren is:", "Blended", ["Nuclear", "Extended", "Single-parent"], "Blended families combine previous families."),
        (1, "The three domains of development are physical, cognitive, and:", "Social-emotional", ["Financial", "Political", "Spiritual only"], "They interact with each other."),
    ]),
    ((4, 5, 6), [
        (4, "Major organs form during which prenatal period?", "Embryonic", ["Germinal", "Fetal", "Postnatal"], "Weeks 3–8."),
        (4, "Substances that can cause birth defects are:", "Teratogens", ["Vitamins", "Hormones", "Antibodies"], "Alcohol is a common teratogen."),
        (4, "Newborns are quickly assessed using the:", "Apgar score", ["Braden scale", "Glasgow Coma Scale", "BMI"], "It checks color, heart rate, reflexes, tone, breathing."),
        (5, "Understanding that objects exist when out of sight is:", "Object permanence", ["Conservation", "Egocentrism", "Abstract thinking"], "It develops in infancy."),
        (5, "Erikson's stage for infants is:", "Trust vs. mistrust", ["Autonomy vs. shame", "Initiative vs. guilt", "Industry vs. inferiority"], "Consistent care builds trust."),
        (5, "To reduce SIDS risk, infants should sleep:", "On their backs", ["On their stomachs", "With pillows", "In adult beds"], "'Back to sleep.'"),
        (6, "Erikson's stage for toddlers is:", "Autonomy vs. shame and doubt", ["Trust vs. mistrust", "Identity vs. role confusion", "Generativity vs. stagnation"], "Toddlers want independence."),
        (6, "Frequent 'no' and tantrums in toddlers are:", "Normal parts of seeking independence", ["Signs of illness", "Signs of poor parenting always", "Rare"], "Patience and consistency help."),
        (4, "Folic acid before and during pregnancy helps prevent:", "Neural tube defects", ["Colds", "Allergies", "Tooth decay"], "Example: spina bifida."),
    ]),
    ((7, 8, 9), [
        (7, "Preschoolers who can't see things from another's view show:", "Egocentrism", ["Conservation", "Object permanence", "Abstract thinking"], "It's typical of the preoperational stage."),
        (7, "Erikson's stage for preschoolers is:", "Initiative vs. guilt", ["Industry vs. inferiority", "Trust vs. mistrust", "Intimacy vs. isolation"], "They take initiative in play."),
        (8, "Understanding that quantity stays the same when shape changes is:", "Conservation", ["Egocentrism", "Object permanence", "Symbolic play"], "It develops in the concrete operational stage."),
        (8, "Erikson's stage for school-age children is:", "Industry vs. inferiority", ["Initiative vs. guilt", "Identity vs. role confusion", "Autonomy vs. shame"], "Children build competence."),
        (9, "Abstract reasoning develops in Piaget's:", "Formal operational stage", ["Concrete operational stage", "Preoperational stage", "Sensorimotor stage"], "It begins in adolescence."),
        (9, "Erikson's stage for adolescents is:", "Identity vs. role confusion", ["Intimacy vs. isolation", "Industry vs. inferiority", "Integrity vs. despair"], "Teens explore who they are."),
        (9, "The brain area still developing in adolescence that controls judgment is the:", "Prefrontal cortex", ["Brainstem", "Cerebellum", "Spinal cord"], "It matures in the mid-20s."),
        (7, "For preschoolers, play is important because it:", "Helps them learn and develop skills", ["Wastes time", "Prevents growth", "Replaces sleep"], "Play is a child's work."),
        (8, "A common concern in middle childhood is:", "Bullying", ["Menopause", "Retirement", "Teething"], "Schools and families can address it."),
    ]),
    ((10, 11, 12), [
        (10, "Erikson's stage for early adulthood is:", "Intimacy vs. isolation", ["Generativity vs. stagnation", "Integrity vs. despair", "Identity vs. role confusion"], "Forming close relationships."),
        (10, "Physical abilities usually peak in:", "Early adulthood", ["Middle adulthood", "Older adulthood", "Infancy"], "Healthy habits now pay off later."),
        (11, "Erikson's stage for middle adulthood is:", "Generativity vs. stagnation", ["Intimacy vs. isolation", "Integrity vs. despair", "Industry vs. inferiority"], "Contributing to the next generation."),
        (11, "Adults caring for both children and aging parents are the:", "Sandwich generation", ["Lost generation", "Silent generation", "Baby boomers"], "It can be very stressful."),
        (11, "The end of menstruation in middle adulthood is:", "Menopause", ["Puberty", "Menarche", "Ovulation"], "It usually occurs around age 50."),
        (12, "Erikson's final stage is:", "Integrity vs. despair", ["Generativity vs. stagnation", "Intimacy vs. isolation", "Trust vs. mistrust"], "Reflecting on one's life."),
        (12, "Which statement about aging is true?", "Dementia is not a normal part of aging", ["All older adults have dementia", "Older adults can't learn", "Aging means disability"], "Many older adults stay sharp."),
        (12, "The first stage of grief described by Kübler-Ross is:", "Denial", ["Anger", "Bargaining", "Acceptance"], "Then anger, bargaining, depression, acceptance."),
        (10, "A major focus of early adulthood is:", "Careers and relationships", ["Retirement", "Teething", "Puberty"], "Many also start families."),
    ]),
    ((13, 14, 15), [
        (13, "Services that care for older adults during the day are:", "Adult day services", ["Preschools", "Hospitals", "Schools"], "They support families who work."),
        (13, "When choosing child care, families should check:", "Licensing and staff-to-child ratios", ["Only price", "Only location", "Nothing"], "Quality and safety matter."),
        (14, "Community resources help families facing:", "Illness, disability, or financial hardship", ["Only vacations", "Only celebrations", "No challenges"], "Support networks reduce stress."),
        (14, "Managing time and money helps families:", "Meet their needs", ["Avoid all problems", "Skip planning", "Increase stress"], "Planning builds stability."),
        (15, "The first step in career planning is:", "Assessing your interests and skills", ["Retiring", "Applying everywhere", "Skipping education"], "Self-knowledge guides choices."),
        (15, "Communication and teamwork are examples of:", "Soft skills", ["Technical skills", "Certifications", "Degrees"], "Employers value them highly."),
        (15, "A summary of education and experience is a:", "Résumé", ["Cover letter", "Reference", "Transcript"], "Keep it clear and honest."),
        (13, "Assisted living facilities provide:", "Housing with some help for daily activities", ["Full hospital care", "Schooling", "Child care"], "Residents keep much independence."),
        (14, "Families meet emotional needs by providing:", "Support and connection", ["Only money", "Only food", "Only shelter"], "Emotional needs are as important as physical ones."),
    ]),
    ((16, 17), [
        (16, "Early childhood educators need knowledge of:", "Child development and learning", ["Surgery", "Accounting only", "Engineering"], "They plan age-appropriate activities."),
        (16, "School counselors help students with:", "Academic, career, and personal concerns", ["Medical surgery", "Taxes", "Car repair"], "They often need a master's degree."),
        (17, "Social workers help people:", "Access resources and cope with challenges", ["Build houses", "Fix computers", "Sell products"], "They work in many settings."),
        (17, "Child life specialists support:", "Children and families in hospitals", ["Retired adults only", "Pets", "Athletes only"], "They reduce children's fear of medical care."),
        (17, "Gerontology careers focus on:", "Older adults", ["Infants", "Teenagers only", "Animals"], "Demand is growing with an aging population."),
        (16, "Trainers in businesses help employees:", "Learn new skills", ["Avoid work", "Get sick days", "Retire early"], "Training is a career path in education."),
        (17, "Human services careers help people:", "At every life stage", ["Only in childhood", "Only in old age", "Only at work"], "They support well-being across the lifespan."),
        (16, "Teachers usually need:", "A degree and certification", ["No training", "Only a driver's license", "A medical license"], "Requirements vary by state."),
        (17, "Family counselors help families:", "Improve relationships and solve problems", ["Plan vacations", "Build homes", "Find jobs only"], "They often hold a license."),
    ]),
]

BOOK = {
    "titles": ["Lifespan Development"],
    "edition": "3rd edition (2024)",
    "source": "Goodheart-Willcox table of contents",
    "chapters": C,
    "quizzes": Q,
}
