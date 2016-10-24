# arrays
bonus        = [0.005, 0.12, 0.345, 0.68, 1.125, 1.68, 2.345, 3.12, 4.005, 5   , 6.105, 7.32 ]
loss         = [0]
probability  = [0.359, 0.330, 0.3 , 0.27 , 0.24, 0.21 , 0.18, 0.15 , 0.12, 0.09 , 0.06, 0.03 ]
time         = []
cookies_lost = []

# constants
cps = 11.696 #quadrillion

# counters
total_time = 0

# calculations
i = 0
while i < 11:
    loss.append(bonus[i] - bonus[i-1])
    i = i + 1
i = 0
while i < 12: 
    time.append(100/probability[i])
    cookies_lost.append(cps*loss[i]*time[i])
    i = i + 1
    
# questions
current_wrinklers = int(input("How many Wrinklers do you have? - "))
spend = float(input("How much are you spending? [quad] - "))
gain = float(input("what's the cps gain? [%] - "))

# calculations
cookies_gained = cps * gain/100 * time[current_wrinklers-1]
change = cookies_gained - cookies_lost[current_wrinklers-1]

# results
print("the wrinkler will be offline for " + str(time[current_wrinklers-1]) + " s")
print("you will gain " + str(cookies_gained) + " quadrillion cookies")
print("you will lose " + str(cookies_lost[current_wrinklers-1]) + " quadrillion cookies")
print("total chage - " + str(change) + " quadrillion cookies")



