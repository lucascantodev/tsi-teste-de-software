## Bibliotecas e Dependências

### Principais Dependências
```txt
pytest>=7.0.0          # Framework de testes moderno
mutmut>=2.4.0          # Ferramenta de Mutation Testing  
coverage>=7.0.0        # Análise de cobertura de código
```

### Estrutura do venv
O projeto utiliza ambiente virtual Python com as seguintes bibliotecas instaladas:

**Teste e Qualidade:**
- `pytest` - Framework principal de testes
- `mutmut` - Mutation testing# E-commerce Voucher Validator

**Disciplina:** Teste de Software  
**Professor:** Marcelo Damasceno  
**Ambiente:** WSL (Windows Subsystem for Linux)

## Sobre o Projeto

Este projeto implementa um validador de vouchers para e-commerce com foco em qualidade e robustez dos testes. O diferencial está na aplicação de Teste de Mutação (Mutation Testing) usando a ferramenta `mutmut` para garantir que os testes são realmente eficazes.

**Regra de Negócio:** Vouchers são válidos apenas para compras entre R$ 50,00 e R$ 500,00 (valores inclusive).

## Objetivos

- Aplicar Análise de Valor Limite (Boundary Value Analysis)
- Implementar Teste de Mutação para validação da qualidade dos testes
- Demonstrar uso de ferramentas profissionais de teste
- Criar suite de testes robusta que detecta alterações maliciosas no código
- Aplicar boas práticas de organização de projeto Python

## Resultados

- **12 métodos de teste** executados com sucesso
- **4/4 mutantes eliminados** (100% de eficácia)
- **0 mutantes sobreviventes**
- **100% cobertura** de código

## Ambiente de Desenvolvimento

### WSL (Windows Subsystem for Linux)
Este projeto foi desenvolvido inteiramente no **WSL com distribuição Debian**, proporcionando um ambiente Linux nativo no Windows. O WSL foi escolhido porque:

- Melhor compatibilidade com ferramentas Python de teste
- Ambiente mais estável para `mutmut`
- Comandos Unix nativos
- Performance superior para execução de testes

### Configuração do Ambiente
```bash
# WSL Debian
Python 3.11.2
pip 23.0.1
Ambiente virtual (venv)
```

## Técnicas de Teste Aplicadas

### 1. **Análise de Valor Limite**
Testes nos valores críticos (50.00, 500.00) e adjacentes para detectar erros nos limites.

### 2. **Teste de Mutação**
O `mutmut` cria versões "defeituosas" do código alterando:
- Operadores relacionais (`<=` → `<`)
- Constantes numéricas (`50.00` → `51.00`)
- Operadores lógicos (`AND` → `OR`)

### 3. **Casos de Teste Estratégicos**
- **Limites exatos**: R$ 50,00 e R$ 500,00
- **Valores adjacentes**: R$ 49,99 e R$ 500,01
- **Casos extremos**: valores negativos, zero, muito altos
- **Valores reais**: simulando compras típicas de e-commerce

### 4. **Testes Parametrizados**
Uso do `@pytest.mark.parametrize` para cobertura sistemática com múltiplos cenários.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **pytest** - Framework de testes
- **mutmut** - Ferramenta de Mutation Testing
- **coverage** - Análise de cobertura de código
- **WSL** - Ambiente de desenvolvimento Linux no Windows

## 📁 Estrutura do Projeto

```
ecommerce-voucher-validator/
├── src/
│   └── voucher/
│       ├── __init__.py
│       └── validador.py          # Função principal
├── tests/
│   ├── __init__.py
│   └── test_validador.py         # Suite de testes
├── venv/                         # Ambiente virtual
├── requirements.txt              # Dependências
├── pytest.ini                   # Configuração pytest
└── README.md                     # Documentação
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- WSL ou Linux (recomendado)

### Setup
```bash
git clone https://github.com/SEU_USUARIO/ecommerce-voucher-validator.git
cd ecommerce-voucher-validator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Executar Testes
```bash
# Testes unitários
pytest -v

# Cobertura de código
coverage run -m pytest
coverage report -m

# Análise de mutantes
mutmut run
mutmut results
```

## 📊 Exemplo de Saída do Mutmut

```
⠴ 4/4  🎉 4 🫥 0  ⏰ 0  🤔 0  🙁 0  🔇 0

All mutants killed! 🎉
```

**Tradução:** 4 mutantes criados, 4 eliminados, 0 sobreviventes = **100% de eficácia**

## 🎓 Aprendizados da Disciplina

Este projeto demonstra conceitos fundamentais da disciplina **Teste de Software**:

1. **Qualidade vs Quantidade**: Não basta ter muitos testes, eles devem ser **eficazes**
2. **Teste de Mutação**: Técnica avançada para validar a qualidade dos testes
3. **Automação**: Uso de ferramentas para análise automatizada de qualidade
4. **Cobertura Real**: Cobertura de 100% não garante testes bons - mutantes sim!
5. **Pensamento Crítico**: Antecipar possíveis falhas e criar testes defensivos

## 🔍 Casos de Teste Destacados

### Eliminação de Mutantes Específicos
```python
def test_valores_proximos_ao_limite_minimo(self):
    """Se alguém alterar o limite de 50 para 51, esse teste detecta"""
    assert validar_voucher(50.50) is True
    assert validar_voucher(49.50) is False
```

### Testes com Contexto Real
```python
def test_alguns_valores_comuns_de_compra(self):
    """Valores que pessoas realmente gastam em e-commerce"""
    compras_validas = [75.90, 120.50, 199.99, 350.00, 450.75]
    for valor in compras_validas:
        assert validar_voucher(valor) is True
```

## 📈 Métricas de Qualidade

| Métrica | Resultado |
|---------|-----------|
| Métodos de Teste | 12 |
| Execuções Totais | 20 |
| Cobertura de Código | 100% |
| Mutantes Eliminados | 4/4 (100%) |
| Mutantes Sobreviventes | 0 |

## 💡 Contribuições Acadêmicas

Este projeto serve como **referência** para:
- Estudantes aprendendo Teste de Software
- Demonstração prática de Mutation Testing
- Exemplo de aplicação de Análise de Valor Limite
- Estrutura profissional de projeto Python com testes
---

**🎯 Resultado Final:** Testes tão robustos que detectam qualquer alteração maliciosa no código, garantindo confiabilidade máxima da funcionalidade implementada.
