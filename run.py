from pricing_agent import PricingAgent
from forecast_agent import DemandForecastingAgent

def main():
    try:
        use_llm = input("Do you want help from the LLM? (yes/no): ").strip().lower()

        if use_llm == "yes":
            agent_choice = input("Which agent would you like to ask? (pricing/forecast): ").strip().lower()
            prompt = input("Enter your question for the LLM: ")

            if agent_choice == "pricing":
                agent = PricingAgent()
                response = agent.get_llm_suggestion(prompt)
                if response.startswith("LLM Timeout/Error") or response.startswith("LLM Error"):
                    raise Exception(response)
                print("\nLLM - Pricing Agent Response:\n", response)

            elif agent_choice == "forecast":
                agent = DemandForecastingAgent()
                if hasattr(agent, 'get_llm_suggestion'):
                    response = agent.get_llm_suggestion(prompt)
                    if response.startswith("LLM Timeout/Error") or response.startswith("LLM Error"):
                        raise Exception(response)
                    print("\nLLM - Forecast Agent Response:\n", response)
                else:
                    print("This agent does not yet support LLM input.")

            else:
                print("Unknown agent name. Try 'pricing' or 'forecast'.")

        else:
            raise Exception("LLM use not requested")

    except Exception as e:
        print(f"\nLLM Unavailable or Skipped: {e}")
        print("[Running agent logic manually instead...]\n")

        pricing_agent = PricingAgent()
        print("Pricing Agent - Adjusted Restock Quantity:", pricing_agent.adjusted_restock_quantity())

        forecast_agent = DemandForecastingAgent()
        print("Forecast Agent - Predicted Demand:", forecast_agent.predict_demand())


if __name__ == "__main__":
    main()
