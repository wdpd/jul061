import random


class People:
    """People and their information"""
    people_num = 0
    people_num_alive = 0

    def __init__(self, name, gender=-1, age=-1):
        People.people_num += 1
        People.people_num_alive += 1
        self.id = People.people_num
        self.name = name
        self.gender = gender
        self.age = age
        self.alive = True

    def __del__(self):
        People.people_num -= 1

    def kill(self):
        self.alive = False
        People.people_num_alive -= 1


def randstr(length):
    """Generate random string for names"""
    str_dict = 'abcdefghijklmnopqrstuvwxyz'
    rand_str = ''
    for i in range(length):
        rand_str += random.choice(str_dict)
    return rand_str


def epoch(people_list,start, step):
    """Run an epoch and kill one people"""
    people_alive = [x for x in people_list if x.alive]
    start_index = people_alive.index(start)
    next_start_index = (start_index + step) % len(people_alive)
    to_kill_index = (start_index + step - 1) % len(people_alive)
    next_start = people_alive[next_start_index]
    people_alive[to_kill_index].kill()
    return next_start


def info_printer(input_list):
    print('ID\tName\tGender\tAge\tAlive')
    print('-------------------------------------')
    for x in input_list:
        print('{}\t{}\t{}\t{}\t{}'.format(x.id, x.name, x.gender, x.age, x.alive))


def people_generator(people_num, name_length):
    rand_name = [randstr(name_length) for i in range(people_num)]
    rand_gender = [random.choice(['Male', 'Female']) for i in range(people_num)]
    rand_age = [random.randint(1, 80) for i in range(people_num)]
    people_list = [People(rand_name[i], rand_gender[i], rand_age[i]) for i in range(people_num)]
    return people_list


def josephus_problem(people_num, count_start, count_step, people_remain, name_length):
    people_list = people_generator(people_num, name_length)
    counting = people_list[count_start - 1]
    while People.people_num_alive > people_remain:
        counting = epoch(people_list, counting, count_step)
    return people_list


PEOPLE_NUM = 10
COUNT_START = 5
COUNT_STEP = 3
PEOPLE_REMAIN = 7
NAME_LENGTH = 5

people_info = josephus_problem(PEOPLE_NUM, COUNT_START, COUNT_STEP, PEOPLE_REMAIN, NAME_LENGTH)
people_alive_info = people_alive = [x for x in people_info if x.alive]
info_printer(people_info)
print()
info_printer(people_alive)

assert([x.id for x in josephus_problem(PEOPLE_NUM, COUNT_START, COUNT_STEP, PEOPLE_REMAIN) if x.alive] == [1, 2, 4, 5, 6, 8, 9])
