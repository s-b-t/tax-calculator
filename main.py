# Boldens text for user to clearly discern what the program is trying to validate in order to enhance user experience
def boldText(text):
    return "\033[1m" + text + "\033[0m"

# Ensures that the program keeps asking the user to enter a valid input dealing with floats
def getFloatInput(prompt):
    while True:
        userInput = input(prompt)
        if userInput == '':
            print(boldText('You need to enter a value.'))
        else:
            try:
                return float(userInput)
            except ValueError:
                print(boldText('Invalid input. Please enter a valid number.'))

# Employee Hours/Cash Tips (User Inputs Reg Hours, Hourly Rate, Cash Tips, Tax Withheld)
input('Grab your most recent paystub and press [Enter] to continue...')
regHours = getFloatInput('Enter your regular hours worked: 🕘 ')
hourlyRate = getFloatInput('Enter your hourly rate: 💲 ')
cashTips = getFloatInput('Enter your cash tips earned: 💲 ')
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

# Employee Breakdown
print('------------------------------')
print(boldText('EMPLOYEE BREAKDOWN:'))
print('Employee Tax Rate:', round(taxRate, 3) * 100, '%')

# If netPay is not equal to checkAmount, print both of them separately to show the amounts respectively
if netPay != checkAmount:
    print('Net Pay:', '💲', round(netPay, 2))
    print('Check Amount:', '💲', round(checkAmount, 2))
# Otherwise, if they are equal, combine them when displaying to the user
else: 
    print('Net Pay/Check Amount:', '💲', round(checkAmount, 2))

# If cashTips are greater than 0, make sure user sees that displayed in the breakdown, otherwise if 0, no need to display to user
if cashTips > 0:
    print('Cash Tips:', '💲', round(cashTips, 2))

# If hourlyPay is not equal to grossEarnings, print both of them separately to show the amounts respectively
if hourlyPay != grossEarnings:
    print('Hourly Pay Total:', '💲', round(hourlyPay, 2))
    print('Gross Earnings:', '💲', round(grossEarnings, 2))
# Otherwise, if they are equal, combine them when displaying to the user
else: 
    print('Hourly Pay Total/Gross Earnings:', '💲', round(grossEarnings, 2))

print('------------------------------')

