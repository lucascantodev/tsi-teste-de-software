## 🎯 Objetivo
Implementar função `validar_voucher` com suite de testes que elimina 100% dos mutantes gerados pelo `mutmut`.

## 📋 Regra de Negócio
Voucher válido para compras entre **R$ 50,00** e **R$ 500,00** (inclusive).

## 🧬 Resultados
- ✅ **12 testes** executados com sucesso
- ✅ **4/4 mutantes eliminados**
- ✅ **0 mutantes sobreviventes**

## 🚀 Como Executar
```bash
source venv/bin/activate
pytest -v
mutmut run
mutmut results
