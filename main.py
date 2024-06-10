import re

# Boldens text using ANSI escape characters for user to clearly discern what the program is trying to validate in order to enhance user experience
def boldText(text):
    return "\033[1m" + text + "\033[0m"

# Ensures that the program gets a name from the user and keeps asking the user to enter their name if they do not provide one
def getName(prompt):
    while True:
        userName = input(prompt).strip()
        if userName == '':
            print()
            print(boldText('You did not enter your name. Please enter your name.'))
            print()
        # Ensures that the user is only able to enter alphabetic characters/space, no special characters or numbers
        elif not re.match("^[A-Za-z ]*$", userName):
            print()
            print(boldText('Invalid name. Please enter a name using only alphabetic characters and spaces.'))
            print()
        else:
            return userName

# Ensures that the program keeps asking the user to enter a valid input when dealing with float inputs
def getFloatInput(prompt):
    while True:
        userInput = input(prompt)
        if userInput == '':
            print()
            print(boldText('You need to enter a value.'))
            print()
        else:
            try:
                return float(userInput)
            except ValueError:
                print()
                print(boldText('Invalid input. Please enter a valid number.'))
                print()

def saveToTextFile(outputData):
    while True:
        fileName = input("Enter the file name you'd like to save your earnings/tax breakdown to. " + boldText("You do not need to add a file extension.") + " A .txt file will be saved by default: ")
        print()
        if fileName == "":
            print(boldText("You did not enter a file name. Please enter a file name."))
            print()
            continue

        if not fileName.endswith(".txt"):
            fileName += ".txt"
        try:
            with open(fileName, 'w') as file:
                file.write(outputData)
            print(f"Earnings/tax breakdown successfully saved to " + boldText(f'{fileName}'))
            print()
            break
        except Exception as e:
            print("An error occurred while trying to save the file: " + boldText(f'{e}'))
            print()
            continue
        

# Prompts user to grab their most recent paystub and continue, then prompts user to enter all the pertinent values the program needs to calculate tax rate and finalize the employee breakdown
input('Grab your most recent paystub and press ' + boldText('[Enter]') + ' to continue... ')
print()
name = getName('Enter your name: ').upper()
regHours = getFloatInput('Enter your regular hours worked in the pay period (weekly, bi-weekly, etc.): 🕘 ')
hourlyRate = getFloatInput('Enter your hourly rate: 💲 ')
cashTips = getFloatInput('Enter your cash tips/commissions earned (Type 0 if N/A): 💲 ')
taxWithheld = getFloatInput('Enter your taxes withheld: 💲 ')
deductionsWithheld = getFloatInput('Enter your total amounts deducted (Benefits, 401K, etc.): 💲 ')
print('\n')

hourlyPay = (regHours * hourlyRate)
hourlyTotal = (hourlyPay + cashTips)
grossEarnings = hourlyTotal

# Employee Tax Rate
taxRate = (taxWithheld / hourlyTotal)

# Net Pay/Check Amount
netPay = (grossEarnings - (taxWithheld + deductionsWithheld))
checkAmount = (netPay - cashTips)

# Breakdown for user
outputData = (
    '----------------------------------------------------\n'
    + boldText(f'EARNINGS/TAX BREAKDOWN FOR {name} __ THRU __:') + '\n'
    + f'Your Tax Rate: {round(taxRate, 3) * 100} %\n'
)

# If netPay is not equal to checkAmount, print both of them separately to show the amounts respectively
if netPay != checkAmount:
    outputData += f'Net Pay: 💲 {round(netPay, 2)}\n'
    outputData += f'Check Amount: 💲 {round(checkAmount, 2)}\n'
# Otherwise, if they are equal, combine them when displaying to the user
else: 
    outputData += f'Net Pay/Check Amount: 💲 {round(checkAmount, 2)}\n'

# If cashTips are greater than 0, make sure user sees that displayed in the breakdown, otherwise if 0, no need to display to user
if cashTips > 0:
    outputData += f'Cash Tips/Commissions: 💲 {round(cashTips, 2)}\n'

# If hourlyPay is not equal to grossEarnings, print both of them separately to show the amounts respectively
if hourlyPay != grossEarnings:
    outputData += f'Hourly Pay Total: 💲 {round(hourlyPay, 2)}\n'
    outputData += f'Gross Earnings: 💲 {round(grossEarnings, 2)}\n'
# Otherwise, if they are equal, combine them when displaying to the user
else: 
    outputData += f'Hourly Pay Total/Gross Earnings: 💲 {round(grossEarnings, 2)}\n'

outputData += '----------------------------------------------------'

# Print the output data
print(outputData)

# Ask the user if they want to save the output to a text file
while True:
    saveChoice = input("Would you like to save your earnings/tax breakdown to a text file? " + boldText('(Y/N)') + ": ").strip().lower()
    print()
    if saveChoice == "":
        print(boldText("You did not enter an answer. Please answer Yes or No."))
        print()
    elif saveChoice in ['yes', 'y']:
        saveToTextFile(outputData)
        break
    elif saveChoice in ['n', 'no']:
        print(boldText("Earnings/tax breakdown was not saved."))
        print()
        break
    else:
        print(boldText("Please answer Yes or No."))
        print()
        continue

