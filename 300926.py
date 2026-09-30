positives = 0
negatives = 0

variable = int(input())

while variable != 0:
    if variable > 0:
        positives += 1
    else:
        negatives += 1 
    variable = int(input())
    
print(positives)
print(negatives)
