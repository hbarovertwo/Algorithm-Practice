"""
merges two sub arrays from a given array
arry[left....right] -> [0..mid] and [mid+1...right]
"""

def mergeSort(arr):
	if len(arr)>1:
		mid = len(arr)//2
		firsthalf = arr[:mid]
		sechalf = arr[mid:]
		
		mergeSort(firsthalf)
		mergeSort(sechalf)
		
		i,j,k = 0,0,0
		while i < len(firsthalf) and j < len(sechalf):
			if firsthalf[i] <= sechalf[j]:
				arr[k] = firsthalf[i]
				i += 1
			else:
				arr[k] = sechalf[j]
				j += 1
			k += 1
		while i < len(firsthalf):
			arr[k] = firsthalf[i]
			i += 1
			k += 1
		while j < len(sechalf):
			arr[k] = sechalf[j]
			j += 1
			k += 1

			
		
	