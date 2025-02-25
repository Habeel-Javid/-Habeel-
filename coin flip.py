import random

def coin_toss():
    heads_count = 0
    tails_count = 0

    print("Welcome to the Virtual Coin Toss!")
    num_flips = int(input("How many times would you like to flip the coin? "))

    for _ in range(num_flips):
        result = random.choice(["Heads", "Tails"])
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    print("\nResults:")
    print(f"Heads: {heads_count} times ({heads_count / num_flips * 100:.2f}%)")
    print(f"Tails: {tails_count} times ({tails_count / num_flips * 100:.2f}%)")

    repeat = input("\nWould you like to flip again? (yes/no): ").strip().lower()
    if repeat == "yes":
        coin_toss()
    else:
        print("Thank you for using the Virtual Coin Toss!")

if __name__=="__main__":
    coin_toss()