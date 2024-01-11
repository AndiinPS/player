import sqlite3

# Conectar ao banco de dados 
conn = sqlite3.connect('music_player.db')

# Criar um cursor para interagir com o banco de dados
cursor = conn.cursor()

# Criar a tabela para as músicas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS musicas (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        artista TEXT,
        album TEXT
    )
''')

# Exemplo de inserção de uma música
cursor.execute('''
    INSERT INTO musicas (nome, artista, album) 
    VALUES ('Nome da Música', 'Nome do Artista', 'Nome do Álbum')
''')

# Salvar as alterações e fechar a conexão com o banco de dados
conn.commit()
conn.close()
