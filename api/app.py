from fastapi import FastAPI

from api.dao import get_pool
from api.endpoints import router
from api.endpoints.endpoint_categorie import router as router_categorie
from api.endpoints.endpoint_mot import router as router_mot
from api.version import __version__ as git_version


def make_app() -> FastAPI:
    _app = FastAPI(
        title="MV-FLOW-LP-API",
        version=git_version,
        root_path="/",
        swagger_ui_parameters={  # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
            "defaultModelsExpandDepth": 0,
            "docExpansion": "none",
            "syntaxHighlight.theme": "tomorrow-night",
            "tryItOutEnabled": True,
            "requestSnippetsEnabled": True,
        },
    )

    @_app.on_event("startup")
    def initialize_bdd_pool():
        get_pool()

    @_app.on_event("shutdown")
    def close_pool():
        cnx = get_pool()
        print("Fermeture de la piscine de connexions ❌")
        cnx.closeall()

    _app.include_router(router_categorie)
    _app.include_router(router_mot)
    _app.include_router(router)

    return _app
