DOMAIN = "http://localhost:8100"
SERVER = DOMAIN + "/api/v3"
# DOMAIN = "https://petstore.swagger.io"
# SERVER = DOMAIN + "/v2/pet"
EP_PET = "/pet"

ID = 2220000777
PET_MAKE = \
{ "id": ID,
  "name": "Мухтар",
  "category": {"id": 1,
               "name": "Dogs"},
  "photoUrls": ["string"],
  "tags": [{ "id": 0,
             "name": "string"}],
  "status": "available"
}
