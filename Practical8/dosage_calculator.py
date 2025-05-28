# Define a function to calculate the dosage.
def dosage_calculator(weight,strength):
    
    # Determine whether the weight is within the expected range or not.
    if not 10.0<=weight<=100.0:
        result='The supplied weight is outwith the expected range.'
        return result
    else:

        # Determine whether the strength matches an expected concentration.
        if strength!=120 and strength!=250:
            result='The paracetamol strength does not match an expected concentration.'
            return result
        else:

            # Calculate the volume of drug.
            dose=weight*15
            volume=dose/(strength/5)
            result=str(volume)+'ml'
            return result
        
# Request the user to input the weight and strength.
weight=float(input('weitgh(kg):'))
strength=int(input('strength(mg/5ml):'))

volume=dosage_calculator(weight,strength)
print(volume)
        