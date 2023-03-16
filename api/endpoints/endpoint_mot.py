from typing import Any

from fastapi import APIRouter, Path, HTTPException, Depends
from pydantic import BaseModel, Field, constr, conint

from api.dao.dao_mot import get_mot_by_id, get_all_mots, add_mot, edit_mot, delete_mot, get_mots_by_terminaison, \
    get_mot_by_id_ktk, get_mots_by_groupe, get_mots_by_type, get_mots_by_traduction

router = APIRouter(tags=["Mot"])


def valid_mot_from_path(
        id_mot: int = Path(ge=1, description="L'identifiant du mot", example=4)
) -> dict[str | Any]:
    found_mot = get_mot_by_id(id_mot)
    if found_mot is None:
        raise HTTPException(
            status_code=404,
            detail=f"Le mot d'identifiant {id_mot!r} n'a pas été trouvée"
        )
    return found_mot


class CreateMotModel(BaseModel):
    id_kanji_to_kana: int | None = Field(None, description="Id du mot dans le kanji to kana", example=4)
    mot_katakana: constr(strip_whitespace=True) | None = Field(...,
                                                               description="Ecriture du mot en katakana",
                                                               example="")
    mot_hiragana: constr(strip_whitespace=True) | None = Field(...,
                                                               description="Ecriture du mot en hiragana",
                                                               example="ひと")
    mot_kanji: constr(strip_whitespace=True) | None = Field(..., description="Ecriture du mot en kanji",
                                                            example="人")
    traduction: constr(strip_whitespace=True) = Field(..., description="Traduction du mot en français",
                                                      example="une personne, un humain")
    type: constr(strip_whitespace=True, min_length=1) = Field(..., description="Type du mot",
                                                              example="nom_commun")
    groupe: conint(ge=1, le=3) | None = Field(..., description="Groupe du verbe", example="")


class MotModel(CreateMotModel):
    id_mot: int = Field(None, description="Identifiant du mot", example=4)
    terminaison: constr(strip_whitespace=True) | None = Field(...,
                                                              description="Terminaison du mot si "
                                                                          "celui-ci est un verbe",
                                                              exemple="く")


@router.get("/liste_mots", response_model=list[MotModel], summary="Affiche tous les mots")
def get_mots():
    """
    # Get Mots

    Affiche tous les mots
    """
    return get_all_mots()


@router.get("/mot_id/{id_mot}", response_model=MotModel, summary="Affiche un mot")
def get_mot(
        mot=Depends(valid_mot_from_path)
):
    """
    # Get Mot

    Affiche un mot
    """
    return mot


@router.get("/mots_terminaison/{terminaison}", response_model=list[MotModel],
            summary="Affiche les verbes portant la terminaison")
def get_mots_terminaison(
        terminaison: str = Path(description="Terminaison du verbe", example="く")
):
    """
    # Get Mots Terminaison

    Affiche les verbes portant la terminaison
    """
    return get_mots_by_terminaison(terminaison=terminaison)


@router.get("/mots_traduction/{traduction}", response_model=list[MotModel],
            summary="Affiche le ou les mots correspondant à cette traduction")
def get_mots_traduction(
        traduction: str = Path(description="traduction du mot", example="manger")
):
    """
    # Get Mots Traduction

    Affiche le ou les mots correspondant à cette traduction
    """
    return get_mots_by_traduction(traduction=traduction)


@router.get("/mot_ktk/{id_ktk}", response_model=MotModel,
            summary="Affiche le mot basé sur son identifiant Kanji to Kana")
def get_mot_ktk(
        id_ktk: int = Path(ge=1, description="Terminaison du verbe", example=4)
):
    """
    # Get Mot Ktk

    Affiche le mot basé sur son identifiant Kanji to Kana
    """
    return get_mot_by_id_ktk(id_ktk=id_ktk)


@router.get("/mots_groupe/{groupe}", response_model=list[MotModel],
            summary="Affiche les verbes du groupe donné")
def get_mots_groupe(
        groupe: int = Path(ge=1, description="groupe du verbe", example=4)
):
    """
    # Get Mots Groupe

    Affiche les verbes du groupe donné
    """
    return get_mots_by_groupe(groupe=groupe)


@router.get("/mots_type/{type_mot}", response_model=list[MotModel],
            summary="Affiche les verbes du type donné")
def get_mots_type(
        type_mot: str = Path(description="groupe du verbe", example="verbe")
):
    """
    # Get Mots type

    Affiche les verbes du type donné
    """
    return get_mots_by_type(type_mot=type_mot)


@router.post("/mot", response_model=MotModel, summary="Crée un mot")
def post_mot(
        createMot: CreateMotModel
):
    """
    # Post mot

    Crée un mot
    """
    return add_mot(
        id_kanji_to_kana=createMot.id_kanji_to_kana,
        mot_katakana=createMot.mot_katakana,
        mot_hiragana=createMot.mot_hiragana,
        mot_kanji=createMot.mot_kanji,
        traduction=createMot.traduction,
        type=createMot.type,
        terminaison=createMot.mot_hiragana[len(createMot.mot_hiragana) - 1]
        if createMot.type.lower() == "verbe" else None,
        groupe=createMot.groupe
    )


@router.put("/mot/{id_mot}", response_model=MotModel, summary="Met à jour un mot")
def post_mot(
        createMot: CreateMotModel,
        mot=Depends(valid_mot_from_path)
):
    """
    # Put Mot

    Met à jour un mot
    """
    terminaison = createMot.mot_hiragana[len(createMot.mot_hiragana) - 1] if createMot.type.lower() == "verbe" else None

    return edit_mot(
        id_mot=mot["id"],
        id_kanji_to_kana=createMot.id_kanji_to_kana,
        mot_katakana=createMot.mot_katakana,
        mot_hiragana=createMot.mot_hiragana,
        mot_kanji=createMot.mot_kanji,
        traduction=createMot.traduction,
        type=createMot.type,
        terminaison=terminaison,
        groupe=createMot.groupe
    )


@router.delete("/mot/{id_mot}", summary="Supprime un mot")
def del_mot(
        mot=Depends(valid_mot_from_path)
):
    """
    # Del Mot

    Supprime un mot
    """
    delete_mot(id_mot=mot["id"])
