import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from src.app import create_app
from src.database.models import setup_db, Movie, Actor

unittest.defaultTestLoader.sortTestMethodsUsing = None

class CastrTestCase(unittest.TestCase):
    # """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.TEST_TOKEN_CASTING_ASSISTANT = "Bearer {}".format('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDNjZGE3OGI3YTAwNzA2YmU2ZGUiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2Mzc3MDQxODUsImV4cCI6MTYzNzc5MDU4NSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.ASL8H1iNqn8-ve6UFwkpLRTMhi04T_B6sCuopivhyZlKqjU-ZLOPOZZCpTyTfgSS88dsMZWAkNX8nrEH1qrgcDo8M_-aY8d491Nbx5YewwK0MUAAvHoM5G_X42ogB6kdgPLQgbCTvTGky3UnUQK5-hlL5n5pMBthv09UyZX5AyDEgYCs2DshfutgbfCNA096qi-0yl05nogeNE_IrS8dD0M3-pyU8jUDTRtY47fIK38Kh0lJJcsdR-a_pgr9JeUvYtb1R0pWoT6DDutcrm0AL0Cze08AfLhyWvvi8izFTjc7Gy6E88Q_2shtqqBndaoSIvkvLzGjboADk2eNXi8qIw')
        self.TEST_TOKEN_CASTING_DIRECTOR = "Bearer {}".format('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDRiYjJhNDRlYjAwNjkwNDdlMTEiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2Mzc3MDQzNTIsImV4cCI6MTYzNzc5MDc1MiwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.ADfv8GfzKin9KjU1dfY8nMQS1pC2g3DDwxPM6UcSUl-2KcDETrHDfPdY6PbBr8_fpjLJ4tk6VkBB9uLby30K3YZLCdC2eITl6jj_1LPnuwIVyffQL5I-VPoyoYW478OhHvy1caQteQgop_wGY5Gsa7n3mLEIQFiFyDKVRFrrE_-YjIKl814zp898s6qIWy71Hq2mIm7oWoEOatVbMUifFTQLytUwXKgPDynbCEDwovzNIs7dlBL2psHXbgjGtORGH5mFUTq9-_TVMFHiYXl87I2FcpTxKWdOkeXQ8HC19jrKmcjwwJnnbPzaHOpvDkfQdu8r0V7LzOXuo2qwd02-jg')
        self.TEST_TOKEN_EXECUTIVE_PRODUCER = "Bearer {}".format('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2Mzc3MDQ0ODgsImV4cCI6MTYzNzc5MDg4OCwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.PFDVxuquWuAcKjUnI_DPMTR7Im7caV0_ZxtrkYI56hz4AxaLsBHeU-kPzmrtxNiC48jstDYLqDSMOIEmm7eLW6Zpm54lidY_YLRpHUdzwuJKy7wznAgC8GustT4uag2swGeoSsZiqEmL2b8K0rrea4hG6VxA8EXH7NR9WIexvTFdDtKbTCeeTDMSaYNR_mYgETkZcn6ISKRc79SJ9xiELGdx2jtRXVb6IY1W6baGdq_rIt8rQydsRINir3ZTFbT1D5oNYWxfki97YfvehD1FGU9DVSsBvUxGliZpsvevYNj47SyeKbe5Q8f0r4AN_5KTnZDqj6ZQ84fF7flpUcixLw')

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "castr_test"
        self.database_path = "postgresql://{}{}/{}".format('postgres:admin@', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass


# TESTS FOR EXECUTIVE PRODUCER
# reminder: executive producers MAY view, update, delete, or add new movies and actors
#
#   TESTS FOR EXECUTIVE PRODUCER:MOVIES
#   {{POST requests}}
    def test_01_EXECUTIVE_PRODUCER_200_post_valid_movie(self):
        res = self.client().post('http://127.0.0.1:5000/movies', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

#   {{GET requests}}
    def test_02_EXECUTIVE_PRODUCER_200_get_movies(self):
        res = self.client().get('http://127.0.0.1:5000/movies', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_03_EXECUTIVE_PRODUCER_200_get_individual_movies(self):
        res = self.client().get('http://127.0.0.1:5000/movies/1', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_04_EXECUTIVE_PRODUCER_404_get_nonexistent_movie(self):
        res = self.client().get('http://127.0.0.1:5000/movies/a', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{PATCH requests}}
    def test_05_EXECUTIVE_PRODUCER_200_patch_valid_movie(self):
        res = self.client().patch('http://127.0.0.1:5000/movies/1', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_06_EXECUTIVE_PRODUCER_404_patch_nonexistent_movie(self):
        res = self.client().patch('http://127.0.0.1:5000/movies/a', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{DELETE requests}}
    def test_07_EXECUTIVE_PRODUCER_200_delete_valid_movie(self):
        res = self.client().delete('http://127.0.0.1:5000/movies/1', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_08_EXECUTIVE_PRODUCER_404_delete_nonexistent_movie(self):
        res = self.client().delete('http://127.0.0.1:5000/movies/a', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   TESTS FOR EXECUTIVE PRODUCER:ACTORS
#   {{POST requests}}
    def test_09_EXECUTIVE_PRODUCER_200_post_valid_actor(self):
        res = self.client().post('http://127.0.0.1:5000/actors', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

#   {{get requests}}
    def test_10_EXECUTIVE_PRODUCER_200_get_actors(self):
        res = self.client().get('http://127.0.0.1:5000/actors', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_11_EXECUTIVE_PRODUCER_200_get_individual_movies(self):
        res = self.client().get('http://127.0.0.1:5000/actors/1', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_12_EXECUTIVE_PRODUCER_404_get_nonexistent_actor(self):
        res = self.client().get('http://127.0.0.1:5000/actors/a', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{PATCH requests}}
    def test_13_EXECUTIVE_PRODUCER_200_patch_valid_actor(self):
        res = self.client().patch('http://127.0.0.1:5000/actors/1', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_14_EXECUTIVE_PRODUCER_404_patch_nonexistent_actor(self):
        res = self.client().patch('http://127.0.0.1:5000/actors/a', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{DELETE requests}}
    def test_15_EXECUTIVE_PRODUCER_200_delete_valid_actor(self):
        res = self.client().delete('http://127.0.0.1:5000/actors/1', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_16_EXECUTIVE_PRODUCER_404_delete_nonexistent_actor(self):
        res = self.client().delete('http://127.0.0.1:5000/actors/a', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')


# TESTS FOR CASTING DIRECTOR
# reminder: casting directors MAY view, update, delete, and add new actors
# They MAY also view and update movies, but they MAY NOT add or delete movies
#
#   TESTS FOR CASTING DIRECTOR:MOVIES
#   {{POST requests}}
    def test_17_CASTING_DIRECTOR_403_post_movie_invalid_permissions(self):
        res = self.client().post('http://127.0.0.1:5000/movies', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

#   {{GET requests}}
    def test_18_CASTING_DIRECTOR_200_get_movies(self):
        self.client().post('http://127.0.0.1:5000/movies', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        # In order to test the GET calls below, it is necessary to successfully POST to the table

        res = self.client().get('http://127.0.0.1:5000/movies', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_19_CASTING_DIRECTOR_200_get_individual_movies(self):
        res = self.client().get('http://127.0.0.1:5000/movies/2', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_20_CASTING_DIRECTOR_404_nonexistent_movie(self):
        res = self.client().get('http://127.0.0.1:5000/movies/a', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{PATCH requests}}
    def test_21_CASTING_DIRECTOR_200_patch_valid_movie(self):
        res = self.client().patch('http://127.0.0.1:5000/movies/2', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_22_CASTING_DIRECTOR_404_patch_nonexistent_movie(self):
        res = self.client().patch('http://127.0.0.1:5000/movies/a', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{DELETE requests}}
    def test_23_CASTING_DIRECTOR_403_delete_movie_invalid_permissions(self):
        res = self.client().delete('http://127.0.0.1:5000/movies/2', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

#   TESTS FOR CASTING DIRECTOR:ACTORS
#   {{POST requests}}
    def test_24_CASTING_DIRECTOR_200_post_valid_actor(self):
        res = self.client().post('http://127.0.0.1:5000/actors', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

#   {{get requests}}
    def test_25_CASTING_DIRECTOR_200_get_actors(self):
        res = self.client().get('http://127.0.0.1:5000/actors', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_26_CASTING_DIRECTOR_200_get_individual_movies(self):
        res = self.client().get('http://127.0.0.1:5000/actors/2', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_27_CASTING_DIRECTOR_404_get_nonexistent_actor(self):
        res = self.client().get('http://127.0.0.1:5000/actors/a', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{PATCH requests}}
    def test_28_CASTING_DIRECTOR_200_patch_valid_actor(self):
        res = self.client().patch('http://127.0.0.1:5000/actors/2', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_29_CASTING_DIRECTOR_404_patch_nonexistent_actor(self):
        res = self.client().patch('http://127.0.0.1:5000/actors/a', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{DELETE requests}}
    def test_30_CASTING_DIRECTOR_200_delete_valid_actor(self):
        res = self.client().delete('http://127.0.0.1:5000/actors/2', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_31_CASTING_DIRECTOR_404_delete_nonexistent_actor(self):
        res = self.client().delete('http://127.0.0.1:5000/actors/a', headers={ 'Authorization': self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')


# TESTS FOR CASTING ASSISTANT
# reminder: casting assistants MAY view movies and actors
# They MAY NOT update, delete, or post new movies and actors
#
#   TESTS FOR CASTING ASSISTANT:MOVIES
#   {{POST requests}}
    def test_32_CASTING_ASSISTANT_403_post_movie_invalid_permissions(self):
        res = self.client().post('http://127.0.0.1:5000/movies', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

#   {{GET requests}}
    def test_33_CASTING_ASSISTANT_200_get_movies(self):
        self.client().post('http://127.0.0.1:5000/movies', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        # In order to test the GET calls below, it is necessary to successfully POST to the table

        res = self.client().get('http://127.0.0.1:5000/movies', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_34_CASTING_ASSISTANT_200_get_individual_movies(self):
        res = self.client().get('http://127.0.0.1:5000/movies/3', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_35_CASTING_ASSISTANT_404_get_nonexistent_movie(self):
        res = self.client().get('http://127.0.0.1:5000/movies/a', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{PATCH requests}}
    def test_36_CASTING_ASSISTANT_403_patch_movie_invalid_permissions(self):
        res = self.client().patch('http://127.0.0.1:5000/movies/3', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

#   {{DELETE requests}}
    def test_37_CASTING_ASSISTANT_403_delete_movie_invalid_permissions(self):
        res = self.client().delete('http://127.0.0.1:5000/movies/3', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

#   TESTS FOR CASTING ASSISTANT:ACTORS
#   {{get requests}}
    def test_38_CASTING_ASSISTANT_200_get_actors(self):
        self.client().post('http://127.0.0.1:5000/actors', headers={ 'Authorization': self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        # In order to test the GET calls below, it is necessary to successfully POST to the table

        res = self.client().get('http://127.0.0.1:5000/actors', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_39_CASTING_ASSISTANT_200_get_individual_movies(self):
        res = self.client().get('http://127.0.0.1:5000/actors/3', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_40_CASTING_ASSISTANT_404_nonexistent_actor(self):
        res = self.client().get('http://127.0.0.1:5000/actors/a', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')

#   {{POST requests}}
    def test_41_CASTING_ASSISTANT_403_post_actor_invalid_permissions(self):
        res = self.client().post('http://127.0.0.1:5000/actors', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

#   {{PATCH requests}}
    def test_42_CASTING_ASSISTANT_403_patch_actor_invalid_permissions(self):
        res = self.client().patch('http://127.0.0.1:5000/actors/3', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

#   {{DELETE requests}}
    def test_43_CASTING_ASSISTANT_403_delete_actor_invalid_permissions(self):
        res = self.client().delete('http://127.0.0.1:5000/actors/3', headers={ 'Authorization': self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
