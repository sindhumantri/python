#!/usr/bin/python

#http://openweathermap.org/current
#http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=70926ddfd37fdf454548b8db13695995

import urllib2
import json
import unittest

class RestApiTest(unittest.TestCase):
    def setUp(self):
        self.ApiUrl="http://api.openweathermap.org/data/2.5/weather"
        self.ApiKey="70926ddfd37fdf454548b8db13695995"

    def test_weather_api_by_cityname1(self):
        testurl="{}?q=London,uk&appid={}".format(self.ApiUrl, self.ApiKey)
        print(testurl)
        url = urllib2.urlopen(testurl)
        response = url.read()
        print(response)
        self.assertTrue("London" in response)

    def test_weather_api_by_cityname2(self):
        testurl="{}?q=London,uk&appid={}".format(self.ApiUrl, self.ApiKey)
        print(testurl)
        url = urllib2.urlopen(testurl)
        response = url.read()
        json_loads = json.loads(response)
        print(json_loads)
        city = json_loads["name"]
        self.assertTrue(city == "London")

    def tearDown(self):
        print("-----Test is over------")


if __name__ == "__main__":
    unittest.main()
