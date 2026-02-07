def register_issue(issue_name, description, suspected_cause):
    """
    Register a recurring issue during test operations.
    """
    return {
        "issue": issue_name,
        "description": description,
        "suspected_cause": suspected_cause
    }
