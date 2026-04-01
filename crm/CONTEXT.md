# apps/crm/CONTEXT.md

## Domínio
Módulo de CRM do ERP.

## Models Principais
- Cliente: Entidade principal
- Contato: Contatos do cliente (dependente)

## Regras de Negócio
1. Cliente pode ser PF ou PJ
2. Contato deve ter um cliente
3. Cliente não pode ser excluído, fica apenas com uma marcação no campo deleted_at

## Relacionamentos Externos
- crm.Cliente (ForeignKey)