def agregar_ingrediente(ingredient, eleccion):
    disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo',
                 'Jamón','Carne','Tocino','Queso']
    nuevo_ingrediente = disponibles[eleccion-1]
    print (ingredient['ingredientes'])
    if nuevo_ingrediente in ingredient['ingredientes']:
        print('El ingrediente ya existe')
    else:
        ingredient['ingredientes'].append(nuevo_ingrediente)
        print(f'Se ha agregado {nuevo_ingrediente}')

    print (ingredient)

