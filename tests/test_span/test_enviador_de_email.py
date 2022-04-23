import pytest

from span.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['felippecalcado@gmail.com', 'foo@bar.com.br']
                         )
def test_remetente(remetente):
    enviador = Enviador()

    resultado = enviador.enviar(
        remetente,
        'felippecalcado@gmail.com',
        'Curso Python Pro',
        'primeiro span criado'
    )
    assert remetente in resultado


@pytest.mark.parametrize('remetente',
                         ['felippecalcadogmail.com',
                          '']
                         )
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'felippecalcado@gmail.com',
            'Curso Python Pro',
            'primeiro span criado'
            )
