import pytest

from agent import Agent, MatopeliAI, train

@pytest.fixture
def agent():
    return Agent()

def test_agent_initial_state(agent):
    assert agent.n_games == 0
    assert agent.epsilon == 0
    assert agent.gamma == 0.9
    assert len(agent.memory) == 0
    assert len(list(agent.model.parameters())) == 4
    assert agent.model.linear1.in_features == 15
    assert agent.model.linear1.out_features == 256
    assert agent.model.linear2.in_features == 256
    assert agent.model.linear2.out_features == 3

def test_get_state(agent):
    state = agent.get_state(MatopeliAI())
    assert state.shape == (15,)

def test_remember(agent):
    state = agent.get_state(MatopeliAI())
    action = [0, 1, 0]
    reward = 10
    next_state = agent.get_state(MatopeliAI())
    done = False

    agent.remember(state, action, reward, next_state, done)
    assert len(agent.memory) == 1
    assert len(agent.memory[0]) == 5
    assert (agent.memory[0][0] == state).all()
    assert agent.memory[0][1] == action
    assert agent.memory[0][2] == reward
    assert (agent.memory[0][3] == next_state).all()
    assert agent.memory[0][4] == done

def test_train_short_memory(agent):
    state = agent.get_state(MatopeliAI())
    action = [0, 1, 0]
    reward = 10
    next_state = agent.get_state(MatopeliAI())
    done = False

    agent.train_short_memory(state, action, reward, next_state, done)

def test_train_long_memory(agent):
    state = agent.get_state(MatopeliAI())
    action = [0, 1, 0]
    reward = 10
    next_state = agent.get_state(MatopeliAI())
    done = False

    for i in range(100):
        agent.remember(state, action, reward, next_state, done)

    agent.train_long_memory()

def test_get_action(agent):
    state = agent.get_state(MatopeliAI())
    action = agent.get_action(state)
    assert len(action) == 3
    assert sum(action) == 1
    assert all(isinstance(a, int) for a in action)
