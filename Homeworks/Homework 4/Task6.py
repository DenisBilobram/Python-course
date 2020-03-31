from itertools import cycle, count
# a)
iterator_a = (el for el in count(0))
for i in iterator_a:
    print(i)
    if i == 100:
        break

# b)
my_list = [1, 2, 3, 4]
iterator_b = (el for el in cycle(my_list))
c = 0
for i in iterator_b:
    if c == 11:
        break
    print(i)
    c += 1

# *) не понимаю какую именно задачу здесь я должен решить.