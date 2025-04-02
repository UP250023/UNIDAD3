#08_DayExcercise

dog = {}
dog = {'nombre',:'Yago'
'color':'negro',
'raza':'rottweiler',
'piernas': '4',
'edad': '2'}

dog = {'name':'Fanta','color':'cafe','pan':'pug','brazo':4,'age':1}


student = {'first_name':'Gael','last_name':'Cortes','cliente':'hombre', 'age':20,'marital_status':'single', 'skills':
           ['Python','SQL','C++','JS'],'country':'Mexico','city':'Aguacalientes', 'addres':{ 'streat':
        'salvador martinez','zipcode':'20126',}}


print(f'The lenght of the student dictionary is {len(student)}')
print(f'The data type of student skills is {type(student["skills"])}')


student['skills'].append('PHP')
print(student['skills'])


keyList = list(student.keys())
print(keyList)


valList = list(student.values())
print(valList)



studentTuple = student.items()
print(studentTuple)


student.pop('gender')
print(student)


del dog
