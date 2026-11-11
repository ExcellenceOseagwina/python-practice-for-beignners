# LESSON: Check scores, add them, and choose a risk level
# int() changes each answer into a whole number. Enter whole numbers from 1 to 5.

vulnerability_name = input("Enter vulnerability name: ")

severity = int(input("Enter severity score (1-5): "))
likelihood = int(input("Enter likelihood score (1-5): "))
impact = int(input("Enter impact score (1-5): "))

# None means a score or risk level has not been chosen yet. The program fills
# these in after checking the answers.
risk_score = None
risk_level = None
risk_message = None

# `or` means any one score outside 1 to 5 makes this check true. Parentheses
# let the long check continue on several lines.
if (
    severity < 1
    or severity > 5
    or likelihood < 1
    or likelihood > 5
    or impact < 1
    or impact > 5
):
    risk_message = f"""
=============================================
        Vulnerability Assessment Report
=============================================

Assessment Factor         Score
Vulnerability Name        {vulnerability_name}
Severity Score            {severity}
Likelihood Score:         {likelihood}
Impact Score:             {impact}
Total Risk Score:         {"??"}/15
Risk Classification:       Nothing to classify since the scores are either less than 1 or above 5

===============================================
"""
else:
    # Add the three valid scores. Their total can be from 3 to 15. The choices
    # below use that total to select a risk level.

    risk_score = severity + likelihood + impact
    if risk_score <= 5:
        risk_level = "Low"
        risk_message = f"""
=============================================
        Vulnerability Assessment Report ✅
=============================================

Assessment Factor         Score
Vulnerability Name        {vulnerability_name}
Severity Score            {severity}
Likelihood Score:         {likelihood}
Impact Score:             {impact}
Total Risk Score:         {risk_score}/15
Risk Classification:       {risk_level}

===============================================
"""
    elif risk_score <= 8:
        risk_level = "Medium"
        risk_message = f"""
=============================================
        Vulnerability Assessment Report ⚠️
=============================================

Assessment Factor         Score
Vulnerability Name        {vulnerability_name}
Severity Score            {severity}
Likelihood Score:         {likelihood}
Impact Score:             {impact}
Total Risk Score:         {risk_score}/15
Risk Classification:       {risk_level}

===============================================

"""
    elif risk_score <= 12:
        risk_level = "High"
        risk_message = f"""
=============================================
        Vulnerability Assessment Report 🚨
=============================================

Assessment Factor         Score
Vulnerability Name        {vulnerability_name}
Severity Score            {severity}
Likelihood Score:         {likelihood}
Impact Score:             {impact}
Total Risk Score:         {risk_score}/15
Risk Classification:       {risk_level}

===============================================
"""
    elif risk_score <= 15:
        risk_level = "Critical"
        risk_message = f"""
=============================================
        Vulnerability Assessment Report 💀
=============================================

Assessment Factor         Score
Vulnerability Name        {vulnerability_name}
Severity Score            {severity}
Likelihood Score:         {likelihood}
Impact Score:             {impact}
Total Risk Score:         {risk_score}/15
Risk Classification:       {risk_level}

===============================================
"""
    # Note: A code can run without an else. Else is like a fallback. This is normal not only to python but to all other programming languages like Javascript and the rest.
    # else:
    #     print("You!")

# Display the assessment report, including the validation message if needed.
print(risk_message)
