print("hellow world!")

print("Hello world: how are you?")


def add(num_1: int, num_2: int, num_3: float):
    return (num_1 + num_2) * num_3


some_list = [
    1,
    4,
    4,
    6,
]

sum = 0
for i, each_num in enumerate(some_list):
    sum += each_num

print(sum)


assert 7 == add(3, 4)

print("The sum of 3 and 4 is " + str(add(3, 4)))
