import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from src.app import create_app
from src.database.models import setup_db, Movie, Actor


class CastrTestCase(unittest.TestCase):
    # """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.TEST_TOKEN_CASTING_ASSISTANT = "Bearer {}".format('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRkZDUyZDk2MmNkOTAwNzA1MTUyN2EiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2MjUyODMwOTYsImV4cCI6MTYyNTM2OTQ5NiwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.Fl9KCLIkFUbx0orcxnoY1a2Tnfi9qT-xS2BXN3H4ZFOQ9Uho6L8IplWnsV9rzExdxxHJkdC6dsxJs850vwIUTgJiUyzUnck2MvTMWGByJhTcF-OZ25HiCu4IZqOi48_HgW2Xg0jgfHkzplZg5zujCUZvTMfRFJUAao5iD2wU1-P3DUX-npX5QoC1gtSMA_9MYxxmwTzksRr3XdokLnIie4oVFdgzGVff_LZF7LfuF95JXn5a7YHmwBSdEQ9hR1Y23bawXubhbKSgw30LTuqQnAHjulbgVvaGKSkwVnEUv_cIfiGr0Si2hlKtl2GAMdtlkmcReqSyg5Kh5QAp_LT8cg')
        self.TEST_TOKEN_CASTING_DIRECTOR = "Bearer {}".format('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDRiYjJhNDRlYjAwNjkwNDdlMTEiLCJhdWQiOlsiY2FzdHItYXBpIiwiaHR0cHM6Ly9jb2ZmZWVzaG9wLWZzbmQtdWRhY2l0eS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI1MjgzOTcyLCJleHAiOjE2MjUzNzAzNzIsImF6cCI6IlYzdWV2aGZXeHJhcmxYaHl1UTRyMG9CU1Q2aXptWUYzIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.ZyxNO-3GgG5UIDgcCKIS8-q0WGAeSe9iLoqSBtknjHtnooijBlY7--Bn-qFwt0gijXrG53t7eBJIclPxGi4GpAjqtBLnUgqDhYvuV1ARi0ji4oLepAuT4GysKBqJXetf8mLdEr4ynxfcsP8uuYFp7mXTCnPclIvI3CX5Uj_6fPfQM-nLo2wHbsaoKhloxgaNgnZcHail-0A0HjgQ5D4adeefEnNRdUVdFjk_G4H7ubdfhTZUyHBRw2MOHPoz-3Pfhu625UrdnpwB5CFyPh10o4zJB4_KMy8YomZTPtSs_5uqX0a9r_ExIJbUTgANI5iqXkM5ouPff3XI91Oijkcn8Q')
        self.TEST_TOKEN_EXECUTIVE_PRODUCER = "Bearer {}".format('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOlsiY2FzdHItYXBpIiwiaHR0cHM6Ly9jb2ZmZWVzaG9wLWZzbmQtdWRhY2l0eS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI1Mjg0MDg0LCJleHAiOjE2MjUzNzA0ODQsImF6cCI6IlYzdWV2aGZXeHJhcmxYaHl1UTRyMG9CU1Q2aXptWUYzIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.xLwLlriq8oX-BMlw7SKUozdFJc21US_dvWguDYg5fuZdnB98Ygb7QnasYTFl_ISiI4BjfFpbgE8sK28QZsVjziR49Siqq4XM9_70GoSO_Iz0lIZdjGlKacEr4K2P8x4wDJqLLLkYVR_z8FRcNfPFXF3ZmqPVgqJlRUFYeoLHfZCMRoTDYX_6WWj6Kkm_-5CkzAZoAfUdfvFwJQeY0ZWx-yh9xWTyfzdbnSTvUS7Ly6MA1rf69bwmS3Tim-T5T1hyp2aXE6mN1KcYP8-NHsVivSBNF8Q2xl0dGhYUlkyd9Agz4t4IaB-XVgg9M0lxvfNddmmWigPpVYhzV7WO49-LBg')

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

