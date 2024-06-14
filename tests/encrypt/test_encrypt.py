from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123, 1)
        encrypt_message('message', '1')
    assert encrypt_message('message', 0) == 'egassem'
    assert encrypt_message('message', -7) == 'egassem'
    assert encrypt_message('message', 1) == 'm_egasse'
    assert encrypt_message('message', 2) == 'egass_em'
    assert encrypt_message('message', 3) == 'sem_egas'
    assert encrypt_message('message', 4) == 'ega_ssem'
    assert encrypt_message('message', 5) == 'assem_eg'
    assert encrypt_message('message', 6) == 'e_gassem'
