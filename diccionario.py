from time import process_time_ns


persona={
    'nombre':'Yeferson',
    'edad':21,
    'estatura':1.73,
    'leGustaFutbol':True
}

print(persona)
print(persona['nombre'])
print(persona.get('edad'))

persona['carrera']='Ingeniero'
print(persona)
