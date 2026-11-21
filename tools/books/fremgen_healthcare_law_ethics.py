# Fremgen - Healthcare Law and Ethics (Pearson). Formerly "Medical Law and Ethics".
# Chapter list: 7th edition, from the publisher's table of contents (pearson.com).
# Chapter numbers follow the order listed there. Summaries are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Introduction to Healthcare Law, Ethics, and Bioethics", "Law is a set of enforceable rules; ethics are moral principles; bioethics deals with issues from medical advances; etiquette is professional courtesy. Ethical principles include autonomy, beneficence, nonmaleficence, and justice. Decision-making models help resolve dilemmas.", ["Law vs. ethics vs. etiquette", "Bioethics", "Four core principles", "Decision-making models"]),
    ch(2, "The Legal System", "U.S. law comes from constitutions, statutes, administrative regulations, and common (case) law based on precedent (stare decisis). Law is public (including criminal) or private (civil: torts and contracts). Courts are federal and state. A lawsuit includes the plaintiff, defendant, discovery, depositions, and trial.", ["Sources of law", "Stare decisis", "Criminal vs. civil", "Plaintiff and defendant"]),
    ch(3, "Essentials of the Legal System for Healthcare Professionals", "Health professionals may testify as fact witnesses or expert witnesses. Subpoenas order appearance (subpoena duces tecum orders records). Statutes of limitations limit when suits can be filed. Alternative dispute resolution includes mediation and arbitration.", ["Subpoena duces tecum", "Expert witness", "Statute of limitations", "Mediation and arbitration"]),
    ch(4, "Working in Today's Healthcare Environment", "Licensure (mandatory, state), certification (voluntary, professional groups), and registration credential health workers. Scope of practice limits duties. Practice types include sole proprietorship, partnership, group practice, and corporations. Managed care organizations (HMOs, PPOs) shape delivery.", ["Licensure vs. certification", "Scope of practice", "Practice types", "HMOs and PPOs"]),
    ch(5, "The Patient Relationship", "The provider-patient relationship is a contract—expressed or implied. Informed consent requires explaining procedures, risks, benefits, and alternatives. Patients have rights and responsibilities. Providers must not abandon patients; terminating care requires written notice.", ["Expressed vs. implied contract", "Informed consent", "Patients' rights", "Avoid abandonment"]),
    ch(6, "Professional Liability and Medical Malpractice", "Malpractice is professional negligence. Plaintiffs must prove the four Ds: duty, dereliction, direct cause, and damages. Doctrines include res ipsa loquitur ('the thing speaks for itself') and respondeat superior. Defenses include contributory and comparative negligence and assumption of risk. Malpractice insurance and risk management reduce exposure.", ["Four Ds", "Res ipsa loquitur", "Respondeat superior", "Comparative negligence"]),
    ch(7, "Public Duties of the Healthcare Professional", "Health professionals must report births, deaths, certain communicable diseases, child and elder abuse, and injuries from violence. Good Samaritan laws protect those who help in emergencies in good faith. Controlled substances are regulated by the DEA.", ["Mandatory reporting", "Good Samaritan laws", "Report abuse", "DEA controlled substances"]),
    ch(8, "Workplace Law and Ethics", "Employment laws include Title VII (no discrimination), the ADA, the Age Discrimination in Employment Act, the Family and Medical Leave Act, the Fair Labor Standards Act, and OSHA safety rules. Sexual harassment includes quid pro quo and hostile environment. Employment-at-will allows ending employment for most reasons.", ["Title VII", "ADA and FMLA", "OSHA", "Sexual harassment types"]),
    ch(9, "The Medical Record", "The medical record is a legal document owned by the provider; the information belongs to the patient. Records must be accurate, timely, and complete. Correct errors with a single line, initials, and date—never erase. Electronic health records must be secured. Retention rules vary by state.", ["Legal document", "Single-line corrections", "Provider owns the record", "EHR security"]),
    ch(10, "Patient Confidentiality and HIPAA", "HIPAA's Privacy Rule protects identifiable health information (PHI); the Security Rule protects electronic PHI. Disclosures generally need authorization except for treatment, payment, and operations, or as required by law. Breaches must be reported under HITECH. Patients can access and request amendments to their records.", ["PHI protection", "Privacy and Security Rules", "TPO exceptions", "Breach notification"]),
    ch(11, "Ethical and Bioethical Issues in Healthcare", "Bioethical issues include allocation of scarce resources, organ transplantation, research ethics (informed consent, IRBs), genetic testing and privacy, and conflicts of interest.", ["Resource allocation", "Organ transplants", "Research ethics", "Genetic testing"]),
    ch(12, "Ethical Issues Related to the Beginning of Life", "Issues include contraception, sterilization, abortion, assisted reproductive technologies (in vitro fertilization, surrogacy), genetic screening, and stem cell research. Conscience clauses may let providers decline to participate.", ["IVF and surrogacy", "Genetic screening", "Stem cell research", "Conscience clauses"]),
    ch(13, "Ethical Issues Related to the End of Life", "End-of-life issues include advance directives (living wills, durable power of attorney for health care), DNR orders, the Patient Self-Determination Act, hospice and palliative care, brain death criteria, organ donation (Uniform Anatomical Gift Act), and euthanasia and physician-assisted death.", ["Advance directives", "Patient Self-Determination Act", "Hospice", "Uniform Anatomical Gift Act"]),
    ch(14, "Trends in Healthcare", "Trends include telehealth, artificial intelligence, value-based care, changes in insurance coverage, workforce shortages, and growing attention to health equity.", ["Telehealth", "Artificial intelligence", "Value-based care", "Health equity"]),
    ch(15, "Codes of Ethics", "Professional associations (AMA, ANA, AAMA, and others) publish codes of ethics that set standards of conduct, such as respecting patients, maintaining confidentiality, and acting with honesty and competence.", ["AMA Code of Medical Ethics", "Nursing code", "Shared values", "Professional standards"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Moral principles that guide conduct are:", "Ethics", ["Laws", "Etiquette", "Statutes"], "Laws are enforceable."),
        (1, "Doing no harm is the principle of:", "Nonmaleficence", ["Beneficence", "Autonomy", "Justice"], "Beneficence = doing good."),
        (1, "Issues arising from medical advances are studied in:", "Bioethics", ["Etiquette", "Civil law", "Accounting"], "Such as cloning or genetic testing."),
        (2, "The principle of following precedent is:", "Stare decisis", ["Res ipsa loquitur", "Respondeat superior", "Habeas corpus"], "'Let the decision stand.'"),
        (2, "The person who files a lawsuit is the:", "Plaintiff", ["Defendant", "Judge", "Witness"], "The defendant is sued."),
        (2, "Torts and contracts are part of:", "Civil law", ["Criminal law", "Constitutional law only", "Administrative law"], "Private law."),
        (3, "A subpoena duces tecum orders a person to bring:", "Records or documents", ["Only themselves", "A lawyer", "Payment"], "'Bring with you.'"),
        (3, "A witness with special knowledge who gives opinions is an:", "Expert witness", ["Fact witness", "Plaintiff", "Juror"], "Fact witnesses state what they saw."),
        (3, "The time limit for filing a lawsuit is the:", "Statute of limitations", ["Discovery period", "Deposition", "Arbitration"], "Varies by state."),
    ]),
    ((4, 5, 6), [
        (4, "A mandatory credential granted by the state is:", "Licensure", ["Certification", "Registration", "Accreditation"], "Required to practice."),
        (4, "Duties legally allowed for a profession are its:", "Scope of practice", ["Job description", "Contract", "Code of ethics"], "Set by law."),
        (4, "An HMO is a type of:", "Managed care organization", ["Sole proprietorship", "Partnership", "Court"], "Controls costs."),
        (5, "Holding out an arm for a vaccine creates an:", "Implied contract", ["Expressed contract", "Written contract", "Void contract"], "Shown by actions."),
        (5, "Informed consent includes explaining:", "Risks, benefits, and alternatives", ["Only the cost", "Only the procedure name", "Nothing"], "Patient must understand."),
        (5, "Ending care without proper notice is:", "Abandonment", ["Negligence per se", "Consent", "Battery"], "Give written notice."),
        (6, "The four Ds of negligence are duty, dereliction, direct cause, and:", "Damages", ["Defense", "Deposition", "Diagnosis"], "All must be proven."),
        (6, "'The thing speaks for itself' is:", "Res ipsa loquitur", ["Respondeat superior", "Stare decisis", "Quid pro quo"], "E.g., a sponge left in a patient."),
        (6, "When both parties share fault and damages are reduced proportionally, it's:", "Comparative negligence", ["Contributory negligence", "Assumption of risk", "Res judicata"], "Percent of fault."),
    ]),
    ((7, 8, 9), [
        (7, "Laws protecting people who help in emergencies are:", "Good Samaritan laws", ["HIPAA", "OSHA", "Stark laws"], "Good-faith aid."),
        (7, "Health professionals must report suspected:", "Child abuse", ["Messy homes", "Missed appointments", "Low income"], "Mandatory reporting."),
        (7, "Controlled substances are regulated by the:", "DEA", ["FDA only", "OSHA", "CDC"], "Drug Enforcement Administration."),
        (8, "Title VII of the Civil Rights Act prohibits discrimination based on:", "Race, color, religion, sex, or national origin", ["Age only", "Disability only", "Income"], "Employment law."),
        (8, "Unpaid job-protected leave for family or medical reasons is provided by the:", "FMLA", ["ADA", "FLSA", "OSHA"], "Family and Medical Leave Act."),
        (8, "Requesting favors in exchange for job benefits is:", "Quid pro quo harassment", ["Hostile environment", "Discrimination by age", "At-will employment"], "'This for that.'"),
        (9, "The physical medical record is owned by the:", "Provider or facility", ["Patient", "Insurance company", "Government"], "The information belongs to the patient."),
        (9, "To correct an error in a paper record, you should:", "Draw a single line, initial, and date", ["Erase it", "Use correction fluid", "Rip out the page"], "Keep it readable."),
        (9, "A medical record is a:", "Legal document", ["Personal diary", "Optional note", "Billing form only"], "Can be used in court."),
    ]),
    ((10, 11, 12), [
        (10, "HIPAA's Privacy Rule protects:", "Protected health information (PHI)", ["Only billing data", "Public records", "Employee salaries"], "Identifiable health info."),
        (10, "PHI may be shared without authorization for:", "Treatment, payment, and operations", ["Marketing", "Social media", "Curiosity"], "TPO."),
        (10, "Breach notification requirements were strengthened by the:", "HITECH Act", ["ADA", "FMLA", "OSHA"], "2009."),
        (11, "Research involving people is overseen by an:", "IRB", ["HMO", "OSHA", "DEA"], "Institutional Review Board."),
        (11, "Deciding who gets scarce organs raises issues of:", "Resource allocation", ["Etiquette", "Billing", "Licensing"], "Justice."),
        (11, "A situation where personal gain may influence decisions is a:", "Conflict of interest", ["Contract", "Tort", "Consent"], "Must be disclosed."),
        (12, "Fertilizing an egg outside the body is:", "In vitro fertilization", ["Sterilization", "Contraception", "Cloning"], "IVF."),
        (12, "Laws allowing providers to refuse participation in procedures on moral grounds are:", "Conscience clauses", ["Good Samaritan laws", "Stark laws", "Statutes of limitations"], "Protect provider beliefs."),
        (12, "A woman carrying a baby for another couple is a:", "Surrogate", ["Donor", "Guardian", "Proxy"], "Surrogacy."),
    ]),
    ((13, 14, 15), [
        (13, "A document stating treatment wishes if a person can't speak is a:", "Living will", ["DNR only", "Power of attorney for finances", "Will"], "Type of advance directive."),
        (13, "The law requiring facilities to inform patients about advance directives is the:", "Patient Self-Determination Act", ["HIPAA", "EMTALA", "Uniform Anatomical Gift Act"], "1990."),
        (13, "Organ donation is governed by the:", "Uniform Anatomical Gift Act", ["Patient Self-Determination Act", "ADA", "FMLA"], "Allows donation."),
        (14, "Providing care remotely through technology is:", "Telehealth", ["Hospice", "Managed care", "Arbitration"], "Growing trend."),
        (14, "Payment tied to patient outcomes is:", "Value-based care", ["Fee-for-service", "Self-pay", "Charity care"], "Rewards quality."),
        (14, "Efforts to ensure everyone can attain good health focus on:", "Health equity", ["Profit", "Marketing", "Licensing"], "Reduce disparities."),
        (15, "Professional codes of ethics are written by:", "Professional associations", ["Courts", "Insurance companies", "Patients"], "Like the AMA or ANA."),
        (15, "Most health care codes of ethics require:", "Confidentiality and honesty", ["Profit first", "Secrecy from patients", "Ignoring laws"], "Shared values."),
        (15, "The AMA publishes a code of ethics for:", "Physicians", ["Nurses", "Pharmacists", "Dentists"], "American Medical Association."),
    ]),
]

BOOK = {
    "titles": ["Healthcare Law and Ethics"],
    "edition": "7th edition",
    "source": "Pearson table of contents",
    "chapters": C,
    "quizzes": Q,
}
