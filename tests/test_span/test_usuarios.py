import pytest

from span.db import Conexao
from span.modelos import Usuario




@pytest.fixture
def conexao():
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    #TearDown
    conexao_obj.fechar()

@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Felippe')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)

def test_listar_usuarios(conexao,sessao):
    usuarios = [Usuario(nome='Felippe'),
                Usuario(nome='foo')] #,email='felippecalcado@gmail.com') #,email='foo@bar.com.br')

    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

