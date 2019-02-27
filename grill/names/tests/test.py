# standard
import unittest
from pathlib import Path
# package
from grill.names import *


def _get_project_kwargs():
    project = 'tstabc'
    workarea = 'current'
    return locals()


def _get_primitive_kwargs():
    values = _get_project_kwargs()
    values.update(prim='hero', stage='concept')
    return values


def _get_asset_kwargs():
    values = _get_primitive_kwargs()
    values.update(workarea='schrgeo', variant='original', partition='master', layer='default')
    return values


def _get_assetfile_kwargs():
    values = _get_asset_kwargs()
    values.update(version=0, suffix='ext')
    return values


class TestNames(unittest.TestCase):

    def test_project(self):
        name = Project()
        name.name = name.get_name(**_get_project_kwargs())
        self.assertEqual('tstabc_current', name.nice_name)

    def test_environment(self):
        name = Environment()
        name.name = name.get_name(**_get_project_kwargs())
        self.assertEqual('tst', name.environment)
        name.environment = 'gme'
        self.assertEqual('gme', name.environment)
        self.assertEqual('abc', name.code)

    def test_audiovisual(self):
        name = Primitive()
        name.name = name.get_name(**_get_primitive_kwargs())
        self.assertEqual('tstabc_current_hero_concept', name.name)

    def test_asset(self):
        name = AssetFile()
        name.name = name.get_name(**_get_assetfile_kwargs())
        name.name = name.get_name(area='model')
        self.assertEqual(name.workarea, 'schrmodel')
        path = Path.joinpath(Path(), 'abc', 'tst', 'pro', 's', 'chr', 'hero', 'model', 'concept', 'original', 'master',
                             'default', '0', 'tstabc_schrmodel_hero_concept_original_master_default.0.ext')
        self.assertEqual(Path(path), name.path)
        name.sep = '-'
        self.assertEqual('-', name.sep)
        self.assertEqual('tstabc-schrmodel-hero-concept-original-master-default.0.ext', name.get_name())
        name.sep = '.'
        self.assertEqual(name.sep, '.')
        self.assertEqual('tstabc.schrmodel.hero.concept.original.master.default.0.ext', name.get_name())
        name.sep = ' '
        name.name = name.get_name(area='rig')
        self.assertEqual('schrrig', name.workarea)
        self.assertEqual(' ', name.sep)
        self.assertEqual('tstabc schrrig hero concept original master default.0.ext', name.get_name())
        name.sep = '_'
        name.branch = 'dev'
        path = Path.joinpath(Path(), 'abc', 'tst', 'dev', 's', 'chr', 'hero', 'rig', 'concept', 'original', 'master',
                             'default', '0', 'tstabc_schrrig_hero_concept_original_master_default.0.ext')
        self.assertEqual(Path(path), name.path)

    def test_asset_default(self):
        name = Asset.get_default(prim='hero')
        self.assertEqual(name.name, 'envcode_kgrparea_hero_stage_original_master_default')
        name = AssetFile.get_default()
        self.assertEqual(name.name, 'envcode_kgrparea_prim_stage_original_master_default.0.ext')

    def test_cgasset(self):
        self.assertEqual(CGAsset().get_name(),
                         '{code}-{env}-{kingdom}-{cluster}-{area}-{branch}-{item}-{step}-{variant}-{part}')
        self.assertEqual(CGAsset.get_default().name,
                         'demo-3d-abc-entity-rnd-master-atom-main-all-whole')
