# Imports 'regular expression' library for validations on alphabetic-only entries
import re
# Imports datetime usage/validations for user input involving date
from datetime import datetime

# Boldens text using ANSI escape characters for user to clearly discern what the program is trying to validate in order to enhance user experience
def boldText(text):
    return "\033[1m" + text + "\033[0m"

# Ensures that the program gets a name from the user and keeps asking the user to enter their name if they do not provide one
def getName(prompt):
    while True:
        # Sets userName equivalent to an input required from the user when prompted to enter their name and strips whitespace from the entry
        userName = input(prompt).strip()
        # If userName is blank, keep prompting the user to enter their name
        if userName == '':
            print()
            print(boldText('You did not enter your name. Please enter your name.'))
            print()
        # Ensures that the user is only able to enter alphabetic characters/space, no special characters or numbers--utilizes regular expression for the user input
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
        # If userInput is blank, keep prompting the user to enter a value
        if userInput == '':
            print()
            print(boldText('You need to enter a value.'))
            print()
        # Otherwise, alert user that their entry was invalid
        else:
            try:
                return float(userInput)
            except ValueError:
                print()
                print(boldText('Invalid input. Please enter a valid number.'))
                print()

# Function utilizing datetime that allows a proper date (MM/DD/YY) to be passed in as user input
def getDate(prompt):
    while True:
        # Strips any spaces/white space from user input
        dateInput = input(prompt).strip()
        # Tries to validate the user input as a valid, acceptable date
        try:
            valid_date = datetime.strptime(dateInput, "%m/%d/%y")
            return valid_date.strftime("%m/%d/%y")
        # If the date was invalid or not entered properly, alerts the user and reminds them what the proper format is
        except ValueError:
            print()
            print(boldText('Invalid date format. Please enter the date in MM/DD/YY format.'))
            print()

# Defines the function that allows the user to be able to save their output to a text file for record keeping
def saveToTextFile(outputData):
    while True:
        # Allows user to name their file via user input and tells them to not worry about adding a file extension because the program does it by default anyways
        fileName = input("Enter the file name you'd like to save your earnings/tax breakdown to. " + boldText("You do not need to add a file extension.") + " A .txt (text file) extension will be automatically appended to the file name you type: ")
        print()
        # If fileName is blank, alert the user that they didn't enter anything and asks them again by continuing the loop
        if fileName == "":
            print(boldText("You did not enter a file name. Please enter a file name."))
            print()
            continue
        # If the fileName does not end with a .txt extension, the program appends the .txt extension by default so the user does not have to worry about typing a file extension themselves
        if not fileName.endswith(".txt"):
            fileName += ".txt"
        # When the program appends the .txt extension, it tries to write the file to be saved as long as there are no errors, and lets the user know it was successfully saved and breaks the loop
        try:
            with open(fileName, 'w') as file:
                file.write(outputData)
            print(f"Earnings/tax breakdown successfully saved to " + boldText(f'{fileName}'))
            print()
            break
        # If an error is encountered, the program lets the user know what error they are encountering and continues the loop to behave as expected
        except Exception as e:
            print("An error occurred while trying to save the file: " + boldText(f'{e}'))
            print()
            continue
        
# Prompts user to grab their most recent paystub and continue, then prompts user to enter all the pertinent values the program needs to calculate tax rate and construct the earnings/tax breakdown
print()
input('Grab your most recent paystub and press ' + boldText('[Enter]') + ' to continue... ')
print()
# Collects the user's name and sets it uppercase to be printed out in the final breakdown
name = getName('Enter your name: ').upper()
# Collects the startDate of the pay period calling on the getDate function for proper date format
startDate = getDate('Enter the ' + boldText('start date') + ' of the pay period in ' + boldText('(MM/DD/YY)') + ' format: ')
# Collects the endDate of the pay period calling on the getDate function for proper date format
endDate = getDate('Enter the ' + boldText('end date') + ' of the pay period in ' + boldText('(MM/DD/YY)') + ' format: ')
# Collects the user's regular hours worked in the pay period
regHours = getFloatInput('Enter your regular hours worked in the pay period ' + boldText('(Weekly, Bi-Weekly, etc.)') + ': 🕘 ')
# Collects the user's hourly rate ($/hr)
hourlyRate = getFloatInput('Enter your hourly rate: 💲 ')

