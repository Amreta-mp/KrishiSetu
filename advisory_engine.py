def generate_advice(query):
    if "paddy" in query.lower():
        return "For paddy, ensure timely irrigation and monitor rust disease."
    elif "yellow leaves" in query:
        return "Yellowing leaves may be due to nitrogen deficiency. Apply urea."
    else:
        return "Please provide more details or upload an image."
