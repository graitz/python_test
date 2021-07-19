print ('*******************************')
print ('Welcome the riddle game')
print ('*******************************')

secret_number = 42

kicked_str = input ('Type your number here:')

print ('You type', kicked_str)

kicked = int (kicked_str)

hit = secret_number == kicked

missed_up = kicked > secret_number
missed_donw = kicked < secret_number

if (hit):
    print ('You win!')
else:
    if (missed_up):
        print ('You missed! Your kick was bigger than the secret number')
    elif (missed_donw):
        print ('You missed! Your kick was less than the secret number')
    print ('You lose!')

print ('The end')
