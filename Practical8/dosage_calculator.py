# Request the user to input the weight and strength.
weight=input('weitgh(kg):')
strength=int(input('strength(mg/5ml):'))

# Determine whether the weight is within the expected range.
if not 10.0<=weight<=100.0:
    print('The supplied weight is outwith the expected range.')
else:

    # Determine whether the strength matches an expected concentration.
    if strength!=120 and strength!=250:
        print('The paracetamol strength does not match an expected concentration.')
    else:

        # Calculate the volume of drug.
        dose=weight*15
        volume=dose/(strength/5)
        print(volume,'ml')
        