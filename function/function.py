def find_largest(numbers):
    largest = numbers[0]        # पहला number मान लो सबसे बड़ा है
    
    for num in numbers:         # हर number check करो
        if num > largest:       # अगर current number बड़ा है
            largest = num       # तो उसे largest बना दो
    
    return largest              # सबसे बड़ा number return करो
