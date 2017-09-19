def selection_sort(a_list):
    for filter_slots in range(len(a_list) -1, 0 , -1):
        pos_of_max = 0
        for location in range(1, filter_slots +1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location

        temp = a_list[filter_slots]
        print('Temp: ', temp)
        print(a_list)
        a_list[filter_slots] = a_list[pos_of_max]
        print('pos_of_max: ', a_list[pos_of_max])
        a_list[pos_of_max] = temp
