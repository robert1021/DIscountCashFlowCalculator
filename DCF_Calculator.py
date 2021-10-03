import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yahoo_fin.stock_info as si


class DiscountCashFlowCalculator:

    def __init__(self):
        self.current_ticker = None
        self.current_stock_price = None
        self.required_return = None
        self.perpetual_growth_rate = 0.025
        self.years_to_project = None
        self.previous_net_incomes = None
        self.previous_free_cash_flows = None
        self.average_free_cash_flow_to_net_income = None
        self.previous_revenues = None
        self.annual_average_growth_rate = None
        self.projected_revenues = None
        self.projected_net_incomes = None
        self.projected_free_cash_flows = None
        self.shares_outstanding = None
        self.terminal_value = None
        self.discount_factors = None
        self.pv_future_cash_flows = None
        self.discounted_terminal_value = None
        self.todays_value = None
        self.fair_value_of_equity = None
        self.margins_of_safety = None

    # setters
    def set_current_ticker(self, ticker: str):
        """ Sets the current ticker.

        Parameters
        ----------
            ticker(str): A list of previous years free cash flows.

        """
        ticker = ticker.upper()
        self.current_ticker = ticker

    def set_current_stock_price(self):
        """ Sets the current stock price.

        """
        self.current_stock_price = round(si.get_live_price(self.current_ticker), 2)

    def set_required_rate_return(self, required_return: float):
        """ Sets required rate of return in the constructor.

        """
        self.required_return = required_return

    def set_previous_net_incomes(self, previous_net_incomes: list):
        """ Sets previous net incomes in the constructor to a list of values.

        Parameters
        ----------
            previous_net_incomes(list): A list of previous years net incomes.

        """
        if type(previous_net_incomes) is not list:
            self.previous_net_incomes = [previous_net_incomes]
        else:
            self.previous_net_incomes = previous_net_incomes

    def set_previous_free_cash_flows(self, previous_free_cash_flows: list):
        """ Sets previous free cash flows in constructor to a list of values.

        Parameters
        ----------
            previous_free_cash_flows(list): A list of previous years free cash flows.

        """
        if type(previous_free_cash_flows) is not list:
            self.previous_free_cash_flows = [previous_free_cash_flows]
        else:
            self.previous_free_cash_flows = previous_free_cash_flows

    def set_average_free_cash_flow_net_income(self):
        """ Sets average free cash flows to net income in the constructor.
        
        """
        self.average_free_cash_flow_to_net_income = self.calculate_free_cash_flow_net_income()

    def set_previous_revenues(self, previous_revenues: list):
        """ Sets previous revenues in the constructor.

        """
        if type(previous_revenues) is not list:
            self.previous_revenues = [previous_revenues]
        else:
            self.previous_revenues = previous_revenues

    def set_annual_average_growth_rate(self):
        """ Sets the annual average growth rate.

        """
        self.annual_average_growth_rate = self.calculate_annual_average_growth_rate()

    def set_projected_revenues(self):
        """ Sets projected revenues for x amount of years in the constructor.

        Parameters
        ----------
            years_to_project(int): The amount of years of revenue to project.

        """
        self.projected_revenues = self.calculate_projected_revenue_for_x_years()

    def set_projected_net_incomes(self):
        """ Sets projected net incomes in the constructor.

        """
        self.projected_net_incomes = self.calculate_projected_net_income()

    def set_projected_free_cash_flows(self):
        """ Sets projected free cash flows in the constructor.

        """
        self.projected_free_cash_flows = self.calculate_projected_free_cash_flow()

    def set_shares_outstanding(self, number_shares_outstanding: int or float):
        """ Sets previous net incomes in the constructor to a list of values.

        Parameters
        ----------
            number_shares_outstanding(int): The number of shares outstanding.

        """
        self.shares_outstanding = number_shares_outstanding

    def set_terminal_value(self):
        """ Sets terminal value in the constructor.

        """
        self.terminal_value = self.calculate_terminal_value()

    def set_discount_factors(self):
        """ Sets discount factors in the constructor.

        """
        self.discount_factors = self.calculate_discount_factor()

    def set_pv_future_cash_flows(self):
        """ Sets present values of future cash flows in the constructor.

        """
        self.pv_future_cash_flows = self.calculate_pv_future_cash_flows()

    def set_discounted_terminal_value(self):
        """ Sets the discounted terminal value in the constructor.

        """
        self.discounted_terminal_value = self.calculate_discounted_terminal_value()

    def set_todays_value(self):
        """ Sets todays value of the company in the constructor.

        """
        self.todays_value = self.calculate_todays_value()

    def set_fair_value_of_equity(self):
        """ Sets fair value of equity in the constructor.

        """
        self.fair_value_of_equity = self.calculate_fair_value_of_equity()

    def set_margins_of_safety(self):
        """ Sets margins of safety in the constructor.

        """
        self.margins_of_safety = self.calculate_margins_of_safety()

    def set_years_to_project(self, years_to_project: int):
        """ Sets years to project in the constructor.

        """
        self.years_to_project = years_to_project

    def get_current_stock_price(self, ticker: str):
        """ Gets the current stock price from provided ticker.

        Parameters
        ----------
            ticker(str): The ticker of stocks price you would like.

        Returns
        ----------
            current_stock_price(float): The current stock price of the provided ticker.

        """
        self.set_current_ticker(ticker)
        self.set_current_stock_price()
        return self.current_stock_price

    def calculate_free_cash_flow_net_income(self):
        """ Calculate free cash flow to net income ratio.

        Returns
        ----------
            average_fcfe_to_net_income(float): The average fcfe to net income of all periods.
        """
        # list of fcfe / net income
        results = []
        for income, cash_flow in zip(self.previous_net_incomes, self.previous_free_cash_flows):
            result_of_calculation = cash_flow / income
            results.append(result_of_calculation)
        add_all_results = sum(results)
        average_fcfe_to_net_income = add_all_results / len(results)
        return average_fcfe_to_net_income

    def calculate_annual_average_growth_rate(self):
        """ Calculate annual average growth rate from given revenues for x time frame.

        Returns
        ----------
            aagr(float): Annual average growth rate.

        """
        # counter
        counter = 1
        # list of growth rates
        growth_rates = []
        last_revenues_index = len(self.previous_revenues) - 1
        for rev in self.previous_revenues:
            if not counter > last_revenues_index:
                growth_rate = (self.previous_revenues[counter] / rev) - 1
                counter += 1
                growth_rates.append(growth_rate)
        aagr = sum(growth_rates) / last_revenues_index
        return aagr

    def calculate_projected_revenue_for_x_years(self):
        """ Calculates the projected revenue for x amount of years.

        Parameters
        ----------
            years_to_project(int): The amount of years of revenue to project.

        Returns
        ----------
            projections(list): The projected revenue numbers.

        """
        # list to hold revenue projections
        projections = []
        last_revenue_number = self.previous_revenues[-1]
        years_to_project = self.years_to_project
        for i in range(1, (years_to_project + 1)):
            revenue = last_revenue_number * (1 + self.annual_average_growth_rate)
            last_revenue_number = revenue
            projections.append(int(revenue))
        return projections

    def calculate_projected_net_income(self):
        """ Calculates the projected net incomes for x amount of years.

        Returns
        ----------
            projected_net_incomes(list): The projected net income numbers.

        """
        # list to hold project incomes
        projected_net_incomes = []
        # list of net income margins
        net_income_margins = []
        for income, revenue in zip(self.previous_net_incomes, self.previous_revenues):
            net_income_margin = income / revenue
            net_income_margins.append(net_income_margin)
        average_net_income_margins = sum(net_income_margins) / len(self.previous_net_incomes)
        for rev in self.projected_revenues:
            net_income = int(rev * average_net_income_margins)
            projected_net_incomes.append(net_income)
        return projected_net_incomes

    def calculate_projected_free_cash_flow(self):
        """ Calculates the projected free cash flows for x amount of years.

        Returns
        ----------
            projected_free_cash_flows(list): The projected free cash flow numbers.

        """
        # list of project free cash flows
        projected_free_cash_flows = []
        for income in self.projected_net_incomes:
            cash_flow = int(income * self.average_free_cash_flow_to_net_income)
            projected_free_cash_flows.append(cash_flow)
        return projected_free_cash_flows

    def calculate_terminal_value(self):
        """ Calculates the terminal value.

        Returns
        ----------
            terminal_value(int): The terminal value.

        """
        final_free_cash_flow = self.projected_free_cash_flows[-1]
        terminal_value = int((final_free_cash_flow * (1 + self.perpetual_growth_rate)) /
                             (self.required_return - self.perpetual_growth_rate))
        return terminal_value

    def calculate_discount_factor(self):
        """ Calculates the discount factor for each period.

       Returns
       ----------
           discount_factors(list): The discount factor of each period.

       """
        # list to hold discount factors for each time period
        discount_factors = []
        len_time_periods = len(self.projected_revenues)
        for i in range(1, (len_time_periods + 1)):
            discount_factor = round((1 + self.required_return) ** i, 3)
            discount_factors.append(discount_factor)
        return discount_factors

    def calculate_pv_future_cash_flows(self):
        """ Calculates the present value of future cash flow for each period.

       Returns
       ----------
           pv_future_cash_flows(list): The present values of future cash flows.

       """
        # list to hold pv of future cash flows for each period
        pv_future_cash_flows = []
        for cash_flow, discount_factor in zip(self.projected_free_cash_flows, self.discount_factors):
            pv_future_cash_flow = int(cash_flow / discount_factor)
            pv_future_cash_flows.append(pv_future_cash_flow)
        return pv_future_cash_flows

    def calculate_discounted_terminal_value(self):
        """ Calculates the discounted terminal value.

       Returns
       ----------
           discounted_terminal_value(int): The discounted terminal value.

       """
        last_discount_factor = self.discount_factors[-1]
        discounted_terminal_value = int(self.terminal_value / last_discount_factor)
        return discounted_terminal_value

    def calculate_todays_value(self):
        """ Calculates todays value of the company.

       Returns
       ----------
           todays_value(int): Todays value of the company.

       """
        todays_value = int(sum(self.pv_future_cash_flows) + self.discounted_terminal_value)
        return todays_value

    def calculate_fair_value_of_equity(self):
        """ Calculates fair value of equity.

       Returns
       ----------
           fair_value(float): Fair value of equity.

       """
        fair_value = round(self.todays_value / self.shares_outstanding, 2)
        return fair_value

    def calculate_margins_of_safety(self):
        """ Calculates the margins of safety of fair value of equity.

       Returns
       ----------
           margins_of_safety(dict): Dict of 25, 15, 10 , and 5 percent margins of safety.

       """
        margins_of_safety = {}
        numbers_to_use = [0.25, 0.15, 0.10, 0.05]
        for number in numbers_to_use:
            result = round(self.fair_value_of_equity / (1 + number), 2)
            margins_of_safety.setdefault(f'percent_{int(number * 100)}', result)
        return margins_of_safety

    def visualize_revenue(self):
        """ Plots the revenue for the current ticker.

        """
        all_revenues = self.previous_revenues + self.projected_revenues
        # values
        x_axis_numbers = [i for i in range(1, len(all_revenues) + 1)]
        x_axis = x_axis_numbers
        y1 = all_revenues[0:4]
        y2 = all_revenues[3:]
        # plot
        plt.plot(x_axis[0:4], y1, 'b-')
        plt.plot(x_axis[3:], y2, 'g--')
        # disabling offset on y axis
        plt.ticklabel_format(style='plain')
        # set labels
        plt.xlabel('YEARS')
        plt.ylabel('REVENUE')
        plt.title('PROJECTED REVENUE')
        # show
        plt.show()

    def visualize_net_income(self):
        """ Plots the net income for the current ticker.

        """
        all_net_incomes = self.previous_net_incomes + self.projected_net_incomes
        # values
        x_axis_numbers = [i for i in range(1, len(all_net_incomes) + 1)]
        x_axis = x_axis_numbers
        y1 = all_net_incomes[0:4]
        y2 = all_net_incomes[3:]
        # plot
        plt.plot(x_axis[0:4], y1, 'b-')
        plt.plot(x_axis[3:], y2, 'g--')
        # disabling offset on y axis
        plt.ticklabel_format(style='plain')
        # set labels
        plt.xlabel('YEARS')
        plt.ylabel('NET INCOME')
        plt.title('PROJECTED NET INCOME')
        # show
        plt.show()

    def visualize_free_cash_flow(self):
        """ Plots the free cash flow for the current ticker.

        """
        all_free_cash_flows = self.previous_free_cash_flows + self.projected_free_cash_flows
        # values
        x_axis_numbers = [i for i in range(1, len(all_free_cash_flows) + 1)]
        x_axis = x_axis_numbers
        y1 = all_free_cash_flows[0:4]
        y2 = all_free_cash_flows[3:]
        # plot
        plt.plot(x_axis[0:4], y1, 'b-')
        plt.plot(x_axis[3:], y2, 'g--')
        # disabling offset on y axis
        plt.ticklabel_format(style='plain')
        # set labels
        plt.xlabel('YEARS')
        plt.ylabel('FREE CASH FLOW')
        plt.title('PROJECTED FREE CASH FLOW')
        # show
        plt.show()

    def visualize_all_time_chart(self):
        """ Plots the all time chart for the current ticker.

        """
        df = si.get_data(self.current_ticker)
        df.reset_index(level=0, inplace=True)
        fig = go.Figure(data=[go.Candlestick(x=df['index'],
                                             open=df['open'],
                                             high=df['high'],
                                             low=df['low'],
                                             close=df['close'])])
        fig.update_layout(title=f'{self.current_ticker} ALL TIME CHART',
                          xaxis_title='DATE',
                          yaxis_title='PRICE')
        fig.show()

    def run_visualizations(self):
        """ Run four functions to visualize data.

        """
        self.visualize_revenue()
        self.visualize_net_income()
        self.visualize_free_cash_flow()
        self.visualize_all_time_chart()







