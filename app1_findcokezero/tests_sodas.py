# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# using test.TestCase instead of unittest.TestCase to make sure tests run within the suite - not just in isolation
from django.test import TestCase
from django_webtest import WebTest
from django.db import IntegrityError

from app1_findcokezero.models import Retailer, Soda


class SodaTestCase(TestCase):
    def setUp(self):
        Soda.objects.create(name="CherryCokeZero", abbreviation="CZ", low_calorie=True)
        Soda.objects.create(name="Coke Classic", abbreviation="CC", low_calorie=False)

    def test_database_stores_sodas(self):
        """Soda types are stored in database and identified by abbreviation"""
        soda1 = Soda.objects.get(abbreviation="CZ")
        soda2 = Soda.objects.get(abbreviation="CC")
        self.assertEqual(soda1.name, "CherryCokeZero")
        self.assertEqual(soda2.name, "Coke Classic")
        self.assertEqual(soda1.low_calorie, True)
        self.assertEqual(soda2.low_calorie, False)

    def test_database_does_not_allow_duplicate_names(self):
        """For Sodas, duplicate names are not allowed"""
        with self.assertRaises(IntegrityError):
            Soda.objects.create(name="Coke Classic", abbreviation="CL", low_calorie=False)

    def test_database_does_not_allow_duplicate_abbreviations(self):
        """For Sodas, duplicate abbreviations are not allowed"""
        with self.assertRaises(IntegrityError):
            Soda.objects.create(name="CherryCokeZero2", abbreviation="CZ", low_calorie=False)

    def test_database_retrieves_soda_by_retailer(self):
        """Sodas are retreived in a group by retailer"""
        retailer = Retailer.objects.create(name="Shell", street_address="598 Bryant Street", city="San Francisco", postcode="94107")
        soda1 = Soda.objects.get(abbreviation="CZ")
        soda2 = Soda.objects.get(abbreviation="CC")
        retailer.sodas.add(soda1, soda2)
        self.assertEqual(retailer.sodas.get(pk=soda1.pk), soda1)
        self.assertEqual(retailer.sodas.get(pk=soda2.pk), soda2)


class SodaWebTestCase(WebTest):
    csrf_checks = False

    def setUp(self):
        Soda.objects.create(name="CherryCokeZero", abbreviation="CZ", low_calorie=True)
        Soda.objects.create(name="Coke Classic", abbreviation="CC", low_calorie=False)

    def test_show_sodas(self):
        # "For sodas, HTTP get request with no params retrieves all retailers in database"
        get_response = self.app.get('/api/sodas/')
        self.assertEqual(get_response.status, "200 OK")
        self.assertEqual(len(get_response.json), 2)

    def test_view_all_sodas_by_retailer(self):
        # "HTTP get request with retailer ID and 'sodas' in params retrieves all sodas associated with that retailer"
        retailer = Retailer.objects.create(name="Shell", street_address="598 Bryant Street", city="San Francisco", postcode="94107")
        soda1 = Soda.objects.create(name="Diet Coke", abbreviation="DC", low_calorie=True)
        retailer.sodas.add(soda1)
        soda2 = Soda.objects.get(abbreviation="CC")
        retailer.sodas.add(soda2)

        retailer_id = retailer.id
        get_response = self.app.get("/api/retailers/%d/sodas/" % retailer_id)

        self.assertEqual(get_response.status, "200 OK")
        self.assertEqual(len(get_response.json), 2)


    def test_create_soda(self):
        # """For sodas, HTTP request post request with valid data results in creation of object and response with all object data"""
        post_response = self.app.post_json('/api/sodas/',
                                           params={"abbreviation": "DC", "low_calorie": "True", "name": "Diet Coke"})
        self.assertEqual(post_response.status, "201 Created")

        self.assertEqual(post_response.json["abbreviation"], "DC")
        self.assertEqual(post_response.json["low_calorie"], True)
        self.assertEqual(post_response.json["name"], "Diet Coke")
        self.assertTrue(post_response.json.has_key("id"), "Expected Retailer object to have key 'id', but it was missing.")

        new_soda_id = post_response.json["id"]

        get_response = self.app.get('/api/sodas/%d/' % new_soda_id)

        self.assertEqual(get_response.status, "200 OK")
        self.assertEqual(len(get_response.json.keys()), 5)
        self.assertEqual(get_response.json, post_response.json)