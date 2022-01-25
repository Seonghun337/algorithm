import math

def getFee(minute, fees):
    base_time, base_fee, unit_time, unit_fee = fees
    
    res = base_fee
    if minute > base_time:
        res += math.ceil((minute-base_time)/unit_time) * unit_fee
    return res

def getMin(strHM):
    res = 0
    _strHM = strHM.split(':')
    res += int(_strHM[0])*60
    res += int(_strHM[1])
    return res

def solution(fees, records):
    park = {}
    accum_fee = {}
    
    for rec in records:
        at, car_id, typ = rec.split()
        if typ == "IN":
            park[car_id] = getMin(at)
        else:
            stay_time = getMin(at) - park[car_id]
            park[car_id] = -1
            if car_id in accum_fee:
                accum_fee[car_id] += stay_time
            else:
                accum_fee[car_id] = stay_time
        
    MAX_AT = getMin('23:59')
    for car_id in park:
        if park[car_id] != -1:
            stay_time = MAX_AT - park[car_id]
            park[car_id] = -1
            if car_id in accum_fee:
                accum_fee[car_id] += stay_time
            else:
                accum_fee[car_id] = stay_time
    
    
    car_ids = sorted(list(accum_fee.keys()))
    answer = []
    for car_id in car_ids:
        answer.append(getFee(accum_fee[car_id],fees))
    
    # accum_fee 이름 -> accum_time으로 나중에
    
    return answer