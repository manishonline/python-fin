import matplotlib.pyplot as plt
import random
import numpy

def multiply101(price):
        return price*1.01

def multiply099(price):
        return price*0.99

def multiply102(price):
    return price*1.02

def multiply098(price):
    return price*0.98

def run(price):
    randomPrices = []
    randomPrices.append(price)
    for i in range(1,200,1):
        test = random.choice([multiply099,multiply098,multiply101,multiply102])
        randomPrices.append(test(randomPrices[-1]))
    return randomPrices

def mean(price):
    return numpy.mean(price,axis=0)

def stddev(price):
    return numpy.std(price,axis=0)

def main():
    startPrice = 100
    prices = run(startPrice)
    print prices
    x_axis = numpy.arange(1,200,10)
    x = mean(prices)
    y = stddev(prices)
    fig,ax = plt.subplots()
    data_line = ax.plot(prices,label='Prices')
    mean_line = ax.plot(x, label='Mean', linestyle='--')
    mean_line = ax.plot(y, label='Standard Deviation', linestyle='__')
    # Make a legend
    legend = ax.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    main()