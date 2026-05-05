from api.pet_api import PetApi
from data.pet_data_api import EP_PET, ID, PET_MAKE, SERVER


class TestApi:

    def test_make_pet_01(self):
        pet = PetApi(SERVER)
        resp = pet.post(EP_PET, PET_MAKE)
        print(resp)
        print("--------------------")

        resp = pet.get(f"{EP_PET}/{ID}")
        print(resp)
