# Ritter & Graham - Medical Law & Professional Ethics (Goodheart-Willcox).
# Chapter list: 2nd edition (2022), from the publisher's table of contents (g-w.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Overview of Medical Law and Ethics", "Law is a system of rules enforced by government; ethics are moral principles about right and wrong; etiquette is professional courtesy. Health care professionals need both legal knowledge and ethical judgment. Bioethics addresses issues raised by medical advances, such as genetic testing and end-of-life care.", ["Law = enforceable rules", "Ethics = right and wrong", "Bioethics = issues from medical advances", "Etiquette = professional courtesy"]),
    ch(2, "Professional Ethics", "Ethical principles include autonomy (respecting choices), beneficence (doing good), nonmaleficence (doing no harm), justice (fairness), fidelity (keeping promises), and veracity (truthfulness). Professional codes of ethics (such as the AMA's and those of nursing and allied health associations) guide practice. Ethical decision-making models help resolve dilemmas.", ["Autonomy, beneficence, nonmaleficence, justice", "Fidelity and veracity", "Codes of ethics", "Decision-making models"]),
    ch(3, "The Source of Law and Regulations", "U.S. law comes from constitutions, statutes (laws passed by legislatures), administrative regulations (agency rules), and common law (court decisions and precedent). Law is divided into public law (including criminal law) and private (civil) law. Federal and state courts interpret the law.", ["Constitutional, statutory, administrative, common law", "Precedent guides courts", "Criminal vs. civil law", "Federal and state systems"]),
    ch(4, "Certification and Licensing of Healthcare Professionals", "Licensure is mandatory, granted by state boards, and defines scope of practice. Certification is usually voluntary and granted by professional organizations. Registration lists qualified people on a registry. Licenses can be revoked or suspended for unprofessional conduct, and continuing education keeps credentials current.", ["Licensure = mandatory, state", "Certification = professional organization", "Scope of practice", "Revocation for misconduct"]),
    ch(5, "Civil Liability of Healthcare Practitioners", "Civil liability includes torts. Intentional torts include assault (threat), battery (unauthorized touching), false imprisonment, defamation (slander spoken, libel written), and invasion of privacy. Negligence requires the four Ds: duty, dereliction (breach), direct cause, and damages. Malpractice is professional negligence. Doctrines include res ipsa loquitur and respondeat superior.", ["Four Ds of negligence", "Assault = threat; battery = touching", "Slander = spoken; libel = written", "Respondeat superior: employer liable"]),
    ch(6, "Criminal Liability of Healthcare Practitioners", "Crimes are offenses against the state, classified as felonies (serious) or misdemeanors (less serious). Health care crimes include fraud (Medicare and Medicaid fraud), drug diversion, abuse, and assisting in illegal acts. Penalties include fines, imprisonment, and loss of license.", ["Felony vs. misdemeanor", "Medicare and Medicaid fraud", "Drug diversion", "Loss of license"]),
    ch(7, "Federal Statutes and Regulations That Impact Healthcare", "Key laws include HIPAA (privacy and security of health information), EMTALA (emergency treatment regardless of ability to pay), the Affordable Care Act, the Americans with Disabilities Act, the Controlled Substances Act, OSHA rules, CLIA (lab standards), the False Claims Act, and the Anti-Kickback Statute and Stark Law.", ["HIPAA = privacy", "EMTALA = emergency care for all", "ADA protects people with disabilities", "False Claims Act, Anti-Kickback, Stark"]),
    ch(8, "Managing Risk in Healthcare", "Risk management identifies and reduces risks to patients and organizations. Tools include incident reports, quality improvement, safety protocols, accurate documentation, and malpractice insurance. Good communication and following policies reduce lawsuits.", ["Incident reports", "Accurate documentation", "Quality improvement", "Malpractice insurance"]),
    ch(9, "The Patient-Professional Relationship", "The relationship is a contract that can be expressed or implied. Informed consent requires explaining the diagnosis, procedure, risks, benefits, and alternatives. Patients have rights to privacy, respect, and refusal. Abandonment (ending care without proper notice) is a legal risk. Confidentiality must be maintained.", ["Expressed vs. implied contracts", "Informed consent elements", "Abandonment is a legal risk", "Right to refuse treatment"]),
    ch(10, "Health Information Technology", "Electronic health records improve care but require security. HIPAA's Privacy and Security Rules and the HITECH Act govern health information, including breach notification. Telehealth, social media, and data sharing raise legal and ethical questions.", ["EHR security", "HIPAA Privacy and Security Rules", "HITECH and breach notification", "Social media risks"]),
    ch(11, "Genetics and Drugs", "Genetic testing raises issues of privacy and discrimination; GINA (Genetic Information Nondiscrimination Act) protects against discrimination in health insurance and employment. Drug laws regulate prescribing, controlled substance schedules, and FDA approval. Research involving humans requires informed consent and IRB oversight.", ["GINA prevents genetic discrimination", "Controlled substance schedules", "FDA drug approval", "IRBs protect research subjects"]),
    ch(12, "Complexity of Facilities Administration", "Health care facilities must follow licensing, accreditation (The Joint Commission), employment law, workplace safety, and billing rules. Administrators balance legal compliance, ethics, and quality care.", ["Accreditation by The Joint Commission", "Employment law", "Billing compliance", "Workplace safety"]),
    ch(13, "Minors: Health Law and Ethics", "Minors generally need parental consent for treatment, with exceptions for emancipated minors, mature minors in some states, emergencies, and certain services such as reproductive and mental health care. Health care workers are mandatory reporters of suspected child abuse.", ["Parental consent usually required", "Emancipated minor exceptions", "Mandatory reporting of child abuse", "Confidential services for minors"]),
    ch(14, "Adults: Health Law and Ethics", "Adults have the right to make their own health decisions if competent. Issues include informed consent, refusal of treatment, mental health law, reproductive rights, and organ donation (Uniform Anatomical Gift Act).", ["Competent adults decide for themselves", "Right to refuse treatment", "Organ donation laws", "Mental health law"]),
    ch(15, "Older Adults: Health Law and Ethics", "Older adults have rights to autonomy and protection from elder abuse (physical, emotional, financial, neglect), which must be reported. Advance directives (living wills and durable power of attorney for health care), guardianship, DNR orders, hospice, and the Patient Self-Determination Act address end-of-life decisions.", ["Report elder abuse", "Living will and durable POA for health care", "DNR orders", "Patient Self-Determination Act"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Moral principles about right and wrong are:", "Ethics", ["Laws", "Etiquette", "Regulations"], "Laws are enforced by government."),
        (1, "Ethical issues raised by medical advances are studied in:", "Bioethics", ["Etiquette", "Criminal law", "Accounting"], "Examples: genetic testing, end-of-life care."),
        (2, "Respecting a patient's right to make decisions is:", "Autonomy", ["Beneficence", "Justice", "Fidelity"], "Informed consent supports autonomy."),
        (2, "'Do no harm' is the principle of:", "Nonmaleficence", ["Beneficence", "Veracity", "Justice"], "Beneficence means doing good."),
        (2, "Telling patients the truth reflects:", "Veracity", ["Fidelity", "Justice", "Autonomy"], "Veracity = truthfulness."),
        (3, "Laws passed by legislatures are:", "Statutes", ["Common law", "Regulations", "Constitutions"], "Agencies create regulations."),
        (3, "Law based on previous court decisions is:", "Common law", ["Statutory law", "Administrative law", "Constitutional law"], "Precedent guides future cases."),
        (3, "Criminal law is a type of:", "Public law", ["Private law", "Contract law", "Tort law"], "Crimes are offenses against society."),
        (2, "Fair distribution of resources reflects:", "Justice", ["Autonomy", "Fidelity", "Beneficence"], "Justice means fairness."),
    ]),
    ((4, 5, 6), [
        (4, "A mandatory credential granted by a state is a:", "License", ["Certification", "Registration", "Diploma"], "It defines scope of practice."),
        (4, "Certification is usually granted by:", "A professional organization", ["A state board", "A hospital", "A court"], "It's often voluntary."),
        (5, "Threatening to hit a patient is:", "Assault", ["Battery", "Libel", "Slander"], "Battery is actual touching."),
        (5, "Spoken false statements that harm a reputation are:", "Slander", ["Libel", "Assault", "Battery"], "Libel is written."),
        (5, "The four Ds of negligence are duty, dereliction, direct cause, and:", "Damages", ["Diagnosis", "Documentation", "Deposition"], "All four must be proven."),
        (5, "An employer being liable for employees' actions is:", "Respondeat superior", ["Res ipsa loquitur", "Res judicata", "Stare decisis"], "'Let the master answer.'"),
        (6, "A serious crime punishable by more than a year in prison is a:", "Felony", ["Misdemeanor", "Tort", "Infraction"], "Misdemeanors are less serious."),
        (6, "Billing for services never provided is:", "Fraud", ["Malpractice", "Battery", "Defamation"], "Medicare fraud is a federal crime."),
        (6, "Stealing controlled drugs from a workplace is:", "Drug diversion", ["Abandonment", "Negligence", "Libel"], "It can lead to criminal charges."),
    ]),
    ((7, 8, 9), [
        (7, "Which law requires emergency treatment regardless of ability to pay?", "EMTALA", ["HIPAA", "ADA", "CLIA"], "Emergency Medical Treatment and Labor Act."),
        (7, "Which law protects the privacy of health information?", "HIPAA", ["EMTALA", "OSHA", "GINA"], "It sets privacy and security rules."),
        (7, "The Stark Law addresses:", "Physician self-referral", ["Patient privacy", "Workplace safety", "Lab quality"], "It limits referrals to entities with financial ties."),
        (8, "Documenting an unexpected event, such as a patient fall, uses an:", "Incident report", ["Consent form", "Advance directive", "Living will"], "It helps prevent future incidents."),
        (8, "A key way to reduce lawsuits is:", "Accurate documentation and good communication", ["Avoiding patients", "Skipping charts", "Refusing questions"], "'If it wasn't documented, it wasn't done.'"),
        (9, "A contract shown by actions rather than words is:", "Implied", ["Expressed", "Written", "Void"], "Example: holding out your arm for a shot."),
        (9, "Ending care without proper notice is:", "Abandonment", ["Consent", "Negligence per se", "Battery"], "Give written notice and help transfer care."),
        (9, "Informed consent includes explaining:", "Risks, benefits, and alternatives", ["Only the cost", "Only the doctor's name", "Nothing"], "The patient must understand."),
        (7, "The Americans with Disabilities Act protects:", "People with disabilities from discrimination", ["Only veterans", "Only children", "Only employers"], "It requires reasonable accommodations."),
    ]),
    ((10, 11, 12), [
        (10, "The HITECH Act strengthened rules on:", "Electronic health information and breach notification", ["Drug pricing", "Hospital construction", "Licensing"], "It also promoted EHR adoption."),
        (10, "Posting patient information on social media:", "Violates privacy laws", ["Is allowed if names are left out always", "Is encouraged", "Is required"], "Even details can identify patients."),
        (11, "GINA protects against discrimination based on:", "Genetic information", ["Age", "Income", "Height"], "In health insurance and employment."),
        (11, "Research involving humans is overseen by an:", "Institutional Review Board (IRB)", ["Insurance company", "Pharmacy", "Licensing board"], "IRBs protect research subjects."),
        (11, "New drugs must be approved by the:", "FDA", ["DEA", "CDC", "OSHA"], "The DEA regulates controlled substances."),
        (12, "Hospitals are commonly accredited by:", "The Joint Commission", ["The FDA", "The DEA", "The FBI"], "Accreditation shows quality standards are met."),
        (12, "Health care administrators must ensure compliance with:", "Laws, regulations, and accreditation standards", ["Only budgets", "Only marketing", "Nothing"], "Compliance protects patients and organizations."),
        (10, "EHRs must be protected by:", "Passwords and security measures", ["Sharing logins", "Leaving screens open", "Printing everything"], "HIPAA's Security Rule requires safeguards."),
        (11, "Controlled substances are regulated by the:", "DEA", ["FDA only", "CMS", "OSHA"], "Drug Enforcement Administration."),
    ]),
    ((13, 14, 15), [
        (13, "A minor who is legally independent from parents is:", "Emancipated", ["A ward", "Incompetent", "A guardian"], "They can consent to their own care."),
        (13, "Health care workers who suspect child abuse must:", "Report it", ["Ignore it", "Confront the parents alone", "Wait for proof"], "They are mandatory reporters."),
        (13, "Generally, treating a minor requires:", "Parental consent", ["No consent", "Court approval always", "The child's consent only"], "There are some exceptions."),
        (14, "A competent adult has the right to:", "Refuse treatment", ["Demand any drug", "Ignore laws", "Skip consent forms"], "Autonomy protects this right."),
        (14, "Organ donation is governed by the:", "Uniform Anatomical Gift Act", ["HIPAA", "EMTALA", "ADA"], "It allows people to donate organs."),
        (15, "A document naming someone to make health decisions for you is a:", "Durable power of attorney for health care", ["Living will", "DNR order", "Will"], "A living will states treatment wishes."),
        (15, "Financial exploitation of an older adult is a form of:", "Elder abuse", ["Malpractice", "Libel", "Fraud by the patient"], "It must be reported."),
        (15, "The Patient Self-Determination Act requires facilities to:", "Inform patients about advance directives", ["Provide free care", "Hire more nurses", "Ban DNR orders"], "It applies to facilities receiving Medicare/Medicaid."),
        (15, "A DNR order means:", "Do not resuscitate", ["Do not report", "Daily nursing review", "Do not refer"], "It must be followed."),
    ]),
]

BOOK = {
    "titles": ["Medical Law & Professional Ethics"],
    "edition": "2nd edition (2022)",
    "source": "Goodheart-Willcox table of contents",
    "chapters": C,
    "quizzes": Q,
}
