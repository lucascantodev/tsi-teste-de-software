import pytest
import sys
import os

# Garantir que conseguimos importar nossos módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from voucher.validador import validar_voucher


class TestValidarVoucher:
    """
    Testes para a função validar_voucher.
    
    O objetivo é garantir que vouchers sejam aceitos apenas para compras 
    entre R$ 50,00 e R$ 500,00 (valores inclusos).
    """
    
    def test_cinquenta_reais_deve_ser_aceito(self):
        """Valor mínimo de R$ 50 deve ser válido"""
        assert validar_voucher(50.00) is True
    
    def test_quinhentos_reais_deve_ser_aceito(self):
        """Valor máximo de R$ 500 deve ser válido"""
        assert validar_voucher(500.00) is True
    
    def test_quarenta_e_nove_reais_deve_ser_rejeitado(self):
        """Um centavo abaixo do mínimo deve ser rejeitado"""
        assert validar_voucher(49.99) is False
    
    def test_acima_de_quinhentos_deve_ser_rejeitado(self):
        """Qualquer valor acima de R$ 500 deve ser rejeitado"""
        assert validar_voucher(500.01) is False
    
    def test_valores_proximos_ao_limite_minimo(self):
        """Testando a fronteira inferior com valores próximos"""
        # Se alguém alterar o limite de 50 para 51, esse teste vai pegar
        assert validar_voucher(50.50) is True
        # Se alguém alterar o limite de 50 para 49, esse teste vai pegar  
        assert validar_voucher(49.50) is False
    
    def test_valores_proximos_ao_limite_maximo(self):
        """Testando a fronteira superior com valores próximos"""
        # Protege contra mudanças no limite superior
        assert validar_voucher(499.50) is True
        assert validar_voucher(500.50) is False
    
    def test_nao_aceita_valores_muito_baixos(self):
        """Valores muito baixos ou negativos devem ser rejeitados"""
        assert validar_voucher(30.00) is False
        assert validar_voucher(0.0) is False
        assert validar_voucher(-10.0) is False
    
    def test_nao_aceita_valores_muito_altos(self):
        """Valores exorbitantes devem ser rejeitados"""
        assert validar_voucher(600.00) is False
        assert validar_voucher(1000.0) is False
    
    def test_valor_intermediario_deve_funcionar(self):
        """Um valor bem no meio do intervalo deve sempre funcionar"""
        valor_medio = 275.0  # Meio termo entre 50 e 500
        assert validar_voucher(valor_medio) is True
    
    def test_precisao_de_centavos(self):
        """Teste com precisão de centavos nos limites"""
        # Casos bem próximos aos limites
        assert validar_voucher(49.999999) is False
        assert validar_voucher(50.000001) is True
        assert validar_voucher(499.999999) is True
        assert validar_voucher(500.000001) is False
    
    def test_alguns_valores_comuns_de_compra(self):
        """Testando valores que pessoas realmente gastam"""
        # Valores típicos de e-commerce
        compras_validas = [75.90, 120.50, 199.99, 350.00, 450.75]
        for valor in compras_validas:
            assert validar_voucher(valor) is True, f"R$ {valor} deveria ser válido"
        
        # Valores que não deveriam passar
        compras_invalidas = [25.50, 45.00, 550.00, 1200.99]
        for valor in compras_invalidas:
            assert validar_voucher(valor) is False, f"R$ {valor} deveria ser inválido"
    
    # Testes parametrizados para cobertura sistemática
    @pytest.mark.parametrize("valor,deve_aceitar", [
        # Casos críticos nos limites
        (49.99, False),
        (50.00, True), 
        (50.01, True),
        # Alguns valores no meio
        (100.0, True),
        (250.0, True), 
        (400.0, True),
        # Limite superior
        (499.99, True),
        (500.00, True),
        (500.01, False),
    ])
    def test_casos_sistematicos(self, valor, deve_aceitar):
        """Casos de teste sistemáticos para garantir cobertura completa"""
        resultado = validar_voucher(valor)
        assert resultado is deve_aceitar, f"R$ {valor}: esperado {deve_aceitar}, obtido {resultado}"