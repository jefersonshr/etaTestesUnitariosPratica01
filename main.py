from src.models.user import User
from src.service.service_user import ServiceUser

service = ServiceUser()

# Incluir
resultado = service.add_user("Jeferson", "Analista")
print(resultado)
print(service.store.bd[0].name)
print(service.store.bd[0].job)

# Buscar usuário existente
usuario = service.get_user_by_name("Jeferson")
print(usuario.name if isinstance(usuario, User) else usuario)

# Buscar usuário inexistente
usuario = service.get_user_by_name("Regiane")
print(usuario)

# Adicionar outro usuário
resultado = service.add_user("Regiane", "Gerente")
print(resultado)

# Buscar novo usuário
usuario = service.get_user_by_name("Regiane")
print(usuario.name if isinstance(usuario, User) else usuario)

# Atualizar usuário existente
resultado = service.update_user("Jeferson", "Desenvolvedor")
print(resultado)
print(service.store.bd[0].name)
print(service.store.bd[0].job)

# Atualizar usuário inexistente
resultado = service.update_user("Regiane", "Gerente")
print(resultado)

# Incluir outro usuário
resultado = service.add_user("Regiane", "Gerente")
print(resultado)
print(service.store.bd[1].name)
print(service.store.bd[1].job)

# Atualizar novo usuário
resultado = service.update_user("Regiane", "Diretora")
print(resultado)
print(service.store.bd[1].name)
print(service.store.bd[1].job)

# Remover
resultado = service.remove_user("Jeferson", "Desenvolvedor")
print(resultado)

