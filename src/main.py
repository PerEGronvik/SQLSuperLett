import sqlite3

def kjor_sql_kommando(conn, kommando):
    try:
        cursor = conn.cursor()
        cursor.execute(kommando)

        if kommando.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            conn.commit()
            return None
    except sqlite3.Error as e:
        print(f"Det har oppstått en feil: {e}")

def liste_tabeller(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabeller = cursor.fetchall()
    print("\nTabeller i databasen:")
    for tabell in tabeller:
        print(tabell[0])

def endre_eller_opprett_database(conn):
    if conn:
        conn.commit()
        conn.close()

    db_navn = input("\n\n----Velkommen til SQL SuperLett et program av Per-Erik Grønvik---- \n\nLegg evt en databasefil i src-mappen for å bruke denne.\n\nSkriv navnet på databasen du ønsker å koble til eller å opprette: ")
    return sqlite3.connect(db_navn), db_navn

def vis_kommandoer():
    kolonne_bredde = 15
    print("\nKommandoer:\n")
    print(f"{'database':<{kolonne_bredde}} - Navigere til/opprette en ny database")
    print(f"{'tabeller':<{kolonne_bredde}} - List alle tabeller i databasen")
    print(f"{'exit':<{kolonne_bredde}} - for å avslutte.")
    print(f"{'hjelp':<{kolonne_bredde}} - for å få tips og råd om SQL-spørringer")

def vis_hjelpetekst():
    kolonne_bredde = 15
    print("\nHjelp for SQL SuperLett:")
    print(f"{'SELECT':<{kolonne_bredde}} - for å hente data.")
    print(f"{'INSERT INTO':<{kolonne_bredde}} - for å legge til data.")
    print(f"{'UPDATE':<{kolonne_bredde}} - for å endre eksisterende data.")
    print(f"{'DELETE FROM':<{kolonne_bredde}} - for å slette data.")
    print("Eksempel: SELECT fornavn, etternavn FROM Ansatt")


def main():
    conn = None
    conn, db_navn = endre_eller_opprett_database(conn)
    vis_kommandoer()

    while True:
        sql_kommando = input(f"\nSkriv en SQL kommando i databasen {db_navn}: ")

        if sql_kommando.lower() == 'exit':
            print("\nAvslutter programmet...")
            break
        elif sql_kommando.lower() == 'database':
            conn, db_navn = endre_eller_opprett_database(conn)
            vis_kommandoer()
        elif sql_kommando.lower() == 'hjelp':
            vis_hjelpetekst()
        elif sql_kommando.lower() == 'tabeller':
            liste_tabeller(conn)
        else:
            resultater = kjor_sql_kommando(conn, sql_kommando)
            if resultater is not None:
                for rad in resultater:
                    print(rad)

    if conn:
        conn.commit()
        conn.close()

if __name__ == "__main__":
    main()
