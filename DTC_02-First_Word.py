# Functions
def string_check(question, valid_ans_list):
    """Checks that users enter the full word or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

# Main Routine

levels = ['easy', 'medium', 'hard']

like_coffee = string_check(question= "Do you like coffee? ", valid_ans_list= ['yes', 'no']
print(f"You chose {like_coffee}")
choose_level = string_check(question="Choose a Level: ", valid_ans_list= levels)
print(f"You chose {choose_level}")

