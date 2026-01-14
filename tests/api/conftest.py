import random

import pytest
from requests import HTTPError

from src.api.pet_client import PetClient
from src.models.category import Category
from src.models.pet import Pet
from src.models.tag import Tag


@pytest.fixture(scope="session")
def pet_client():
    return PetClient(base_url="https://petstore.swagger.io/v2")


@pytest.fixture()
def created_pet(pet_client, pet_with_full_body):
    response = pet_client.add_new_pet_to_store(pet_with_full_body)
    response_pet = Pet.model_validate(response.json())

    yield response_pet

    try:
        pet_client.delete_pet(response_pet.id)
    except HTTPError as e:
        if e.response.status_code == 404:
            pass
        else:
            raise e


@pytest.fixture()
def deleted_pet(pet_client, pet_with_full_body):
    response = pet_client.add_new_pet_to_store(pet_with_full_body)
    response_pet = Pet.model_validate(response.json())
    pet_client.delete_pet(response_pet.id)
    yield response_pet


# --- PET PRESETS ---

@pytest.fixture
def pet_with_full_body():
    return Pet(
        name="Ara Charlie",
        photo_urls=[
            "https://example.com/images/parrot-ara-1.jpg",
            "https://example.com/images/parrot-ara-2.jpg"
        ],
        id=random.randint(100000, 999999),
        category=Category(id=6460, name="Birds"),
        tags=[
            Tag(id=5479, name="parrot"),
            Tag(id=3572, name="talking"),
        ],
        status="available"
    )


@pytest.fixture
def pet_with_only_required_fields():
    return Pet(
        name="Ara Charlie",
        photo_urls=[
            "https://example.com/images/parrot-ara-1.jpg",
            "https://example.com/images/parrot-ara-2.jpg"
        ]
    )

# --- /// ---
