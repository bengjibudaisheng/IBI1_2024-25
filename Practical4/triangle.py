                                # Tn=1+2+...+n 
n=1                             # Start from the first value.
while n<=10 :                   # Display the first ten values.
    T=0
    for i in range(1,n+1) :     # i is the number of dots needed in the i layer.
        T+=i                    # Add up the number of dots in all layers.
    print("T",n,"=",T)
    n+=1                        # Turn to the next value.