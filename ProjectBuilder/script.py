import os
import json

TEMPLATES_FOLDER = "templates"
ENTITIES_FOLDER = os.path.join(TEMPLATES_FOLDER, "entities")
DTOS_FOLDER = os.path.join(TEMPLATES_FOLDER, "dtos")
REPOSITORIES_FOLDER = os.path.join(TEMPLATES_FOLDER, "repositories")
SECURITY_FOLDER = os.path.join(TEMPLATES_FOLDER, "security")
SERVICEIMPLEMENTS_FOLDER = os.path.join(TEMPLATES_FOLDER, "serviceimplements")
SERVICEINTERFACES_FOLDER = os.path.join(TEMPLATES_FOLDER, "serviceinterfaces")
UTIL_FOLDER = os.path.join(TEMPLATES_FOLDER, "util")
CONTROLLERS_FOLDER = os.path.join(TEMPLATES_FOLDER, "controllers")

def read_file_content(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def generate_attributes(attributes):
    return '\n'.join([f"@Column(name = \"{attribute}\")\nprivate {attributes[attribute]} {attribute};" for attribute in attributes])

def generate_dto_attributes(attributes, relationships):
    dto_attributes = [f"private {attributes[attribute]} {attribute};" for attribute in attributes]

    if relationships:
        relationship_attributes = [f"private {relationship_info['entity']} {relationship.lower()};" for relationship, relationship_info in relationships.items()]
        return '\n'.join(dto_attributes + relationship_attributes)
    else:
        return '\n'.join(dto_attributes)

def generate_relationship_attributes(relationships):
    return [f"private {relationship_info['entity']} {relationship.lower()};" for relationship, relationship_info in relationships.items()]

def generate_constructor_assignments(attributes):
    return '\n'.join([f"this.{attribute} = {attribute};" for attribute in attributes])

def create_users_entity(projectname):
    entity_content = read_file_content(os.path.join(ENTITIES_FOLDER, "user_entity_content.txt")).format(projectname=projectname)
    return entity_content

def create_role_entity(projectname):
    entity_content = read_file_content(os.path.join(ENTITIES_FOLDER, "role_entity_content.txt")).format(projectname=projectname)
    return entity_content

def create_users_dto(projectname):
    dto_content = read_file_content(os.path.join(DTOS_FOLDER, "user_dto_content.txt")).format(projectname=projectname)
    return dto_content

def create_role_dto(projectname):
    dto_content = read_file_content(os.path.join(DTOS_FOLDER, "role_dto_content.txt")).format(projectname=projectname)
    return dto_content

def create_users_repository(projectname):
    repository_content = read_file_content(os.path.join(REPOSITORIES_FOLDER, "UserRepository.txt")).format(projectname=projectname)
    return repository_content

def create_role_repository(projectname):
    repository_content = read_file_content(os.path.join(REPOSITORIES_FOLDER, "IRoleRepository.txt")).format(projectname=projectname)
    return repository_content

def create_entity_class(class_name, attributes, relationships=None):
    attributes_code = generate_attributes(attributes)
    relationships_code = generate_relationships(relationships)
    entity_template = read_file_content(os.path.join(ENTITIES_FOLDER, "entity_class_template.txt")).format(
        projectname=projectname,
        class_name=class_name,
        attributes_code=attributes_code,
        relationships_code=relationships_code,
        parameters=', '.join([f"{attributes[attribute]} {attribute}" for attribute in attributes] + [f"{relationship_info['entity']} {relationship.lower()}" for relationship, relationship_info in relationships.items()]) if relationships else ', '.join([f"{attributes[attribute]} {attribute}" for attribute in attributes]),  # Modificado aquí
        constructor_assignments='\n'.join([f"this.{attribute} = {attribute};" for attribute in attributes] + [f"this.{relationship.lower()} = {relationship.lower()};" for relationship, relationship_info in relationships.items()]) if relationships else '\n'.join([f"this.{attribute} = {attribute};" for attribute in attributes]),
        getters_setters=generate_getters_setters(attributes, relationships)
    )
    return entity_template


def create_dto_class(class_name, attributes, relationships=None):
    attributes_code = generate_dto_attributes(attributes, relationships)
    getters_setters = generate_getters_setters(attributes, relationships)

    dto_template = read_file_content(os.path.join(DTOS_FOLDER, "dto_class_template.txt")).format(
        projectname=projectname,
        class_name=class_name,
        attributes_code=attributes_code,
        getters_setters=getters_setters
    )
    return dto_template


def create_repository_interface(projectname, class_name):
    repository_template = read_file_content(os.path.join(REPOSITORIES_FOLDER, "repository_class_template.txt")).format(
        projectname=projectname,
        class_name=class_name
    )
    return repository_template

def create_service_implement(class_name, projectname, repository_name, service_interface_name, methods):
    service_implement_content = read_file_content(os.path.join(SERVICEIMPLEMENTS_FOLDER, "serviceimplements_template.txt")).format(
        projectname=projectname,
        class_name=class_name,
        repository_name=repository_name,
        service_interface_name=service_interface_name,
        methods=methods
    )
    return service_implement_content

def create_controller_class(class_name, projectname, lowercase_class_name=None):
    if lowercase_class_name is None:
        lowercase_class_name = class_name.lower()

    controller_content = read_file_content(os.path.join(CONTROLLERS_FOLDER, "controllers_template.txt")).format(
        projectname=projectname,
        class_name=class_name,
        lowercase_class_name=lowercase_class_name
    )
    return controller_content


def generate_getters_setters(attributes, relationships=None):
    getters_setters = [
        f"public {attributes[attribute]} get{attribute.capitalize()}() {{\n    return {attribute};\n}}\n\npublic void set{attribute.capitalize()}({attributes[attribute]} {attribute}) {{\n    this.{attribute} = {attribute};\n}}"
        for attribute in attributes
    ]

    if relationships:
        getters_setters += [
            f"public {relationship_info['entity']} get{relationship.capitalize()}() {{\n    return {relationship.lower()};\n}}\n\npublic void set{relationship.capitalize()}({relationship_info['entity']} {relationship.lower()}) {{\n    this.{relationship.lower()} = {relationship.lower()};\n}}"
            for relationship, relationship_info in relationships.items()
        ]

    return '\n\n'.join(getters_setters)

def generate_relationships(relationships):
    if relationships:
        relationship_code = ""
        for relationship, relationship_info in relationships.items():
            if isinstance(relationship_info, dict):
                relationship_code += f"\n@ManyToOne\n@JoinColumn(name = \"{relationship_info['join_column']}\")\nprivate {relationship_info['entity']} {relationship.lower()};\n"
            else:
                relationship_code += f"\n@ManyToOne\n@JoinColumn(name = \"{relationship_info}\")\nprivate {relationship} {relationship.lower()};\n"
        return relationship_code
    else:
        return ""

def create_project_structure(projectname, databasename):
    # Crear la carpeta raíz del proyecto
    os.makedirs(projectname, exist_ok=True)

    # Crear el archivo pom.xml
    pom_content = read_file_content(os.path.join(TEMPLATES_FOLDER, "pom.txt")).format(projectname=projectname)
    with open(os.path.join(projectname, "pom.xml"), "w") as pom_file:
        pom_file.write(pom_content)

    # Crear la estructura de directorios y archivos dentro de src/main
    src_path = os.path.join(projectname, "src", "main")
    os.makedirs(src_path, exist_ok=True)

    # Crear el directorio resources
    resources_path = os.path.join(src_path, "resources")
    os.makedirs(resources_path, exist_ok=True)

    # Crear el archivo application.properties
    application_properties_content = read_file_content(os.path.join(TEMPLATES_FOLDER, "application.properties.txt")).format(databasename=databasename)
    with open(os.path.join(resources_path, "application.properties"), "w") as app_properties_file:
        app_properties_file.write(application_properties_content)

    # Crear la estructura de directorios dentro de src/main/java/pe/edu/upc/aaw/projectname
    java_path = os.path.join(src_path, "java", "pe",
                             "edu", "upc", "aaw", projectname)
    for folder in ["controllers", "dtos", "entities", "repositories", "security", "serviceimplements", "serviceinterfaces", "util"]:
        os.makedirs(os.path.join(java_path, folder), exist_ok=True)

    # Crear el archivo CORS.java
    cors_content = read_file_content(os.path.join(UTIL_FOLDER, "CORS.txt")).format(projectname=projectname)
    with open(os.path.join(java_path, "util", "CORS.java"), "w") as cors_file:
        cors_file.write(cors_content)

    # Crear los archivos del package security
    security_files = [
        "WebSecurityConfig",
        "JwtTokenUtil",
        "JwtResponse",
        "JwtRequest",
        "JwtRequestFilter",
        "JwtAuthenticationEntryPoint"
    ]
    for filename in security_files:
        # Crear el archivo .java
        security_content = read_file_content(os.path.join(SECURITY_FOLDER, f"{filename}.txt")).format(projectname=projectname)
        with open(os.path.join(java_path, "security", f"{filename}.java"), "w") as security_file:
            security_file.write(security_content)

    # Crear archivos .java para service interfaces
    service_interface_files = [
        "IUsersService",
        "IRoleService"
    ]

    for filename in service_interface_files:
        # Crear el archivo .java
        service_interface_content = read_file_content(os.path.join(SERVICEINTERFACES_FOLDER, f"{filename}.txt")).format(projectname=projectname)
        with open(os.path.join(java_path, "serviceinterfaces", f"{filename}.java"), "w") as service_interface_file:
            service_interface_file.write(service_interface_content)

        # Crear archivos .java para service implements
    service_implement_files = [
        "JwtUserDetailsService",
        "UsersServiceImplement",
        "RoleServiceImplement"
    ]

    for filename in service_implement_files:
        # Crear el archivo .java
        service_implement_content = read_file_content(os.path.join(SERVICEIMPLEMENTS_FOLDER, f"{filename}.txt")).format(projectname=projectname)
        with open(os.path.join(java_path, "serviceimplements", f"{filename}.java"), "w") as service_implement_file:
            service_implement_file.write(service_implement_content)

    # Crear las clases de entidad
    entity_classes_content = read_file_content(os.path.join(ENTITIES_FOLDER, "entity_classes.json"))
    entity_relationships_content = read_file_content(os.path.join(ENTITIES_FOLDER, "entity_relationships.json"))

    # Convertir JSON a diccionarios
    entity_classes = json.loads(entity_classes_content)
    entity_relationships = json.loads(entity_relationships_content)

    for dto_class, attributes in entity_classes.items():
        relationships = entity_relationships.get(dto_class)
        users_dto_content = create_users_dto(projectname)
        role_dto_content = create_role_dto(projectname)
        dto_content = create_dto_class(dto_class, attributes, relationships)

        dto_path = os.path.join(java_path, "dtos", f"{dto_class}DTO.java")
        users_dto_path = os.path.join(java_path, "dtos", "UsersDTO.java")
        role_dto_path = os.path.join(java_path, "dtos", "RoleDTO.java")

        # Crear el archivo .java para DTOs
        with open(dto_path, "w") as entity_file:
            entity_file.write(dto_content)
        with open(users_dto_path, "w") as users_dto_file:
            users_dto_file.write(users_dto_content)
        with open(role_dto_path, "w") as role_dto_file:
            role_dto_file.write(role_dto_content)

    for entity_class, attributes in entity_classes.items():
        relationships = entity_relationships.get(entity_class)
        users_entity_content = create_users_entity(projectname)
        role_entity_content = create_role_entity(projectname)
        entity_content = create_entity_class(entity_class, attributes, relationships)
        repository_content = create_repository_interface(projectname, entity_class)
        users_repository_content=create_users_repository(projectname)
        role_repository_content=create_role_repository(projectname)
        service_implement_content = read_file_content(os.path.join(SERVICEIMPLEMENTS_FOLDER, "serviceimplements_template.txt")).format(projectname=projectname, class_name=entity_class)
        service_interface_content = read_file_content(os.path.join(SERVICEINTERFACES_FOLDER, "serviceinterfaces_template.txt")).format(projectname=projectname, class_name=entity_class)

        # Crear el archivo .java para entidades
        entity_path = os.path.join(java_path, "entities", f"{entity_class}.java")
        users_entity_path = os.path.join(java_path, "entities", "Users.java")
        role_entity_path = os.path.join(java_path, "entities", "Role.java")
        repository_path = os.path.join(java_path, "repositories", f"I{entity_class}Repository.java")
        users_repository_path=os.path.join(java_path, "repositories", "UserRepository.java")
        role_repository_path=os.path.join(java_path, "repositories", "IRoleRepository.java")
        service_implement_path = os.path.join(java_path, "serviceimplements", f"{entity_class}ServiceImplement.java")
        service_interface_path = os.path.join(java_path, "serviceinterfaces", f"I{entity_class}Service.java")

        with open(entity_path, "w") as entity_file:
            entity_file.write(entity_content)
        with open(users_entity_path, "w") as users_entity_file:
            users_entity_file.write(users_entity_content)
        with open(role_entity_path, "w") as role_entity_file:
            role_entity_file.write(role_entity_content)
        with open(repository_path, "w") as repository_file:
            repository_file.write(repository_content)
        with open(role_repository_path, "w") as repository_file:
            repository_file.write(role_repository_content)
        with open(users_repository_path, "w") as repository_file:
            repository_file.write(users_repository_content)
        with open(service_implement_path, "w") as service_implement_file:
            service_implement_file.write(service_implement_content)
        with open(service_interface_path, "w") as service_interface_file:
            service_interface_file.write(service_interface_content)

    # Crear archivos .java para controllers
    for entity_class, attributes in entity_classes.items():
        relationships = entity_relationships.get(entity_class)
        users_controller_content = read_file_content(os.path.join(CONTROLLERS_FOLDER, "UsersController.txt")).format(projectname=projectname)
        role_controller_content = read_file_content(os.path.join(CONTROLLERS_FOLDER, "RoleController.txt")).format(projectname=projectname)
        jwt_controller_content = read_file_content(os.path.join(CONTROLLERS_FOLDER, "JwtAuthenticationController.txt")).format(projectname=projectname)
        entity_controller_content = create_controller_class(entity_class, projectname, lowercase_class_name=entity_class.lower())

        # Crear el archivo .java
        controller_path = os.path.join(java_path, "controllers", f"{entity_class}Controller.java")
        users_controller_path = os.path.join(java_path, "controllers", "UsersController.java")
        role_controller_path = os.path.join(java_path, "controllers", "RoleController.java")
        jwt_controller_path = os.path.join(java_path, "controllers", "JwtAuthenticationController.java")

        with open(controller_path, "w") as controller_file:
            controller_file.write(entity_controller_content)
        with open(users_controller_path, "w") as users_controller_file:
            users_controller_file.write(users_controller_content)
        with open(role_controller_path, "w") as role_controller_file:
            role_controller_file.write(role_controller_content)
        with open(jwt_controller_path, "w") as jwt_controller_file:
            jwt_controller_file.write(jwt_controller_content)

# Definir los nombres de proyecto y base de datos
projectname = "etcapi"
databasename = "etcdb"

# Llamar a la función para crear la estructura del proyecto
create_project_structure(projectname, databasename)