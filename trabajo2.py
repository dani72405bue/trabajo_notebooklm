# programa de "EL JEFE FINAL"
compañeros = ["andres", "diego", "stevan", "juandacho", "daniel"]

edades = [15, 16, 14, 14, 15]

música = ["salsa", "cumbia", "rock", "phonk", "pop"]

# promedio de edades 

promedio = sum(edades) / len(compañeros)
print ("tu promedio de edades es:", promedio)

# mayores de 15

mayores = [edad for edad in edades if edad > 15]
print ("edades > 15:", mayores)

# fans del rock

fans_rock = [gen for gen in música if gen == "rock"]
print("total de gente que les gusta el rock es:", len(fans_rock))