# TESTS FOR CASTING ASSISTANT
# reminder: casting assistants MAY view movies and actors
# They MAY NOT update, delete, or post new movies and actors
#
#   TESTS FOR CASTING ASSISTANT:MOVIES
#   {{GET requests}}
    def test_CASTING_ASSISTANT_200_get_movies(self):
        res = self.client().get('/movies', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_CASTING_ASSISTANT_200_get_individual_movies(self):
        res = self.client().get('/movies/8', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_CASTING_ASSISTANT_404_get_nonexistent_movie(self):
        res = self.client().get('/movies/a', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{POST requests}}
    def test_CASTING_ASSISTANT_403_post_movie_invalid_permissions(self):
        res = self.client().post('/movies', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found')

#   {{PATCH requests}}
    def test_CASTING_ASSISTANT_403_patch_movie_invalid_permissions(self):
        res = self.client().patch('/movies/8', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found')

#   {{DELETE requests}}
    def test_CASTING_ASSISTANT_403_delete_movie_invalid_permissions(self):
        res = self.client().delete('/movies/8', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found')

#   TESTS FOR CASTING ASSISTANT:ACTORS
#   {{get requests}}
    def test_CASTING_ASSISTANT_200_get_actors(self):
        res = self.client().get('/actors', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_CASTING_ASSISTANT_200_get_individual_movies(self):
        res = self.client().get('/actors/10', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_CASTING_ASSISTANT_404_nonexistent_actor(self):
        res = self.client().get('/actors/a', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{POST requests}}
    def test_CASTING_ASSISTANT_403_post_actor_invalid_permissions(self):
        res = self.client().post('/actors', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found')

#   {{PATCH requests}}
    def test_CASTING_ASSISTANT_403_patch_actor_invalid_permissions(self):
        res = self.client().patch('/actors/10', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found')

#   {{DELETE requests}}
    def test_CASTING_ASSISTANT_403_delete_actor_invalid_permissions(self):
        res = self.client().delete('/actors/10', headers={ Authorization: self.TEST_TOKEN_CASTING_ASSISTANT,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found')

# TESTS FOR CASTING DIRECTOR
# reminder: casting directors MAY view, update, delete, and add new actors
# They MAY also view and update movies, but they MAY NOT add or delete movies
#
#   TESTS FOR CASTING DIRECTOR:MOVIES
#   {{GET requests}}
    def test_CASTING_DIRECTOR_200_get_movies(self):
        res = self.client().get('/movies', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_CASTING_DIRECTOR_200_get_individual_movies(self):
        res = self.client().get('/movies/8', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_CASTING_DIRECTOR_404_nonexistent_movie(self):
        res = self.client().get('/movies/a', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{POST requests}}
    def test_CASTING_DIRECTOR_403_post_movie_invalid_permissions(self):
        res = self.client().post('/movies', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found')

#   {{PATCH requests}}
    def test_CASTING_DIRECTOR_200_patch_valid_movie(self):
        res = self.client().patch('/movies/8', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_CASTING_DIRECTOR_404_patch_nonexistent_movie(self):
        res = self.client().patch('/movies/a', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{DELETE requests}}
    def test_CASTING_DIRECTOR_403_delete_movie_invalid_permissions(self):
        res = self.client().delete('/movies/8', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found')

#   TESTS FOR CASTING DIRECTOR:ACTORS
#   {{get requests}}
    def test_CASTING_DIRECTOR_200_get_actors(self):
        res = self.client().get('/actors', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_CASTING_DIRECTOR_200_get_individual_movies(self):
        res = self.client().get('/actors/10', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_CASTING_DIRECTOR_404_get_nonexistent_actor(self):
        res = self.client().get('/actors/a', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{POST requests}}
    def test_CASTING_DIRECTOR_200_post_valid_actor(self):
        res = self.client().post('/actors', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

#   {{PATCH requests}}
    def test_CASTING_DIRECTOR_200_patch_valid_actor(self):
        res = self.client().patch('/actors/10', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_CASTING_DIRECTOR_404_patch_nonexistent_actor(self):
        res = self.client().patch('/actors/a', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{DELETE requests}}
    def test_CASTING_DIRECTOR_200_delete_valid_actor(self):
        res = self.client().delete('/actors/10', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_CASTING_DIRECTOR_404_delete_nonexistent_actor(self):
        res = self.client().delete('/actors/a', headers={ Authorization: self.TEST_TOKEN_CASTING_DIRECTOR,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

# TESTS FOR EXECUTIVE PRODUCER
# reminder: executive producers MAY view, update, delete, or add new movies and actors
#
#   TESTS FOR CASTING DIRECTOR:MOVIES
#   {{GET requests}}
    def test_EXECUTIVE_PRODUCER_200_get_movies(self):
        res = self.client().get('/movies', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_EXECUTIVE_PRODUCER_200_get_individual_movies(self):
        res = self.client().get('/movies/8', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_EXECUTIVE_PRODUCER_404_get_nonexistent_movie(self):
        res = self.client().get('/movies/a', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{POST requests}}
    def test_EXECUTIVE_PRODUCER_200_post_valid_movie(self):
        res = self.client().post('/movies', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

#   {{PATCH requests}}
    def test_EXECUTIVE_PRODUCER_200_patch_valid_movie(self):
        res = self.client().patch('/movies/8', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_EXECUTIVE_PRODUCER_404_patch_nonexistent_movie(self):
        res = self.client().patch('/movies/a', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'title':'jaws', 'release_date':'2021-07-08'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{DELETE requests}}
    def test_EXECUTIVE_PRODUCER_200_delete_valid_movie(self):
        res = self.client().delete('/movies/8', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_EXECUTIVE_PRODUCER_404_delete_nonexistent_movie(self):
        res = self.client().delete('/movies/a', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   TESTS FOR CASTING DIRECTOR:ACTORS
#   {{get requests}}
    def test_EXECUTIVE_PRODUCER_200_get_actors(self):
        res = self.client().get('/actors', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_EXECUTIVE_PRODUCER_200_get_individual_movies(self):
        res = self.client().get('/actors/10', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_EXECUTIVE_PRODUCER_404_get_nonexistent_actor(self):
        res = self.client().get('/actors/a', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{POST requests}}
    def test_EXECUTIVE_PRODUCER_200_post_valid_actor(self):
        res = self.client().post('/actors', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

#   {{PATCH requests}}
    def test_EXECUTIVE_PRODUCER_200_patch_valid_actor(self):
        res = self.client().patch('/actors/10', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_EXECUTIVE_PRODUCER_404_patch_nonexistent_actor(self):
        res = self.client().patch('/actors/a', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,}, json={'name':'Gene Wilder', 'age':83, 'gender':'male'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

#   {{DELETE requests}}
    def test_EXECUTIVE_PRODUCER_200_delete_valid_actor(self):
        res = self.client().delete('/actors/10', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)
        #REVIEWER, PLEASE NOTE: you may need to update the id number for this specific test to work properly

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_EXECUTIVE_PRODUCER_404_delete_nonexistent_actor(self):
        res = self.client().delete('/actors/a', headers={ Authorization: self.TEST_TOKEN_EXECUTIVE_PRODUCER,})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
