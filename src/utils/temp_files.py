import io
import os
from tempfile import NamedTemporaryFile
from typing import Generator


class GenerateTempFile:
    def __init__(self, cleanup: bool = True):
        self.cleanup = cleanup
        self.tmp = NamedTemporaryFile(delete=False)

    def __call__(self) -> Generator[io.BytesIO, None, None]:
        try:
            yield self.tmp
        finally:
            self.cleanup and os.unlink(self.tmp.name)


class GenerateTempFileDepends:
    def __init__(self, cleanup: bool = True):
        self.cleanup = cleanup

    def __call__(self) -> io.BytesIO:
        _cls = GenerateTempFile(cleanup=self.cleanup)
        return _cls.tmp
