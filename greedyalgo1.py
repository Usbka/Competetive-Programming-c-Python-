
def activity_selection(start, finish):
    n = len(start)

    activities = []

    for i in range(n):
        activities.append((finish[i], start[i], i + 1))

    activities.sort()

    selected = []
    last_finish = 0

    for f, s, activity in activities:
        if s >= last_finish:
            selected.append(activity)
            last_finish = f

    return selected


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

print(activity_selection(start, finish))
