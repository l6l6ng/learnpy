import numpy as np
import matplotlib.pyplot as plt
def simpmarket(win_rate, play_cnt=1000, stock_num=9, commission=0.01):
    money = np.zeros(play_cnt)
    money[0] = 1000
    binomial = np.random.binomial(stock_num, win_rate, play_cnt)
    print(binomial)
    for i in range(1, play_cnt):
        if binomial[i] > stock_num//2:
            money[i] = money[i-1] + 1
        else:
            money[i] = money[i-1] - 1
        money[i] -= commission
        if money[i] <= 0:
            break
    return money
[plt.plot(np.arange(1000), simpmarket(0.5, play_cnt=1000,  stock_num=9, commission = 0)) \
for _ in np.arange(0, 50)]