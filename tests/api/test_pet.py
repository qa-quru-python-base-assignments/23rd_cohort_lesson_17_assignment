from src.models.pet import Pet


def test_create_pet_with_full_body_returns_200(pet_client, pet_with_full_body):
    # Act
    response = pet_client.add_new_pet_to_store(pet_with_full_body)

    # Assert
    assert response.status_code == 200
    assert Pet.model_validate(response.json())

    # Cleanup
    pet_client.delete_pet(pet_with_full_body.id)


def test_create_pet_with_required_fields_only_returns_200(pet_client, pet_with_only_required_fields):
    # Act
    response = pet_client.add_new_pet_to_store(pet_with_only_required_fields)

    # Assert
    assert response.status_code == 200
    assert Pet.model_validate(response.json())

    # Cleanup
    pet_client.delete_pet(response.json()["id"])


def test_get_existing_pet_returns_correct_data_types(pet_client, created_pet):
    # Act
    response = pet_client.find_pet_by_id(created_pet.id)

    # Assert
    assert response.status_code == 200
    returned_pet = Pet.model_validate(response.json())
    assert returned_pet.id == created_pet.id


def test_update_pet_status_to_sold_returns_updated_body(pet_client, created_pet):
    # Act
    created_pet.status = "sold"
    response = pet_client.update_existing_pet(created_pet)

    # Assert
    assert response.status_code == 200
    assert Pet.model_validate(response.json())
    returned_pet = pet_client.find_pet_by_id(created_pet.id)
    assert returned_pet.json()["status"] == "sold"


def test_delete_existing_pet_returns_success_message(pet_client, created_pet):
    # Act
    response = pet_client.delete_pet(created_pet.id)

    # Assert
    assert response.status_code == 200
    response = pet_client.find_pet_by_id(created_pet.id)
    actual_status_code = response.status_code
    assert actual_status_code == 404


def test_get_non_existent_pet_returns_404_error(pet_client, deleted_pet):
    # Act
    response = pet_client.find_pet_by_id(deleted_pet.id)

    # Assert
    assert response.status_code == 404
