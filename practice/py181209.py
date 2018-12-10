from functools import reduce

l1 = [x for x in range(-10, 1)]
m1 = map(abs, l1)
print(list(m1))

def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 +y

print(reduce(fn, [1, 3, 5, 7, 9]))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
l2 = ['adam', 'LISA', 'barT']

def name(s):
  return s.capitalize()

l3 = list(map(name, l2))
print(l3)

def prod(x, y):
    return x * y

print(reduce(prod, [1, 2, 3, 4]))

#filter
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', 'c'])))

print(sorted([36, 5, -12, 9, -21], key=abs))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5)
print(f())

print(list(map(lambda x: x * x, [1, 2, 3, 4])))

f = lambda x: x * x
print(f(3))

def now():
    print('2018')

f = now
f()