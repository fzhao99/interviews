import sys

def coin_change(value, num_coins, coins):

    coin_req = [sys.maxsize] * (value +1)
    coin_req[0] = 0
    for amt in range(1, value):
        for j in range(num_coins):
            if coins[j] < amt:
                coin_req[amt] = min(coin_req[amt - coins[j]] + 1, coin_req[amt])
 


    return coin_req[value]
