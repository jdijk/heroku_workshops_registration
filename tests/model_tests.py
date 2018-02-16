import sys, os
import unittest
import datetime


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'projherokureg.settings'
django.setup()

from appherokureg.models import Workshop

class TestViews(unittest.TestCase):

    def test_models(self):
        e = Workshop(slug='a_new_event', dateandtime=datetime.datetime.now())
        assert(e.slug == 'a_new_event')


if __name__ == '__main__':
    unittest.main()