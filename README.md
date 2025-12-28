# Introducao_DS_EBAC

Repositório com meus estudos e exercícios de DS na EBAC, reunidos em um único projeto (monorepo).

## Conteúdos praticados
- **Pandas (EDA e manipulação):** `read_csv`, `head`, `info`, `describe`, `nunique`, `value_counts`
- **Agregações:** `groupby`, criação de métricas por categoria (freq e %)
- **Preparação de dados (features):**
  - One-hot (`pd.get_dummies`)
  - Ordinal (`map` com dicionário de ordem)
  - Códigos numéricos (`cat.codes` e `LabelEncoder`)
- **Transformações numéricas:** `log(x+1)` e **Box-Cox** (valores + `lambda`)
- **Organização do dataset:** criação/remoção de colunas (`drop(columns=[...])`)

## Estrutura
- `Python para Dados/` → fundamentos e rotinas com pandas
- `Preparacao de dados/` → encoding e transformações
- `Tratamento de dados/` → ajustes e padronizações


## Requisitos
Bibliotecas usadas nos exercícios:
- pandas
- scikit-learn
- scipy
