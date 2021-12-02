def alaram(input_data):
    alarams_list, res = [], []
    data = list(map(int, input_data.split(' ')))
    n = data[0] #qantity of alarms
    x = data[1] #period
    k = data[2] #qantity of alarms to be disabled

    while len(alarams_list) < n: 
        alarams_list.append(int(input())) #enter alarm values
    
    alarams_list.sort()

    while len(res) < k:
        for i in alarams_list:
            res += [i + step * x for step in range(k) if i + step * x not in res]
    
        return list(sorted(res))[k - 1]

print(alaram('5 7 12')) 
# print(alaram('6 5 10')) 