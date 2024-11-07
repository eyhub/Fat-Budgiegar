import random

def random_number_generator(min, max):
    """
    Generate a random number (integer) between parameters min and max.

    Parameters
    ----------
    min : int
        minimum value the random integer can take.
    max : int
        maximum value the random integer can take.

    Returns
    ----------
    int
        A random integer between min and max.
    """
    return random.randint(min, max)

def random_operator_generator():
    """
    Generate a random operator from the choices of '+', '-', '*'.

    Returns
    -------
    str
        Random operator from the initial set: '+', '-', '*'.
    """
    return random.choice(['+', '-', '*'])

def expression_generator(param1, param2, operator):
    """
    Calculate the result of an arithmetic expression.

    Parameters
    ----------
    param1 : int or float
        The first number in the expression.
    param2 : int or float
        The second number in the expression.
    operator : str
        The operator for the calculation, expected values are '+', '-', or '*'.

    Returns
    -------
    tuple
        A tuple containing:
        - expression (str): A string representation of the problem.
        - result (int or float): The result of the arithmetic operation.

    Raises
    ------
    ValueError
        If an unsupported operator is provided.
    """
    # Create the string representation of the expression
    expression = f"{param1} {operator} {param2}"

    # Perform the operation based on the specified operator
    if operator == '+': 
        result = param1 + param2
    elif operator == '-': 
        result = param1 - param2
    elif operator == '*': 
        result = param1 * param2
    else:
        # Raise an error if the operator is unsupported
        raise ValueError("Unexpected operator. Use '+', '-', or '*'.")

    return expression, result

def math_quiz():
    """
    Starts an arithmetic quiz game for the user.

    The quiz provides a set number of random arithmetic questions, 
    evaluates the user's answers, and keeps track of the score. For 
    each question answered correctly, the user earns one point. At 
    the end, the function displays the user's score out of the total 
    number of questions.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the user provides a non-integer answer input.
    """
    score = 0
    number_of_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers in integers only.\n")

    for _ in range(number_of_questions):
        # Generate two random numbers and a random operator for the expression
        n1 = random_number_generator(1, 10)
        n2 = random_number_generator(1, 5)
        o = random_operator_generator()

        # Create the math problem and calculate the correct answer
        problem, answer = expression_generator(n1, n2, o)
        
        # Loop until the user provides a valid integer answer
        while True:
            print(f"\nQuestion: {problem}")
            print("Please enter your answer as an integer.")
            
            try:
                user_answer = int(input("Your answer: "))
                break  # Exit loop if user enters a valid integer
            except ValueError:
                print("Invalid input. Please enter an integer only.")

        # Check if the user's answer matches the correct answer
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{number_of_questions}")

if __name__ == "__main__":
    math_quiz()
