# BayesCoinFlips
Using Bayesian statistics to update our belief about a coin being biased or not.

## Problem Description
We have a large jar containing many coins. Half of the coins are fair and the other half are biased towards tail. 
With a biased coin, you would flip a tail in 3 out of 4 cases. We have data from 12 different experiments. In each experiment, a coin is randomly picked from the jar. That coin is then flipped 20 times. During this process we can update our belief about the coin being biased or not. We will use Bayesian statistics to determine for each coin the probability of it being biased.

## Results

In the following you can see the result of the experiment.

![alt text](https://github.com/githubprgrammer/BayesCoinFlips/blob/master/Results.png)

As one can see there are some coins for which it is (based on our experiment with 20 flips) very clear to say whether they are biased or fair. coin 3 (green) and coin 8 (gray) for example are very likely (almost 100%) to be biased. Coin 12 for example is very unlikely (almost 0%) to be biased. If we look at the dataset of coin 12 then we can find, that all coin-flips produced head. So our chart makes sense since a biased coin is more likely to produce tail than head. There are other coins in the middle of these (like coin 11 and 4) for which it is unclear if they are fair or biased. In order to find this out we would have to conduct more
flips. Eventually the probability-curve of these coins would get closer to either 0 or 1.
