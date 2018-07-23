print('Hello!')

animals = ['Cat','Dog','Tiger','Deer']
domestic = animals
print(domestic)
domestic[2:4] = ['Hen','Parrot']
print(domestic)
domesticbirds = domestic[2:]
domesticanimals = domestic[:2]
print(domesticbirds[0]+', ' + domesticbirds[1] +' & '+ domesticanimals[0]+', ' + domesticanimals[1])
