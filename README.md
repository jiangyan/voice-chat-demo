# LiveKit Voice Assistant

This project is a real-time voice chat application featuring an AI-powered voice assistant. It consists of a Next.js frontend and a Python backend, using LiveKit for real-time communication.

## Project Overview

The project is divided into two main parts:

1. **Frontend**: A Next.js application providing the user interface for connecting to the voice chat room and interacting with the voice assistant.
2. **Backend**: A Python service using LiveKit Agents to handle speech-to-text, natural language processing, and text-to-speech.

## Key Features

- Real-time voice chat powered by LiveKit.
- AI-based voice assistant capabilities.
- Supports Chinese language interaction.
- Audio visualization using BarVisualizer.

## Project Structure

- **Frontend**: Located in the `frontend/voice-chat-ui` directory.
- **Backend**: Located in the `backend` directory, utilizes LiveKit Agents and other AI services.

## Prerequisites

- **Node.js and npm** for the frontend.
- **Python 3.7+** for the backend.
- **LiveKit account** for API credentials.

## Setup Instructions

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend/voice-chat-ui
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create a `.env.local` file in the frontend directory and add your LiveKit credentials:
   ```env
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   ```

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables for API keys:
   ```bash
   export LIVEKIT_URL=your_livekit_url
   export LIVEKIT_API_KEY=your_api_key
   export LIVEKIT_API_SECRET=your_api_secret
   export DEEPGRAM_API_KEY=your_deepgram_key
   export OPENAI_API_KEY=your_openai_key
   ```

## Running the Application

1. Start the frontend development server:
   ```bash
   cd frontend/voice-chat-ui
   npm run dev
   ```
2. In a separate terminal, start the backend:
   ```bash
   cd backend
   python main.py dev
   ```

3. Open your browser and navigate to `http://localhost:3000` to use the application.

## Usage

1. Click the "Connect" button on the frontend to join the voice chat room.
2. Interact with the AI voice assistant using your microphone.
3. The assistant responds in Chinese to voice inputs.

## Customization

- Modify the AI assistant's behavior or language by editing the `backend/main.py` file.
- Change the frontend appearance or add features by modifying files in the `frontend/voice-chat-ui/app` directory.

## Troubleshooting

- **Chinese Language Support**: Ensure Deepgram STT is configured with `language="zh-CN"`.
- **OpenAI Integration**: Verify OpenAI LLM and TTS are correctly set up for Chinese.
- **Audio Issues**: Check microphone settings to ensure audio is being captured properly.

## License

[Specify your chosen license here]

## Acknowledgements

This project uses the following technologies:

- [Next.js](https://nextjs.org/)
- [LiveKit](https://livekit.io/)
- [OpenAI](https://openai.com/)
- [Deepgram](https://deepgram.com/)

