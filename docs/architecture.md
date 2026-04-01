
# Stack Tecnológica - Backend & Core

| Camada | Tecnologia | Justificativa |
| :--- | :--- | :--- |
| Linguagem | Python 3.14+ | Tipagem moderna, ecossistema robusto |
| Framework Web | Django 6.x | "Baterias inclusas", segurança, admin, ORM |
| Banco de Dados | PostgreSQL 15+ | Confiabilidade, JSONB, transações ACID |
| ORM | Django ORM (Models) | Produtividade, migrations, integração nativa |
| Arquitetura | DDD Pragmático | Models ricos + Service Layer para regras complexas |
| Cache | Redis | Sessões, cache de queries, filas (Celery) |
| Filas/Tasks | Celery + Redis | Processamento assíncrono (emails, relatórios) |

┌─────────────────────────────────────────────────────────────┐
│                        CLIENTES (SaaS)                      │
│                    (Qualquer IP, 2FA opcional)              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Cloudflare / WAF                       │
│                  (DDoS, Rate Limit, SSL)                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                        Nginx (Proxy)                        │
│          /app/* → Django  |  /static/* → Arquivos           │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────────┐
│   Django App (Gunicorn) │     │   Admin Interno (Restrito)  │
│   - HTMX + Tailwind     │     │   - IP Whitelist + VPN      │
│   - Alpine.js           │     │   - 2FA Obrigatório         │
│   - Service Layer       │     │   - django-unfold           │
└─────────────────────────┘     └─────────────────────────────┘
              │                               │
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────────┐
│     PostgreSQL (DB)     │     │      Redis (Cache/Filas)    │
│   - Multi-Tenant Data   │     │   - Celery Tasks            │
│   - Simple History      │     │   - Session Storage         │
└─────────────────────────┘     └─────────────────────────────┘

Tailwind CSS + DaisyUI (visual moderno e profissional)
django-htmx (integração obrigatória)
Alpine.js (interatividade complementar)
django-crispy-forms (forms rápidos e bonitos)
DataTables/Tom Select/Flatpickr (componentes específicos de ERP)