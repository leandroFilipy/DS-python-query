## importa a biblioteca panda e quando for usar funções dela vou me refirir a ela como pd
import pandas as pd


print("")
print("")

## de padrão não seria mostrado para mim todas as linhas apenas algumas, então eu adicionei essa parte que obriga o pandas a mostrar todas as linhas e colunas que tiver na tabela
pd.set_option('display.max_rows', None)     
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', 1000)


## é aqui onde vai o arquivo para a análise 
df = pd.read_excel(r"Tabela final (5).xlsx", 
sheet_name = "Página1",
skiprows=1,
nrows = 8
)


## remove espaçamento para não ter chance de dar erro nos nomes
df.columns = df.columns.astype(str).str.strip()
## é aqui onde eu ponho as colunas que vão ser utilizadas para leitura
colunas_desejadas = [
    f"VALOR",
    f"TIPO_GASTOS"
]

df = df[colunas_desejadas]


## printa a planilha com todas as colunas e linha
print(df)





print("")
print("")


## aqui tira os R$ que iria causar erros quando fosse fazer a análise da coluna que contém os valores
df['VALOR'] = df['VALOR'].astype(str).str.replace('R$', '', regex=False).str.replace(',', '.', regex=False).str.strip()

## caso de algum erro na leitura de algum valor, sera mostrado um NaN
df['VALOR'] = pd.to_numeric(df['VALOR'], errors='coerce')


maiorValorPagoPorCliente = df.groupby('TIPO_GASTOS')['VALOR'].max()

print("\n=======================================================")
print("                 Qual o maior gasto               ")
print("=======================================================")
print(str(maiorValorPagoPorCliente))

