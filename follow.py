import json

def carregar_dados(arquivo):
    with open(arquivo, 'r') as file:
        data = json.load(file)
    usuarios = []
    # Verificar se estamos lidando com o arquivo 'following.json'
    if 'relationships_following' in data:
        for item in data['relationships_following']:
            usuarios.extend([user['value'] for user in item['string_list_data']])
    else:
        # Processar arquivos que têm a estrutura original, como 'followers.json'
        for item in data:
            if 'string_list_data' in item and isinstance(item['string_list_data'], list):
                usuarios.extend([user['value'] for user in item['string_list_data']])
    return usuarios

# Carregar dados dos seguidores e seguindo
followers = carregar_dados('followers.json')
following = carregar_dados('following.json')

# Encontrar usuários que você segue, mas que não te seguem de volta
nao_seguem_de_volta = [user for user in following if user not in followers]

if nao_seguem_de_volta:
    print(f"Usuários que você segue, mas não te seguem de volta: {nao_seguem_de_volta}")
else:
    print("Todos que você segue também te seguem.")
