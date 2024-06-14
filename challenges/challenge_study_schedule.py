def valid_period(period):
    return isinstance(period, tuple) and len(
        period) == 2 and all(isinstance(time, int) for time in period)


def student_present(period, target_time):
    start, end = period
    return start <= target_time <= end


def study_schedule(permanence_period, target_time):
    if target_time is None or any(not valid_period(period)
                                  for period in permanence_period):
        return None
    return sum(student_present(period, target_time)
               for period in permanence_period)
