import pytest

from game import BLOCK_SIZE, Direction, MatopeliAI, Point

@pytest.fixture
def test_reset():
    game = MatopeliAI()
    game.reset()
    assert game.direction == Direction.RIGHT
    assert game.snake == [Point(game.w/2, game.h/2),
                          Point(game.w/2-BLOCK_SIZE, game.h/2),
                          Point(game.w/2-(2*BLOCK_SIZE), game.h/2)]
    assert game.score == 0
    assert game.redScore == 0
    assert game.greenScore == 0
    assert game.food is not None
    assert game.food2 is not None
    assert game.enemy is not None

# Generoi punainen omena
def test_place_food():
    game = MatopeliAI()
    game.reset()
    game._place_food()
    assert game.food not in game.snake
    assert game.food != game.food2

# Generoi vihreä omena
def test_place_food2():
    game = MatopeliAI()
    game.reset()
    game._place_food2()
    assert game.food2 not in game.snake
    assert game.food2 != game.food

# Generoi vihollinen
def test_place_enemy():
    game = MatopeliAI()
    game.reset()
    game._place_enemy()
    assert game.enemy not in game.snake
    assert game.enemy != game.food
    assert game.enemy != game.food2
    assert game.enemy != game.enemy2

# Törmäystestit
def test_is_collision():
    game = MatopeliAI()

    # Mato törmää itseensä
    game.snake = [Point(1, 2), Point(2, 2), Point(3, 2)]
    assert game.is_collision(Point(3, 2)) == True
    assert game.is_collision(Point(2, 2)) == True
    assert game.is_collision(Point(1, 2)) == False

    # Kun mato törmää viholliseen
    game.enemy = Point(2, 2)
    game.enemy2 = Point(5, 5)
    assert game.is_collision(Point(2, 2)) == True
    assert game.is_collision(Point(5, 5)) == True
    assert game.is_collision(Point(1, 1)) == False
    assert game.is_collision(Point(3, 3)) == False