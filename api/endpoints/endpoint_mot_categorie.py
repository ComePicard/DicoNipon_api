from fastapi import APIRouter, Path
from pydantic import BaseModel, Field, conint

from api.dao.dao_mot_categorie import get_all_categories_mots, get_categories_of_mot, get_mots_of_categorie, \
    add_mot_categorie, edit_mot_categorie, delete_mot_categorie

router = APIRouter(tags=["Mot"])


class MotCategorieModel(BaseModel):
    id_mot: conint(ge=1) = Field(None, description="Identifiant du mot en BDD", example="3")
    id_categorie: conint(ge=1) = Field(None, description="Identifiant de la catégorie en BDD", example="3")


@router.get('/mots_categories', response_model=list[MotCategorieModel], summary="Renvoie la liste des liaisons "
                                                                                "mot-catégorie")
def get_categories():
    """
    # Get Categories

    Renvoie la liste de toutes les liaisons entre un mot et sa/ses catégories
    """
    return get_all_categories_mots()


@router.get('/mot_categorie/{id_mot}', response_model=list[MotCategorieModel],
            summary="Renvoie la liste des catégories liés à un mot")
def get_categories_from_mot(
        id_mot: int = Path(description="Identifiant du mot en BDD", example=4)
):
    """
    # Get Categorie From Mot

    Renvoie toutes les catégories liées au mot
    """
    return get_categories_of_mot(id_mot=id_mot)


@router.get('/mot_categorie/{id_categorie}', response_model=list[MotCategorieModel],
            summary="Renvoie la liste des mots liés à une catégorie")
def get_mots_from_categorie(
        id_categorie: int = Path(description="Identifiant de la categorie en BDD", example=4)
):
    """
    # Get Mots From Categorie

    Renvoie tous les mots liés à la catégorie
    """
    return get_mots_of_categorie(id_categorie=id_categorie)


@router.post("/mot_categorie/", response_model=MotCategorieModel, summary="Crée un lien entre un mot et une catégorie")
def post_mot_categorie(
        createMotCategorie: MotCategorieModel
):
    """
    # Post Mot Categorie

    Crée un lien entre un mot et une catégorie
    """
    return add_mot_categorie(id_mot=createMotCategorie.id_mot, id_categorie=createMotCategorie.id_categorie)


@router.put("/mot_categorie/{id_mot}/{id_categorie}", response_model=MotCategorieModel,
            summary="Met à jour le lien entre un mot et sa catégorie")
def put_mot_categorie(
        id_mot: int = Path(description="Identifiant du mot en BDD", example=4),
        id_categorie: int = Path(description="Identifiant de la catégorie en BDD", example=4)
):
    """
    # Put Mot Categorie

    Met à jour le lien entre un mot et sa catégorie
    """
    return edit_mot_categorie(id_mot=id_mot, id_categorie=id_categorie)


@router.delete("/mot_categorie/{id_mot}/{id_categorie}", summary="Supprime le lien entre un mot et sa catégorie")
def del_mot_categorie(
        id_mot: int = Path(description="Identifiant du mot en BDD", example=4),
        id_categorie: int = Path(description="Identifiant de la catégorie en BDD", example=4)
):
    """
    # Del Mot Categorie

    Supprime le lien entre un mot et une catégorie
    """
    delete_mot_categorie(id_mot=id_mot, id_categorie=id_categorie)
