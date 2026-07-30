def hiring_decision(score):
    if score >= 80:
        return "Selected"
    elif score >= 65:
        return "Hold for Review"
    else:
        return "Rejected"