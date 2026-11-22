# Barr - Health Disparities in the United States: Social Class, Race, Ethnicity, and the Social Determinants of Health
# (Johns Hopkins University Press). Chapter list supplied by the site owner (not verified against the publisher).
# Summaries are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Health Disparities in the United States: An Introduction", "Health disparities are differences in health outcomes among groups defined by income, education, race, ethnicity, and other factors. The U.S. spends more on health care than any other nation yet has lower life expectancy than many peers, partly due to disparities.", ["Definition of disparities", "U.S. spending vs. outcomes", "Groups affected", "Why disparities matter"]),
    ch(2, "What Is Health? What Causes Health?", "Health is shaped by biology, behavior, environment, social conditions, and health care. Social determinants such as income, education, housing, and neighborhood strongly influence health, often more than medical care.", ["WHO definition of health", "Determinants of health", "Medical care's limited role", "Social determinants"]),
    ch(3, "How Does Social Status Affect Health?", "Social status, measured by income, education, and occupation, strongly predicts health. Lower status is linked to higher rates of disease and earlier death, as shown in studies like the Whitehall studies of British civil servants.", ["Socioeconomic status", "Whitehall studies", "Income and education", "Occupation and health"]),
    ch(4, "Socioeconomic Status and Health: Explaining the Gradient", "Health improves step by step with each increase in social status (the social gradient), not just between rich and poor. Explanations include material resources, health behaviors, chronic stress, sense of control, and early-life conditions.", ["Social gradient", "Chronic stress", "Sense of control", "Early-life conditions"]),
    ch(5, "Understanding Race and Ethnicity", "Race is a social construct rather than a precise biological category; genetic variation within groups exceeds variation between groups. Ethnicity refers to shared culture, language, and ancestry. How race is defined and measured affects research.", ["Race as a social construct", "Ethnicity", "Genetic variation", "Measuring race"]),
    ch(6, "Race, Ethnicity, and Health: Does Race Matter?", "Racial and ethnic groups differ in outcomes such as infant mortality, life expectancy, and chronic disease. Explanations include socioeconomic differences, discrimination and racism, stress ('weathering'), and unequal access to care, not genetics alone.", ["Infant mortality gaps", "Racism and discrimination", "Weathering", "Beyond genetics"]),
    ch(7, "The Role of Place: Neighborhoods, Segregation, and Health", "Where people live affects health through housing quality, pollution, food access, safety, and services. Residential segregation, historically shaped by redlining, concentrates disadvantage.", ["Neighborhood effects", "Residential segregation", "Redlining", "Food deserts"]),
    ch(8, "Disparities in Health Care: How the System Treats Different Groups", "Groups differ in insurance coverage, access, and the quality of care they receive. The Institute of Medicine's 'Unequal Treatment' report found that minorities often receive lower-quality care even with similar insurance; implicit bias contributes.", ["Insurance and access", "Unequal Treatment report", "Implicit bias", "Quality of care"]),
    ch(9, "Disparities in the Health Care Workforce", "Underrepresentation of some racial and ethnic groups among physicians and other professionals affects access and patient-provider trust. Diversity programs and pipeline initiatives aim to build a more representative workforce.", ["Workforce diversity", "Underrepresented groups", "Patient-provider concordance", "Pipeline programs"]),
    ch(10, "Gender, Sexual Orientation, and Health Disparities", "Health differs by gender (e.g., women live longer but report more chronic illness) and sexual orientation and gender identity (LGBTQ+ people face stigma, discrimination, and barriers to care, linked to minority stress).", ["Gender differences", "LGBTQ+ health", "Minority stress", "Barriers to care"]),
    ch(11, "Addressing Health Disparities: Policy and Practice", "Solutions include expanding insurance coverage, addressing social determinants (housing, education, income), community health programs, cultural competence, reducing bias, and Health in All Policies approaches.", ["Insurance expansion", "Social determinants policy", "Community programs", "Health in All Policies"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Differences in health outcomes among groups are:", "Health disparities", ["Health equity", "Health literacy", "Health insurance"], "Often preventable."),
        (1, "Compared with peer nations, the U.S. has:", "Higher spending but lower life expectancy", ["Lower spending and higher life expectancy", "The same outcomes", "No disparities"], "Partly due to disparities."),
        (1, "Groups commonly affected by disparities are defined by:", "Income, education, race, and ethnicity", ["Height only", "Eye color", "Favorite sport"], "Social factors."),
        (2, "Conditions where people live, learn, and work that affect health are:", "Social determinants of health", ["Genetic factors", "Vital signs", "Medical errors"], "Shape outcomes."),
        (2, "Medical care alone explains:", "Only part of health outcomes", ["All health outcomes", "None of health", "Only infectious disease"], "Social factors matter greatly."),
        (2, "Which is a determinant of health?", "Housing", ["Shoe size", "Hair color", "Handwriting"], "Housing quality affects health."),
        (3, "Studies of British civil servants showing health varies by job rank are the:", "Whitehall studies", ["Framingham study", "Tuskegee study", "Nurses' Health Study"], "Social status and health."),
        (3, "Socioeconomic status is usually measured by income, education, and:", "Occupation", ["Height", "Age", "Hobbies"], "Three key measures."),
        (3, "Lower socioeconomic status is linked to:", "Higher disease rates and earlier death", ["Longer life", "Better health always", "No difference"], "Strong association."),
    ]),
    ((4, 5, 6), [
        (4, "Health improving with each step up in social status is the:", "Social gradient", ["Poverty line", "Bell curve", "Health ceiling"], "Not just rich vs. poor."),
        (4, "One explanation for the gradient is:", "Chronic stress", ["Eye color", "Blood type", "Random chance only"], "Stress affects the body."),
        (4, "Having control over one's life is linked to:", "Better health", ["Worse health", "No effect", "Only financial outcomes"], "Sense of control."),
        (5, "Race is best described as a:", "Social construct", ["Precise biological category", "Blood type", "Single gene"], "Defined by society."),
        (5, "Genetic variation is greater:", "Within racial groups than between them", ["Between groups than within", "Equal in all cases", "Only between groups"], "Key genetics finding."),
        (5, "Shared culture, language, and ancestry describe:", "Ethnicity", ["Race only", "Nationality only", "Income"], "Ethnic identity."),
        (6, "Health erosion from repeated stress of discrimination is called:", "Weathering", ["Resilience", "Adaptation", "Immunity"], "Arline Geronimus's term."),
        (6, "Racial gaps in infant mortality are mainly explained by:", "Social factors including racism", ["Genetics alone", "Diet alone", "Chance"], "Not just biology."),
        (6, "Discrimination affects health through:", "Stress and unequal access", ["Improving immunity", "No pathway", "Better sleep"], "Multiple pathways."),
    ]),
    ((7, 8, 9), [
        (7, "Historic denial of mortgages in minority neighborhoods was:", "Redlining", ["Gentrification", "Zoning", "Blockbusting only"], "Shaped segregation."),
        (7, "Areas with little access to healthy, affordable food are:", "Food deserts", ["Food banks", "Farmers markets", "Grocery hubs"], "Linked to poor diets."),
        (7, "Residential segregation concentrates:", "Disadvantage and poor environmental conditions", ["Wealth evenly", "Hospitals", "Parks only"], "Affects health."),
        (8, "The report showing minorities receive lower-quality care is:", "Unequal Treatment", ["Healthy People", "The Flexner Report", "The Belmont Report"], "Institute of Medicine, 2003."),
        (8, "Unconscious attitudes that affect decisions are:", "Implicit bias", ["Explicit policy", "Health literacy", "Informed consent"], "Affects care."),
        (8, "A major barrier to care for many low-income people is:", "Lack of insurance", ["Too many doctors", "Free care everywhere", "Short travel distances"], "Coverage matters."),
        (9, "Patients sharing a background with their clinician is:", "Patient-provider concordance", ["Discordance", "Triage", "Malpractice"], "May improve trust."),
        (9, "Programs that help underrepresented students enter health careers are:", "Pipeline programs", ["Residency programs only", "Insurance programs", "Recruitment bans"], "Build a diverse workforce."),
        (9, "Workforce diversity matters because it:", "Improves access and trust", ["Lowers quality", "Has no effect", "Increases costs only"], "Benefits patients."),
    ]),
    ((10, 11), [
        (10, "Stress from stigma and discrimination faced by LGBTQ+ people is:", "Minority stress", ["Eustress", "Burnout", "Weathering only"], "Linked to health risks."),
        (10, "Compared with men, women in the U.S. on average:", "Live longer", ["Live shorter lives", "Have no chronic illness", "Never use health care"], "But report more chronic illness."),
        (10, "LGBTQ+ people may avoid care because of:", "Fear of discrimination", ["Too many clinics", "Free insurance", "Short wait times"], "Barrier to care."),
        (11, "Considering health effects in decisions across all sectors is:", "Health in All Policies", ["Medicare", "Managed care", "Triage"], "Housing, transport, education."),
        (11, "Expanding insurance coverage helps reduce:", "Disparities in access", ["Life expectancy", "Health literacy", "Hospital quality"], "E.g., Medicaid expansion."),
        (11, "Addressing social determinants includes improving:", "Housing, education, and income", ["Only hospital buildings", "Only drug prices", "Only surgery"], "Root causes."),
        (11, "Community health workers help by:", "Connecting residents to care and resources", ["Performing surgery", "Writing laws", "Running insurance companies"], "Trusted local members."),
        (10, "Sexual orientation and gender identity data help:", "Identify disparities", ["Hide disparities", "Replace care", "Lower costs only"], "What gets measured gets addressed."),
        (11, "Cultural competence training aims to:", "Improve care for diverse patients", ["Reduce staff", "Increase bias", "Cut services"], "Respect differences."),
    ]),
]

BOOK = {
    "titles": ["Health Disparities in the US"],
    "edition": "Edition not verified; chapter list supplied by the site owner",
    "source": "Chapter list supplied by the site owner",
    "chapters": C,
    "quizzes": Q,
}
