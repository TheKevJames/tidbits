# pylint: disable=import-self,no-member
import nox


@nox.session
@nox.parametrize('python_version', ['2.7', '3.4', '3.5', '3.6', '3.7'])
def unit_tests(session, python_version):
    session.interpreter = 'python{}'.format(python_version)
    session.virtualenv_dirname = 'unit-' + python_version

    session.install('mock', 'pytest', 'pytest-cov')
    session.install('python-json-logger', 'raven')
    session.install('-e', '.')

    session.run(
        'py.test',
        '--quiet',
        '--cov=tidbits',
        '--cov-append',
        '--cov-report=',
        'tests',
        *session.posargs)


@nox.session
@nox.parametrize('python_version', ['2.7', '3.6', '3.7'])
def lint_setup_py(session, python_version):
    session.interpreter = 'python{}'.format(python_version)
    session.virtualenv_dirname = 'setup-' + python_version

    session.install('docutils', 'Pygments')
    session.run(
        'python',
        'setup.py',
        'check',
        '--restructuredtext',
        '--strict')


@nox.session
@nox.parametrize('python_version', ['3.7'])
def cover(session, python_version):
    session.interpreter = 'python{}'.format(python_version)
    session.virtualenv_dirname = 'cover'

    session.install('coverage', 'pytest-cov')

    session.run('coverage', 'report', '--show-missing', '--fail-under=90')
    session.run('coverage', 'erase')
