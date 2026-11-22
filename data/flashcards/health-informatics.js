// Health Informatics flashcards. Built by tools/build_content.py
window.CONTENT = window.CONTENT || {};
window.CONTENT["health-informatics"] = window.CONTENT["health-informatics"] || {};
window.CONTENT["health-informatics"].flashcards = [
 {
  "section": "Systems & Standards",
  "description": "Health IT systems and how they connect",
  "cards": [
   {
    "front": "EHR",
    "back": "Digital record that follows the patient across providers"
   },
   {
    "front": "CPOE",
    "back": "Computerized provider order entry"
   },
   {
    "front": "CDSS",
    "back": "Clinical decision support: alerts and recommendations"
   },
   {
    "front": "PACS",
    "back": "Picture Archiving and Communication System (images)"
   },
   {
    "front": "HIE",
    "back": "Health information exchange between organizations"
   },
   {
    "front": "MPI",
    "back": "Master patient index: one ID per patient"
   },
   {
    "front": "HL7",
    "back": "Standards for exchanging health data"
   },
   {
    "front": "FHIR",
    "back": "Modern HL7 standard using web APIs"
   },
   {
    "front": "Interoperability",
    "back": "Systems exchanging and using data"
   },
   {
    "front": "Semantic interoperability",
    "back": "Shared meaning of exchanged data"
   },
   {
    "front": "Data warehouse",
    "back": "Historical data from many sources, for analysis"
   },
   {
    "front": "Alert fatigue",
    "back": "Ignoring alerts because there are too many"
   }
  ]
 },
 {
  "section": "Statistics & Analytics",
  "description": "Measures, charts, and analytics types",
  "cards": [
   {
    "front": "Mean / median / mode",
    "back": "Average / middle value / most frequent value"
   },
   {
    "front": "Range",
    "back": "Highest minus lowest"
   },
   {
    "front": "Standard deviation",
    "back": "Spread of values around the mean"
   },
   {
    "front": "68–95–99.7 rule",
    "back": "Share of normal data within 1, 2, and 3 SD"
   },
   {
    "front": "Nominal / ordinal",
    "back": "Unordered categories / ordered categories"
   },
   {
    "front": "Descriptive analytics",
    "back": "What happened"
   },
   {
    "front": "Predictive analytics",
    "back": "What will happen"
   },
   {
    "front": "Prescriptive analytics",
    "back": "What to do"
   },
   {
    "front": "Incidence",
    "back": "New cases in a period"
   },
   {
    "front": "Prevalence",
    "back": "All existing cases"
   },
   {
    "front": "Sensitivity",
    "back": "TP ÷ (TP + FN): finds people who have the disease"
   },
   {
    "front": "Specificity",
    "back": "TN ÷ (TN + FP): clears people who don't have the disease"
   },
   {
    "front": "Type I error",
    "back": "False positive: rejecting a true null hypothesis"
   },
   {
    "front": "p < 0.05",
    "back": "Statistically significant (usual threshold)"
   },
   {
    "front": "ALOS",
    "back": "Average length of stay"
   }
  ]
 },
 {
  "section": "Data Quality & Governance",
  "description": "Keeping data trustworthy and well managed",
  "cards": [
   {
    "front": "Accuracy",
    "back": "Data is correct"
   },
   {
    "front": "Completeness",
    "back": "All required elements are present"
   },
   {
    "front": "Timeliness",
    "back": "Data is current and available when needed"
   },
   {
    "front": "Validity",
    "back": "Values are in acceptable ranges and formats"
   },
   {
    "front": "Granularity",
    "back": "Level of detail"
   },
   {
    "front": "Duplicate record",
    "back": "Two records for one patient"
   },
   {
    "front": "Overlay",
    "back": "One patient's data in another patient's record"
   },
   {
    "front": "Audit trail",
    "back": "Log of who accessed or changed data, and when"
   },
   {
    "front": "Data steward",
    "back": "Oversees quality and use of a data set"
   },
   {
    "front": "Data dictionary",
    "back": "Defines each data element"
   },
   {
    "front": "Metadata",
    "back": "Data about data"
   },
   {
    "front": "Legal health record",
    "back": "Official record released on request"
   }
  ]
 },
 {
  "section": "Code Sets & Terminologies",
  "description": "Which code set does what",
  "cards": [
   {
    "front": "ICD-10-CM",
    "back": "Diagnoses"
   },
   {
    "front": "ICD-10-PCS",
    "back": "Inpatient hospital procedures"
   },
   {
    "front": "CPT",
    "back": "Physician and outpatient procedures and services"
   },
   {
    "front": "HCPCS Level II",
    "back": "Supplies, equipment, and services not in CPT"
   },
   {
    "front": "LOINC",
    "back": "Lab tests and clinical observations"
   },
   {
    "front": "SNOMED CT",
    "back": "Detailed clinical terminology"
   },
   {
    "front": "RxNorm",
    "back": "Standard clinical drug names"
   },
   {
    "front": "Upcoding",
    "back": "Billing a higher-level service than provided (fraud)"
   }
  ]
 },
 {
  "section": "Privacy & Security",
  "description": "HIPAA and cybersecurity basics",
  "cards": [
   {
    "front": "PHI",
    "back": "Protected health information"
   },
   {
    "front": "Privacy Rule",
    "back": "Who may use and share PHI"
   },
   {
    "front": "Security Rule",
    "back": "Administrative, physical, and technical safeguards for ePHI"
   },
   {
    "front": "Minimum necessary",
    "back": "Use only the PHI needed for the task"
   },
   {
    "front": "TPO",
    "back": "Treatment, payment, operations: no authorization needed"
   },
   {
    "front": "Business associate agreement",
    "back": "Required for vendors handling PHI"
   },
   {
    "front": "Breach of 500+",
    "back": "Notify individuals, HHS, and the media"
   },
   {
    "front": "Safe Harbor",
    "back": "Remove 18 identifiers to de-identify data"
   },
   {
    "front": "Encryption",
    "back": "Makes data unreadable without a key"
   },
   {
    "front": "Two-factor authentication",
    "back": "Two different kinds of proof to log in"
   },
   {
    "front": "Phishing",
    "back": "Fake message that tricks people into sharing information"
   },
   {
    "front": "Ransomware",
    "back": "Locks data and demands payment"
   },
   {
    "front": "Role-based access",
    "back": "Access matches job duties"
   }
  ]
 },
 {
  "section": "Research & Ethics",
  "description": "Study design and ethical research",
  "cards": [
   {
    "front": "Independent variable",
    "back": "What the researcher changes"
   },
   {
    "front": "Dependent variable",
    "back": "The outcome that is measured"
   },
   {
    "front": "RCT",
    "back": "Randomized controlled trial"
   },
   {
    "front": "Cohort study",
    "back": "Follows a group over time"
   },
   {
    "front": "Case-control study",
    "back": "Compares cases with controls, looking back"
   },
   {
    "front": "Double-blind",
    "back": "Neither participants nor researchers know the groups"
   },
   {
    "front": "Confounder",
    "back": "Linked to both exposure and outcome"
   },
   {
    "front": "IRB",
    "back": "Protects human research participants"
   },
   {
    "front": "Belmont Report",
    "back": "Respect for persons, beneficence, justice"
   },
   {
    "front": "Internal validity",
    "back": "Correct cause-and-effect within the study"
   },
   {
    "front": "External validity",
    "back": "Results apply to others"
   }
  ]
 },
 {
  "section": "History, Careers & Emerging Tech",
  "description": "Key laws, roles, and new technology",
  "cards": [
   {
    "front": "HITECH Act (2009)",
    "back": "EHR incentives (meaningful use)"
   },
   {
    "front": "21st Century Cures Act",
    "back": "Bans information blocking"
   },
   {
    "front": "ONC",
    "back": "Federal office that leads health IT"
   },
   {
    "front": "AHIMA",
    "back": "Health information management association"
   },
   {
    "front": "RHIA / RHIT",
    "back": "Registered Health Information Administrator / Technician"
   },
   {
    "front": "CMIO",
    "back": "Physician leader for clinical IT"
   },
   {
    "front": "CHDA",
    "back": "Certified Health Data Analyst"
   },
   {
    "front": "Machine learning",
    "back": "Learns patterns from data"
   },
   {
    "front": "NLP",
    "back": "Extracts meaning from text"
   },
   {
    "front": "Precision medicine",
    "back": "Care tailored to genes, environment, and lifestyle"
   }
  ]
 },
 {
  "section": "More Informatics Concepts",
  "description": "Additional systems, standards, and data terms.",
  "cards": [
   {
    "front": "Meaningful Use / Promoting Interoperability",
    "back": "CMS program giving incentives for using certified EHRs effectively."
   },
   {
    "front": "Patient portal",
    "back": "Secure website where patients view records, results, and message providers."
   },
   {
    "front": "Telehealth",
    "back": "Delivering health care remotely using technology."
   },
   {
    "front": "Remote patient monitoring",
    "back": "Collecting patient data (e.g., BP, glucose) at home and sending it to providers."
   },
   {
    "front": "DICOM",
    "back": "Standard for storing and transmitting medical images."
   },
   {
    "front": "API",
    "back": "Application programming interface: allows software systems to exchange data."
   },
   {
    "front": "Cloud computing",
    "back": "Storing and processing data on remote servers over the internet."
   },
   {
    "front": "Big data",
    "back": "Very large data sets analyzed to find patterns, trends, and associations."
   },
   {
    "front": "Dashboard",
    "back": "Visual display of key metrics for quick decision-making."
   },
   {
    "front": "Information blocking",
    "back": "Practices that interfere with access or exchange of EHI; prohibited under the Cures Act."
   },
   {
    "front": "Disaster recovery plan",
    "back": "Procedures to restore systems and data after an outage or disaster."
   },
   {
    "front": "Backup",
    "back": "Copy of data stored separately to restore after loss."
   },
   {
    "front": "Downtime procedures",
    "back": "Paper or backup processes used when the EHR is unavailable."
   },
   {
    "front": "Usability",
    "back": "How easily and efficiently users can use a system; poor usability causes errors."
   },
   {
    "front": "Clinical documentation improvement",
    "back": "Programs that make records more accurate and complete for care and coding."
   },
   {
    "front": "Registry",
    "back": "Database tracking patients with a specific condition (e.g., cancer registry)."
   },
   {
    "front": "Data mining",
    "back": "Discovering patterns in large data sets."
   },
   {
    "front": "Population health management",
    "back": "Using data to improve outcomes for a defined group of patients."
   },
   {
    "front": "Social engineering",
    "back": "Manipulating people into revealing confidential information."
   }
  ]
 }
];
