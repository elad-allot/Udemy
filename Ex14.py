"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
#


def get_questions():
    try:
        questions_file = open('questions.txt', 'r')
    except FileNotFoundError:
        print("We Lost the Test you get a 100!!!")
        raise FileNotFoundError
    else:
        questions = (questions_file.readlines())
        questions_file.close()
        return [q.strip().split('=') for q in questions]


def publish_grade(correct_answers, number_of_questions):
    publish_message = 'Your final score is %s/%s.' % (correct_answers, number_of_questions)
    output_file = open('result.txt', 'w')
    output_file.write(publish_message)
    print(publish_message)


def quiz():
    corr = 0
    # num_of_questions = 0
    try:
        questions = get_questions()
        num_of_questions = len(questions)
    except FileNotFoundError:
        # corr = 0
        num_of_questions = 0
    else:
        for q in questions:
            ans = input('%s=' % q[0])
            if ans == q[1]:
                corr += 1
    finally:
        publish_grade(corr, num_of_questions)


quiz()
