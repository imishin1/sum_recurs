#суммирование элементов массива рекурсией
def summ (massiv):
	#базовый случай
	if len(massiv) == 1 or 0: 
		return massiv[len(massiv)-1]
	#рекурсивный случай
	else:
		return massiv[len(massiv)-1] + summ(massiv[0 : (len(massiv)-1)]) 