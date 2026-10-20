# Patient and Doctor Treatment
# Basic rule-based symptom checker for an AICA educational project.
# Educational demonstration only - not for real diagnosis or treatment.

symptom = {
    "fever": "possible_viral_illness",
    "cough": "respiratory_irritation",
    "headache": "headache_symptom",
    "stomach_pain": "digestive_discomfort",
    "cold": "common_cold"
}

advice = {
    "possible_viral_illness":
        "Rest, drink fluids, and seek medical advice if symptoms worsen.",
    "respiratory_irritation":
        "Avoid smoke and irritants. Seek medical advice if breathing is difficult.",
    "headache_symptom":
        "Rest and drink water. Seek medical advice for severe headaches.",
    "digestive_discomfort":
        "Drink fluids if appropriate and seek medical advice for severe pain.",
    "common_cold":
        "Rest, drink fluids, and monitor your symptoms."
}

def treatment_support(patient_symptom):
    condition = symptom.get(patient_symptom)
    if condition:
        suggestion = advice.get(condition)
        return condition, suggestion
    return None

def run_check(patient_symptom):
    result = treatment_support(patient_symptom)
    if result:
        condition, suggestion = result
        print("\\nInput symptom:", patient_symptom)
        print("Possible match:", condition)
        print("General suggestion:", suggestion)
        print("Safety note: This is not a diagnosis or prescription.")
    else:
        print("\\nNo example rule found for:", patient_symptom)
        print("Please consult a qualified healthcare professional.")

user_symptom = input(
    "Enter symptom (fever, cough, headache, stomach_pain, cold): "
).lower().strip().replace(" ", "_")

run_check(user_symptom)
