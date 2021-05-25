def getCalories(question): #ask how many calories consumed
    calories = input(question)
    if calories.isdigit(): #Check to see if calories are float or integer
        calories = int(calories)
        if calories > -1 and calories < 50000: #Check to see if calorie count is reasonable
            return calories
        else:
            print("Invalid input")
            return getCalories(question) #If fail, the function must run again
    else:
        print("Use positive numbers")
        return getCalories(question)

print("Welcome to the calorie counter\n")
print("Please enter your calories for the last 7 days")

week = []
for i in range(7):
    day = getCalories(question = "Day " + str(i+1) + ":")
    week.append(day)

total = sum(week)
average = int(total / 7)

print("Your total calorie intake for the week:", total)
print("\nYour average calorie intake for the week:", average)

if total > 21000:
    print("\nYou are eating too many calories. Please consider lowering intake!")
elif total < 8000:
    print("\nYou are eating far too few calories. Please consider increasing intake.")