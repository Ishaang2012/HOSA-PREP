# ASHP - Manual for Pharmacy Technicians (Bachenheimer & Phillips, eds.).
# Chapter list supplied by the site owner (not verified against the publisher). Summaries are written for this site.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Introduction to Pharmacy Practice", "Pharmacy technicians assist pharmacists in community, hospital, long-term care, mail-order, and specialty settings. Technicians are certified through PTCB or NHA and registered or licensed by state boards. Professionalism and continuing education are expected.", ["Practice settings", "PTCB/NHA certification", "State boards", "Professionalism"]),
    ch(2, "Pharmacy Law, Regulations, and Standards", "Key laws include the Food, Drug, and Cosmetic Act, Durham-Humphrey (Rx vs. OTC), Kefauver-Harris (efficacy), the Controlled Substances Act (Schedules I–V), Poison Prevention Packaging Act, OBRA '90 (counseling), HIPAA, and the Combat Methamphetamine Epidemic Act. USP standards guide compounding.", ["Controlled Substances Act", "Durham-Humphrey", "OBRA '90 counseling", "HIPAA"]),
    ch(3, "Communication and Teamwork", "Technicians communicate with patients, pharmacists, prescribers, and insurers. Skills include active listening, professional phone etiquette, and knowing which questions to refer to the pharmacist (counseling is the pharmacist's role).", ["Active listening", "Refer clinical questions", "Phone etiquette", "Teamwork"]),
    ch(4, "Dosage Forms and Routes of Administration", "Dosage forms include tablets, capsules, solutions, suspensions, ointments, creams, suppositories, inhalers, patches, and injectables. Routes include oral, sublingual, buccal, topical, rectal, inhalation, and parenteral (IV, IM, subQ).", ["Solid vs. liquid forms", "Enteral vs. parenteral", "Extended-release", "Don't crush enteric-coated"]),
    ch(5, "Pharmacology", "Pharmacology covers how drugs work (pharmacodynamics) and how the body handles them (pharmacokinetics: absorption, distribution, metabolism, excretion). Technicians learn drug classes, brand and generic names, and common side effects and interactions.", ["ADME", "Drug classes", "Brand vs. generic", "Interactions"]),
    ch(6, "Medication Safety", "Medication errors are prevented with Tall Man lettering for look-alike/sound-alike drugs, avoiding error-prone abbreviations, barcode scanning, double-checks for high-alert drugs, and reporting errors (e.g., to ISMP).", ["Look-alike/sound-alike drugs", "Tall Man lettering", "High-alert drugs", "Error reporting"]),
    ch(7, "Pharmacy Calculations", "Technicians calculate doses, days' supply, conversions (metric and household), concentrations, dilutions, IV flow rates, and pediatric weight-based doses accurately.", ["Days' supply", "Conversions", "IV rates", "Weight-based doses"]),
    ch(8, "Community Pharmacy Practice", "Community workflow: receive and verify prescriptions, enter data, process insurance, fill and label, pharmacist verification, and patient pickup with counseling offer. Technicians also manage OTC sales and pseudoephedrine logs.", ["Prescription workflow", "Labeling", "Insurance processing", "Counseling offer"]),
    ch(9, "Hospital Pharmacy Practice", "Hospital technicians fill unit-dose carts, restock automated dispensing cabinets, prepare IV admixtures, and support medication reconciliation. Medication orders come through CPOE.", ["Unit dose", "Automated dispensing cabinets", "IV admixtures", "Medication orders"]),
    ch(10, "Nonsterile Compounding", "Nonsterile compounding (USP <795>) prepares creams, ointments, suspensions, and capsules. Techniques include trituration, levigation, and geometric dilution; beyond-use dates and documentation are required.", ["USP <795>", "Trituration and levigation", "Geometric dilution", "Beyond-use dates"]),
    ch(11, "Sterile Compounding and Hazardous Drugs", "Sterile compounding (USP <797>) uses aseptic technique in ISO Class 5 primary engineering controls. Hazardous drugs (USP <800>), like chemotherapy, require containment, special PPE, and biological safety cabinets.", ["USP <797>", "Aseptic technique", "ISO Class 5", "USP <800> hazardous drugs"]),
    ch(12, "Billing and Reimbursement", "Technicians process claims with PBMs, handle rejections, prior authorizations, and coordination of benefits. Terms include copay, deductible, formulary, and NDC-based billing. Medicare Part D covers outpatient drugs.", ["PBMs", "Prior authorization", "Formulary", "Medicare Part D"]),
    ch(13, "Inventory Management and Informatics", "Inventory management includes ordering, receiving, rotating stock (first in, first out), handling expired and recalled drugs, and controlled substance inventory (DEA Form 222 for Schedule II). Informatics includes pharmacy software and automation.", ["FIFO rotation", "Recalls", "DEA Form 222", "Pharmacy automation"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Pharmacy technicians can be certified through:", "PTCB or NHA", ["NBRC", "DANB", "BOC"], "CPhT credential."),
        (1, "Pharmacy technicians are regulated by:", "State boards of pharmacy", ["The AMA", "Hospitals only", "The FDA only"], "Rules vary by state."),
        (1, "Who is responsible for final prescription verification?", "The pharmacist", ["The technician", "The cashier", "The patient"], "Technicians assist."),
        (2, "The law that separated prescription and OTC drugs is:", "Durham-Humphrey Amendment", ["Kefauver-Harris", "OBRA '90", "HIPAA"], "1951."),
        (2, "Drugs with no accepted medical use are:", "Schedule I", ["Schedule II", "Schedule IV", "Schedule V"], "E.g., heroin."),
        (2, "OBRA '90 requires pharmacists to:", "Offer counseling to Medicaid patients", ["Stock all drugs", "Lower prices", "Hire technicians"], "Drug utilization review too."),
        (3, "If a patient asks how to take a new drug, the technician should:", "Refer to the pharmacist", ["Answer from memory", "Guess", "Tell them to search online"], "Counseling is the pharmacist's role."),
        (3, "Fully focusing on a speaker is:", "Active listening", ["Interrupting", "Multitasking", "Lecturing"], "Builds trust."),
        (3, "Teamwork in pharmacy improves:", "Patient safety", ["Errors", "Wait times only", "Profits only"], "Clear communication."),
    ]),
    ((4, 5, 6), [
        (4, "A drug placed under the tongue is given:", "Sublingually", ["Buccally", "Topically", "Rectally"], "Fast absorption."),
        (4, "Enteric-coated tablets should not be:", "Crushed", ["Swallowed whole", "Taken with water", "Stored dry"], "Protects the stomach or drug."),
        (4, "A liquid with undissolved particles that must be shaken is a:", "Suspension", ["Solution", "Elixir", "Syrup"], "Shake well."),
        (5, "The body's processing of a drug (ADME) is:", "Pharmacokinetics", ["Pharmacodynamics", "Pharmacognosy", "Toxicology"], "Absorption to excretion."),
        (5, "Most drug metabolism occurs in the:", "Liver", ["Kidneys", "Lungs", "Skin"], "Kidneys excrete."),
        (5, "A drug's nonproprietary name is its:", "Generic name", ["Brand name", "Trade name", "Chemical name only"], "Lowercase."),
        (6, "Writing hydrOXYzine and hydrALAZINE uses:", "Tall Man lettering", ["Leading zeros", "Bold font only", "Abbreviations"], "Prevents mix-ups."),
        (6, "Insulin and heparin are:", "High-alert medications", ["OTC drugs", "Vitamins", "Placebos"], "Extra checks."),
        (6, "Medication errors can be reported to:", "ISMP's reporting program", ["The DEA only", "Social media", "No one"], "Learn and prevent."),
    ]),
    ((7, 8, 9), [
        (7, "A 30 mL bottle with 1 mL twice daily lasts:", "15 days", ["30 days", "10 days", "60 days"], "30 ÷ 2."),
        (7, "1 teaspoon equals:", "5 mL", ["15 mL", "30 mL", "1 mL"], "1 tbsp = 15 mL."),
        (7, "A 44-lb child weighs:", "20 kg", ["44 kg", "10 kg", "88 kg"], "Divide by 2.2."),
        (8, "The first step in community prescription processing is:", "Receiving and reviewing the prescription", ["Bagging", "Counseling", "Billing"], "Check completeness."),
        (8, "Pseudoephedrine sales are limited by the:", "Combat Methamphetamine Epidemic Act", ["HIPAA", "OBRA '90", "Stark Law"], "Logbook and ID."),
        (8, "Prescription labels must include:", "Patient name, drug, strength, directions", ["Only the price", "Only the drug name", "The pharmacist's phone number only"], "Plus other required info."),
        (9, "Single, ready-to-use doses common in hospitals are:", "Unit doses", ["Bulk bottles", "Stock bottles", "Compounded creams"], "Reduce errors."),
        (9, "Machines that store and dispense drugs on hospital units are:", "Automated dispensing cabinets", ["Centrifuges", "Autoclaves", "Incubators"], "E.g., Pyxis."),
        (9, "Mixing medications into IV fluids is preparing:", "IV admixtures", ["Suppositories", "Tablets", "Ointments"], "Sterile technique."),
    ]),
    ((10, 11, 12, 13)[:2], [
        (10, "Nonsterile compounding standards are in:", "USP <795>", ["USP <797>", "USP <800>", "HIPAA"], "Creams, capsules."),
        (10, "Grinding a powder to fine particles is:", "Trituration", ["Levigation", "Geometric dilution", "Reconstitution"], "Mortar and pestle."),
        (10, "Mixing small amounts of drug with equal amounts of base stepwise is:", "Geometric dilution", ["Trituration", "Levigation", "Filtration"], "Even distribution."),
        (11, "Sterile compounding standards are in:", "USP <797>", ["USP <795>", "USP <800>", "OBRA"], "Aseptic technique."),
        (11, "Hazardous drug handling standards are in:", "USP <800>", ["USP <795>", "USP <797>", "HIPAA"], "E.g., chemotherapy."),
        (11, "Sterile preparations are made in an:", "ISO Class 5 environment", ["Open counter", "Break room", "ISO Class 9"], "Laminar airflow hood or BSC."),
        (10, "The date after which a compounded product shouldn't be used is the:", "Beyond-use date", ["Expiration of the bottle", "Fill date", "Refill date"], "BUD."),
        (11, "Chemotherapy is prepared in a:", "Biological safety cabinet", ["Horizontal laminar flow hood only", "Open counter", "Refrigerator"], "Protects the worker."),
        (10, "Mixing a powder with a small amount of liquid to form a paste is:", "Levigation", ["Trituration", "Spatulation only", "Pulverization"], "Smooth ointments."),
    ]),
    ((12, 13), [
        (12, "Companies that manage prescription benefits for insurers are:", "PBMs", ["HMOs", "PPOs", "DEA"], "Pharmacy benefit managers."),
        (12, "Insurance approval needed before covering certain drugs is:", "Prior authorization", ["Copay", "Deductible", "Formulary"], "Insurer review."),
        (12, "Medicare's outpatient drug benefit is:", "Part D", ["Part A", "Part B", "Part C"], "Prescription coverage."),
        (12, "A list of drugs covered by a plan is a:", "Formulary", ["Requisition", "Prescription", "Invoice"], "Tiers affect cost."),
        (13, "Using older stock first is:", "FIFO (first in, first out)", ["LIFO", "Just in time", "Par level"], "Prevents expiration."),
        (13, "Schedule II drugs are ordered with:", "DEA Form 222 (or CSOS)", ["DEA Form 41", "DEA Form 106", "Any order form"], "Strict tracking."),
        (13, "When a drug is recalled, the technician should:", "Remove affected lots per the recall", ["Ignore it", "Sell it quickly", "Repackage it"], "Follow recall instructions."),
        (13, "Theft or loss of controlled substances is reported on:", "DEA Form 106", ["DEA Form 222", "DEA Form 41", "No form"], "Report promptly."),
        (12, "Coordination of benefits applies when a patient has:", "More than one insurance plan", ["No insurance", "Cash only", "Free samples"], "Primary and secondary."),
    ]),
]

BOOK = {
    "titles": ["Manual for Pharmacy Technicians"],
    "edition": "Edition not verified; chapter list supplied by the site owner",
    "source": "Chapter list supplied by the site owner",
    "chapters": C,
    "quizzes": Q,
}
