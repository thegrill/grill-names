# standard
import unittest
from pathlib import Path
# package
from grill.names import *


class TestNames(unittest.TestCase):

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

    def test_time(self):
        tf = DateTimeFile.get_default(date='2019-10-28', suffix='txt')
        tf.year = 1999
        current_name = tf.name
        with self.assertRaises(ValueError):
            tf.month = 14
        # after attempting an incorrect iso value, we should kepe the last name
        self.assertEqual(current_name, tf.name)
        tf.hour = 1
        tf.minute = 1
        tf.second = 1
        tf.microsecond = 1

        tf2 = DateTimeFile(tf.name)
        self.assertEqual("1999-10-28 1-1-1-1.txt", tf2.name)
        self.assertEqual(datetime.fromisoformat("1999-10-28T01:01:01.000001"),
                         tf2.datetime)

        tf2.name = ""
        with self.assertRaises(AttributeError):
            tf2.datetime

    def test_sub_datetime(self):
        class SubTime(DateTimeFile):
            config = dict(extra=r'\w+')

        tf = SubTime("1999-10-28 1-1-1-1 subclassed.txt")
        self.assertEqual("subclassed", tf.extra)
