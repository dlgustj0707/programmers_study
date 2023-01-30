def solution(bridge_length, weight, truck_weights):
    second = 0 #시간
    bridge_crossing = [0] * bridge_length #다리를 건너는 트럭 리스트 
    #다리의 길이 만큼 0을 넣은 리스트 생성
    while bridge_crossing != []: 
        second += 1
        bridge_crossing.pop(0)
        if len(truck_weights) != 0:
            if sum(bridge_crossing) + truck_weights[0] <= weight:
                bridge_crossing.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                bridge_crossing.append(0)
    return second
