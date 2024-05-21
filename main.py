# Employee Hours/Cash Tips (User Inputs Reg Hours, Hourly Rate, Cash Tips, Tax Withheld)
input('Grab your most recent paystub and press [Enter] to continue...')
regHours = float(input('Enter your regular hours worked: 🕘 '))
hourlyRate = float(input('Enter your hourly rate: 💲 '))
cashTips = float(input('Enter your cash tips earned: 💲 '))
taxWithheld = float(input('Enter your taxes withheld: 💲 '))
deductionsWithheld = float(input('Enter your total amounts deducted (Benefits, 401K, etc.): 💲 '))
print('\n\n')
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
print('EMPLOYEE BREAKDOWN:')
print('Employee Tax Rate:', round(taxRate, 3) * 100, '%')

if netPay != checkAmount:
    print('Net Pay:', '💲', round(netPay, 2))
    print('Check Amount:', '💲', round(checkAmount, 2))
else: 
    print('Net Pay/Check Amount:', '💲', round(checkAmount, 2))

if cashTips > 0:
    print('Cash Tips:', '💲', round(cashTips, 2))

if hourlyPay != hourlyTotal:
    print('Hourly Pay:', '💲', round(hourlyPay, 2))
    print('Hourly Total:', '💲', round(hourlyTotal, 2))
else: 
    print('Hourly Pay/Hourly Total:', '💲', round(hourlyTotal, 2))
    
print('------------------------------')

