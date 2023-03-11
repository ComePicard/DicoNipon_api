import logging

import uvicorn
from requests.adapters import HTTPAdapter


def requests_adapter_cert_verify(self, *args, **kwargs):
    return


# Monkey patching du module requests pour éviter d'avoir des erreurs SSL en local
HTTPAdapter.cert_verify = requests_adapter_cert_verify

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
    )
