from src.models.user import User
from src.service.service_user import ServiceUser


class TestServiceUser:

        def test_add_user_sucesso(self):
            #Setup
            service = ServiceUser()
            resultado_esperado = "Usuário adicionado!"

            #Chamada
            resultado = service.add_user("Jeferson", "Analista")

            #Avaliacao
            # Avaliação
            assert resultado == resultado_esperado
            assert len(service.store.bd) == 1
            assert service.store.bd[0].name == "Jeferson"
            assert service.store.bd[0].job == "Analista"

        def test_add_user_falha(self):
            # Setup
            service = ServiceUser()
            service.add_user("Jeferson", "Analista")
            resultado_esperado = "Usuário já existe!"

            # Chamada
            resultado = service.add_user("Jeferson", "Analista")

            # Avaliação
            assert resultado == resultado_esperado
            assert len(service.store.bd) == 1

        def test_update_user_sucesso(self):
            # Setup
            service = ServiceUser()
            service.add_user("Jeferson", "Analista")
            resultado_esperado = "Usuário atualizado com sucesso!"

            # Chamada
            resultado = service.update_user("Jeferson", "Desenvolvedor")

            # Avaliação
            assert resultado == resultado_esperado
            assert service.store.bd[0].job == "Desenvolvedor"

        def test_update_user_falha(self):
            # Setup
            service = ServiceUser()
            resultado_esperado = "Usuário não encontrado!"

            # Chamada
            resultado = service.update_user("Regiane", "Gerente")

            # Avaliação
            assert resultado == resultado_esperado

        def test_get_user_by_name_sucesso(self):
            # Setup
            service = ServiceUser()
            service.add_user("Jeferson", "Analista")

            # Chamada
            usuario = service.get_user_by_name("Jeferson")

            # Avaliação
            assert isinstance(usuario, User)
            assert usuario.name == "Jeferson"
            assert usuario.job == "Analista"

        def test_get_user_by_name_falha(self):
            # Setup
            service = ServiceUser()
            resultado_esperado = "Usuário não encontrado!"

            # Chamada
            resultado = service.get_user_by_name("Regiane")

            # Avaliação
            assert resultado == resultado_esperado

        def test_get_user_by_name_parametro_invalido(self):
            # Setup
            service = ServiceUser()
            resultado_esperado = "O nome deve ser uma string"

            # Chamada
            resultado = service.get_user_by_name(123)

            # Avaliação
            assert resultado == resultado_esperado