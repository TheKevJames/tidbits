import nox


@nox.session(python=['2.7', '3.4', '3.5', '3.6', '3.7'], reuse_venv=True)
def unit_tests(session):
    session.install('mock', 'pytest', 'pytest-cov')
    session.install('-e', '.[gcloud,sentry]')

    session.run('py.test', '--quiet', '--cov=tidbits', '--cov-append',
                '--cov-report=', 'tests', *session.posargs)


@nox.session(python=['2.7', '3.6', '3.7'], reuse_venv=True)
def lint_setup_py(session):
    session.install('docutils', 'Pygments')
    session.run('python', 'setup.py', 'check', '--restructuredtext',
                '--strict')


@nox.session(python=['3.7'], reuse_venv=True)
def cover(session):
    session.install('coverage', 'pytest-cov')

    session.run('coverage', 'report', '--show-missing', '--fail-under=90')
    session.run('coverage', 'erase')
