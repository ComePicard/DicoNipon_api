from api.dao import get_cursor


def get_all_categories_mots():
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot_categorie
        """
        cur.execute(sql)
        result = cur.fetchall()
    return result


def get_categories_of_mot(id_mot: int):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM categorie
            INNER JOIN mot_categorie
            ON categorie.id_categorie = mot_categorie.id_categorie
            WHERE id_mot = %(id_mot)s  
        """
        cur.execute(sql, {"id_mot": id_mot})
        result = cur.fetchall()
    return result


def get_mots_of_categorie(id_categorie: int, ):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot
            INNER JOIN mot_categorie
            ON mot.id_mot = mot_categorie.id_mot
            WHERE id_categorie = %(id_categorie)s
        """
        cur.execute(sql, {"id_categorie": id_categorie})
        result = cur.fetchall()
    return result


def add_mot_categorie(id_mot: int, id_categorie: int):
    with get_cursor() as cur:
        sql = """
            INSERT INTO mot_categorie (id_mot, id_categorie)
            VALUES (
                %(id_mot)s,
                %(id_categorie)s
            )
            RETURNING *
        """
        cur.execute(sql, {"id_mot": id_mot, "id_categorie": id_categorie})
        result = cur.fetchone()
    return result


def edit_mot_categorie(id_mot: int, id_categorie: int):
    with get_cursor() as cur:
        sql = """
            UPDATE mot_categorie
            SET id_categorie = %(id_categorie)s
            WHERE id_mot = %(id_mot)s
            AND id_categorie = %(id_categorie)s
            RETURNING *
        """
        cur.execute(sql, {"id_mot": id_mot, "id_categorie": id_categorie})
        result = cur.fetchone()
    return result


def delete_mot_categorie(id_mot: int, id_categorie: int):
    with get_cursor() as cur:
        sql = """
            DELETE FROM mot_categorie
            WHERE id_categorie = %(id_categorie)s
            AND id_mot = %(id_mot)s
        """
        cur.execute(sql, {"id_mot": id_mot, "id_categorie": id_categorie})
