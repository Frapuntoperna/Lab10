from database.DB_connect import DBConnect

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    def __init__(self):
        self.nome_filiale_origine: str = None
        self.nome_filiale_destinazione: str = None
        self.importo_totale_filiale: float = None
        self.conteggio_bonifici: int = None

    def __str__(self):
        pass

    def __hash__(self):
        pass

    def get_filiali(self):


        cnx = DBConnect.get_connection()

        if cnx is not None:
            print('cnx is not None')
            query=('''select distinct f1.nome, f2.nome, sum(importo), count(*)
                    from bonifico b, filiale f1, filiale f2
                    where b.id_filiale_destinazione =f2.id and b.id_filiale_origine = f1.id
                    group by b.id_filiale_origine, b.id_filiale_destinazione''')

            cursor = cnx.cursor()
            cursor.execute(query)

            self.lista_filiali = []
            for row in cursor:
                media = (row[2]/row[3])
                coppia=[row[0], row[1], media]
                self.lista_filiali.append(coppia)

            cursor.close()
            cnx.close()
            print(f'lista_filiali dao {self.lista_filiali}')
        else:
            print('cnx is None')

        return self.lista_filiali