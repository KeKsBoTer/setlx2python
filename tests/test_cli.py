"""Tests for setlx2python CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from setlx2python import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['setlx2python', '-h'], stdout=PIPE).communicate()[0]
        print(output)
        self.assertTrue('Usage:'.encode('utf-8') in output)

        output = popen(['setlx2python', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:'.encode('utf-8') in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['setlx2python', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION.encode('utf-8'))