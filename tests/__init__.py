import pytest
import logging

from nomad.datamodel import EntryArchive

from exampleparser import ExampleParser


@pytest.fixture
def parser():
    return ExampleParser()


def test_example(parser):
    archive = EntryArchive()
    parser.run('tests/data/example.out', archive, logging)

    run = archive.section_run[0]
    assert run.program_name == 'EXAMPLE'