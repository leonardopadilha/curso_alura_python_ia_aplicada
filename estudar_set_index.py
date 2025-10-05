"""
TUTORIAL: O que é o set_index() do pandas?

Este arquivo demonstra como usar o método set_index() do pandas.
O set_index() permite transformar uma coluna em índice do DataFrame.

IMPORTANTE: 
- Índice = é como um "endereço" de cada linha
- Por padrão, pandas usa números (0, 1, 2, 3...) como índice
- Com set_index(), podemos usar valores de uma coluna como índice
"""

# Importando a biblioteca pandas (necessária para trabalhar com dados)
import pandas as pd

print("=" * 60)
print("TUTORIAL: APRENDENDO O SET_INDEX() DO PANDAS")
print("=" * 60)

# PASSO 1: Carregando dados de um arquivo CSV
print("\n📁 PASSO 1: Carregando dados do arquivo reviews.csv")
print("-" * 50)

# pd.read_csv() lê um arquivo CSV e cria um DataFrame
# DataFrame = é como uma tabela do Excel, mas no Python
df = pd.read_csv("reviews.csv")

print("✅ Dados carregados com sucesso!")
print(f"📊 Total de linhas: {len(df)}")
print(f"📊 Total de colunas: {len(df.columns)}")

# PASSO 2: Visualizando o DataFrame original
print("\n📋 PASSO 2: Visualizando o DataFrame original")
print("-" * 50)

print("🔍 Primeiras 5 linhas do DataFrame:")
print(df.head())  # head() mostra apenas as primeiras 5 linhas

print(f"\n📝 Índice atual (padrão): {df.index}")
print("   👆 Por padrão, pandas usa números: 0, 1, 2, 3...")

print(f"\n📝 Colunas disponíveis: {df.columns.tolist()}")
print("   👆 Estas são as 'categorias' de dados que temos")

# PASSO 3: Usando set_index() - Transformando uma coluna em índice
print("\n🔄 PASSO 3: Usando set_index() - Transformando reviewerID em índice")
print("-" * 50)

print("💡 O que vamos fazer:")
print("   - Pegar a coluna 'reviewerID' (que tem IDs únicos)")
print("   - Transformar ela no índice do DataFrame")
print("   - Isso vai facilitar encontrar dados de usuários específicos")

# set_index() cria uma NOVA versão do DataFrame com a coluna como índice
df_indexed = df.set_index('reviewerID')

print("\n✅ DataFrame transformado!")
print("🔍 Primeiras 5 linhas do novo DataFrame:")
print(df_indexed.head())

print(f"\n📝 Novo índice: {df_indexed.index}")
print("   👆 Agora o índice são os IDs dos usuários, não mais números!")

# PASSO 4: Acessando dados usando o novo índice
print("\n🎯 PASSO 4: Acessando dados usando o novo índice")
print("-" * 50)

print("💡 Agora podemos encontrar dados de um usuário específico facilmente!")
print("   - Antes: precisávamos saber a posição (linha 0, 1, 2...)")
print("   - Agora: podemos usar o ID do usuário diretamente")

# .loc[] permite acessar dados usando o índice
reviewer_especifico = df_indexed.loc['A2FII3I2MBMUIA']

print(f"\n🔍 Dados do usuário 'A2FII3I2MBMUIA':")
print(reviewer_especifico)

# PASSO 5: Índice hierárquico (múltiplas colunas)
print("\n🏗️ PASSO 5: Criando índice hierárquico (múltiplas colunas)")
print("-" * 50)

print("💡 Índice hierárquico = usar 2 ou mais colunas como índice")
print("   - Útil quando queremos organizar dados por categoria e subcategoria")
print("   - Exemplo: organizar por usuário E produto")

# Definindo múltiplas colunas como índice
df_multi_index = df.set_index(['reviewerID', 'asin'])

print("\n✅ Índice hierárquico criado!")
print("🔍 Primeiras 5 linhas:")
print(df_multi_index.head())

print(f"\n📝 Estrutura do índice hierárquico:")
print("   👆 Agora cada linha tem 2 'endereços': (usuário, produto)")

# PASSO 6: Parâmetro drop=False
print("\n🔧 PASSO 6: Parâmetro drop=False - Mantendo a coluna original")
print("-" * 50)

