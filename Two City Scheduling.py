class Solution:
    
    def twoCitySchedCost(self, costs) -> int:
        costs.sort(key=lambda x:x[1]-x[0])
        k = len(costs) >> 1
        return sum(x[i<k] for i, x in enumerate(costs))

    sum = twoCitySchedCost(twoCitySchedCost, [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
    print(sum)