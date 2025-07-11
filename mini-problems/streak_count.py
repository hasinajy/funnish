# Parameters
MAX_MISS_COUNT = 0

# Data
streak_data = [1, 1, 0, 1, 1, 0, 0]
consecutive_misses = 0

# Current streak
current_streak = 0
current_streak_total = 0

# Longest streak
longest_streak = 0
longest_streak_total = 0

for streak_value in streak_data:
    if consecutive_misses > MAX_MISS_COUNT:
        if current_streak > longest_streak:
            longest_streak = current_streak
            longest_streak_total = current_streak_total
        current_streak = 0
        current_streak_total = 0

    if streak_value != 0:
        current_streak += 1
        current_streak_total += streak_value
        consecutive_misses = 0
    else:
        consecutive_misses += 1

print("Current streak:", current_streak)
print("Current streak total:", current_streak_total)
print("Longest streak:", longest_streak)
print("Longest streak total:", longest_streak_total)
