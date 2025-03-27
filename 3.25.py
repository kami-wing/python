death=['jake','joker','rose']
death.append('教皇')
death.insert(1,'花生')
death.pop(2)
death[1]='rose'
print(death)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
height = 1.75
weight = 80.5
bmi =weight/height**2
if bmi<18.5:
    print('过轻')
elif 18.5<bmi<25:
    print('正常')
elif 25<bmi<28:
    print('过重')
elif 28<bmi<32:
    print('肥胖')
elif bmi>32:
    print('严重肥胖')

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']
match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
    
N = ['Bart', 'Lisa', 'Adam']
for x in N:
    print('hellow',x)
