# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

# Define the basic variables.
S=9999
I=1
R=0
N=10000
beta=0.3
gamma=0.05

# Create arrays for three variables.
S_array=np.array([S])
I_array=np.array([I])
R_array=np.array([R])

for i in range(1001):
    
    # Calculate the number of new infections and the number of new recoveries.
    infection_rate=beta*I/N
    I1=np.sum(np.random.choice(range(2),S,p=[1-infection_rate,infection_rate]))
    R1=np.sum(np.random.choice(range(2),I,p=[1-gamma,gamma]))

    # Determine the numbers of susceptible individuals, the numbers of infected individuals, the numbers of recovered individuals in this loop.
    S-=I1
    I+=(I1-R1)
    R+=R1
    
    # Record the numbers of susceptible people, infected people and recovered people evolving over time.
    S_array=np.append(S_array,S)
    I_array=np.append(I_array,I)
    R_array=np.append(R_array,R)

# Draw curves and set labels.
plt.plot(S_array,label='susceptible')
plt.plot(I_array,label='infected')
plt.plot(R_array,label='recovered')

# Set the labels and title of the gragh.
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')

plt.legend()
plt.show()