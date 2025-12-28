# Preparacao de dados

Materiais e exercícios focados em preparar variáveis para análise e ML.

## O que foi praticado
### Encoding
- **One-hot:** `pd.get_dummies(col, prefix=...)`
- **Ordinal:** `map({categoria: ordem})`
- **Códigos numéricos:**
  - pandas: `astype('category').cat.codes`
  - sklearn: `LabelEncoder().fit_transform()`

### Transformações
- **Log:** `np.log(x + 1)`
- **Box-Cox:** `stats.boxcox(x + 1)` → retorna `(valores_transformados, lambda)`
