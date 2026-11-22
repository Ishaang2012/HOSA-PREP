# Tamparo & Lewis - Medical Law, Ethics, & Bioethics for the Health Professions (F.A. Davis).
# Chapter list supplied by the site owner (not verified against the publisher). Summaries are written for this site.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "The Need for Law, Ethics, and Bioethics in Health Care", "Law sets enforceable rules; ethics are moral principles; bioethics addresses issues from medical advances like genetic testing and life support. Core principles are autonomy, beneficence, nonmaleficence, and justice. Ethical decision-making models help resolve dilemmas.", ["Law vs. ethics vs. bioethics", "Four core principles", "Ethical dilemmas", "Decision-making models"]),
    ch(2, "The Legal System and Current Issues in Health Care", "Sources of law include constitutions, statutes, regulations, and case law. Law is criminal or civil (torts, contracts). Courts are federal and state. Current issues include health reform, access to care, and telehealth.", ["Sources of law", "Criminal vs. civil", "Torts and contracts", "Court systems"]),
    ch(3, "The Health Care Professional's Role and Responsibilities", "Professionals are credentialed through licensure (mandatory, state), certification, and registration, and must work within their scope of practice. Duties include public reporting (births, deaths, communicable diseases, abuse) and following Good Samaritan principles.", ["Licensure vs. certification", "Scope of practice", "Mandatory reporting", "Good Samaritan laws"]),
    ch(4, "Workplace Law and Ethics", "Employment laws include Title VII, the ADA, ADEA, FMLA, OSHA, and wage laws. Sexual harassment can be quid pro quo or hostile environment. Employment-at-will and workplace ethics shape employer-employee relationships.", ["Title VII", "ADA and FMLA", "OSHA", "Sexual harassment"]),
    ch(5, "The Medical Record", "The medical record is a legal document. Entries must be accurate, timely, and complete; errors are corrected with a single line, date, and initials. Records belong to the provider, but patients can access their information. Retention and electronic records rules apply.", ["Legal document", "Correcting errors", "Patient access", "Electronic records"]),
    ch(6, "Informed Consent", "Informed consent requires explaining the diagnosis, procedure, risks, benefits, and alternatives in understandable language. Consent can be expressed or implied. Special cases include minors, emancipated minors, emergencies, and patients lacking capacity.", ["Elements of informed consent", "Expressed vs. implied", "Minors and capacity", "Emergency exception"]),
    ch(7, "Privacy, Confidentiality, and Privileged Communication", "HIPAA protects identifiable health information. Confidentiality means not sharing information without authorization; privileged communication protects certain patient-provider communications in court. Exceptions include mandatory reporting and duty to warn.", ["HIPAA", "Confidentiality", "Privileged communication", "Duty to warn"]),
    ch(8, "Professional Liability and Medical Malpractice", "Malpractice is professional negligence. Plaintiffs must prove duty, dereliction, direct cause, and damages. Doctrines include res ipsa loquitur and respondeat superior. Defenses include contributory and comparative negligence and statutes of limitations. Risk management reduces liability.", ["Four Ds", "Res ipsa loquitur", "Respondeat superior", "Defenses"]),
    ch(9, "Birth and the Beginning of Life", "Issues include contraception, sterilization, abortion, assisted reproduction (IVF, surrogacy), genetic testing and counseling, and the rights of parents and fetuses.", ["Contraception", "IVF and surrogacy", "Genetic counseling", "Reproductive rights"]),
    ch(10, "Death and Dying", "End-of-life issues include defining death (brain death), advance directives (living will, durable power of attorney for health care), DNR orders, hospice and palliative care, organ donation, and physician-assisted death.", ["Brain death", "Advance directives", "DNR orders", "Organ donation"]),
    ch(11, "Bioethical Issues in Health Care", "Bioethical topics include allocation of scarce resources, organ transplantation, research ethics and informed consent, genetic engineering, stem cells, and access to care.", ["Resource allocation", "Research ethics", "Genetic engineering", "Stem cells"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Moral principles guiding right and wrong are:", "Ethics", ["Laws", "Regulations", "Statutes"], "Laws are enforceable."),
        (1, "Issues arising from medical advances are studied in:", "Bioethics", ["Etiquette", "Criminal law", "Accounting"], "E.g., life support decisions."),
        (1, "'Do no harm' is the principle of:", "Nonmaleficence", ["Beneficence", "Autonomy", "Justice"], "Beneficence means doing good."),
        (2, "Laws made by legislatures are:", "Statutes", ["Case law", "Regulations", "Constitutions"], "Agencies make regulations."),
        (2, "A civil wrong causing harm is a:", "Tort", ["Felony", "Misdemeanor", "Contract"], "Negligence is a tort."),
        (2, "Law based on court decisions is:", "Case (common) law", ["Statutory law", "Administrative law", "Constitutional law"], "Precedent."),
        (3, "A mandatory, state-granted credential is:", "Licensure", ["Certification", "Registration", "Accreditation"], "Required to practice."),
        (3, "Health professionals must report:", "Suspected child abuse", ["Patient hobbies", "Political views", "Insurance type"], "Mandatory reporting."),
        (3, "Laws protecting people who help in emergencies in good faith are:", "Good Samaritan laws", ["HIPAA", "OSHA", "Stark laws"], "Encourage bystander help."),
    ]),
    ((4, 5, 6), [
        (4, "Unpaid job-protected leave for medical reasons is provided by:", "FMLA", ["ADA", "OSHA", "Title VII"], "Family and Medical Leave Act."),
        (4, "A workplace made offensive by harassment is a:", "Hostile work environment", ["Quid pro quo", "At-will job", "Safe harbor"], "Type of harassment."),
        (4, "Workplace safety standards are set by:", "OSHA", ["FDA", "CDC", "DEA"], "Includes bloodborne pathogens."),
        (5, "To correct a paper record error:", "Draw one line, date, and initial", ["Erase it", "Use correction fluid", "Tear out the page"], "Keep it readable."),
        (5, "The medical record is a:", "Legal document", ["Personal diary", "Optional note", "Billing form only"], "Used in court."),
        (5, "Who owns the physical medical record?", "The provider or facility", ["The patient", "The insurer", "The government"], "Patients own the information."),
        (6, "Informed consent requires explaining:", "Risks, benefits, and alternatives", ["Only the cost", "Only the procedure name", "Nothing"], "Plus the diagnosis."),
        (6, "Rolling up a sleeve for a vaccine shows:", "Implied consent", ["Expressed consent", "Refusal", "Informed refusal"], "Consent by action."),
        (6, "Consent isn't needed when:", "A true emergency threatens life and the patient can't consent", ["The patient is busy", "The doctor is in a hurry", "The patient is an adult"], "Emergency exception."),
    ]),
    ((7, 8, 9), [
        (7, "Health information privacy is protected by:", "HIPAA", ["OSHA", "ADA", "EMTALA"], "Privacy Rule."),
        (7, "Communications protected from being disclosed in court are:", "Privileged communication", ["Public records", "Hearsay", "Testimony"], "E.g., patient-physician."),
        (7, "Warning a threatened person about a dangerous patient reflects the:", "Duty to warn", ["Right to privacy", "Good Samaritan law", "Statute of limitations"], "Tarasoff case."),
        (8, "The four Ds of negligence are duty, dereliction, direct cause, and:", "Damages", ["Deposition", "Diagnosis", "Defense"], "All must be proven."),
        (8, "'The thing speaks for itself' is:", "Res ipsa loquitur", ["Respondeat superior", "Stare decisis", "Quid pro quo"], "E.g., an instrument left inside."),
        (8, "Employers being responsible for employees' acts is:", "Respondeat superior", ["Res ipsa loquitur", "Comparative negligence", "Assumption of risk"], "'Let the master answer.'"),
        (9, "Fertilizing an egg outside the body is:", "In vitro fertilization", ["Sterilization", "Contraception", "Cloning"], "IVF."),
        (9, "A woman carrying a baby for another couple is a:", "Surrogate", ["Donor", "Guardian", "Proxy"], "Surrogacy."),
        (9, "Counseling families about inherited disease risk is:", "Genetic counseling", ["Psychotherapy", "Physical therapy", "Triage"], "Helps informed decisions."),
    ]),
    ((10, 11), [
        (10, "Irreversible loss of all brain function is:", "Brain death", ["Coma", "Persistent vegetative state", "Syncope"], "Legal death."),
        (10, "A document naming someone to make health decisions is a:", "Durable power of attorney for health care", ["Living will", "DNR", "Will"], "Health care proxy."),
        (10, "A DNR order means:", "Do not resuscitate", ["Do not refer", "Do not report", "Do not release"], "No CPR."),
        (10, "Comfort-focused care for terminal illness is:", "Hospice", ["Rehabilitation", "Acute care", "Surgery"], "Includes family support."),
        (11, "Deciding who gets scarce organs raises issues of:", "Resource allocation", ["Billing", "Licensing", "Etiquette"], "Justice."),
        (11, "Research involving people must have:", "Informed consent and ethics review", ["Payment only", "No oversight", "Secret methods"], "IRB approval."),
        (11, "Unspecialized cells that can become many cell types are:", "Stem cells", ["Red blood cells", "Neurons", "Platelets"], "Ethical debate in research."),
        (10, "Organ donation is governed by the:", "Uniform Anatomical Gift Act", ["HIPAA", "ADA", "FMLA"], "Allows donation."),
        (11, "Changing an organism's DNA for medical purposes is:", "Genetic engineering", ["Vaccination", "Triage", "Sterilization"], "Includes gene therapy."),
    ]),
]

BOOK = {
    "titles": ["Medical Law, Ethics, & Bioethics for the Health Professions"],
    "edition": "Edition not verified; chapter list supplied by the site owner",
    "source": "Chapter list supplied by the site owner",
    "chapters": C,
    "quizzes": Q,
}
