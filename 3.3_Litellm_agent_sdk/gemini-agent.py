import nest_asyncio
nest_asyncio.apply()

from __future__ import annotations
import asyncio
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

set_tracing_disabled(disabled=True)

MODEL = "gemini/gemini-2.0-flash"
GEMINI_API_KEY = "AIzaSyAjRyfEVcdz9AltsIx6OvpKb_Oxq1zBVCo" 

@function_tool
def get_weather(city: str) -> str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


# 🔁 Synchronous run
def run_sync_agent():
    print("\n=== Running Sync Agent ===")
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
    )

    result = Runner.run_sync(agent, "What's the weather in Tokyo?")
    print(result.final_output)


# ⚡ Asynchronous run
async def run_async_agent():
    print("\n=== Running Async Agent ===")
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
    )

    result = await Runner.run(agent, "What's the weather in Tokyo?")
    print(result.final_output)


if __name__ == "__main__":
    run_sync_agent()
    asyncio.run(run_async_agent())
