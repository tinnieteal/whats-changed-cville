import unittest
from django.test import Client
from django.test import TestCase
from mainapp.models import Change, Place, Leaderboard
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.test import TestCase
import oauth2
import mock

class ResponsesTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        reponses = []
        reponses.append(self.client.get('/mainapp/map/'))
        reponses.append(self.client.get('/mainapp/'))

        # Check that the response is 200 OK.
        for r in reponses:
            # print("test", r)
            self.assertEqual(r.status_code, 200)

class PlaceTest(TestCase):
    def create_place(self, place_name="test place", place_address="test address"):
        return Place.objects.create(place_name=place_name, place_address=place_address)
    
    def test_place_creation(self):
        p = self.create_place()
        self.assertTrue(isinstance(p, Place))
        self.assertEqual(p.place_name, 'test place')
        self.assertEqual(p.place_address, 'test address')

class ChangeTest(TestCase):
    # def create_change(self, covid_rating="test rating", place_change="test change", submitting_user="test"):
    #     return Change.objects.create(covid_rating=covid_rating, place_change=place_change, submitting_user=submitting_user)
    
    def test_change_creation(self):
        p = Place.objects.create(place_name="test place", place_address="test address")
        c = p.change_set.create(covid_rating="test rating", place_change="test change", submitting_user="test")
        self.assertTrue(isinstance(c, Change))
        self.assertEqual(c.covid_rating, 'test rating')
        self.assertEqual(c.place_change, 'test change')
        self.assertEqual(c.submitting_user, 'test')
        self.assertEqual(c.place, p)
        self.assertEqual(p.change_set.count(), 1)
class ChangeTest2(TestCase):
    def test_change_2(self):
        p = Place.objects.create(place_name="new place", place_address="new address")
        c = p.change_set.create(covid_rating="new rating", place_change="new change", submitting_user="other")
        self.assertTrue(isinstance(c, Change))
        self.assertEqual(c.covid_rating, 'new rating')
        self.assertEqual(c.place_change, 'new change')
        self.assertEqual(c.submitting_user, 'other')
        self.assertEqual(c.place, p)
        self.assertEqual(p.change_set.count(), 1)
class AddSamePlace(TestCase):
    def test_add_same_place(self):
        p = Place.objects.create(place_name="new place", place_address="new address")
        c = Place.objects.create(place_name="new place", place_address="new address")
        self.assertFalse(isinstance(c, Change))
        
class LoginTest(TestCase):
    #general login
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="computing_id2021",
            password="passwd10",
            email="testing@example.com")
        # self.user.save()
    #def teardown(self):
        #self.user.delete()
    def test_correct(self):
        user = authenticate(username='computing_id2021', password='passwd10')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='passwd10')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='computing_id2021', password='wrongpassword')
        self.assertFalse(user is not None and user.is_authenticated)
    def test_all_wrong(self):
        user = authenticate(username='incorrect', password='wrongpassword')
        self.assertFalse(user is not None and user.is_authenticated)
'''def test_login(self):
        #user = User.objects.create(username='computing_id2')
        #user.set_password('passwd3')
        #user.save()
        #c = Client()
        #logged_in = c.login(username = 'computing_id', password='passwd')
        #self.setUp()
        self.client.force_login(self.user)
        self.assertEqual(self.user.username, "computing_id2004")
        user = authenticate(username="computing_id2010") 
        self.assertTrue(user is not None and user.isAuthenticated)
        User.objects.filter(email = "admin1@example.com").delete()
class LogoutTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
    def test_logout(self):
        user = User.objects.create(username='computing_id4')
        user.set_password('passwd4')
        user.save()
        self.client.login(username='computing_id4', password="passwd4")

        # Check response code
        response = self.client.get('/mainapp/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        #self.assertTrue('Log out' in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/mainapp/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        #self.assertTrue('Log in' in response.content)
class IncorrectLogin(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
    def test_incorrect_login(self):
        wrong_user = "not_Right"
        self.client.login(username=wrong_user, password="passwd4")
        self.assertNotEqual(self.user.username, wrong_user)''' 

#class SearchBarTest(TestCase):

class OauthTest(object):
    #test the Google part
    def get_redirect_url(self):
        raise NotImplementedError
    def get_redirect_mock_response(self, *args, **kwargs):
        raise NotImplementedError
    @mock.patch('oauth2.Client.request')
    def redirect(self, MockRequest):
        MockRequest.side_effect = get_mock_func(self.get_redirect_mock_response)
        response = self.oauth2.client.post(self.get_redirect_url())
        return response