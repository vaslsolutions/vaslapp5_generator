from vaslapp5generator.config import *


replacements = {
    'namespace_base': 'com.vasl.ario.{module_name}'.format(module_name=module_name),
    'namespace_dto': 'api.dto.{entity_package}'.format(entity_package=entity_package),
    'namespace_adapter': 'api.adapter',
    'namespace_adapter_mapper': 'api.adapter.mapper',
    'namespace_api_adapter': 'api.adapter',
    'namespace_entity': 'dal.entity.{entity_package}'.format(entity_package=entity_package),
    'namespace_service': 'service',
    'namespace_service_mapper': 'service.mapper',

    'entity_name': entity_name,
    'entity_names': entity_names,
    'entity_variable': entity_variable,
    'entity_variables': entity_variables,
    'entity_kebab': entity_kebab,

    'collection_name': collection_name,
}


files_classes = {
    'adapter': '{entity_name}Adapter',
    'adapter_mapper': '{entity_name}AdapterMapper',
    'controller': '{entity_name}Controller',
    'dto_input': '{entity_name}InputDto',
    'dto_output': '{entity_name}Dto',
    'dto_page_query_params': '{entity_name}PageQueryParams',
    'entity': '{entity_name}',
    'repository': '{entity_name}Repository',
    'repository_custom': 'Custom{entity_name}Repository',
    'repository_custom_impl': 'Custom{entity_name}RepositoryImpl',
    'service': '{entity_name}Service',
    'service_impl': 'Simple{entity_name}Service',
    'service_mapper': '{entity_name}ServiceMapper',
}


def generate_all(name):
    for stub_file_name, java_class_name in files_classes.items():
        with open('stubs/{file_name}.java'.format(file_name=stub_file_name)) as stub_file:
            stub_file_content = str(stub_file.read())
            for key, value in replacements.items():
                stub_file_content = stub_file_content.replace('{' + key + '}', value)
            print(stub_file_content)
            # for key, value in replacements.items():
            # open('') java_class_file = stub_file.write()
    print(name)


if __name__ == '__main__':
    generate_all('PyCharm')
