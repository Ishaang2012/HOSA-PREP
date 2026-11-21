# Craig - Dosage Calculations Made Easy: Solving Problems Using Dimensional Analysis (Wolters Kluwer).
# Chapter list: 8th edition (2024), from the publisher's table of contents (shop.lww.com).
# The book's practice-problem and case-study sections are not numbered chapters and are not summarized here.
# Summaries are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Arithmetic Review", "Dosage calculations rely on fractions, decimals, percentages, ratios, and proportions. Key skills: reducing fractions, multiplying and dividing fractions and decimals, converting among fractions, decimals, and percents, and rounding. Always use a leading zero (0.5, not .5) and never a trailing zero (5, not 5.0) to prevent errors.", ["Fractions, decimals, percents", "Leading zero: 0.5", "No trailing zero", "Rounding rules"]),
    ch(2, "Systems of Measurement and Common Equivalents", "The metric system is standard: 1 g = 1,000 mg; 1 mg = 1,000 mcg; 1 L = 1,000 mL; 1 kg = 2.2 lb. Household equivalents: 1 tsp = 5 mL, 1 tbsp = 15 mL, 1 oz = 30 mL, 1 cup = 240 mL, 1 inch = 2.54 cm. Apothecary units are rarely used.", ["1 g = 1,000 mg", "1 kg = 2.2 lb", "1 tsp = 5 mL; 1 tbsp = 15 mL", "1 oz = 30 mL"]),
    ch(3, "Solving Problems Using Dimensional Analysis", "Dimensional analysis sets up a problem as a chain of conversion factors so unwanted units cancel, leaving the desired unit. Steps: identify the given quantity and wanted unit, write conversion factors as fractions, cancel units, then multiply and divide.", ["Units cancel", "Conversion factors as fractions", "Start with the given", "End with the wanted unit"]),
    ch(4, "One-Factor Medication Problems", "One-factor problems involve a single given quantity, such as converting a dose ordered in grams to milligrams, or calculating tablets or milliliters to give: amount to give = dose ordered ÷ dose on hand × quantity.", ["Tablets to give", "mL to give", "Unit conversions", "D/H × Q"]),
    ch(5, "Two-Factor Medication Problems", "Two-factor problems add a second variable, often body weight (mg/kg) or time. Example: 5 mg/kg for a 44-lb child = 20 kg × 5 mg = 100 mg. IV infusion rates in mL/hr also use two factors.", ["Weight-based dosing", "Convert lb to kg first", "mL/hr rates", "Check safe dose range"]),
    ch(6, "Three-Factor Medication Problems", "Three-factor problems combine dose, weight, and time—such as mcg/kg/min infusions—or calculate IV drip rates in gtt/min using the drop factor: gtt/min = volume (mL) × drop factor (gtt/mL) ÷ time (min).", ["mcg/kg/min", "gtt/min formula", "Drop factor", "Multiple conversions"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Which is the correct way to write one-half milligram?", "0.5 mg", [".5 mg", "0.50 mg", "1/2.0 mg"], "Always use a leading zero."),
        (1, "Trailing zeros (5.0 mg) are avoided because they:", "Can be misread as 50 mg", ["Are too precise", "Look unprofessional", "Are required by law"], "Ten-fold error risk."),
        (1, "0.25 as a fraction is:", "1/4", ["1/2", "1/3", "2/5"], "25/100 reduced."),
        (2, "1 gram equals:", "1,000 mg", ["100 mg", "10 mg", "10,000 mg"], "Metric conversion."),
        (2, "1 kilogram equals about:", "2.2 lb", ["1 lb", "5 lb", "10 lb"], "Divide lb by 2.2 to get kg."),
        (2, "1 teaspoon equals:", "5 mL", ["15 mL", "30 mL", "1 mL"], "1 tbsp = 15 mL."),
        (2, "1 fluid ounce equals:", "30 mL", ["5 mL", "15 mL", "240 mL"], "1 cup = 240 mL."),
        (3, "In dimensional analysis, conversion factors are arranged so that:", "Unwanted units cancel", ["All units remain", "Numbers are added", "Units are ignored"], "Leaves the wanted unit."),
        (3, "1 mg equals:", "1,000 mcg", ["100 mcg", "10 mcg", "0.1 mcg"], "Micrograms."),
    ]),
    ((4, 5, 6), [
        (4, "Ordered: 500 mg. On hand: 250 mg tablets. Give:", "2 tablets", ["1 tablet", "0.5 tablet", "4 tablets"], "500 ÷ 250."),
        (4, "Ordered: 0.5 g. On hand: 250 mg tablets. Give:", "2 tablets", ["1 tablet", "0.5 tablet", "5 tablets"], "0.5 g = 500 mg."),
        (4, "Ordered: 50 mg. On hand: 25 mg/mL. Give:", "2 mL", ["0.5 mL", "1 mL", "5 mL"], "50 ÷ 25 × 1 mL."),
        (5, "A child weighs 44 lb. Their weight in kg is:", "20 kg", ["44 kg", "10 kg", "97 kg"], "44 ÷ 2.2."),
        (5, "Order: 5 mg/kg for a 20-kg child. Dose =", "100 mg", ["25 mg", "4 mg", "200 mg"], "5 × 20."),
        (5, "1,000 mL to infuse over 8 hours. Rate =", "125 mL/hr", ["100 mL/hr", "80 mL/hr", "250 mL/hr"], "1,000 ÷ 8."),
        (6, "The formula for drip rate is volume × drop factor ÷:", "Time in minutes", ["Time in hours", "Weight", "Dose"], "gtt/min."),
        (6, "100 mL over 60 min with a 15 gtt/mL set =", "25 gtt/min", ["15 gtt/min", "60 gtt/min", "100 gtt/min"], "100 × 15 ÷ 60."),
        (6, "Doses ordered in mcg/kg/min require factors for dose, weight, and:", "Time", ["Height", "Age", "Temperature"], "Three-factor problems."),
    ]),
]

BOOK = {
    "titles": ["Dosage Calculations Made Easy"],
    "edition": "8th edition (2024)",
    "source": "Wolters Kluwer table of contents",
    "chapters": C,
    "quizzes": Q,
}
