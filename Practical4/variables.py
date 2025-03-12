a=15           # The walk to the bus stop is 15 mins.
b=75           # The bus journey takes 1 hr and 15 mins.
c=a+b
d=90           # The drive takes 1 hr and 30 mins.
e=5            # The walk from the car park takes 5 mins.
f=d+e
if c<f:        # If c is smaller than f, the first method of transport take less time than the second method of transport.
    print("the first method of transport is quicker")
elif c>f:      # If c is bigger than f, the first method of transport take much time than the second method of transport.
    print("the second method of transport is quicker")
else:          # In any other conditions, c equals to f, the first method of transport take the same time as the second method of transpor.
    print("two methods cost the same time")

X=True
Y=False
W=X and Y
#X     Y     W
#True  False False
#True  True  True
#False True  False
#False False False