print("💡 Por padrão, set_index() REMOVE a coluna do DataFrame")
print("   - drop=True (padrão): remove a coluna")
print("   - drop=False: mantém a coluna no DataFrame")

# Mantendo a coluna original no DataFrame
df_keep_column = df.set_index('reviewerID', drop=False)

print("\n✅ DataFrame com drop=False:")
print("🔍 Primeiras 5 linhas:")
print(df_keep_column.head())

print(f"\n📝 Colunas após set_index com drop=False:")
print(f"   {df_keep_column.columns.tolist()}")
print("   👆 Veja que 'reviewerID' ainda está nas colunas!")

# PASSO 7: Parâmetro inplace=True
print("\n⚡ PASSO 7: Parâmetro inplace=True - Modificando o DataFrame original")
print("-" * 50)

print("💡 Por padrão, set_index() cria uma NOVA versão do DataFrame")
print("   - inplace=False (padrão): cria uma cópia")
print("   - inplace=True: modifica o DataFrame original")

# Criando uma cópia para não perder os dados originais
df_original = df.copy()

print(f"\n📝 Índice ANTES da modificação: {df_original.index}")

# Modificando o DataFrame original
df_original.set_index('reviewerID', inplace=True)

print(f"📝 Índice DEPOIS da modificação: {df_original.index}")
print("   👆 O DataFrame original foi modificado!")

# PASSO 8: Voltando ao índice padrão
print("\n🔄 PASSO 8: Voltando ao índice padrão com reset_index()")
print("-" * 50)

print("💡 reset_index() faz o contrário do set_index()")
print("   - Transforma o índice atual de volta em uma coluna")
print("   - Cria um novo índice numérico (0, 1, 2, 3...)")

# Resetando o índice
df_reset = df_indexed.reset_index()

print("\n✅ Índice resetado!")
print(f"📝 Novo índice: {df_reset.index}")
print(f"📝 Colunas após reset: {df_reset.columns.tolist()}")
print("   👆 Agora temos o índice numérico de volta!")

# PASSO 9: Exemplos práticos de uso
print("\n🚀 PASSO 9: Exemplos práticos de uso do set_index()")
print("-" * 50)

print("💡 Agora vamos ver como usar o set_index() na prática:")

# Exemplo 1: Filtrando dados usando o índice
print("\n🎯 Exemplo 1: Encontrando reviews de usuários específicos")
print("   - Usando .loc[] para acessar múltiplos usuários")

usuarios_especificos = df_indexed.loc[['A2FII3I2MBMUIA', 'A3H99DFEG68SR']]
print("✅ Dados encontrados:")
print(usuarios_especificos[['reviewerName', 'reviewText']])

# Exemplo 2: Usando query com índice
print("\n🎯 Exemplo 2: Filtrando reviews com votos úteis")
print("   - Usando .query() para filtrar dados")

df_query = df_indexed.query("helpful_yes > 0")
print(f"✅ Encontrados {len(df_query)} reviews com votos úteis:")
print(df_query[['reviewerName', 'helpful_yes', 'total_vote']].head())

# RESUMO FINAL
print("\n" + "=" * 60)
print("📚 RESUMO: O que aprendemos sobre set_index()")
print("=" * 60)

print("""
🎯 PRINCIPAIS CONCEITOS:

1. 📊 DataFrame = tabela de dados (como Excel)
2. 📝 Índice = "endereço" de cada linha
3. 🔄 set_index() = transforma coluna em índice
4. 🎯 .loc[] = acessa dados usando o índice
5. 🔧 drop=False = mantém coluna original
6. ⚡ inplace=True = modifica DataFrame original
7. 🔄 reset_index() = volta ao índice padrão

💡 QUANDO USAR set_index():
   ✅ Quando você tem uma coluna com valores únicos (IDs, códigos)
   ✅ Quando quer acessar dados rapidamente por esse valor
   ✅ Quando quer organizar dados de forma hierárquica
   ✅ Quando quer fazer análises mais eficientes

🚀 PRÓXIMOS PASSOS:
   - Experimente com seus próprios dados
   - Teste diferentes colunas como índice
   - Combine com outras funções do pandas
""")

print("🎉 Tutorial concluído! Agora você sabe usar o set_index()!")