# Sets overtimeHours and overtimeRate to default values of 0 and 1.5 respectively
overtimeHours = 0
overtimeRate = 1.5
# If overtimeHours are applicable for the user to enter, the program allows the user to enter all the pertinent data (resetting the defaults) required to properly factor in overtime in the final breakdown
while True:
    # Asks the user if they have worked overtime for this pay period, strips whitespace and allows a lowercase input of Y or N to be entered
    overtimeApplicable = input("Have you worked overtime in this pay period? " + boldText("(Y/N)") + ": ").strip().lower()
    # If the user enters a blank, program alerts the user that they need to respond with Yes or No
    if overtimeApplicable == "":
        print()
        print(boldText("You did not enter an answer. Please answer (Y)es or (N)o."))
        print()
    # Otherwise and if the user says 'Yes', new prompts to collect overtime info appear
    elif overtimeApplicable in ['yes', 'y']:
        overtimeHours = getFloatInput('Enter your overtime hours worked in the pay period: 🕘 ')
        overtimeRate = getFloatInput('Enter your overtime rate ' + boldText('(1.5 for time and a half, 2 for double time)') + ': ')
        break
    # Otherwise and if the user says 'No', the program lets the user know that it will not be factoring in overtime to the breakdown
    elif overtimeApplicable in ['no', 'n']:
        print()
        print(boldText("Proceeding without overtime calculations."))
        print()
        break
    # Otherwise, if any other invalid input is entered, alert the user their answer needs to be Y or N
    else:
        print()
        print(boldText("Please answer (Y)es or (N)o."))
        print()
        continue

# Calls on getFloatInput function and prompts the user to enter the proper floated integers in order to factor in cashTips, taxWithheld, and deductionsWithheld
cashTips = getFloatInput('Enter your cash tips/commissions earned ' + boldText('(type 0 if N/A)') + ': 💲 ')
taxWithheld = getFloatInput('Enter your ' + boldText('total') + ' taxes withheld ' + boldText('(FICA + Medicare + Social Security, etc.)') + ': 💲 ')
deductionsWithheld = getFloatInput('Enter your ' + boldText('total') + ' amounts deducted ' + boldText('(Benefits + 401K + Retirement, etc. -- type 0 if N/A)') + ': 💲 ')
print('\n')

# Calculates user hourlyPay, overtimePay, totalEarnings
hourlyPay = (regHours * hourlyRate)
overtimePay = (overtimeHours * hourlyRate * overtimeRate)
totalEarnings = hourlyPay + overtimePay + cashTips
grossEarnings = totalEarnings

# Calculates user taxRate
taxRate = (taxWithheld / totalEarnings)

# Calculates user netPay and checkAmount
netPay = (grossEarnings - (taxWithheld + deductionsWithheld))
checkAmount = (netPay - cashTips)

# Earnings/tax breakdown for user towards the end of the program
outputData = (
    '-------------------------------------------------------\n'
    + f'EARNINGS/TAX BREAKDOWN FOR {name} {startDate}--{endDate}:' + '\n'
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

# If hourlyPay and overtimePay are not equal to grossEarnings, print them separately to show the amounts respectively
outputData += f'Hourly Pay Total: 💲 {round(hourlyPay, 2)}\n'
if overtimeHours > 0:
    outputData += f'Overtime Pay Total: 💲 {round(overtimePay, 2)}\n'
outputData += f'Gross Earnings: 💲 {round(grossEarnings, 2)}\n'

# Appends line break under earnings/tax breakdown for visual purposes and readability
outputData += '-------------------------------------------------------'

# Print the output data (Earnings/tax breakdown)
print(outputData)

# Ask the user if they want to save the output to a text file after the breakdown appears
while True:
    print('\n')
    saveChoice = input("Would you like to save your earnings/tax breakdown to a text file? " + boldText('(Y/N)') + ": ").strip().lower()
    print()
    # If their choice is blank, alert the user they need to answer Y or N
    if saveChoice == "":
        print(boldText("You did not enter an answer. Please answer (Y)es or (N)o."))
        print()
    # Otherwise and if their choice is Y, saves the outputData (earnings/tax breakdown) to a text file
    elif saveChoice in ['yes', 'y']:
        saveToTextFile(outputData)
        break
    # Otherwise and if their choice is N, does not save the outputData (earnings/tax breakdown)
    elif saveChoice in ['n', 'no']:
        print(boldText("Earnings/tax breakdown was not saved."))
        print()
        break
    # Otherwise, if any other invalid input is tried, program alerts the user to please choose Y or N
    else:
        print(boldText("Please answer (Y)es or (N)o."))
        print()
        continue
