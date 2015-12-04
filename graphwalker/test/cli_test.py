# -*- coding: utf-8 -*-
#
import unittest

from graphwalker import cli


class TestCommandlineItf(unittest.TestCase):

    def test_one_reporter(self):
        args = "./cli.py --reporter=mod.class:a,b,ka=va"
        parser = cli.CommandLineParser(args.split())
        self.assertEqual(["mod.class:a,b,ka=va"], parser.reporter)

    def test_multiple_reporters(self):
        args = "./cli.py --reporter=mod1.a:b,ka=va --reporter=mod2.class"
        parser = cli.CommandLineParser(args.split())
        self.assertEqual(["mod1.a:b,ka=va","mod2.class"], parser.reporter)

    def test_no_reporter(self):
        args = "cli.py"
        parser = cli.CommandLineParser(args.split())
        self.assertEqual([], parser.reporter)

    def test_with_a_suite_name(self):
        args = "cli.py --suite-name=a-random-name"
        parser = cli.CommandLineParser(args.split())
        self.assertEqual("a-random-name", parser.suite)

    def test_with_no_suite_name(self):
        args = "cli.py"
        parser = cli.CommandLineParser(args.split())
        self.assertEqual("graphwalker", parser.suite)

    def test_with_no_stop_condition(self):
        args = ["cli"]
        parser = cli.CommandLineParser(args.split())
        self.assertEqual("Coverage", parser.stop)

    def test_with_no_stop_condition(self):
        args = "cli.py"
        parser = cli.CommandLineParser(args.split())
        self.assertEqual("Coverage", parser.stop)

    def test_with_a_stop_condition(self):
        args = "cli.py --stop=Coverage:edges=100"
        parser = cli.CommandLineParser(args.split())
        self.assertEqual("Coverage:edges=100", parser.stop)
