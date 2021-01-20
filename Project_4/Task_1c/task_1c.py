import random

def simulation():
    """
    This function simulates the slot machine with the initial coins numer as 10. It will finally return 
    number of play times.
    """
    coins = 10
    play_num = 0
    while coins >= 1:
        coins -= 1
        # print(coins)
        play_num += 1
        # print(play_num)
        slots = []
        i = 0
        for i in range(3):
            single_slot = random.choice(["BELL", "BAR", "LEMON", "CHERRY", "BLANK", "BLANK", "BLANK", "BLANK"])
            slots.append(single_slot)
        if slots[0] == slots[1] and slots[1] == slots[2]:
            if slots[0] == "BAR":
                coins += 20
            elif slots[0] == "BELL":
                coins += 15
            elif slots[0] == "LEMON":
                coins += 5
            elif slots[0] == "CHERRY":
                coins += 3
        elif slots.count("CHERRY") == 2:
            coins += 2
        elif slots.count("CHERRY") == 1:
            coins += 1
    # print(play_num)
    return play_num

def test(trial_number):
    """
    In this test function, we iterate trial_number times to calculate the mean and median of the trial result.
    """
    result = []
    for i in range(trial_number):
        result.append(simulation())
    mean = sum(result)/trial_number
    median = (sorted(result)[5000] + sorted(result)[5001])/2
    print("The mean is " + str(mean))
    print("The median is " + str(median))

# Run the test with 10000 iteration
test(10000)




                
