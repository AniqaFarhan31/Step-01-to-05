import nest_asyncio
nest_asyncio.apply()

from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import TextContentBlock  

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

assistant = client.beta.assistants.create(
    name="MyAgent",
    instructions="You are a helpful AI assistant.",
    tools=[{"type": "code_interpreter"}],
    model="openrouter/openai/gpt-4"
)

thread = client.beta.threads.create()

client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What is the capital of France?"
)

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    event_handler=AssistantEventHandler(),
)

messages = list(client.beta.threads.messages.list(thread_id=thread.id, order="asc"))

for message in messages:
    for content in message.content:
        if isinstance(content, TextContentBlock):
            print(content.text.value)
