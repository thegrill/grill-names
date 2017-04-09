# todo: populate classes with JSON grill API call
from naming import Name, Pipe, File, PipeFile


class Project(PipeFile):
    config = dict(project='[a-zA-Z0-9]+', workarea='\w+')
    drops = 'base',

    def get_path_pattern_list(self):
        return ['project', 'workarea']


class Environment(Project):
    config = dict(environment='[a-z]{3}', code='[a-z0-9]+')
    compounds = dict(project=('environment', 'code'))

    def get_path_pattern_list(self):
        return ['code', 'environment', 'workarea']


class Audiovisual(Environment):
    config = dict(prim='[a-zA-Z0-9]+', stage='[a-z0-9]+')


class Film(Audiovisual):
    config = dict(kind='[a-z]',
                  group='[a-z0-9]{3}',
                  area='[a-z0-9]+',
                  variant='\w+',
                  partition='[a-zA-Z0-9]+',
                  layer='[a-zA-Z0-9]+')
    compounds = dict(workarea=('kind', 'group', 'area'))

    def get_path_pattern_list(self):
        pattern = super().get_path_pattern_list()
        wa_i = pattern.index('workarea')
        new_p = pattern[:wa_i]
        new_p.extend(['branch', 'kind', 'group', 'prim', 'area', 'stage'])
        new_p.extend(pattern[wa_i + 1:])
        new_p.extend(['variant', 'partition', 'layer', 'version'])
        return new_p

    @property
    def branch(self):
        return 'pro'

    @classmethod
    def get_default(cls):
        # todo: get defaults from environment variables?
        defaults = dict(project='envcode', workarea='kgrparea', prim='prim', stage='stage', variant='original',
                        partition='master', layer='default', version=0, extension='ext')
        name = cls()
        name.set_name(name.get_name(**defaults))
        return name
