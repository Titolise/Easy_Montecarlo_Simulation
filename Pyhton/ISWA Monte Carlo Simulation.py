#Import library 
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# downloadin data and calculation of daily yield
IWDA= yf.download('IWDA.AS',start='2009-09-25', end='2024-09-23')['Adj Close']
returns= IWDA.pct_change().dropna()

#set parametres of simualtion
n_simulation= 1000
n_days= 252
initial_investment= 10000

#simulation
simulation= np.zeros((n_simulation,n_days))
for i in range(n_simulation):
    random_walk=np.random.normal(returns.mean(),returns.std(),n_days)
    simulation[i, :]= initial_investment * np.cumprod(1+random_walk)

#Extract the mean and the standard deviation of the simulation
mean_val=np.round(np.average(simulation))
std_val=np.round(np.std(simulation))
median_val=np.round(np.median(simulation))
print((mean_val),(std_val),(median_val))

#plot
plt.figure(figsize=(15,9))
plt.plot(simulation.T, alpha=0.4)
plt.title("Monte Carlo Simulation: IWDA Investment")
plt.xlabel("Days")
plt.ylabel("Investment Value")
plt.show()

