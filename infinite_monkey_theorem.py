import random


def generate_alphabets():
    alphabets = []
    alpha = 'a'
    for i in range(0, 26):
        alphabets.append(alpha)
        alpha = chr(ord(alpha) + 1)
    alphabets.append(" ")
    return alphabets


def choose_random_alphabet(alphabets):
    random_number = random.randrange(27)
    return alphabets[random_number]


def main():
    expected_string = 'methinks it is like a weasel'
    string_len = len(expected_string)
    alphabets = generate_alphabets()
    current_max_score = 0
    result_list = []
    result = ''
    iteration = 0
    while current_max_score < 1:
        iteration += 1
        for i in range(string_len):
            result_list += choose_random_alphabet(alphabets)
        result = "".join(result_list)
        result_list.clear()
        iteration_score = generate_score(expected_string, result)
        if iteration_score > current_max_score:
            current_max_score = iteration_score
            print(f'Iteration Number: {iteration}')
            print(f'Iteration Score: {iteration_score}')
            print(result + '\n')
    print('Match found')
    print(result)


def generate_score(expected, obtained):
    score = 0
    for i in range(len(expected)):
        if expected[i] == obtained[i]:
            score += 1
    return score/len(expected)

main()