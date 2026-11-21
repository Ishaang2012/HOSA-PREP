# Pierson and Fairchild's Principles & Techniques of Patient Care (Elsevier).
# Chapter list: 7th edition, from the publisher's table of contents (us.elsevierhealth.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Preparation for Patient Care Activities", "Before patient care, review the chart, plan the activity, prepare the environment and equipment, identify the patient, explain the procedure, and get consent. Good communication and professional behavior build trust. Proper documentation follows each session.", ["Review chart and plan", "Identify the patient", "Explain and get consent", "Prepare environment"]),
    ch(2, "Approaches to Infection Control", "Infection control interrupts the chain of infection. Hand hygiene is the most important measure. Standard precautions apply to all patients; transmission-based precautions add contact, droplet, or airborne measures. Don and doff PPE in the correct order and use aseptic technique when needed.", ["Hand hygiene first", "Standard precautions", "Contact, droplet, airborne", "Correct PPE order"]),
    ch(3, "Assessment of Vital Signs", "Vital signs are temperature, pulse (60–100 bpm adults), respiration (12–20/min), blood pressure (normal under 120/80), oxygen saturation, and pain. They're checked before, during, and after activity to judge tolerance. Abnormal responses mean stopping or modifying activity.", ["Pulse 60–100", "Respirations 12–20", "BP < 120/80", "Monitor during activity"]),
    ch(4, "Body Mechanics", "Good body mechanics protect the caregiver: wide base of support, lowered center of gravity, keep the load close, bend knees and hips (not the back), avoid twisting, and push rather than pull.", ["Wide base of support", "Keep load close", "Bend knees, not back", "Don't twist"]),
    ch(5, "Positioning and Draping", "Positioning includes supine, prone, side-lying, and sitting, using pillows and supports to protect skin and joints and prevent contractures. Reposition at least every 2 hours. Draping protects modesty and warmth while exposing only the treatment area.", ["Reposition every 2 hours", "Prevent pressure injuries", "Prevent contractures", "Draping protects modesty"]),
    ch(6, "Basic Exercise: Passive and Active Range of Motion", "Range of motion exercises maintain joint mobility. Passive ROM (PROM) is done entirely by the clinician; active-assistive ROM (AAROM) with help; active ROM (AROM) by the patient alone. Move slowly, support the joint, and stop at pain or resistance.", ["PROM: clinician moves", "AAROM: assisted", "AROM: patient moves", "Support the joint"]),
    ch(7, "Features and Activities of Wheelchairs", "Wheelchair parts include armrests, footrests/legrests, brakes (wheel locks), push rims, and anti-tippers. Proper fit includes seat width and depth and back height. Patients learn propulsion, curbs, ramps (go up forward, down backward), and pressure relief.", ["Lock brakes before transfers", "Proper fit", "Pressure relief", "Down ramps backward"]),
    ch(8, "Transfer Activities", "Transfers include dependent (lifts), assisted, and independent types: sliding board, stand-pivot, and mechanical lift transfers. Use a gait belt, lock wheelchair brakes, and move toward the patient's stronger side when possible.", ["Gait belt", "Lock brakes", "Move toward stronger side", "Mechanical lifts for dependent patients"]),
    ch(9, "Assistive Devices, Patterns, and Activities", "Assistive devices include walkers (most stable), crutches, and canes (held on the stronger side). Gait patterns include 2-point, 3-point, 4-point, and swing-through. Weight-bearing status ranges from non-weight-bearing to full. On stairs, 'up with the good, down with the bad.'", ["Walker most stable", "Cane on strong side", "Weight-bearing status", "Up with the good, down with the bad"]),
    ch(10, "Special Equipment and Patient Care Environments", "Special environments include the ICU, with lines and tubes such as IVs, catheters, chest tubes, ventilators, and monitors. Clinicians must avoid disrupting lines and know alarms. Special beds help prevent pressure injuries.", ["ICU lines and tubes", "Don't disrupt lines", "Know monitor alarms", "Special beds"]),
    ch(11, "Basic Wound Care and Specialized Interventions", "Wound care includes cleaning, dressings, and protecting healing tissue, using sterile technique when indicated. Wounds include pressure injuries, arterial and venous ulcers, and surgical wounds. Other topics include bandaging and compression.", ["Sterile technique", "Wound types", "Dressings", "Compression"]),
    ch(12, "Incidents and Emergencies", "Clinicians must respond to falls, fainting, seizures, hypoglycemia, cardiac emergencies (CPR and AED), and bleeding. Incidents must be documented in an incident report. If a patient begins to fall, guide them safely to the floor.", ["Guide falling patient down", "CPR and AED", "Incident reports", "Hypoglycemia: give sugar"]),
    ch(13, "Americans With Disabilities Act and Environmental Assessments", "The ADA requires accessible public spaces. Standards include ramps with a 1:12 slope, doorways at least 32 inches clear, and grab bars. Home assessments find barriers and recommend modifications for safety.", ["ADA accessibility", "Ramp slope 1:12", "32-inch doorways", "Home modifications"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Before any patient care activity, you should first:", "Review the chart and plan", ["Start the activity", "Skip identification", "Ask the family to do it"], "Know the patient's condition."),
        (1, "Before treatment, the patient must be:", "Identified and informed", ["Sedated", "Left alone", "Billed"], "Get consent."),
        (2, "The most important infection control measure is:", "Hand hygiene", ["Gowns", "Masks", "Antibiotics"], "Before and after every patient."),
        (2, "Patients with C. difficile need:", "Contact precautions", ["Airborne precautions", "No precautions", "Droplet only"], "Use soap and water for hands."),
        (2, "Standard precautions apply to:", "All patients", ["Only infected patients", "Only surgery patients", "Only children"], "Treat all fluids as infectious."),
        (3, "A normal adult resting pulse is:", "60–100 bpm", ["40–50 bpm", "110–130 bpm", "150 bpm"], "Above 100 is tachycardia."),
        (3, "Vital signs are monitored during activity to:", "Judge the patient's tolerance", ["Fill time", "Bill more", "Satisfy curiosity"], "Stop if abnormal."),
        (3, "A normal adult blood pressure is below:", "120/80", ["160/100", "140/90 always", "180/110"], "Higher is elevated."),
        (3, "A normal adult respiratory rate is:", "12–20 breaths/min", ["4–8", "25–35", "40–50"], "Count for 30–60 seconds."),
    ]),
    ((4, 5, 6), [
        (4, "Good body mechanics include:", "A wide base of support", ["Feet together", "Twisting while lifting", "Locking knees"], "Improves stability."),
        (4, "When lifting, keep the load:", "Close to your body", ["At arm's length", "Above your head", "Behind you"], "Reduces strain."),
        (4, "It's usually easier and safer to:", "Push rather than pull", ["Pull rather than push", "Lift with your back", "Twist your trunk"], "Uses body weight."),
        (5, "Bedbound patients should be repositioned at least every:", "2 hours", ["8 hours", "12 hours", "24 hours"], "Prevents pressure injuries."),
        (5, "Draping is used to:", "Protect modesty and warmth", ["Restrain patients", "Hide equipment", "Prevent falls"], "Expose only the treatment area."),
        (5, "Lying face down is the:", "Prone position", ["Supine position", "Fowler's position", "Side-lying position"], "Supine is face up."),
        (6, "Range of motion done entirely by the clinician is:", "Passive ROM", ["Active ROM", "Active-assistive ROM", "Resistive exercise"], "Patient doesn't help."),
        (6, "During ROM exercises, the clinician should:", "Support the joint and move slowly", ["Move quickly", "Force past pain", "Skip support"], "Stop at resistance or pain."),
        (6, "A patient who moves with some help is doing:", "Active-assistive ROM", ["Passive ROM", "Active ROM", "Isometric exercise"], "AAROM."),
    ]),
    ((7, 8, 9), [
        (7, "Before any wheelchair transfer, you should:", "Lock the brakes", ["Remove the seat", "Tilt the chair", "Unlock the wheels"], "Prevents rolling."),
        (7, "When going down a steep ramp in a wheelchair, the patient should go:", "Backward", ["Forward quickly", "Sideways", "Without help always"], "Safer control."),
        (7, "Wheelchair users shift weight regularly for:", "Pressure relief", ["Exercise only", "Comfort only", "Speed"], "Prevents pressure injuries."),
        (8, "A belt placed around a patient's waist for safe transfers is a:", "Gait belt", ["Seat belt", "Restraint", "Binder"], "Gives a secure grip."),
        (8, "When possible, transfer a patient toward their:", "Stronger side", ["Weaker side", "Back", "Head"], "Uses their strength."),
        (8, "Dependent patients are often moved with a:", "Mechanical lift", ["Cane", "Walker", "Sliding board only"], "Protects patient and staff."),
        (9, "The most stable assistive device is the:", "Walker", ["Cane", "Crutches", "Wheelchair only"], "Wide base of support."),
        (9, "A cane is held on the:", "Stronger (uninjured) side", ["Weaker side", "Either side", "Behind the body"], "Widens base, unloads weak side."),
        (9, "On stairs, the rule is:", "Up with the good, down with the bad", ["Up with the bad, down with the good", "Always lead with the bad", "Always lead with crutches"], "Stronger leg leads going up."),
    ]),
    ((10, 11), [
        (10, "When working with ICU patients, clinicians must avoid:", "Disrupting lines and tubes", ["Monitoring vitals", "Reading the chart", "Talking to the nurse"], "IVs, catheters, chest tubes."),
        (10, "A tube that drains air or fluid from the chest is a:", "Chest tube", ["Foley catheter", "NG tube", "IV line"], "Keep the drainage unit below the chest."),
        (10, "A urinary catheter bag should be kept:", "Below the bladder", ["Above the bladder", "On the patient's chest", "On the bed rails above the patient"], "Prevents backflow."),
        (11, "Opening sterile dressings requires:", "Sterile technique", ["Clean hands only", "No gloves", "Any technique"], "Prevents infection."),
        (11, "Wounds from poor venous return in the legs are:", "Venous ulcers", ["Arterial ulcers", "Burns", "Surgical wounds"], "Often treated with compression."),
        (11, "Compression wraps are often used for:", "Venous ulcers and swelling", ["Arterial ulcers", "Fractures only", "Burns only"], "Contraindicated with poor arterial flow."),
        (10, "Special pressure-relief beds help prevent:", "Pressure injuries", ["Falls only", "Infections only", "Fractures"], "Distribute pressure."),
        (11, "Arterial ulcers are caused by:", "Poor blood flow to tissues", ["Too much blood flow", "Infection only", "Burns"], "Often painful."),
        (10, "If an ICU monitor alarms during treatment, you should:", "Check the patient and notify the nurse", ["Ignore it", "Turn it off", "Leave"], "Patient safety first."),
    ]),
    ((12, 13), [
        (12, "If a patient starts to fall during gait training, you should:", "Guide them safely to the floor", ["Try to hold them up at all costs", "Let go", "Yell for help and step away"], "Protect their head."),
        (12, "A patient with diabetes who becomes shaky and confused may need:", "Sugar", ["Insulin", "Water only", "Exercise"], "Signs of hypoglycemia."),
        (12, "After an incident like a fall, complete an:", "Incident report", ["Discharge summary", "Bill", "Consent form"], "Documents what happened."),
        (12, "For a patient in cardiac arrest, begin:", "CPR and use an AED", ["Range of motion", "Gait training", "Wound care"], "Call for help."),
        (13, "The ADA requires that public places be:", "Accessible", ["Private", "Expensive", "Closed"], "Americans with Disabilities Act."),
        (13, "The recommended ADA ramp slope is:", "1:12", ["1:2", "1:4", "1:20 only"], "1 inch rise per 12 inches."),
        (13, "ADA doorways should provide at least:", "32 inches of clear width", ["20 inches", "24 inches", "48 inches"], "For wheelchairs."),
        (13, "A home assessment identifies:", "Barriers and safety risks", ["Insurance coverage", "Family history", "Diet"], "Recommends modifications."),
        (13, "Grab bars are commonly installed in:", "Bathrooms", ["Kitchens only", "Garages", "Closets"], "Prevent falls."),
    ]),
]

BOOK = {
    "titles": ["Principles and Techniques of Patient Care"],
    "edition": "7th edition",
    "source": "Elsevier table of contents",
    "chapters": C,
    "quizzes": Q,
}
