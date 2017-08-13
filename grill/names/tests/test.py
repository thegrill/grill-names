# standard
import unittest
from pathlib import Path
# package
from grill.names import *


def _get_project_kwargs():
    project = 'tstabc'
    workarea = 'current'
    version = 0
    extension = 'ext'
    return locals()


def _get_primitive_kwargs():
    values = _get_project_kwargs()
    values.update(prim='hero', stage='concept')
    return values


def _get_asset_kwargs():
    values = _get_primitive_kwargs()
    values.update(workarea='schrgeo', variant='original', partition='master', layer='default')
    return values


class TestNames(unittest.TestCase):

    def test_project(self):
        name = Project()
        name.set_name(name.get_name(**_get_project_kwargs()))
        self.assertEqual('tstabc_current', name.nice_name)
        self.assertEqual(Path('tstabc/current/tstabc_current.0.ext'), name.path)

    def test_environment(self):
        name = Environment()
        name.set_name(name.get_name(**_get_project_kwargs()))
        self.assertEqual('tst', name.environment)
        name.environment = 'gme'
        self.assertEqual('gme', name.environment)
        self.assertEqual('abc', name.code)
        self.assertEqual(Path('abc/gme/current/gmeabc_current.0.ext'), name.path)

    def test_audiovisual(self):
        name = Primitive()
        name.set_name(name.get_name(**_get_primitive_kwargs()))
        self.assertEqual(Path('abc/tst/current/tstabc_current_hero_concept.0.ext'), name.path)

    def test_film(self):
        name = Asset()
        name.set_name(name.get_name(**_get_asset_kwargs()))
        name.set_name(name.get_name(area='model'))
        self.assertEqual(name.workarea, 'schrmodel')
        path = Path.joinpath(Path(), 'abc', 'tst', 'pro', 's', 'chr', 'hero', 'model', 'concept', 'original', 'master',
                             'default', '0', 'tstabc_schrmodel_hero_concept_original_master_default.0.ext')
        self.assertEqual(Path(path), name.path)
        name.separator = '-'
        self.assertEqual('-', name.separator)
        self.assertEqual('tstabc-schrmodel-hero-concept-original-master-default.0.ext', name.get_name())
        name.separator = '.'
        self.assertEqual(name.separator, '.')
        self.assertEqual('tstabc.schrmodel.hero.concept.original.master.default.0.ext', name.get_name())
        name.separator = ' '
        name.set_name(name.get_name(area='rig'))
        self.assertEqual('schrrig', name.workarea)
        self.assertEqual(' ', name.separator)
        self.assertEqual('tstabc schrrig hero concept original master default.0.ext', name.get_name())
        name.separator = '_'
        name.branch = 'dev'
        path = Path.joinpath(Path(), 'abc', 'tst', 'dev', 's', 'chr', 'hero', 'rig', 'concept', 'original', 'master',
                             'default', '0', 'tstabc_schrrig_hero_concept_original_master_default.0.ext')
        self.assertEqual(Path(path), name.path)

    def test_film_default(self):
        name = Asset.get_default()
        self.assertEqual(name.name, 'envcode_kgrparea_prim_stage_original_master_default.0.ext')
