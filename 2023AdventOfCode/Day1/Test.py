import re

def find_last_word_from_number(input_string):
    matches = re.findall(r'\b\d+\b', input_string)
    
    if matches:
        last_number = matches[-1]
        return re.search(r'\b\w+\b', input_string[:input_string.rindex(last_number)]).group()
    else:
        return None

# Test string
test_string = "The price is $100 for product A and $200 for product B"

result = find_last_word_from_number(test_string)

if result:
    print(f'Last word from a number: {result}')
else:import re

def find_last_word_from_number_string(input_string):
    number_word_mapping = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",  # Add more mappings as needed
    }

    matches = re.findall(r'\b\d+\b', input_string)

    if matches:
        last_number = matches[-1]
        corresponding_word = number_word_mapping.get(last_number)
        return corresponding_word

    return None

# Test string
test_string = "The price is $100 for product one and $200 for product five"

result = find_last_word_from_number_string(test_string)

if result:
    print(f'Last word from a number: {result}')
else:
    print('No number found.')

    print('No number found.')