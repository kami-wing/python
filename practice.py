print('jake')
print('True or True=',True or True)
age=int(input('enter your age:'))
if age >= 18:
    print('good')
else:
    print('fuck')
n=123
f=456.789
s1='hellow,world'
s2='hellow,\'adam\''
s3=r'hellow,"bart"'
s4=r'''hellow,
bob!'''
print(n,f,s1,s2,s3,s4)
s1=72 
s2=85 
r=(s2/s1-1)*100
print('提升{:.1f}%'.format(r))
