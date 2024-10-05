import pandas as pd
import os

# Leggi il file CSV nella cartella corrente
# Ottieni il percorso assoluto della directory corrente
current_dir = os.path.dirname(os.path.abspath(__file__))

# Costruisci il percorso completo del file CSV
file_path = os.path.join(current_dir, 'big_5_players_stats_2023_2024.csv')

# Leggi il file CSV
df = pd.read_csv(file_path)

# # Stampa il DataFrame in console
# print(df)

# Estrai la colonna delle competizioni
competitions = df['Competition'].unique()

# Crea un nuovo DataFrame con le competizioni uniche
df_competition = pd.DataFrame(competitions, columns=['Competition'])

# # Stampa il numero di competizioni
# print(f"Numero di competizioni: {len(competitions)}")

# # Stampa il DataFrame delle competizioni
# print(df_competition)

# Crea un dizionario per memorizzare i DataFrame filtrati per ogni competizione
competition_dfs = {}

# Itera attraverso le competizioni uniche e filtra il DataFrame originale
for competition in competitions:
    competition_dfs[competition] = df[df['Competition'] == competition]

# Salva la competizione "Comp" in un DataFrame separato chiamato "leggenda"
leggenda = competition_dfs.pop('Comp', None)

# # Stampa i DataFrame filtrati per ogni competizione
# for competition, competition_df in competition_dfs.items():
#     print(f"\nDataFrame per la competizione: {competition}")
#     print(competition_df)

# # Stampa il DataFrame "leggenda" se esiste
# if leggenda is not None:
#     print("\nDataFrame per la competizione 'Comp':")
#     print(leggenda)
# else:
#     print("\nLa competizione 'Comp' non è presente nel file CSV.")

# Percorso del file Excel da creare
excel_file_path = os.path.join(current_dir, 'Stats24_Top5.xlsx')

# Crea un file Excel con un foglio per ogni competizione
with pd.ExcelWriter(excel_file_path) as writer:
    for competition, competition_df in competition_dfs.items():
        competition_df.to_excel(writer, sheet_name=competition, index=False)
    
    # Aggiungi il DataFrame "leggenda" come ultimo foglio se esiste
    if leggenda is not None:
        leggenda.to_excel(writer, sheet_name='Comp', index=False)

print(f"File Excel creato con successo: {excel_file_path}")
