import hashing
import string
import random

# Generates a deterministic, complex password from a given input string
# input: the input string to hash
# length: the length of the output password
# use_upper: whether to include uppercase characters in the password
# use_numbers: whether to include numbers in the password
# use_special: whether to include special characters in the password
# return: the generated password

def hashpass(input, length=10, use_upper=True, use_numbers=True, use_special=True):
    # Check if input is empty
    if not input:
        raise ValueError("Input string cannot be empty")
    
    if not length:
        raise ValueError("Password length cannot be empty")

    # check if length is valid integer
    if not isinstance(length, int):
        raise ValueError("Length must be an integer")
    
    hashres = hashing.hash_string(input)

    
    # Define character pools
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_upper else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = "!@#$%^&*" if use_special else ''
    
    character_pool = {
        "lower": lower_chars,
        "upper": upper_chars,
        "number": number_chars,
        "special": special_chars
    }
    
    # Create a shuffled index list based on the hashres
    random.seed(hashres)
    index_list = list(range(len(character_pool)))
    random.shuffle(index_list)
    
    # Modified to hashres to include one character from each pool while keeping the length constant
    # every four character, we will insert a character from one pool
    # the pool will be shuffled based on the hashres
    secure_password = []
    for i in range(length):
        pool_index = index_list[i % len(index_list)]
        pool = character_pool[list(character_pool.keys())[pool_index]]
        if len(pool) == 0:
            secure_password.append(random.choice(lower_chars))
        else:
            secure_password.append(random.choice(pool))
    
    
    return ''.join(secure_password)

if __name__ == "__main__":
    # user_password = input("Enter your base password: ")
    # length = int(input("Enter desired password length: "))
    # while length < 4:
    #     print("Password length must be at least 4 characters")
    #     length = int(input("Enter desired password length: "))
    # use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    # use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    # use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # secure_password = hashpass(user_password, length, use_upper, use_numbers, use_special)
    secure_password = hashpass("mysecret", 10, True, True, True)
    print(f"Generated Secure Password: {secure_password}")
    