from setuptools import setup

setup(
    name="DQRCG",
    version='0.1',
    py_modules=['dqrcg'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        services_manager=services_manager:cli
    ''',
)