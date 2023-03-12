from typing import Any

from fastapi import APIRouter, Path, HTTPException, Depends
from pydantic import BaseModel, Field, constr

from api.dao.dao_categorie import get_categorie_by_id, get_all_categories, add_categorie, edit_categorie, \
    delete_categorie

router = APIRouter(tags=["Catégorie"])


def valid_categorie_from_path(
        id_categorie: int = Path(ge=1, description="L'identifiant de la catégorie", example=4)
) -> dict[str | Any]:
    found_categorie = get_categorie_by_id(id_categorie)
    if found_categorie is None:
        raise HTTPException(
            status_code=404,
            detail=f"La catégorie d'identifiant {id_categorie!r} n'a pas été trouvée"
        )
    return found_categorie


class CreateCategorieModel(BaseModel):
    nom_categorie: constr(strip_whitespace=True, min_length=1) = Field(..., description="Le nom de la catégorie",
                                                                       example="Couleur")


class CategorieModel(CreateCategorieModel):
    id_categorie: int = Field(None, description="Identifiant de la catégorie", example=4)


@router.get("/liste_categories", response_model=list[CategorieModel], summary="Affiche toutes les catégories")
def get_categories():
    """
    # Get Categories

    Affiche toutes les catégories
    """
    return get_all_categories()


@router.get("/categorie/{id_categorie}", response_model=CategorieModel, summary="Affiche une catégories")
def get_categorie(
        categorie=Depends(valid_categorie_from_path)
):
    """
    # Get Categorie

    Affiche une catégorie
    """
    return categorie


@router.post("/categorie", response_model=CategorieModel, summary="Crée une catégorie")
def post_categorie(
        createCategorie: CreateCategorieModel
):
    """
    # Post Categorie

    Crée une catégorie
    """
    return add_categorie(nom=createCategorie.nom_categorie)


@router.put("/categorie/{id_categorie}", response_model=CategorieModel, summary="Met à jour une catégorie")
def post_categorie(
        createCategorie: CategorieModel,
        categorie=Depends(valid_categorie_from_path)
):
    """
    # Put Categorie

    Met à jour une catégorie
    """
    return edit_categorie(
        id=categorie["id"],
        nom=createCategorie.nom_categorie
    )


@router.delete("/categorie/{id_categorie}", summary="Supprime une catégorie")
def del_categorie(
        categorie=Depends(valid_categorie_from_path)
):
    """
    # Del Categorie

    Supprime une catégorie
    """
    delete_categorie(id=categorie["id"])
