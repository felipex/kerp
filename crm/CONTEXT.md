# apps/crm/CONTEXT.md

## Domínio
Módulo de CRM do ERP.

## Models Principais
- Cliente: Entidade principal
- Contato: Contatos do cliente (dependente)

## Regras de Negócio
* Cliente pode ser PF ou PJ
* Se for PF, deve ter CPF e RG
* Se for PJ, deve ter CNPJ
* Se for PJ, não pode ter CPF e RG
* Se for PF, não pode ter CNPJ
* CPF e CNPJ devem ser únicos
* Contato deve ter um cliente
* Cliente não pode ser excluído, fica apenas com uma marcação no campo deleted_at

## Relacionamentos Externos
* crm.Cliente (ForeignKey)