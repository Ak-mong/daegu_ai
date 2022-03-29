members=['eoging','duru']
for member in members:
    print('member',member)

members2 = [
    ['egoing','seoul','programer'],
    ['duru','daege','dba']
]
print(members2[0][0])

for member in members2:
    print(member[0], member[1])

egoing1 = ['egoing','seoul','programer']
egoing2={'name':'egoing', 'city': 'seoul', 'job': 'programmer'} #사전형
print(egoing2['city'])
for name in egoing2:
    print(egoing2[name])

members3=[
    {'egoing','seoul','programmer'},
    {'name':'duru', 'city':'daegu','jog':'dba'}
] #리스트문
for memeber in members3:
    print(member['name'])