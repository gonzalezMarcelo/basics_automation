import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except: 
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1:]
    data = load_data(SAVED_DATA)

    if(command == 'save'):
        key = input("Escreve sua chave:")
        data[key] = clipboard.paste() 
        save_data(SAVED_DATA, data)
        print("O seu dado foi salvado!")

    elif (command == 'load'):
        key = input("Escreve sua chave:")
        if key in data:
            clipboard.copy(data[key])
            print("O seu dado foi copiado")
        else:
            print("Essa chave não existe")
    elif (command == 'list'):
        print(data)
    else:
        print("Comando desconhecido")
else:
    print("Por favor, passe um comando somente")