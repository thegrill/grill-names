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

    def test_cgasset_file(self):
        name = CGAssetFile().get_default()
        name.name = name.get_name(area='model')
        self.assertEqual(name.area, 'model')
        path = Path.joinpath(
            Path(),
            'demo', '3d', 'abc', 'entity', 'model', 'master', 'atom', 'main', 'all',
            'whole', '1', 'demo-3d-abc-entity-model-master-atom-main-all-whole.1.ext'
        )
        self.assertEqual(Path(path), name.path)
        name.sep = ':'
        self.assertEqual(':', name.sep)
        self.assertEqual('demo:3d:abc:entity:model:master:atom:main:all:whole.1.ext', name.get_name())
        name.sep = '.'
        self.assertEqual(name.sep, '.')
        self.assertEqual('demo.3d.abc.entity.model.master.atom.main.all.whole.1.ext', name.get_name())
        name.sep = ' '
        name.name = name.get_name(area='rig', part='leg', output='skin', branch='dev')
        self.assertEqual('rig', name.area)
        self.assertEqual('demo 3d abc entity rig dev atom main all leg.skin.1.ext', name.get_name())

    def test_cgasset(self):
        self.assertEqual(CGAsset().get_name(),
                         '{code}-{env}-{kingdom}-{cluster}-{area}-{branch}-{item}-{step}-{variant}-{part}')
        self.assertEqual(CGAsset.get_default().name,
                         'demo-3d-abc-entity-rnd-master-atom-main-all-whole')

    def test_lifetr(self):
        domain = 'Eukarya'
        kingdom = 'Plantae'
        phylum = 'Magnoliophyta (Tracheophyta)'
        klass = 'Magnoliopsida (Equisetopsida)'
        order = 'Fabales'
        family = 'Fabaceae'
        genius = 'Pisum'
        species = 'P. sativum'
        form = 'Pea'
        name = LifeTR(f'{domain}:{kingdom}:{phylum}:{klass}:'
                      f'{order}:{family}:{genius}:{species}:{form}')
        self.assertEqual(name.domain, domain)
        with self.assertRaises(ValueError):
            name.kingdom = ' must start with word char'
