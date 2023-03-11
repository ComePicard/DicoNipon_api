from api.dao import get_cursor


def get_all_categories():
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM categorie
        """
        cur.execute(sql)
        result = cur.fetchall()
    return result


def get_categorie_by_id(id: int, ):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM categorie
            WHERE id_categorie = %(id)s
        """
        cur.execute(sql, {"id": id})
        result = cur.fetchone()
    return result


def add_categorie(nom: str):
    with get_cursor() as cur:
        sql = """
            INSERT INTO categorie (nom_categorie)
            VALUES (
                %(nom)s
            )
            RETURNING *
        """
        cur.execute(sql, {"nom": nom})
        result = cur.fetchone()
    return result


def edit_categorie(id: int, nom: str):
    with get_cursor() as cur:
        sql = """
            UPDATE categorie
            SET nom_categorie = %(nom)s
            WHERE id_categorie = %(id)s
            RETURNING *
        """
        cur.execute(sql, {
            "id": id,
            "nom": nom
        })
        result = cur.fetchone()
    return result


def delete_categorie(id: int):
    with get_cursor() as cur:
        sql = """
            DELETE FROM categorie
            WHERE id_categorie = %(id)s
        """
        cur.execute(sql, {"id": id})
