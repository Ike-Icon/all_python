"""**The Problem: Qualifying for a loan**
1.Does the person have a job, and if so, how long have they worked there, and how much money do they make?
2.Is there good collateral for the loan? (for example, is the loan against a car or home that is worth at least the amount of the loan?)
3.Does the person have a good credit score or history of paying back loans?
4.How much other debt does the person have?
5.How much money does the person have?
6.Will the person have a down payment, and if so, what percentage of the loan does it amount to?
"""

# First, ask for a rating from 1–10 on the following:
print("On a rate from 1 - 10: ")

loan_size = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_pay = int(input("How large is your down payment? "))

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        decision = "yes"
    
    elif (credit >= 7 or income >=7) and down_pay >= 5:
        decision = "yes"
    else:
        decision = "no"

else:
    if loan_size != 5 or loan_size < 5:
        if credit < 4:
            decision = "no"
        elif income >= 7 or down_pay >= 7:
            decision = "yes"
        elif income >= 4 and down_pay >= 4:
            decision = "yes"
        else:
            decision = "no"


if decision == "yes":
    print("\nThe decision is yes. This is a good loan.")
else:
    print("\nThe decision is no. You should not loan this money.")