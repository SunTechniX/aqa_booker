import pytest

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

    @pytest.mark.parametrize("exp_id,exp_code", [(-1, 200),
                                                 ("-1", 200),
                                                 ("werweEFE", 400)])
    def test_make_pet_02(self, exp_id, exp_code):
        pet = PetApi(SERVER)
        data_json = PET_MAKE
        data_json["id"] = exp_id
        # print("\n".join([str(item) for item in str(data_json).split()]))
        resp = pet.post(EP_PET, data_json, expected_status_code=exp_code)
        print(resp)

    def test_make_pet_03(self):
        pet = PetApi(SERVER)
        PET_MAKE["id"] = 123123123
        print(PET_MAKE)
        resp = pet.post(EP_PET, PET_MAKE)
        print(resp)

    def test_make_pet_04(self):
        pet = PetApi(SERVER)
        resp = pet.post(EP_PET, PET_MAKE)
        print(f"\n{resp['name']=}")
        print(resp)
        data_json = { "id": ID,
                      "name": "Мухтаридзе"}
        print(data_json)
        resp = pet.put(EP_PET, data_json)
        print(f"{resp['name']=}")
        resp = pet.get(f"{EP_PET}/{ID}")
        print(f"{resp['name']=}")
        print(resp)
