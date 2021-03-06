import argparse
import importlib
import os
import unittest
import warnings

from flask_script import Manager, Command
from flask_script import prompt_bool

from app.config import Config

warnings.simplefilter('ignore')

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-d", "--debug", action="store_true")
group.add_argument("-t", "--test", action="store_true")
args, _ = parser.parse_known_args()

if args.debug:
    Config.configure_app(config="debug")
elif args.test:
    Config.configure_app(config="test")
else:
    Config.configure_app(config="prod")

core = importlib.import_module("app.core")
model = importlib.import_module("app.model")

manager = Manager(core.app)
manager.add_option("-d", "--debug",
                   action="store_true", dest="debug", required=False)
manager.add_option("-t", "--test",
                   action="store_true", dest="test", required=False)


class SeedDB(Command):
    """Seed the db """
    def run(self):
        if args.test:
            raise Exception("Test Database is seed in test case tear up !")
        #some seed method


manager.add_command('seeddb', SeedDB())


class DropDB(Command):
    """drop db """
    def run(self):
        if prompt_bool("Are you sure you want to lose all your data"):
            os.system("python manage.py -t db downgrade base")


manager.add_command('dropdb', DropDB())


class CheckDB(Command):
    """Print database structure"""

    def run(self):
        print("List of parsed tables:")
        print(core.meta.tables.keys())
        query = model.SETTINGS.select()
        # query = model.SETTINGS.select(model.SETTINGS.c.key == 'content_basedir')
        result = query.execute()
        print("\nSETTINGS content :")
        for res in result:
            print(res.key + " = " + res.value + " -> " + res.description)
        model.getUser(id=1)


manager.add_command('checkdb', CheckDB())


class RunTests(Command):
    """Seed the db """
    def run(self):
        if not args.test:
            raise Exception("Les tests doivent etre lancés en config de test")
        test_loader = unittest.defaultTestLoader
        test_runner = unittest.TextTestRunner()
        test_suite = test_loader.discover('tests')
        test_runner.run(test_suite)


manager.add_command('runtests', RunTests())

if __name__ == '__main__':
    manager.run()
