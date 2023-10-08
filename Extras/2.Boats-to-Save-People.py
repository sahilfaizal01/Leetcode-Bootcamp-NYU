class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        light = 0
        heavy = len(people)-1
        people.sort()
        while(heavy>=light):
            if(people[heavy]+people[light]<=limit):
                boats+=1
                heavy-=1
                light+=1
            else:
                boats+=1
                heavy-=1
        return boats
