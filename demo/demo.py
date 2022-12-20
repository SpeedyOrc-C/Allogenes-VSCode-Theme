class GuessNumber:
    '''
    Guess number game
    '''
    def __init__(self, upper_bound: int) -> None:
        self.upper_bound = upper_bound

    def main(self):
        from random import randint

        print('Guess a number between 1 and 100')
        number = randint(1, self.upper_bound)
        guess = int(input('Enter your guess: '))
        while guess != number:
            if guess < number:
                print('Too low')
            else:
                print('Too high')
            guess = int(input('Enter your guess: '))
        print('You guessed it!')


def calculate_pi(iter: int) -> float:
    '''
    Calculate π using the Leibniz formula
    '''
    result = 0
    for i in range(1, iter+1):
        result += 1 / (i**2)
    return (result * 6) ** 0.5


if __name__ == '__main__':
    print(f'π is approximately {calculate_pi(1000)}', end='\n')
    guessNumber = GuessNumber()
    guessNumber.main()
