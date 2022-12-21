class GuessNumber:
    '''
    Guess number game
    '''
    def __init__(self, answer: int) -> None:
        self.answer = answer

    def main(self):
        from random import randint

        print('Guess a number between 1 and 100')
        guess = int(input('Enter your guess: '))
        while guess != self.answer:
            if guess < self.answer:
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
    print(f'π is approximately {calculate_pi(100)}', end='\n')
    guessNumber = GuessNumber(39)
    guessNumber.main()
