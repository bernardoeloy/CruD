import sqlite3
 
def criar_banco():
    conn = sqlite3.connect('biblioteca_jogos.db')
    cursor = conn.cursor()
 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogos (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo    TEXT    NOT NULL,
            genero    TEXT    NOT NULL,
            plataforma TEXT   NOT NULL,
            preco     REAL    NOT NULL DEFAULT 0.0
        )
    ''')
 
    jogos_iniciais = [
        ('The Witcher 3',         'RPG',          'PC',           149.90),
        ('Red Dead Redemption 2', 'Ação/Aventura', 'PS4',          199.90),
        ('Minecraft',             'Sandbox',       'PC',            99.90),
        ('God of War',            'Ação/Aventura', 'PS5',          249.90),
        ('Hollow Knight',         'Metroidvania',  'PC',            37.99),
        ('FIFA 25',               'Esporte',       'Xbox Series X', 299.90),
        ('Elden Ring',            'RPG',           'PC',           179.90),
        ('Stardew Valley',        'Simulação',     'PC',            37.99),
        ('Hades',                 'Roguelike',     'PC',            47.99),
        ('The Legend of Zelda',   'Aventura',      'Nintendo Switch',299.90),
    ]
 
    cursor.executemany(
        "INSERT INTO jogos (titulo, genero, plataforma, preco) VALUES (?, ?, ?, ?)",
        jogos_iniciais
    )
 
    conn.commit()
    conn.close()
 
    print("Banco de dados 'biblioteca_jogos.db' criado com sucesso!")
    print(f"{len(jogos_iniciais)} jogos inseridos.")
 
if __name__ == '__main__':
    criar_banco()