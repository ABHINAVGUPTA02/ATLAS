# 🗺️ Atlas - AI Travel Planner

Atlas is an AI-powered travel planning assistant that helps users plan comprehensive trips with detailed itineraries, cost estimates, weather information, and local recommendations.

## ✨ Features

- **Intelligent Trip Planning**: Generate detailed day-by-day itineraries based on your preferences
- **Weather Information**: Get current weather and forecasts for your destination
- **Place Search**: Find attractions, restaurants, activities, and transportation options
- **Expense Calculator**: Calculate hotel costs, total expenses, and daily budgets
- **Currency Conversion**: Convert between different currencies using real-time exchange rates
- **Document Export**: Save your travel plans as markdown files

## 🏗️ Architecture

Atlas uses a **ReAct (Reasoning + Acting) agent** built with LangGraph that can:
1. Reason about user queries
2. Decide which tools to use
3. Execute tools and incorporate results
4. Provide comprehensive travel recommendations

### Tools Available

| Tool | Description |
|------|-------------|
| `get_current_weather` | Get current weather for a city |
| `get_weather_forecast` | Get 5-day weather forecast |
| `search_attractions` | Find tourist attractions |
| `search_restaurants` | Find restaurants and dining options |
| `search_activities` | Find activities and things to do |
| `search_transportation` | Find transportation options |
| `estimate_total_hotel_cost` | Calculate total hotel expenses |
| `calculate_total_expenses` | Sum up all travel expenses |
| `calculate_daily_expense_budget` | Calculate daily budget |
| `convert_currency` | Convert between currencies |

## 📁 Project Structure

```
Atlas/
├── agent/
│   └── agentic_workflow.py      # LangGraph agent implementation
├── config/
│   └── config.yaml              # Model configuration
├── prompt_library/
│   └── prompt.py                # System prompts
├── tools/
│   ├── weather_info_tool.py     # Weather tools
│   ├── place_search_tool.py     # Place search tools
│   ├── expense_calculator_tool.py # Expense calculation tools
│   └── currency_conversion_tool.py # Currency conversion tool
├── utils/
│   ├── weather_info.py          # Weather API utility
│   ├── place_info_search.py     # Place search utilities
│   ├── expense_calculator.py    # Calculator utility
│   ├── currency_converter.py    # Currency converter utility
│   ├── model_loader.py          # LLM model loader
│   └── save_to_document.py      # Document export utility
├── main.py                      # FastAPI backend
├── streamlit_app.py             # Streamlit frontend
├── requirements.txt             # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- API Keys for:
  - [Groq](https://console.groq.com/) or [OpenAI](https://platform.openai.com/)
  - [OpenWeatherMap](https://openweathermap.org/api)
  - [Tavily](https://tavily.com/)
  - [Google Places](https://developers.google.com/maps/documentation/places/web-service)
  - [ExchangeRate API](https://www.exchangerate-api.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Atlas.git
   cd Atlas
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   # LLM API Keys
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key

   # Tool API Keys
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
   TAVILY_API_KEY=your_tavily_api_key
   GPLACES_API_KEY=your_google_places_api_key
   EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key
   ```

### Running the Application

1. **Start the FastAPI backend**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

2. **Start the Streamlit frontend** (in a new terminal)
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the application**
   - Frontend: http://localhost:8501
   - API Docs: http://localhost:8000/docs

## 📖 Usage

### Via Streamlit UI

1. Open http://localhost:8501 in your browser
2. Enter your travel query (e.g., "Plan a trip to Goa for 5 days with a budget of Rs 50000")
3. Click "Send" and wait for your personalized travel plan

### Via API

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "Plan a trip to Goa for 5 days"}'
```

---

**Happy Travels! 🌍✈️**