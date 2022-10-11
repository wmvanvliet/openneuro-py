from pathlib import Path
from unittest import mock

import openneuro
from openneuro.config import init_config, load_config, get_token


def test_config(tmp_path: Path):
    """Test creating and reading the config file."""
    openneuro.config.config_fname = tmp_path / '.openneuro'
    with mock.patch('getpass.getpass', lambda _: 'test'):
        init_config()
    assert openneuro.config.config_fname.exists()
    assert load_config() == {'apikey': 'test', 'errorReporting': False,
                             'url': 'https://openneuro.org/'}
    assert get_token() == 'test'
