def solution(bridge_length, weight, truck_weights):
    second = 0
    bridge_crossing = [0] * bridge_length
    while bridge_crossing != []: 
        second += 1
        bridge_crossing.pop(0)
        if len(truck_weights) != 0:
            if sum(bridge_crossing) + truck_weights[0] < weight:
                bridge_crossing.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                bridge_crossing.append(0)
            print(bridge_crossing)
            print(truck_weights)
    return second

print(solution(2, 10, [7,4,5,6]))
