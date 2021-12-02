def interesting_game(k, n): #k - qantity points, n - qantity cards
    numbers_list = []
    point_Vasya, point_Petya, draw = 0, 0, 0
    
    while len(numbers_list) < n:
        numbers_list.append(int(input()))

    for i in numbers_list:
        if i % 3 == 0 and i % 5 != 0:
            point_Petya += 1
        elif i % 5 == 0 and i % 3 != 0:
            point_Vasya += 1
        else:
            draw += 1

    if  point_Vasya == k or point_Vasya > point_Petya or point_Vasya > draw:
        return 'Vasya'
    elif point_Petya == k or point_Petya > point_Vasya or point_Petya > draw:
        return 'Petya'
    else:
        return 'Draw'

# print(interesting_game(3, 10))
# print(interesting_game(4, 16))
print(interesting_game(3, 5)) 