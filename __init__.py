from pelican import Pelican
from pelican.plugins import signals

from .generators import ResumeGenerator


def add_generator(pelican: Pelican):
    return ResumeGenerator


def register():
    signals.get_generators.connect(add_generator)
