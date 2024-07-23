"""1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).
 
Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])
"""



import numpy as np

# Daily temperature readings for a city (in degrees Celsius)
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])

#Identify hot days (temperature > 35°C) using np.where()
hot_day_indices=np.where(temperatures > 35)

#Identify cold days (temperature < 5°C) using np.where()
cold_day_indices=np.where(temperatures < 5)

#Print the results
print("Hot Days:")
print("Day\tTemperature (°C)")
for index in hot_day_indices[0]:
    print(f"{index+1}\t{temperatures[index]:.1f}")
    
print("\nCold Days:")
print("Day\tTemperature (°C)")
for index in cold_day_indices[0]:
    print(f"{index+1}\t{temperatures[index]:.1f}")


"""
Output:
Hot Days:
Day	Temperature (°C)
3	36.8
6	38.7
10	37.2

Cold Days:
Day	Temperature (°C)
11	4.0
14	-4.0
15	-12.0
"""
