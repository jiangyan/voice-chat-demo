import asyncio

from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import deepgram, openai, silero

# This function is the entrypoint for the agent.
async def entrypoint(ctx: JobContext):
    # Create an initial chat context with a system prompt
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            # "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            # "You should use short and concise responses, and avoiding usage of unpronouncable punctuation."
            "你是一个由 LiveKit 创建的语音助手。你与用户的交互界面将是中文的语音。你应该使用简短而简洁的回复，并避免使用无法发音的标点符号。"
        ),
    )

    # Connect to the LiveKit room
    # indicating that the agent will only subscribe to audio tracks
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # VoiceAssistant is a class that creates a full conversational AI agent.
    # See https://github.com/livekit/agents/tree/main/livekit-agents/livekit/agents/voice_assistant
    # for details on how it works.
    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=deepgram.STT(language="zh-CN"),
        llm=openai.LLM(),
        tts=openai.TTS(voice="alloy"),
        chat_ctx=initial_ctx,
    )

    # Start the voice assistant with the LiveKit room
    assistant.start(ctx.room)

    await asyncio.sleep(1)

    # Greets the user with an initial message
    # await assistant.say("Hey, how can I help you today?", allow_interruptions=True)
    await assistant.say("你好，有什么可以帮你的吗？", allow_interruptions=True)

if __name__ == "__main__":
    # Initialize the worker with the entrypoint
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
