import pytest
from player import Player, PlayerNotAlive


def test_DefaultInitialisation():
    player = Player()
    assert player.health == 100

def test_SettingInitialAmount():
    player = Player(50)
    assert player.health == 50

def test_PlayerHealed():
    player = Player(10)
    player.healPlayer(90)
    assert player.health == 100

def test_PlayerDamaged():
    player = Player(100)
    player.hitPlayer(10)
    assert player.health == 90

def test_healPlayerRaisesExceptionOnDeath():
    player = Player(0)
    with pytest.raises(PlayerNotAlive):
        player.healPlayer(100)