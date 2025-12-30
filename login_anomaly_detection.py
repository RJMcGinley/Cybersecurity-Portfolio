def analyze_logins(username, current_day_logins, average_day_logins,
                   extra_threshold=2, multiplier_threshold=1.5):
    """
    Analyze login activity for a user and determine whether it exceeds
    normal behavior based on historical averages.

    Detection logic:
    - Requires activity to exceed the user's average by an absolute amount
      (a fixed number of additional logins)
    - Requires activity to exceed the user's average by a multiplier
      (a proportional increase)

    This dual condition helps reduce false positives from normal variance.
    """

    # Guard against divide-by-zero / new-user scenarios
    if average_day_logins == 0:
        return current_day_logins > 0

    extra_logins = current_day_logins - average_day_logins
    login_ratio = current_day_logins / average_day_logins

    return (extra_logins >= extra_threshold) and (login_ratio >= multiplier_threshold)


if __name__ == "__main__":
    # Example values for demonstration; in practice these would come from logs.
    user = "ejones"
    current_day_logins = 9
    average_day_logins = 3

    if analyze_logins(user, current_day_logins, average_day_logins):
        print(f"ALERT: {user} shows abnormal login activity")
    else:
        print(f"OK: {user} login activity is within normal range")
