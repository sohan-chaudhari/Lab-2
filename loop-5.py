def pythagorean(limit):
    triplets=[]
    a,b,c=0,0,0
    for a in range(1,limit+1):
        for b in range(a,limit+1):
            c=(a**2 + b**2)**0.5
            
            if c.is_integer() and c<=30:
                triplets.append((a,b,int(c)))
    return triplets        
limit=30    
triplets=pythagorean(limit)
for triplet in triplets:
    print(triplet)  