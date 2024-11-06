immutable_var= 1,2,3,4,5,'A','b'
print(immutable_var)
#immutable_var[0]=10
#print(immutable_var) Выполнение невохможно поскольку кортеж неизменям.Так же данные в кортеже неизменямые
mutable_list=[1,2,3,4,5,'A','b']
print(mutable_list)
mutable_list[0]=10
print(mutable_list)