
from database.DB_connect import DBConnect
from model.hub import Hub
from model.tratta import Tratta


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_hub():
        result = []
        conn = None
        cursor = None
        try:
            conn = DBConnect.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = 'SELECT * FROM hub'
            cursor.execute(query)
            for row in cursor:
                result.append(Hub(row['id'],
                                  row['codice'],
                                  row['nome'],
                                  row['citta'],
                                  row['stato'],
                                  row['latitudine'],
                                  row['longitudine']))
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    @staticmethod
    def get_tratte_valide(threshold):
        conn = None
        cursor = None
        results=[]
        try:
            conn = DBConnect.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = (''' SELECT LEAST(h1.id, h2.id) AS hub1_id,
                                GREATEST(h1.id, h2.id) AS hub2_id,
                                h1.nome as nome1, 
                                h2.nome as nome2,
                                h1.stato as stato1, 
                                h2.stato as stato2, 
                                AVG(s.valore_merce) AS valore_medio
                        FROM spedizione s, hub h1, hub h2
                        WHERE h1.id = s.id_hub_origine AND h2.id = s.id_hub_destinazione
                        GROUP BY LEAST(h1.id,h2.id), GREATEST(h1.id,h2.id)
                        HAVING valore_medio >= %s ''')
            cursor.execute(query, (threshold,))
            for row in cursor:
                results.append(Tratta(row['hub1_id'],row['hub2_id'],row['stato1'], row['stato2'],row['nome1'], row['nome2'], row['valore_medio']))
            return results
        except Exception as e:
            print(e)
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()




