# import argparse
# parser = argparse.ArgumentParser(
#                     prog='BootcampDemo',
#                     description='Manejo de listas de misiones y estados.',
#                     epilog='todos los derechos reservados.')

# # simil a función(valor)
# parser.add_argument('posicional', type=str, help='se envia posicionalmente')

# # simil a función(variable=valor)
# parser.add_argument('-o', '--nombre_opcion',type=int, help='opción que toma un valor')

# args = parser.parse_args()
# print(args)

import argparse
import yaml
import os


class file:
    
    @classmethod 
    def read_file(cls,path_file: str) -> str: 
        with open(path_file) as file:
            return file.read()

def cargar_listas_desde_archivo(archivo):
    with open(archivo, 'r') as file:
        datos = yaml.safe_load(file)
        return datos.get('misiones', []), datos.get('estados', [])

def guardar_listas_en_archivo(archivo, misiones, estados):
    datos = {'misiones': misiones, 'estados': estados}
    with open(archivo, 'w') as file:
        yaml.dump(datos, file)

def main():
    

    parser = argparse.ArgumentParser(
                    prog='BootcampDemo',
                    description='Manejo de listas de misiones y estados.',
                    epilog='todos los derechos reservados.')
    
    #parser.add_argument('--archivo', default='listas.yaml', help='Archivo YAML que contiene las listas')
    parser.add_argument('--a', type=str, help='Elemento a añadir a la lista')
    parser.add_argument('--d', type=str, help='Elemento a quitar de la lista')
    parser.add_argument('--ls', choices=["misiones", "estados"], help='Especificar la lista o elemeto.  a la que afectar')

    # Parsear los argumentos de la línea de comandos
    args = parser.parse_args()
    
    # Cargar listas desde el archivo YAML
    path: str = os.path.join("../","setting","configuration_file.yaml")
    dats: dict = yaml.load(file.read_file(path), Loader=yaml.FullLoader)
        
    misiones = dats["mission"]
    estados = dats["device_status"]


    if not args.lista:
        print('Debes especificar la lista a la que afectar.')
        return


    if args.lista == 'misiones':
        print(f'Lista de misiones actual: {misiones}')
    elif args.lista == 'estados':
        print(f'Lista de estados actual: {estados}')


    if args.agregar:
        if args.lista == 'misiones':
            misiones.append(args.agregar)
        elif args.lista == 'estados':
            estados.append(args.agregar)
        print(f'Elemento añadido a la lista {args.lista}: {args.agregar}')


    if args.quitar:
        if args.lista == 'misiones' and args.quitar in misiones:
            misiones.remove(args.quitar)
            print(f'Elemento quitado de la lista misiones: {args.quitar}')
        elif args.lista == 'estados' and args.quitar in estados:
            estados.remove(args.quitar)
            print(f'Elemento quitado de la lista estados: {args.quitar}')
        else:
            print(f'Elemento no encontrado en la lista {args.lista}: {args.quitar}')


    if args.lista == 'misiones':
        print(f'Lista de misiones actualizada: {misiones}')
    elif args.lista == 'estados':
        print(f'Lista de estados actualizada: {estados}')

if __name__ == '__main__':
    main()
    