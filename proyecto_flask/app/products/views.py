from flask import Blueprint, request, Response

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/', methods=['GET', 'POST'])
def index():
    ''' Description
    params: name 
    return: Response 200
                     400
    
    '''
    if request.method == 'POST':
        return 'PYGROUP', 405


    return '<b>Página de productos</b>', 500

@products.route('/<string:name>', methods=['GET'])
def name(name):
    ''' Description
    params: name 
    return: Response 200
                     400
    
    '''

    if name != 'pygroup':
        return Response("<b>Felicitaciones! Trabajo exitoso {}</b>".format(name), status=200)
    else:
        return Response("<b>ERROR! No se puede usar el nombre pygroup</b>", status=400)


'''
Método Render_Template
Flask proporciona el método render_template() que permite 
el uso del motor de plantillas Jinja. Esto permite que la gestión HTML sea 
mucho más fácil escribiendo código HTML en archivos .html, además de 
utilizar la lógica del código HTML. Se Usarán estos archivos HTML, 
(plantillas), para crear todas las páginas de la aplicación, de igual 
forma que la página principal donde mostrará las entradas actuales del blog, 
la página de la entrada del blog, la página donde el usuario puede añadir una 
nueva entrada, etcétera.
Fuente: DigitalOcean
'''