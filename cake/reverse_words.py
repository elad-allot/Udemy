



def reverse(list_of_chars):
    end_of = len(list_of_chars) - 1
    start_of = 0
    while start_of < end_of:
        # cup = list_of_chars[start_of]
        list_of_chars[start_of], list_of_chars[end_of] = list_of_chars[end_of],  list_of_chars[start_of]
        # list_of_chars[end_of] = cup
        end_of -= 1
        start_of += 1
    return list_of_chars

def reverse_words(message):
    # Decode the message by reversing the words

    message = reverse(message)
    start_index = 0
    for i in range(len(message)):
        if i == len(message) - 1 or message[i + 1] == ' ':
            end_index = i
            while start_index < end_index:
                message[start_index], message[end_index] = message[end_index], message[start_index]
                start_index += 1
                end_index -= 1

            start_index = i + 2

    return message

print(reverse_words(list('thief cake')))





