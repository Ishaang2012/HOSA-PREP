# Buchbinder, Shanks & Kite - Introduction to Health Care Management (Jones & Bartlett Learning).
# Chapter list: 4th edition (2021), from the publisher's sample front matter (samples.jblearning.com).
# A 5th edition (2025) exists; chapters may shift. Summaries are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "An Overview of Health Care Management", "Health care managers plan, organize, lead, and control resources to deliver care. They work at senior, middle, and first-line levels and focus on themselves, their teams, and the organization. Key roles include building culture, managing talent, strategic planning, ensuring high performance and patient experience, developing leaders, leading change, and engaging in policy.", ["Plan, organize, lead, control", "Levels of management", "Culture and talent", "Patient experience"]),
    ch(2, "Leadership", "Leadership is influencing others toward goals; management focuses on planning and control. Models include trait, behavioral, situational, transactional, transformational, and servant leadership. Leaders build trust, communicate vision, and develop others.", ["Leadership vs. management", "Transformational leadership", "Situational leadership", "Servant leadership"]),
    ch(3, "Management and Motivation", "Motivation theories include Maslow's hierarchy, Herzberg's two-factor theory (hygiene factors and motivators), McClelland's needs, expectancy theory, and equity theory. Managers motivate through recognition, growth opportunities, and fair treatment.", ["Maslow", "Herzberg hygiene vs. motivators", "Expectancy theory", "Equity theory"]),
    ch(4, "Organizational Behavior and Management Thinking", "Organizational behavior studies how people act in organizations. Management thought evolved from scientific management (Taylor) and bureaucracy (Weber) to human relations (Hawthorne studies) and systems thinking.", ["Scientific management", "Hawthorne studies", "Systems thinking", "Organizational culture"]),
    ch(5, "Strategic Planning", "Strategic planning sets an organization's mission, vision, values, and goals. Tools include SWOT analysis, environmental scanning, and setting measurable objectives, followed by implementation and evaluation.", ["Mission and vision", "SWOT analysis", "Environmental scanning", "Measurable goals"]),
    ch(6, "Health Care Marketing", "Marketing identifies and meets customer needs. The marketing mix (4 Ps) is product, price, place, and promotion. Health care marketing uses market research, segmentation, and branding while following ethical rules.", ["4 Ps", "Market research", "Segmentation", "Branding"]),
    ch(7, "Quality and Performance Improvement Basics", "Quality improvement uses data to make care safer and more effective. Methods include PDSA cycles, Lean, Six Sigma, and root cause analysis. Donabedian's model measures structure, process, and outcomes.", ["PDSA", "Lean and Six Sigma", "Root cause analysis", "Structure, process, outcome"]),
    ch(8, "Health Information Systems and Technologies", "Health information systems include EHRs, CPOE, clinical decision support, and health information exchange. Benefits include better coordination; challenges include cost, interoperability, and security.", ["EHRs", "CPOE", "Interoperability", "Cybersecurity"]),
    ch(9, "Financing Health Care and Health Insurance", "Health care is paid for by private insurance, Medicare, Medicaid, and out of pocket. Insurance terms include premiums, deductibles, copays, and coinsurance. Payment methods include fee-for-service, capitation, DRGs, and value-based payment.", ["Medicare and Medicaid", "Premiums and deductibles", "Capitation", "DRGs"]),
    ch(10, "Managing Costs and Revenues", "Managers prepare budgets (operating and capital), monitor variances, and manage the revenue cycle from registration to collection. Fixed and variable costs and break-even analysis guide decisions.", ["Operating vs. capital budget", "Variance analysis", "Revenue cycle", "Break-even"]),
    ch(11, "Managing Health Care Professionals", "Managing clinicians requires understanding professional autonomy, credentialing, licensure, scope of practice, and collaboration across disciplines. Burnout and workforce shortages are key challenges.", ["Credentialing", "Scope of practice", "Professional autonomy", "Burnout"]),
    ch(12, "Strategic Management of Human Resources", "HR functions include workforce planning, recruitment, selection, orientation, training, performance appraisal, compensation, and retention, while complying with employment laws.", ["Recruitment and selection", "Performance appraisal", "Compensation", "Employment law"]),
    ch(13, "Teamwork", "Effective teams have shared goals, clear roles, trust, and communication. Team development follows forming, storming, norming, and performing (Tuckman). TeamSTEPPS improves teamwork and patient safety.", ["Tuckman's stages", "Clear roles", "TeamSTEPPS", "Trust and communication"]),
    ch(14, "Addressing Health Disparities: Cultural Proficiency", "Health disparities are preventable differences in health among groups. Cultural proficiency means organizations value diversity, adapt services, use interpreters, and work to eliminate bias.", ["Health disparities", "Cultural proficiency", "Interpreters", "Bias reduction"]),
    ch(15, "Law and Ethics", "Managers must understand contracts, torts, negligence, malpractice, consent, and confidentiality, along with ethical principles: autonomy, beneficence, nonmaleficence, and justice. Ethics committees help resolve dilemmas.", ["Negligence and malpractice", "Consent and confidentiality", "Ethical principles", "Ethics committees"]),
    ch(16, "Health Care Regulation and Compliance", "Health organizations follow regulations from CMS, OSHA, and state agencies and seek accreditation (The Joint Commission). Compliance programs address HIPAA, fraud and abuse laws (Stark, Anti-Kickback, False Claims Act), and EMTALA.", ["Accreditation", "HIPAA", "Fraud and abuse laws", "Compliance programs"]),
    ch(17, "Special Topics and Emerging Issues in Health Care Management", "Emerging issues include population health, telehealth, consumerism, workforce shortages, emergency preparedness, and the shift to value-based care.", ["Population health", "Telehealth", "Value-based care", "Emergency preparedness"]),
    ch(18, "Health Care Management Case Studies and Guidelines", "Case studies let students practice analyzing real management problems: define the issue, gather facts, consider options, choose a solution, and plan implementation.", ["Define the problem", "Analyze options", "Choose and justify", "Plan implementation"]),
]

