# Definição da função loginUsuario
def loginUsuario(perfil):
    # Verificação se o valor do parâmetro perfil é igual a 'admin'
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamada da função com diferentes valores como parâmetro
loginUsuario('Admin')   # Teste com 'Admin'
loginUsuario('admin')   # Teste com 'admin'
loginUsuario('User ')    # Teste com 'User '
loginUsuario('usuário')  # Teste com 'usuário'

