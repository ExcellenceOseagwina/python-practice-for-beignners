# Collect the vulnerability details and three 1-5 assessment scores.

vulnerability_name = input("Enter vulnerability name: ")

severity = int(input("Enter severity score (1-5): "))
likelihood = int(input("Enter likelihood score (1-5): "))
impact = int(input("Enter impact score (1-5): "))

# Keep the report unset until the scores have been validated and assessed.
risk_score = None
risk_level = None
risk_message = None

# Reject scores outside the supported range before calculating a risk score.
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
    # Add the valid scores, then select the matching risk classification.

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
