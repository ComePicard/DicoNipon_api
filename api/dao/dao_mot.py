from api.dao import get_cursor


def get_all_mots():
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot
        """
        cur.execute(sql)
        result = cur.fetchall()
    return result


def get_mot_by_id(id_mot: int, ):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot
            WHERE id_mot = %(id_mot)s
        """
        cur.execute(sql, {"id_mot": id_mot})
        result = cur.fetchone()
    return result


def get_mot_by_id_ktk(id_ktk: int, ):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot
            WHERE id_kanji_to_kana = %(id_ktk)s
        """
        cur.execute(sql, {"id_ktk": id_ktk})
        result = cur.fetchone()
    return result


def get_mots_by_type(type_mot: str):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot
            WHERE type = %(type_mot)s
        """
        cur.execute(sql, {"type_mot": type_mot})
        result = cur.fetchall()
    return result


def get_mots_by_terminaison(terminaison: str):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot
            WHERE terminaison = %(terminaison)s
        """
        cur.execute(sql, {"terminaison": terminaison})
        result = cur.fetchall()
    return result


def get_mots_by_traduction(traduction: str):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot
            WHERE traduction = %(traduction)s
        """
        cur.execute(sql, {"traduction": traduction})
        result = cur.fetchall()
    return result


def get_mots_by_groupe(groupe: int):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM mot
            WHERE groupe = %(groupe)s
        """
        cur.execute(sql, {"groupe": groupe})
        result = cur.fetchall()
    return result


def add_mot(
        id_kanji_to_kana: int,
        mot_katakana: str,
        mot_hiragana: str,
        mot_kanji: str,
        traduction: str,
        type: str,
        terminaison: str,
        groupe: int
):
    with get_cursor() as cur:
        sql = """
            INSERT INTO mot (
                id_kanji_to_kana,
                mot_katakana,
                mot_hiragana,
                mot_kanji,
                traduction,
                type,
                terminaison,
                groupe
            )
            VALUES (
                %(id_kanji_to_kana)s,
                %(mot_katakana)s,
                %(mot_hiragana)s,
                %(mot_kanji)s,
                %(traduction)s,
                %(type)s,
                %(terminaison)s,
                %(groupe)s
            )
            RETURNING *
        """
        cur.execute(sql, {
            "id_kanji_to_kana": id_kanji_to_kana,
            "mot_katakana": mot_katakana,
            "mot_hiragana": mot_hiragana,
            "mot_kanji": mot_kanji,
            "traduction": traduction,
            "type": type,
            "terminaison": terminaison,
            "groupe": groupe
        })
        result = cur.fetchone()
    return result


def edit_mot(
        id_mot: int,
        id_kanji_to_kana: int,
        mot_katakana: str,
        mot_hiragana: str,
        mot_kanji: str,
        traduction: str,
        type: str,
        terminaison: str,
        groupe: int
):
    with get_cursor() as cur:
        sql = """
            UPDATE mot
            SET 
                id_kanji_to_kana = %(id_kanji_to_kana)s,
                mot_katakana = %(mot_katakana)s,
                mot_hiragana: %(mot_hiragana)s,
                mot_kanji = %(mot_kanji)s,
                traduction = %(traduction)s,
                type = %(type)s,
                terminaison = %(terminaison)s,
                groupe = %(groupe)s
            WHERE id_mot = %(id)s
            RETURNING *
        """
        cur.execute(sql, {
            "id_mot": id_mot,
            "id_kanji_to_kana": id_kanji_to_kana,
            "mot_hiragana": mot_hiragana,
            "mot_katakana": mot_katakana,
            "mot_kanji": mot_kanji,
            "traduction": traduction,
            "type": type,
            "terminaison": terminaison,
            "groupe": groupe
        })
        result = cur.fetchone()
    return result


def delete_mot(id_mot: int):
    with get_cursor() as cur:
        sql = """
            DELETE FROM mot
            WHERE id_mot = %(id_mot)s
        """
        cur.execute(sql, {"id_mot": id_mot})
