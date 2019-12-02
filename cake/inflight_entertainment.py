movie_lengths = [2, 4]

def can_two_movies_fill_flight_brute_force(movie_lengths, flight_length):
    for i in range(len(movie_lengths)):
        for j in range(len(movie_lengths)):
            if i != j and movie_lengths[i] + movie_lengths[j] == flight_length:
                return True
    return False




def can_two_movies_fill_flight_allot_of_mem(movie_lengths, flight_length):
    temp_list = [flight_length] * len(movie_lengths)
    temp_set = {}
    for i in range(len(movie_lengths)):
        temp_list[i] -= movie_lengths[i]
        temp_set.add(movie_lengths[i])
    for i in range(len(movie_lengths)):
        if temp_list[i] in temp_set:
            return True
    return False



def can_two_movies_fill_flight_brute_force(movie_lengths, flight_length):
    pos_sec_film = set()

    for movie in movie_lengths:
        time_left = flight_length - movie
        if time_left in pos_sec_film:
            return True
        pos_sec_film.add(movie)
    return False

print(can_two_movies_fill_flight_brute_force(movie_lengths, 6))