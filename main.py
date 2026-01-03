import pandas as pd

df_clientes = pd.read_csv('clientes.csv')
df_compras = pd.read_csv('compras.csv')

if df_clientes.isnull().sum().any() or df_compras.isnull().sum().any():
  print("Aviso: Dados Nulos detectados! Limpando registros incompletos da listagem....")
  df_clientes.dropna(inplace=True)
  df_compras.dropna(inplace=True)

df_cliente_compra = pd.merge(df_clientes, df_compras, left_on='ID', right_on='ID_Cliente')
df_cliente_compra.drop(columns=['ID_Cliente'], inplace=True)

df_inativos = df_cliente_compra[df_cliente_compra['Dias_Desde_Ultima_Visita'] > 7].copy()

def gerar_mensagem(user):
  if user['Valor_No_Carrinho'] <= 149.99:
    return f"Olá, {user['Nome']}! Parece que você esqueceu seu(a) {user['Ultimo_Produto_Visto']}. Não perca a chance, finalize sua compra!"
  elif user['Valor_No_Carrinho'] >= 150 and user['Valor_No_Carrinho'] <= 649.99:
    return f"{user['Nome']}, seu(a) {user['Ultimo_Produto_Visto']} ainda está disponível. Dê o próximo passo para garantir o seu!"
  else:
    return f"Olá, {user['Nome']}. Uma ótima escolha! Seu(a) {user['Ultimo_Produto_Visto']} está reservado para você. Conclua sua compra."

df_inativos['Mensagem'] = df_inativos.apply(gerar_mensagem, axis=1)

df_final = df_inativos[['ID', 'Nome', 'Email', 'Mensagem']]

df_final.to_csv('campanha-retencao.csv', index=False, encoding='utf-8-sig')