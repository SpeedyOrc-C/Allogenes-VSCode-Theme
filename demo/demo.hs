input :: String -> IO String
input prompt = do
    putStr prompt
    getLine

guessNumber :: Integer -> IO ()
guessNumber number = do
    putStrLn "Guess a number between 1 and 100"
    guessNumber' number
    where
    
    guessNumber' :: Integer -> IO ()
    guessNumber' number = do
        guess <- read <$> input "Enter your guess: "
        if guess /= number then do
            if guess < number then
                print "Too low"
            else
                print "Too high"
            guessNumber' number
        else
            putStrLn "You guessed it!"

main = do
    guessNumber 39
