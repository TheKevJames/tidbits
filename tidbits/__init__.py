from pkg_resources import get_distribution
__version__ = get_distribution('tidbits').version


__all__ = ['__version__']
