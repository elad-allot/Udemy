meeting_list = [(1, 10), (2, 6), (3, 5), (7, 9)]


def merge_ranges(meetings):
    merged_meetings = []
    meetings.sort()
    print(meetings)
    start = meetings[0][0]
    end = meetings[0][1]
    for i in range(1, len(meetings)):
        if start <= meetings[i][0] <= end <= meetings[i][1]:
            end = meetings[i][1]
        elif start <= meetings[i][0] <= end:
            continue
        else:
            merged_meetings.append((start, end))
            start = meetings[i][0]
            end = meetings[i][1]
    merged_meetings.append((start, end))
    return merged_meetings


print(merge_ranges(meeting_list))
