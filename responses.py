import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello' :
        return 'hello! gamer'

    if p_message == 'what is your address' :
        return  'you little psycho'

    if message == 'roll' :
        return str(random.randint(0, 999))

    if p_message == 'what do you like to do':
        return 'jump rope, coding, mucking and watch Dani\'s video!'

    if p_message == 'how old are you':
        return '13 years old'

    if p_message == 'what food do you like':
        return 'mango and donut!'

    if p_message == 'hello fellow scratchers':
        return 'no way! want me to spam?'

    if p_message == 'what your favorite programming language':
        return 'Scratch, Csharp and Python, it is easy to learn!'

    if p_message == 'can you code':
        return '`print(\'Hello World \')`'

    if p_message == 'when will maryo done':
        return 'hmm.... maybe December'

    if p_message == 'what is your scratch account':
        return 'https://scratch.mit.edu/users/NecoDevloport'

    return 'sorry, I don\'t know what are you talking about'
