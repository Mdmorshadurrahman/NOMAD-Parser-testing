class ExampleParser(FairdiParser):
    def __init__(self):
        super().__init__(name='parsers/example', code_name='EXAMPLE')

    def run(self, mainfile: str, archive: EntryArchive, logger):
        # Log a hello world, just to get us started. TODO remove from an actual parser.
        logger.info('Hello World')

        run = archive.m_create(Run)
        run.program_name = 'EXAMPLE'