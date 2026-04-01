Você é um desenvolvedor Django senior trabalhando em um ERP.

## CONTEXTO:
- Arquivo: apps/vendas/models/pedido.py
- Domínio: Módulo de vendas
- Regra: Pedido não pode ser alterado após aprovação

## TAREFA:
Adicione campo 'observacoes' (TextField, opcional) no model Pedido.

## RESTRIÇÕES:
- Não modifique outros models
- Mantenha compatibilidade com migrações existentes
- Adicione help_text no campo
- Siga o padrão de docstrings do projeto

## ARQUIVOS RELACIONADOS:
- apps/vendas/models/__init__.py (pode precisar atualizar exports)
- apps/vendas/forms.py (pode precisar adicionar campo ao form)