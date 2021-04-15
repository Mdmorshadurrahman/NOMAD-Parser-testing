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
    assert len(run.section_system) == 2
    assert len(run.section_single_configuration_calculation) == 2
    assert run.section_single_configuration_calculation[0].x_example_magic_value == 42