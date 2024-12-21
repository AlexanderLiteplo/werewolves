from agent import Agent, GameRole, GameState, PlayerInfo, Message
from llm import LLM  # You'll need to implement this
from constants import LLMModel  # You'll need to implement this

async def example_usage():
    # 1. Create an LLM instance (implementation depends on your LLM wrapper)
    llm = LLM(model=LLMModel.GPT4)  # or whatever model you're using

    # 2. Set up game state
    players = [
        PlayerInfo(name="Alice", is_alive=True, role=GameRole.VILLAGER),
        PlayerInfo(name="Bob", is_alive=True, role=GameRole.WEREWOLF),
        PlayerInfo(name="Charlie", is_alive=True, role=GameRole.SEER),
        PlayerInfo(name="David", is_alive=False, role=GameRole.VILLAGER),
    ]
    
    game_state = GameState(
        players=players,
        day_number=2,
        phase="day"
    )

    # 3. Create an agent
    agent = Agent(
        llm=llm,
        name="Charlie",
        game_role=GameRole.SEER,
        system_prompt=Agent.SYSTEM_PROMPT,
        max_memory_tokens=4000  # Optional: defaults to model's context window
    )

    # 4. Interact with the agent
    response = await agent.prompt(
        message="What do you think about Bob's behavior last night?",
        game_state=game_state
    )
    print(f"Agent response: {response}")

    # 5. Get memory summary
    memory = agent.get_memory_summary()
    print("Agent memory:", memory)