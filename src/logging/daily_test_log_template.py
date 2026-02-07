from datetime import date

def create_daily_test_log(test_objective, environment, observations, issues):
    """
    Create a standardized daily test log entry.
    """
    log = {
        "date": date.today().isoformat(),
        "objective": test_objective,
        "environment": environment,
        "observations": observations,
        "issues": issues
    }
    return log
