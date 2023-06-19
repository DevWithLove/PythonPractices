"""
People array is an array of people's weights, i the person has a weight people[i] and each boat can carry at most limit.
Each boat carries at most 2 people at the same time, Given that their weight sum is at most limit.
Return the min number of boats t ocarry every given person.

- 
Desc
The max no of people a boat can carry is 2
The max weight that a bot can carry is an input called limit

Conclusion
every individual person has a weight lower than ore equal to limit
cam use unlimited boats.
"""

from typing import List

def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    heavyP = len(people) - 1
    lightP = 0
    boats = 0
    while lightP <= heavyP:
        if lightP == heavyP:
            boats += 1
            break

        if people[lightP] + people[heavyP] <= limit:
            lightP += 1
        boats +=1
        heavyP -=1
    return boats

print(numRescueBoats([2,1,3,4],4))

