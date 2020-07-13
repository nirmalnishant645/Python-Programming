'''
Given a target amount n and a list (array) of distinct coin values,
what's the fewest coins needed to make the change amount.

For example:

If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

1+1+1+1+1+1+1+1+1+1

5 + 1+1+1+1+1

5+5

10

With 1 coin being the minimum amount.
'''

# Basic Recursion (Not Optimal)
def rec_coin(target, coins):

    # Default Value set to target
    min_coins = target

    # Base case to check if target is in coin values list 
    if target in coins:

        return 1

    else:

        # For every coin value that is <= target
        for i in [c for c in coins if c <= target]:

            # Add a coin count + Recursive  
            num_coins = 1 + rec_coin(target - i, coins)

            # Reset minimum if new num_coins < min_coins
            min_coins = min(num_coins, min_coins)

    return min_coins

# Dynamic Programming Solution (Efficient)
def rec_coin_dyn(target, coins, known_results = None):

    if not known_results:

        known_results = [None] * (target + 1)

    # Default output to target
    min_coins = target

    # Base Case
    if target in coins:

        known_results[target] = 1
        return 1

    # Return a known result if it is < 1
    elif known_results[target]:

        return known_results[target]

    else:

        # For every coin value that is <= target
        for i in [c for c in coins if c <= target]:

            num_coins = 1 + rec_coin_dyn(target - i, coins, known_results)

            min_coins = min(num_coins, min_coins)

            # Reset known results
            known_results[target] = min_coins
            
    return min_coins