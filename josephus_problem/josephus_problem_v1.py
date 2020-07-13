start = 1
end = 30
people = [x for x in range(start, end+1)]
epoch_num = 7
counting_list = 0
counting_epoch = 1
people_left_num = 1

while len(people) > people_left_num:
    if counting_epoch == epoch_num:
        killing = people.pop(counting_list)
        counting_epoch = 1
        if counting_list == len(people):
            counting_list = 0
        print('{} killed itself! People remaining: {}'.format(killing, people))
    else:
        counting_epoch = counting_epoch+1
        if counting_list == len(people)-1:
            counting_list = 0
        else:
            counting_list = counting_list+1
