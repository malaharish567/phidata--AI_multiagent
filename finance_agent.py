from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company):
    #use this function to get the company symbols

    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations=True,stock_fundamentals=True),get_company_symbol],
    instructions = [
        "use the tables to display data,",
        "If you need to find the symbol for a company,use the  get_company_symbol tool."
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True

)

agent.print_response("Summarize and compare analystrecommedations and fundamentals for TSLA and phidata.Show in tables",stream=True)

