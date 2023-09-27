from io import StringIO
from pathlib import Path
from contextlib import redirect_stdout

import pytest

from ninetyone_take_home.main import main


@pytest.fixture
def filepath() -> str:
    return Path(__file__).parent / "resources" / "TestData.csv"


def test_main(filepath: str) -> None:
    output = StringIO()
    with redirect_stdout(output):
        main(filepath=filepath)
    assert output.getvalue().strip() == "\n".join(["George Of The Jungle", "Sipho Lolo", "78"])
