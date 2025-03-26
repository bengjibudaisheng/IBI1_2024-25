# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

# Define the basic variables.
beta=0.3
gamma=0.05

# Substitute the percentages of people who have received vaccinations into i.
for i in range(0,100,10):
    
    # N represents the number of people who have not received vaccinations.
    N=int(10000*(100-i)/100)
    I=1
    R=0

    # In particular, consider the situation where 100% of the population is vaccinated.
    if N-I>0:
        S=N-I
    else:
        S=0
        I=N
    I_array=np.array([I])
    
    for j in range(1001):
        
        # Calculate the number of new infections and the number of new recoveries.
        infection_rate=beta*I/10000
        I1=np.sum(np.random.choice(range(2),S,p=[1-infection_rate,infection_rate]))
        R1=np.sum(np.random.choice(range(2),I,p=[1-gamma,gamma]))
        
        # Determine the numbers of susceptible individuals, the numbers of infected individuals, the numbers of recovered individuals in this loop.
        S-=I1
        I+=(I1-R1)
        R+=R1
        
        # Record the numbers of infected people evolving over time.
        I_array=np.append(I_array,I)

    # Draw curves and set labels.
    plt.plot(I_array,label=f'{i}%')

# Set the labels and title of the gragh.
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')

plt.legend()
plt.show()