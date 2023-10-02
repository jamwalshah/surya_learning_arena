# atm.py
import sys
accBalance = 10000

ch = int(sys.argv[1])
print('Options are: \n1. Check Balance\n2. WithDraw\n3. Deposit Cash\n4. Deposit Check')
if ch == 1:
    print('Balance:', accBalance)
elif ch == 2:
    amt = int(sys.argv[2])
    accBalance-=amt
    print('Withdrew:', amt, "Account Balance:", accBalance)
elif ch == 3:
    amt = int(sys.argv[2])
    accBalance+=amt
    print('Cash Deposited:', amt, "Account Balance:", accBalance)
elif ch == 4:
    amt = int(sys.argv[2])
    accBalance+=amt
    print('Check Deposited:', amt, "Account Balance:", accBalance)
else:
    print('Invalid Option !!')