Q = [
    ((1, 2, 3), [
        (1, "The four management functions are planning, organizing, leading, and:", "Controlling", ["Billing", "Hiring", "Marketing"], "Classic management functions."),
        (1, "A manager who supervises front-line staff is a:", "First-line manager", ["Senior executive", "Board member", "Consultant"], "Lowest management level."),
        (1, "Developing future leaders to replace current ones is:", "Succession planning", ["Downsizing", "Capitation", "Credentialing"], "Ensures continuity."),
        (2, "A leader who inspires followers with a shared vision is:", "Transformational", ["Transactional", "Laissez-faire", "Autocratic"], "Inspires change."),
        (2, "A leader who adapts style to followers' readiness uses:", "Situational leadership", ["Servant leadership", "Trait theory", "Scientific management"], "Hersey and Blanchard."),
        (2, "A leader who focuses on serving and developing others practices:", "Servant leadership", ["Autocratic leadership", "Transactional leadership", "Bureaucracy"], "Robert Greenleaf."),
        (3, "In Herzberg's theory, salary and working conditions are:", "Hygiene factors", ["Motivators", "Self-actualization needs", "Expectancies"], "Prevent dissatisfaction."),
        (3, "Theory that people compare their rewards with others' is:", "Equity theory", ["Expectancy theory", "Maslow's hierarchy", "Two-factor theory"], "Adams."),
        (3, "In Maslow's hierarchy, the highest need is:", "Self-actualization", ["Safety", "Esteem", "Belonging"], "Reaching potential."),
    ]),
    ((4, 5, 6), [
        (4, "Frederick Taylor is associated with:", "Scientific management", ["Human relations", "Bureaucracy", "Servant leadership"], "Efficiency studies."),
        (4, "The Hawthorne studies showed that productivity is influenced by:", "Attention and social factors", ["Only pay", "Only lighting", "Only machines"], "Human relations movement."),
        (4, "Max Weber described the ideal:", "Bureaucracy", ["Matrix structure", "Flat organization", "Startup"], "Rules and hierarchy."),
        (5, "SWOT stands for strengths, weaknesses, opportunities, and:", "Threats", ["Tasks", "Teams", "Targets"], "Strategic analysis."),
        (5, "An organization's statement of its purpose is its:", "Mission", ["Vision", "Budget", "Bylaws"], "Vision is the future goal."),
        (5, "Scanning the outside world for trends is:", "Environmental scanning", ["Credentialing", "Auditing", "Recruiting"], "Informs strategy."),
        (6, "The 4 Ps of marketing are product, price, place, and:", "Promotion", ["Profit", "People", "Policy"], "Marketing mix."),
        (6, "Dividing a market into groups with similar needs is:", "Segmentation", ["Branding", "Pricing", "Positioning only"], "Targets messages."),
        (6, "Gathering data on customer needs is:", "Market research", ["Capitation", "Compliance", "Accreditation"], "Guides marketing."),
    ]),
    ((7, 8, 9), [
        (7, "PDSA stands for Plan, Do, Study, and:", "Act", ["Assess", "Audit", "Analyze"], "Improvement cycle."),
        (7, "Finding the underlying cause of an error is:", "Root cause analysis", ["Benchmarking", "Budgeting", "Branding"], "Prevents recurrence."),
        (7, "Donabedian's model measures structure, process, and:", "Outcomes", ["Profits", "Marketing", "Staffing only"], "Quality framework."),
        (8, "Electronic entry of provider orders is:", "CPOE", ["EHR", "HIE", "PACS"], "Reduces errors."),
        (8, "The ability of systems to share data is:", "Interoperability", ["Usability", "Capitation", "Credentialing"], "Key IT challenge."),
        (8, "Electronic sharing of records between organizations is:", "Health information exchange", ["CPOE", "DRG", "Telehealth only"], "HIE."),
        (9, "Fixed payment per patient per month is:", "Capitation", ["Fee-for-service", "DRG", "Copay"], "Managed care."),
        (9, "Medicare pays hospitals using:", "DRGs", ["Capitation only", "Tips", "Patient choice"], "Diagnosis-related groups."),
        (9, "The amount paid before insurance begins paying is the:", "Deductible", ["Premium", "Copay", "Coinsurance"], "Annual amount."),
    ]),
    ((10, 11, 12), [
        (10, "A budget for major equipment and buildings is the:", "Capital budget", ["Operating budget", "Cash budget", "Revenue cycle"], "Long-term purchases."),
        (10, "Costs that stay the same regardless of volume are:", "Fixed costs", ["Variable costs", "Marginal costs", "Revenue"], "E.g., rent."),
        (10, "The difference between budgeted and actual amounts is a:", "Variance", ["Margin", "Deductible", "Premium"], "Managers explain variances."),
        (11, "Verifying a clinician's qualifications is:", "Credentialing", ["Capitation", "Marketing", "Benchmarking"], "Protects patients."),
        (11, "Emotional exhaustion from work stress is:", "Burnout", ["Engagement", "Motivation", "Retention"], "Common in health care."),
        (11, "The legal limits on what a professional can do is:", "Scope of practice", ["Job satisfaction", "Seniority", "Budget"], "Set by state law."),
        (12, "Formal evaluation of an employee's work is a:", "Performance appraisal", ["Recruitment", "Orientation", "Termination"], "Usually yearly."),
        (12, "Keeping good employees is:", "Retention", ["Recruitment", "Selection", "Turnover"], "Reduces costs."),
        (12, "Introducing new employees to the organization is:", "Orientation", ["Appraisal", "Compensation", "Promotion"], "Onboarding."),
    ]),
    ((13, 14, 15), [
        (13, "Tuckman's stages are forming, storming, norming, and:", "Performing", ["Reforming", "Leading", "Closing"], "Team development."),
        (13, "A program for improving teamwork in health care is:", "TeamSTEPPS", ["Six Sigma", "SWOT", "HIPAA"], "AHRQ and DoD."),
        (13, "Effective teams have shared goals and:", "Clear roles", ["No communication", "Constant conflict", "One decision-maker always"], "Clarity builds trust."),
        (14, "Preventable differences in health among groups are:", "Health disparities", ["Health equity", "Capitation", "Credentialing"], "Linked to social factors."),
        (14, "Using trained interpreters for patients with limited English supports:", "Cultural proficiency", ["Upcoding", "Downsizing", "Capitation"], "Improves care."),
        (14, "Cultural proficiency means an organization:", "Values diversity and adapts services", ["Ignores culture", "Treats everyone identically regardless of need", "Avoids interpreters"], "Highest level of cultural competence."),
        (15, "Failure to provide reasonable care that causes harm is:", "Negligence", ["Battery", "Libel", "Fraud"], "Malpractice is professional negligence."),
        (15, "Respecting a patient's right to choose is:", "Autonomy", ["Justice", "Beneficence", "Fidelity"], "Ethical principle."),
        (15, "Groups that advise on difficult ethical cases are:", "Ethics committees", ["Billing offices", "Marketing teams", "HR departments"], "In most hospitals."),
    ]),
    ((16, 17, 18), [
        (16, "The main hospital accrediting body is:", "The Joint Commission", ["The FDA", "OSHA", "The DEA"], "Voluntary but important."),
        (16, "The law banning physician self-referral is the:", "Stark Law", ["EMTALA", "HIPAA", "ADA"], "Fraud and abuse."),
        (16, "Hospitals must screen and stabilize emergency patients under:", "EMTALA", ["HIPAA", "Stark", "OSHA"], "Regardless of ability to pay."),
        (17, "Delivering care remotely using technology is:", "Telehealth", ["Capitation", "Credentialing", "Accreditation"], "Growing rapidly."),
        (17, "Improving outcomes for a defined group of people is:", "Population health", ["Fee-for-service", "Marketing", "Bureaucracy"], "Focus on groups."),
        (17, "Paying providers for quality rather than volume is:", "Value-based care", ["Fee-for-service", "Self-pay", "Charity care"], "Major trend."),
        (18, "The first step in analyzing a management case is to:", "Define the problem", ["Choose a solution", "Implement", "Evaluate results"], "Clarify the issue."),
        (18, "After choosing a solution, managers should:", "Plan implementation and evaluation", ["Stop", "Ignore stakeholders", "Restart the case"], "Follow through."),
        (18, "Considering several options before deciding helps:", "Find the best solution", ["Delay forever", "Avoid data", "Confuse staff"], "Compare alternatives."),
    ]),
]

BOOK = {
    "titles": ["Introduction to Health Care Management"],
    "edition": "4th edition (2021); a 5th edition was published in 2025",
    "source": "Jones & Bartlett sample front matter",
    "chapters": C,
    "quizzes": Q,
}
