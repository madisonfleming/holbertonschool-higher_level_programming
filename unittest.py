import unittest
from app import create_app

class TestAPIEndpoints(unittest.TestCase):
    """Unittests for Users, Amenities, Places, and Reviews"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    # USER TESTS
    def test_user_crud(self):
        # CREATE
        create_res = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(create_res.status_code, 201)
        data = create_res.get_json()
        self.assertIn("id", data)
        self.assertIn("email", data)
        user_id = data["id"]

        # GET
        get_res = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(get_res.status_code, 200)
        self.assertIn("first_name", get_res.get_json())

        # UPDATE
        update_res = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "Updated",
            "last_name": "Doe",
            "email": "updated@example.com"
        })
        self.assertEqual(update_res.status_code, 200)
        self.assertEqual(update_res.get_json().get("first_name"), "Updated")

        # INVALID CREATE
        invalid_res = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "email": "invalid"
        })
        self.assertEqual(invalid_res.status_code, 400)
        self.assertIn("error", invalid_res.get_json())

        # NOT FOUND
        not_found_res = self.client.get('/api/v1/users/doesnotexist')
        self.assertEqual(not_found_res.status_code, 404)

    # AMENITY TESTS
    def test_amenity_crud(self):
        # CREATE
        create_res = self.client.post('/api/v1/amenities/', json={"name": "Wi-Fi"})
        self.assertEqual(create_res.status_code, 201)
        data = create_res.get_json()
        self.assertIn("id", data)
        amenity_id = data["id"]

        # GET
        get_res = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(get_res.status_code, 200)
        self.assertIn("name", get_res.get_json())

        # UPDATE
        update_res = self.client.put(f'/api/v1/amenities/{amenity_id}', json={"name": "Air Conditioning"})
        self.assertEqual(update_res.status_code, 200)
        self.assertEqual(update_res.get_json().get("name"), "Air Conditioning")

        # INVALID CREATE
        invalid_res = self.client.post('/api/v1/amenities/', json={"name": ""})
        self.assertEqual(invalid_res.status_code, 400)
        self.assertIn("error", invalid_res.get_json())

        # NOT FOUND
        not_found_res = self.client.get('/api/v1/amenities/doesnotexist')
        self.assertEqual(not_found_res.status_code, 404)

    # PLACE TESTS
    def test_place_crud(self):
        # CREATE
        create_res = self.client.post('/api/v1/places/', json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(create_res.status_code, 201)
        data = create_res.get_json()
        self.assertIn("id", data)
        self.assertIn("title", data)
        place_id = data["id"]

        # GET
        get_res = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(get_res.status_code, 200)
        self.assertIn("description", get_res.get_json())

        # UPDATE
        update_res = self.client.put(f'/api/v1/places/{place_id}', json={
            "title": "Updated Apartment",
            "description": "An even nicer place",
            "price": 120.0
        })
        self.assertEqual(update_res.status_code, 200)
        self.assertEqual(update_res.get_json().get("title"), "Updated Apartment")

        # INVALID CREATE
        invalid_res = self.client.post('/api/v1/places/', json={
            "title": "",
            "price": -10
        })
        self.assertEqual(invalid_res.status_code, 400)
        self.assertIn("error", invalid_res.get_json())

        # NOT FOUND
        not_found_res = self.client.get('/api/v1/places/doesnotexist')
        self.assertEqual(not_found_res.status_code, 404)

    # REVIEW TESTS
    def test_review_crud(self):
        # CREATE
        create_res = self.client.post('/api/v1/reviews/', json={
            "text": "Great stay!",
            "rating": 5,
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "place_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(create_res.status_code, 201)
        data = create_res.get_json()
        self.assertIn("id", data)
        review_id = data["id"]

        # GET
        get_res = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(get_res.status_code, 200)
        self.assertIn("text", get_res.get_json())

        # DELETE
        delete_res = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertIn(delete_res.status_code, [200, 204])

        # INVALID CREATE
        invalid_res = self.client.post('/api/v1/reviews/', json={
            "text": "",
            "rating": 10,
            "user_id": "",
            "place_id": ""
        })
        self.assertEqual(invalid_res.status_code, 400)
        self.assertIn("error", invalid_res.get_json())

        # NOT FOUND
        not_found_res = self.client.get('/api/v1/reviews/doesnotexist')
        self.assertEqual(not_found_res.status_code, 404)
