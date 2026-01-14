from src.api.base_client import BaseClient
from src.models.pet import Pet


class PetClient(BaseClient):
    def add_new_pet_to_store(self, pet: Pet):
        return self.post("/pet", json=pet.model_dump(by_alias=True))

    def delete_pet(self, pet_id: int):
        return self.delete(f"/pet/{pet_id}")

    def find_pet_by_id(self, pet_id: int):
        return self.get(f"/pet/{pet_id}")

    def update_existing_pet(self, pet: Pet):
        return self.put("/pet", json=pet.model_dump(by_alias=True))
