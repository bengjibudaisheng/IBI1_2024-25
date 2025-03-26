# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Make array of all susceptible population.
population=np.zeros((100,100))

# Randomly choose where the outbreak is happening.
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1

# Create the gragh at time 0.
plt.figure(figsize=(6,4),dpi =150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

# Define the probability of infection and recovery.
beta=0.3
gamma=0.05

# Create an array to hold the 2D arrays corresponding to the positions of infected individuals.
I_array=np.array([outbreak])
 
for i in range(100):
    
    # Substitute the 2D arrays corresponding to the positions of infected individuals into x and y.
    for x,y in I_array:
        
        # Select the neighbors of the infected individuals.
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if not(dx==0 and dy==0):
                    x1=x+dx
                    y1=y+dy

                    # Select the neighbors who are not beyond the boundaries and have not been infected.
                    if 0<=x1<100 and 0<=y1<100 and population[x1,y1]==0:
                        result=np.random.choice(range(2),1,p=[1-beta,beta])
                        population[x1,y1]=result[0]

                        # Add the individuals that have been successfully infected to the array.
                        if population[x1,y1]==1:
                            I_array=np.append(I_array,[[x1,y1]],axis=0)
    
    # Substitute the 2D arrays into x and y.
    for x,y in I_array:

        # Select the individuals who have not been recovered.
        if population[x,y]==1:
            result=np.random.choice(range(1,3),1,p=[1-gamma,gamma])
            population[x,y]=result[0]
    
    # Create the gragh at time 10, 50, and 100.
    if i in [9,49,99]:
        plt.figure(figsize=(6,4),dpi =150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')

plt.show()