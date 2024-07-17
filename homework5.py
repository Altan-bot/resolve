immutable_var=(5,'Green',1.9,True)
print(immutable_var)
immutable_var[0]=3
#В кортеж нельзя добавить или удалить список потому что он содержит не сам список, а ссылку на него.
#И кортеж занимает меньше памяти.
mutable_list=[5,'Green',1.9,True]
mutable_list[0]=8
print(mutable_list)