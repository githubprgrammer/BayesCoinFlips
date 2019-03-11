import matplotlib.pyplot as plt

'''
We have a large jar containing many coins. Half of the coins are fair and the other half are biased towards tail. 
With a biased coin, you would flip a tail in 3 out of 4 cases. 
We have data from 12 different experiments. In each experiment, a coin is randomly picked from the jar. That coin is then flipped 20 times. 
During this process we can update our belief about the coin being biased or not. We will use Bayesian statistics to determine for each coin 
the probability of it being biased.
'''




#this is our dataset of coinflips. Each List of coinflips is an experiment with a specific coin taken from the jar.
coinFlips = [['H', 'H', 'T', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H'], ['T', 'T', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'H'], ['T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'H'], ['T', 'H', 'H', 'T', 'H', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'H', 'H', 'T', 'T'], ['T', 'H', 'H', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T'], ['H', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'H'], ['H', 'T', 'H', 'T', 'H', 'H', 'H', 'T', 'H', 'H', 'H', 'H', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T'], ['T', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'T', 'T'], ['T', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'T', 'T', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'T'], ['H', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'H', 'H'], ['T', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'T', 'T', 'T'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']]


def posterior(prior, coin):
    p_b = 0.75 if (coin == 'T') else 0.25
    return (0.5 * prior) / (0.5 * prior + p_b * (1 - prior))


def getProbabilityOfCoinBeingBiased(dataset):
    prior_1 = 0.4 if dataset[0] == 'T' else 2 / 3
    listwithResults = [[], []]

    def loop(index, result):
        if index == len(dataset):
            return listwithResults
        listwithResults[0].append(index+1)
        result2 = posterior(result, dataset[index])
        listwithResults[1].append(1 - result2)
        return loop(index + 1, result2)

    return loop(0, prior_1)



plotpoints = list(map(getProbabilityOfCoinBeingBiased, coinFlips))

ax = plt.subplot(111)
for i in range(len(plotpoints)):
    ax.plot(plotpoints[i][0], plotpoints[i][1], label= str(i+1))

plt.title('Flipcoin experiment')
ax.set_xlabel("amount of flips")
ax.set_ylabel("probability of coin being biased")
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
ax.legend(loc='upper center', bbox_to_anchor=(1.2, 0.8), shadow=True, ncol=1)
plt.show()


