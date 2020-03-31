from apng import APNG
from os.path import join

def crear_ubicacion( numero_imagenes, extension ,directorio_carpeta ):
    imagenes = []
    for i in range( numero_imagenes ):
        imagenes.append( directorio + str(i) + '.' + extension )
    return imagenes

def crear_gif( imagenes, path_guardado ):
    animacion = APNG()
    for imagen in imagenes:
        animacion.append_file( imagen, delay=20 )
    animacion.save('./test.png')

directorio = './Imagenes/dataset4/medicion_'
extension = 'jpg'

imgs = crear_ubicacion( 512, extension, directorio )
crear_gif( imgs, './prueba.png' )