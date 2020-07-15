import random
import csv


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


class Josephus:
    """A Josephus Ring"""
    def __init__(self):
        self.people_list = []

    def append(self, people):
        self.people_list.append(people)

    def extend(self, people):
        self.people_list.extend(people)

    def get(self, people_id):
        return self.people_list[people_id-1]

    def get_people_alive_num(self):
        people_alive = [x for x in self.people_list if x.alive]
        return len(people_alive)

    def alive(self, people_id):
        return self.people_list[people_id-1].alive

    def kill(self, people_id):
        self.people_list[people_id-1].kill()

    def pop(self, people_id):
        self.people_list.pop(people_id-1)

    def __len__(self):
        return len(self.people_list)

    def __iter__(self):
        self.iter_id = 1
        return self

    def __next__(self):
        if self.iter_id <= len(self.people_list):
            iter_id_current = self.iter_id
            self.iter_id += 1
            return self.people_list[iter_id_current-1]
        else:
            self.iter_id = 1
            raise StopIteration()


def randstr(length):
    """Generate random string for names"""
    str_dict = 'abcdefghijklmnopqrstuvwxyz'
    rand_str = ''
    for i in range(length):
        rand_str += random.choice(str_dict)
    return rand_str


def epoch(josephus_ring, start, step):
    """Run an epoch and kill one people"""
    people_alive = [x for x in josephus_ring if x.alive]  # get the list of people who are alive
    start_index = people_alive.index(start)
    next_start_index = (start_index + step) % len(people_alive)  # calculate where the next epoch starts
    to_kill_index = (start_index + step - 1) % len(people_alive)    # calculate who is to be killed
    next_start = people_alive[next_start_index]
    josephus_ring.kill(people_alive[to_kill_index].id)      # kill him
    return next_start


def info_printer(input_list):
    print('ID\tName\tGender\tAge\tAlive')
    print('-------------------------------------')
    for x in input_list:
        print('{}\t{}\t{}\t{}\t{}'.format(x.id, x.name, x.gender, x.age, x.alive))


def people_generator(people_num, name_length):
    """To generate people with random information"""
    rand_name = [randstr(name_length) for i in range(people_num)]
    rand_gender = [random.choice(['Male', 'Female']) for i in range(people_num)]
    rand_age = [random.randint(1, 80) for i in range(people_num)]
    josephus_ring = Josephus()
    people_list = [People(rand_name[i], rand_gender[i], rand_age[i]) for i in range(people_num)]
    josephus_ring.extend(people_list)
    return josephus_ring


def people_reader(filename):
    """To read people information from file specified in PEOPLE_LIST_PATH"""
    with open(filename, 'rt') as file:
        csv_reader = csv.reader(file)
        people_raw = [x for x in csv_reader]
    name = [x[1] for x in people_raw]
    gender = [x[2] for x in people_raw]
    age = [int(x[3]) for x in people_raw]
    josephus_ring = Josephus()
    people_list = [People(name[i], gender[i], age[i]) for i in range(len(people_raw))]
    josephus_ring.extend(people_list)
    return josephus_ring


def josephus_problem(people_num, count_start, count_step, people_remain, name_length=5, filename=''):
    """To generate automatically, comment the 'people_reader' line.
    To import from file people_list.csv, comment the 'people_generator' line,
    and change the PEOPLE_LIST_PATH accordingly"""
    # josephus_ring = people_generator(people_num, name_length)
    josephus_ring = people_reader(filename)
    counting = josephus_ring.get(count_start)
    while josephus_ring.get_people_alive_num() > people_remain:
        counting = epoch(josephus_ring, counting, count_step)
    return josephus_ring


PEOPLE_NUM = 100
COUNT_START = 53
COUNT_STEP = 18
PEOPLE_REMAIN = 7
NAME_LENGTH = 5
PEOPLE_LIST_PATH = 'c:\\Users\\karmo\\OneDrive\\Desktop\\python\\jul061\\people_list.csv'

people_info = josephus_problem(PEOPLE_NUM, COUNT_START, COUNT_STEP, PEOPLE_REMAIN, NAME_LENGTH, PEOPLE_LIST_PATH)
people_alive_info = [x for x in people_info if x.alive]
info_printer([x for x in people_info])
print()
info_printer(people_alive_info)

assert ([x.id for x in people_alive_info] == [7, 27, 38, 45, 62, 64, 82])
