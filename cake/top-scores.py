unsorted_scores = [37, 89, 41, 65, 91, 37, 53]
HIGHEST_POSSIBLE_SCORE = 100


def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    my_dict = {}
    for score in unsorted_scores:
        my_dict[score] = (my_dict.get(score) or 0) + 1

    sorted = []
    for i in range(HIGHEST_POSSIBLE_SCORE):
        sorted = sorted + [i] * (my_dict.get(i) or 0)
    return sorted



def sort_scores2(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score + 1)

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        for time in range(count):
            # Add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores




print(sort_scores2(unsorted_scores,HIGHEST_POSSIBLE_SCORE))












