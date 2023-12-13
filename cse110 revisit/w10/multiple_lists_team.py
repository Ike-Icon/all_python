"""Sometimes you have two lists that you want to keep in sync with each other.
 For example, in this assignment, you will track bank accounts and the balances in each one."""

# Create two lists, one for the names of the bank accounts, and one for the balances.
accounts = []
balances = []


print("\nEnter the names and balances of bank accounts (type: quit when done)")

# Ask the user for the name of the bank account and then for it's current balance.
# Keep looping until the user types "quit" for the name of an account

acc_names = ""
acc_balance = ""

while acc_names != "quit":
    acc_names = input("What is the name of this account? ")
    if acc_names != "quit":
        accounts.append(acc_names)
        acc_balance = float(input("What is the balance? "))
        balances.append(acc_balance)


# Loop through the lists using an index and display the name of the account with the balance next to it.
print("\n--------------------------------------------------")
print("Account Information: ")

for i in range(len(accounts)):
    name = accounts[i]
    balance = balances[i]

    print(f"{i}. {name} - ${balance}")
print("--------------------------------------------------")
print()
# Compute and display the total balance in all of the accounts and the average balance.
total_balance = 0
for balance in balances:
    total_balance += balance

    # average balance.
    average = total_balance / len(balances)

print(f"Total: {total_balance:.2f}")
print(f"Average: {average:.2f}")

# II STRETCH CHALLENGE
# Determine which bank account has the highest balance and display the name and balance of that account.
for i in range(len(accounts)):
    name = accounts[i]
    balance = balances[i]

    maxbalance = max(balances)
print(f"Highest balance: {name} - {maxbalance}")

#  ask the user if they want to update an account. If they respond with yes, ask for the index of the account, and the new balance.
print()
acc_update = ""

while acc_update != "no":
    acc_update = input("Do you want to update an account? (yes/no): ")
    if acc_update == "yes":
        update_index = int(input("What account index do you want to update?"))
        new_amount = float(input("What is the new amount? "))
        balances[update_index] = new_amount

    print("\n--------------------------------------------------")
    print("Account Information: ")

    for i in range(len(accounts)):
        name = accounts[i]
        balance = balances[i]

        print(f"{i}. {name} - ${balance}")
    print("--------------------------------------------------")
