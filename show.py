def mostrar_ingredientes(ingredientes):
    print("--Su Pedido: ---")
    print(f'{ingredientes["masa"]}')
    print(f'{ingredientes["salsa"]}')
    print('Los ingredientes de su Pizza:')
    for ing in ingredientes['ingredientes']:
        print({ing})
    
    