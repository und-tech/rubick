import click
import os

from rubick_pkg.rubick import pass_context
from rubick_pkg.utils import dir, file, format

PATTERS = {'F': 'Factory', 'S': 'Singleton'}
class_injector = {}
mock_param = {}
class_param = {}
from_container = ''
data_for_insert = {}
project_name = ''


@click.command()
# @click.option('--name', default='my_project', prompt='Ingresa el nombre de un proyecto existente',
#               help='Nombre del proyecto.')
@click.option('--resource', default='MyResource', prompt='Ingresa el nombre del recurso',
              help='Nombre del Recurso.')
@pass_context
def command(ctx, **kwargs):
    project_config_file = ctx.config['rest']['project_config_file']
    if not os.path.exists('./' + project_config_file):
        raise AttributeError('no es poible obtener el nombre del proyecto, el archivo ' +
                             project_config_file +
                             ' no existe. Ubicate dentro de tu proyecto')
    rubick_config = file.read_json('./' + project_config_file)
    project_name = rubick_config['variables']['name']

    scaffolds_route_base = ctx.config['rest']['scaffolds_route_base']
    project_route_base = ctx.config['rest']['project_route_base']
    scaffolds_name_file = ctx.config['rest']['scaffolds_name_file']
    scaffolds_context_alias = ctx.config['rest']['scaffolds_context_alias']
    kwargs['package'] = rubick_config['variables']['package']
    path_base = ctx.config['rest']['project_route_base']
    resource_name = format.convert_uppercase_to(kwargs['resource'], '_')
    container_path = ''
    handlers_path = ''
    route_file_path = ''

    scaffold_project_dir = os.path.join(ctx.scaffolds_local_repo, scaffolds_route_base)

    if dir.exists(scaffold_project_dir):
        print("== Archivos creados ==")
        for root, dirs, files in os.walk(scaffold_project_dir):
            for file_name in files:
                if scaffolds_name_file in file_name:
                    ## template content ##
                    template_content = file.read(os.path.join(root, file_name))

                    ## paths for new project ##
                    new_project_path = root.replace(scaffolds_context_alias, kwargs['package']).replace(scaffold_project_dir, '.'+path_base)
                    resource_file_name = file_name.replace(scaffolds_name_file, resource_name)
                    prepare_data(new_project_path, kwargs, path_base, resource_name)
                    new_file_path = os.path.join(new_project_path, resource_file_name)

                    ## create file ##
                    kwargs.update({'resource_name': resource_name})
                    file.create(new_file_path, template_content, **kwargs)

                    ## path ##
                    print(new_file_path)

                    if 'handlers' in new_project_path:
                        handlers_path = new_project_path.replace(path_base+project_name + project_route_base, '').replace('/', '.')[1:]
                        print('handlers_path:', handlers_path)

                if 'container' in file_name:
                    container_path = root.replace(scaffold_project_dir, os.path.join('.'+path_base))+'/'+file_name

                if 'routes' in file_name:
                    route_file_path = root.replace(scaffold_project_dir,
                                                  os.path.join('.'+path_base)) + '/' + file_name


        modify_route(route_file_path, build_router_path(handlers_path, kwargs['resource']))
        get_data_for_insert(resource_name)
        modify_container(container_path)
    else:
        print('No se encontro el directorio base para el api rest')


def build_method(*args):
    return '.'.join(args)


def build_param(*args):
    return '('+', '.join(args) + ')'


def prepare_data(new_project_path, kwargs, path_base, resource_name):
    global from_container
    from_path = new_project_path.replace('.'+path_base, '') + '/' + resource_name
    class_name = ''
    if 'mockup' in new_project_path:
        class_name = 'Mock' + kwargs['resource'] + 'Repository'
        class_injector.update({'MockRepository': class_name})

    if 'sqlalchemy' in new_project_path:
        class_name = kwargs['resource'] + 'SqlAlchemyRepository'
        class_injector.update({'Repository': class_name})

    if 'domain/services' in new_project_path:
        class_name = kwargs['resource'] + 'DomainService'
        class_injector.update({'DomainService': class_name, 'MockDomainService': class_name})
        mock_param.update({'MockDomainService': 'MockRepository'})
        class_param.update({'DomainService': 'Repository'})

    if 'application/services' in new_project_path:
        class_name = kwargs['resource'] + 'AppService'
        class_injector.update({'AppService': class_name, 'MockAppService': class_name})
        mock_param.update({'MockAppService': 'MockDomainService'})
        class_param.update({'AppService': 'DomainService'})

    if class_name:
        from_container += 'from ' + from_path[1:].replace('/', '.') + ' import ' + class_name + '\n'


def get_data_for_insert(resource_name):
    for key in class_injector:
        patter = 'S'
        params = [class_injector[key]]
        injector_param = ''

        if 'MockRepository' in key or 'MockDomain' in key:
            patter = 'F'

        if 'Repository' not in key and 'Mock' not in key:
            injector_param = format.convert_uppercase_to(class_param[key]) + ' = ' + class_param[
                key] + 'Injector.' + resource_name

        if 'Mock' in key and key in mock_param:
            injector_param = format.convert_uppercase_to(mock_param[key].replace('Mock', '')) + ' = ' + mock_param[
                key] + 'Injector.' + resource_name

        if injector_param:
            params.append(injector_param)

        data_for_insert.update({key: '    ' + resource_name + ' = ' + build_method('providers', PATTERS[patter]) + build_param(*params) + '\n'})


def modify_container(container_path):
    container_content = file.read_lines(container_path)
    container_list = list(container_content)

    for key, lines in enumerate(container_content, start=0):
        if 'class RepositoryInjector' in lines:
            container_list.insert(key - 2, from_container)

        if 'class DomainServiceInjector' in lines:
            container_list.insert(key - 1, data_for_insert['Repository'])

        if 'class AppServiceInjector' in lines:
            container_list.insert(key, data_for_insert['DomainService'])

        if 'class MockRepositoryInjector' in lines:
            container_list.insert(key - 4, data_for_insert['AppService'])

        if 'class MockDomainServiceInjector' in lines:
            container_list.insert(key + 2, data_for_insert['MockRepository'])

        if 'class MockAppServiceInjector' in lines:
            container_list.insert(key + 3, data_for_insert['MockDomainService'])

        if 'class MockAppServiceInjector' in lines:
            container_list.insert(len(container_list), data_for_insert['MockAppService'])

    container_text = ''.join(map(str, container_list))
    file.save_file(container_path, container_text)
    print('='*10, 'modify container', '='*10)
    print(container_path)


def build_router_path(handlers_path, resource):
    route_path = ''
    handlers = {'/{id}:': 'Handler', '/:': 'CollectionHandler'}
    for key in handlers:
        route_path += '  - '+key+' '+build_method(handlers_path, resource.lower(), resource+handlers[key])+'\n'
    return route_path


def modify_route(route_file_path, routes_path):
    route_content = file.read_lines(route_file_path)
    route_list = list(route_content)
    route_list.insert(len(route_list) - 1, routes_path)
    route_text = ''.join(map(str, route_list))
    file.save_file(route_file_path, route_text)
    print('=' * 10, 'modify route', '=' * 10)
    print(route_file_path)

