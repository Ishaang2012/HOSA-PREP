# Rewald, Lorang & Schramm - Pharmacy Calculations: An Introduction for Pharmacy Technicians (ASHP).
# Chapter list supplied by the site owner (not verified against the publisher). Summaries are written for this site.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Fundamentals of Math", "Core skills: place value, rounding, order of operations, and estimation. Always use a leading zero (0.5) and never a trailing zero (5, not 5.0). Estimating first helps catch errors.", ["Place value", "Rounding", "Leading zero", "No trailing zero"]),
    ch(2, "Fractions and Decimals", "Work with proper and improper fractions, mixed numbers, and decimals: reduce, add, subtract, multiply, divide, and convert between forms (3/4 = 0.75).", ["Reduce fractions", "Mixed numbers", "Fraction to decimal", "Operations"]),
    ch(3, "Ratios, Proportions, and Percents", "A ratio compares two quantities (1:4); a proportion sets two ratios equal and is solved by cross-multiplying. Percent means per 100; convert among percents, decimals, and fractions.", ["Ratios", "Cross-multiplication", "Percent = per 100", "Conversions among forms"]),
    ch(4, "Systems of Measurement", "Pharmacy uses the metric system (grams, liters, meters), with household (teaspoon, tablespoon, ounce) and older apothecary units occasionally seen. Metric prefixes: kilo = 1,000, milli = 1/1,000, micro = 1/1,000,000.", ["Metric system", "Metric prefixes", "Household units", "Apothecary units"]),
    ch(5, "Conversions", "Common conversions: 1 kg = 2.2 lb; 1 g = 1,000 mg; 1 mg = 1,000 mcg; 1 L = 1,000 mL; 1 tsp = 5 mL; 1 tbsp = 15 mL; 1 fl oz ≈ 30 mL; 1 in = 2.54 cm; °C = (°F − 32) ÷ 1.8.", ["1 kg = 2.2 lb", "1 g = 1,000 mg", "1 tsp = 5 mL", "Temperature conversion"]),
    ch(6, "Interpretation of Prescriptions and Medication Orders", "Read prescriptions for patient, drug, strength, dose, route, frequency, quantity, and refills. Know abbreviations (bid, tid, qid, q6h, prn, po) and avoid error-prone ones (U, QD, trailing zeros).", ["Prescription parts", "Sig abbreviations", "Error-prone abbreviations", "Refills"]),
    ch(7, "Dosage Calculations", "Calculate amount to dispense with (desired ÷ have) × quantity or dimensional analysis; compute days' supply, quantity to dispense, and weight-based (mg/kg) and BSA-based doses.", ["D/H × Q", "Days' supply", "mg/kg dosing", "Quantity to dispense"]),
    ch(8, "Concentrations and Dilutions", "Concentrations are expressed as percent (w/v = g/100 mL), ratio strength (1:1,000), or mg/mL. Dilutions use C1V1 = C2V2. Reconstitution adds diluent to powders.", ["% w/v", "Ratio strength", "C1V1 = C2V2", "Reconstitution"]),
    ch(9, "Alligation", "Alligation finds how much of a higher and lower strength to mix to get a desired strength. Subtract across a grid to find parts of each component.", ["Higher and lower strengths", "Parts of each", "Alligation grid", "Check the answer"]),
    ch(10, "Parenteral and Intravenous Calculations", "IV calculations include flow rates (mL/hr), drip rates (gtt/min = volume × drop factor ÷ minutes), infusion time, and dose-based rates (mcg/kg/min). Electrolytes may be in mEq.", ["mL/hr", "gtt/min formula", "Infusion time", "mEq"]),
    ch(11, "Business Math in Pharmacy", "Business math includes markup, gross and net profit, discounts, average wholesale price, dispensing fees, inventory turnover, and insurance reimbursement calculations.", ["Markup", "Gross vs. net profit", "AWP", "Inventory turnover"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Which is written correctly?", "0.5 mg", [".5 mg", "0.50 mg", "5.0 mg"], "Leading zero, no trailing zero."),
        (1, "5.0 mg could be misread as:", "50 mg", ["0.5 mg", "5 mcg", "500 mg"], "Avoid trailing zeros."),
        (1, "Rounding 2.46 to the nearest tenth gives:", "2.5", ["2.4", "2.0", "3.0"], "6 rounds up."),
        (2, "3/4 as a decimal is:", "0.75", ["0.34", "0.43", "1.33"], "3 ÷ 4."),
        (2, "2 1/2 as an improper fraction is:", "5/2", ["3/2", "7/2", "2/5"], "2 × 2 + 1."),
        (2, "6/8 reduced is:", "3/4", ["2/3", "1/2", "6/4"], "Divide by 2."),
        (3, "25% as a decimal is:", "0.25", ["2.5", "25", "0.025"], "Divide by 100."),
        (3, "If 2 tablets contain 500 mg, 6 tablets contain:", "1,500 mg", ["1,000 mg", "3,000 mg", "750 mg"], "Proportion."),
        (3, "Solve x/10 = 3/5:", "6", ["5", "3", "15"], "Cross-multiply."),
    ]),
    ((4, 5, 6), [
        (4, "The prefix milli- means:", "One-thousandth", ["One thousand", "One-millionth", "One hundred"], "1 mL = 0.001 L."),
        (4, "The prefix micro- means:", "One-millionth", ["One-thousandth", "One thousand", "One-hundredth"], "mcg."),
        (4, "The standard system of measurement in pharmacy is:", "Metric", ["Apothecary", "Household", "Avoirdupois only"], "Most accurate."),
        (5, "1 kg equals:", "2.2 lb", ["1 lb", "10 lb", "0.45 lb"], "Divide lb by 2.2."),
        (5, "1 tablespoon equals:", "15 mL", ["5 mL", "30 mL", "10 mL"], "3 teaspoons."),
        (5, "98.6°F in Celsius is:", "37°C", ["32°C", "40°C", "100°C"], "(98.6 − 32) ÷ 1.8."),
        (6, "'tid' means:", "Three times a day", ["Twice a day", "Four times a day", "Every 3 hours"], "Latin ter in die."),
        (6, "'prn' means:", "As needed", ["By mouth", "Before meals", "At bedtime"], "Pro re nata."),
        (6, "Writing 'U' for units is avoided because it can be misread as:", "0 or 4", ["mL", "mg", "IU"], "Write 'units.'"),
    ]),
    ((7, 8, 9), [
        (7, "Order: 500 mg; have 250 mg tablets. Give:", "2 tablets", ["1 tablet", "0.5 tablet", "4 tablets"], "500 ÷ 250."),
        (7, "Order: 5 mg/kg for a 30-kg child. Dose =", "150 mg", ["35 mg", "6 mg", "300 mg"], "5 × 30."),
        (7, "60 tablets taken 2 daily last:", "30 days", ["60 days", "15 days", "120 days"], "Days' supply."),
        (8, "A 5% w/v solution contains:", "5 g per 100 mL", ["5 mg per mL", "5 g per L", "50 g per 100 mL"], "Percent w/v."),
        (8, "Ratio strength 1:1,000 equals:", "1 g in 1,000 mL", ["1 mg in 1,000 mL", "10 g in 100 mL", "1 g in 100 mL"], "= 0.1%."),
        (8, "How much 10% stock makes 100 mL of 2%?", "20 mL", ["10 mL", "50 mL", "2 mL"], "C1V1 = C2V2."),
        (9, "Alligation is used to:", "Mix two strengths to reach a desired strength", ["Calculate IV rates", "Convert units", "Find profit"], "Grid method."),
        (9, "To make 15% from 20% and 10%, you need parts in ratio:", "5 parts 20% : 5 parts 10%", ["10:5", "5:10", "15:5"], "Differences: 15−10=5, 20−15=5."),
        (9, "In alligation, the desired strength must be:", "Between the two available strengths", ["Higher than both", "Lower than both", "Equal to one"], "Otherwise impossible."),
    ]),
    ((10, 11), [
        (10, "1,000 mL over 8 hours runs at:", "125 mL/hr", ["100 mL/hr", "80 mL/hr", "250 mL/hr"], "1,000 ÷ 8."),
        (10, "100 mL over 1 hour with a 15 gtt/mL set is:", "25 gtt/min", ["15 gtt/min", "60 gtt/min", "100 gtt/min"], "100 × 15 ÷ 60."),
        (10, "500 mL at 100 mL/hr takes:", "5 hours", ["2 hours", "50 hours", "10 hours"], "500 ÷ 100."),
        (10, "Electrolytes such as potassium are often measured in:", "mEq", ["mg only", "Units", "gtt"], "Milliequivalents."),
        (11, "Selling price minus cost is the:", "Markup (gross profit)", ["Net profit", "Discount", "AWP"], "Before expenses."),
        (11, "Net profit is gross profit minus:", "Operating expenses", ["Cost of goods only", "Markup", "AWP"], "True profit."),
        (11, "A benchmark price used in drug reimbursement is the:", "Average wholesale price", ["Copay", "Deductible", "Markup"], "AWP."),
        (11, "How often inventory is sold and replaced is:", "Inventory turnover", ["Markup", "Days' supply", "Gross profit"], "Higher is efficient."),
        (11, "A 10% discount on a $50 item makes it:", "$45", ["$40", "$49", "$55"], "50 × 0.9."),
    ]),
]

BOOK = {
    "titles": ["Pharmacy Calculations: An Introduction for Pharmacy Technicians"],
    "edition": "Edition not verified; chapter list supplied by the site owner",
    "source": "Chapter list supplied by the site owner",
    "chapters": C,
    "quizzes": Q,
}
