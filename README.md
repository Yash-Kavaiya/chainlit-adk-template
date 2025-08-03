# Chainlit + Google ADK Template

A production-ready chat application using Chainlit and Google's Agent Development Kit (ADK) with automatic fallback to Google GenerativeAI.

## ✨ Features

- 🤖 **Real AI Responses**: Powered by Google's Gemini models
- 💬 **Interactive Chat Interface**: Clean Chainlit web UI
- 🔄 **Robust Architecture**: ADK with GenAI fallback for reliability
- 🛡️ **Error Handling**: Graceful fallbacks and error recovery
- 🚀 **Production Ready**: Clean, documented, and tested

## 🚀 Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/Yash-Kavaiya/chainlit-adk-template.git
cd chainlit-adk-template
pip install -r requirements.txt
```

### 2. Configure API Key

1. Copy the environment template:
   ```bash
   cp .env.example .env
   ```

2. Get your Google AI Studio API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key

3. Update your `.env` file:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

### 3. Run the Application

```bash
chainlit run app.py
```

Visit `http://localhost:8000` and start chatting!

## 🏗️ Architecture

The application uses a two-tier approach for maximum reliability:

1. **Primary**: Google ADK with streaming responses
2. **Fallback**: Direct Google GenerativeAI client

This ensures you always get real AI responses, even if there are issues with the ADK streaming implementation.

## 📁 Project Structure

```
chainlit-adk-template/
├── app.py              # Main Chainlit application
├── google_agent.py     # Google ADK agent with GenAI fallback
├── config.py          # Configuration settings
├── requirements.txt   # Dependencies (includes both ADK and GenAI)
├── .env.example       # Environment template
├── .gitignore         # Git ignore rules
└── README.md          # Documentation
```

## 🔧 How It Works

1. **Agent Initialization**: Tries Google ADK first, falls back to GenAI if needed
2. **Message Processing**: Attempts ADK streaming, automatically switches to GenAI on errors
3. **Response Handling**: Returns actual AI responses from Google's Gemini models
4. **Error Recovery**: Graceful handling of API issues and network problems

## 🎛️ Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Your Google AI Studio API key (required)
- `GOOGLE_GENAI_USE_VERTEXAI`: Set to `TRUE` to use Vertex AI instead of AI Studio

### Model Settings

Default model: `gemini-1.5-flash` (fast and efficient)

To change models, edit `google_agent.py`:
```python
# For ADK
model="gemini-2.0-flash"

# For GenAI fallback  
genai.GenerativeModel('gemini-1.5-pro')
```

## 📋 Dependencies

- `chainlit`: Web chat interface
- `google-adk`: Google's Agent Development Kit
- `google-generativeai`: Direct Google AI client (fallback)
- `python-dotenv`: Environment variable management

## 🔍 Troubleshooting

### Common Issues

1. **"API key not found"**: Make sure your `.env` file has the correct `GOOGLE_API_KEY`
2. **"Module not found"**: Run `pip install -r requirements.txt`
3. **"Connection errors"**: Check your internet connection and API key validity

### Testing Your Setup

The application includes built-in error handling and will show informative messages if there are configuration issues.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/Yash-Kavaiya/chainlit-adk-template/issues)
- **Documentation**: [Google ADK Docs](https://google.github.io/adk-docs/)
- **API Reference**: [Google AI Studio](https://ai.google.dev/)

---

**Made with ❤️ using Google ADK and Chainlit**