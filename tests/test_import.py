"""Test Scenery."""

import scenery


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(scenery.__name__, str)
