import tkinter as tk
from DCF_Calculator import DiscountCashFlowCalculator
from STOCKS_DCF_DB import StocksDcfDatabase


def get_years_to_project():
    years = int(years_to_project_input.get())
    return years


def get_required_rate_return():
    required_rate = round(float(required_return_input.get()), 2)
    return required_rate


def get_revenue_inputs():
    # list to hold revenues
    revenues_list = []
    rev1 = int(str(rev_input_period_1.get()).replace(',', ''))
    rev2 = int(str(rev_input_period_2.get()).replace(',', ''))
    rev3 = int(str(rev_input_period_3.get()).replace(',', ''))
    rev4 = int(str(rev_input_period_4.get()).replace(',', ''))
    revenues_list.append(rev1)
    revenues_list.append(rev2)
    revenues_list.append(rev3)
    revenues_list.append(rev4)
    return revenues_list


def get_net_income_inputs():
    # list to hold net incomes
    net_incomes_list = []
    net_income1 = int(str(net_incomes_input1.get()).replace(',', ''))
    net_income2 = int(str(net_incomes_input2.get()).replace(',', ''))
    net_income3 = int(str(net_incomes_input3.get()).replace(',', ''))
    net_income4 = int(str(net_incomes_input4.get()).replace(',', ''))
    net_incomes_list.append(net_income1)
    net_incomes_list.append(net_income2)
    net_incomes_list.append(net_income3)
    net_incomes_list.append(net_income4)
    return net_incomes_list


def get_free_cash_flow_inputs():
    # list to hold net incomes
    free_cash_flow_list = []
    free_cash_flow1 = int(str(free_cash_flows_input1.get()).replace(',', ''))
    free_cash_flow2 = int(str(free_cash_flows_input2.get()).replace(',', ''))
    free_cash_flow3 = int(str(free_cash_flows_input3.get()).replace(',', ''))
    free_cash_flow4 = int(str(free_cash_flows_input4.get()).replace(',', ''))
    free_cash_flow_list.append(free_cash_flow1)
    free_cash_flow_list.append(free_cash_flow2)
    free_cash_flow_list.append(free_cash_flow3)
    free_cash_flow_list.append(free_cash_flow4)
    return free_cash_flow_list


def get_shares_outstanding():
    shares = int(shares_outstanding_input.get())
    return shares


def get_stock_ticker():
    ticker = str(ticker_input.get()).upper()
    return ticker


def get_stock_ticker_label():
    price = str(price_results_label.cget('text'))
    return price


def insert_todays_value(value: int):
    todays_value_input.insert(0, value)


def insert_fair_value_of_equity(fair_value: int):
    fair_value_equity_input.insert(0, fair_value)


def insert_margin_of_safety_25(margin_safety: int):
    margin_safety_label_25_input.insert(0, margin_safety)


def insert_margin_of_safety_15(margin_safety: int):
    margin_safety_label_15_input.insert(0, margin_safety)


def insert_margin_of_safety_10(margin_safety: int):
    margin_safety_label_10_input.insert(0, margin_safety)


def insert_price_now(price):
    price_results_label.config(text=price)


def clear_all_inputs():
    rev_input_period_1.delete(0, tk.END)
    rev_input_period_2.delete(0, tk.END)
    rev_input_period_3.delete(0, tk.END)
    rev_input_period_4.delete(0, tk.END)
    net_incomes_input1.delete(0, tk.END)
    net_incomes_input2.delete(0, tk.END)
    net_incomes_input3.delete(0, tk.END)
    net_incomes_input4.delete(0, tk.END)
    free_cash_flows_input1.delete(0, tk.END)
    free_cash_flows_input2.delete(0, tk.END)
    free_cash_flows_input3.delete(0, tk.END)
    free_cash_flows_input4.delete(0, tk.END)
    years_to_project_input.delete(0, tk.END)
    required_return_input.delete(0, tk.END)
    shares_outstanding_input.delete(0, tk.END)
    todays_value_input.delete(0, tk.END)
    fair_value_equity_input.delete(0, tk.END)
    margin_safety_label_25_input.delete(0, tk.END)
    margin_safety_label_15_input.delete(0, tk.END)
    margin_safety_label_10_input.delete(0, tk.END)
    ticker_input.delete(0, tk.END)
    price_results_label.config(text='')


root = tk.Tk()

# start instance of DCF calculator

calc = DiscountCashFlowCalculator()

# start instance of DCF database

dcf = StocksDcfDatabase()

# 1000x800
height = 750
width = 1000

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f'{width}x{height}')

# title
root.title('Discount Free Cash Flow Calculator')

# configure column row weight
root.columnconfigure(0, weight=5)
root.rowconfigure(0, weight=2)
root.columnconfigure(1, weight=5)
root.rowconfigure(1, weight=2)
root.columnconfigure(2, weight=5)
root.rowconfigure(2, weight=2)
# root.columnconfigure(3, weight=10)
# root.rowconfigure(3, weight=2)

# background
root.config(bg='#e4dfdf')

# add things to gui

# top title label
title = tk.Label(root, text='                                       Discount Free Cash Flow Calculator', relief='solid')
title.config(bg='#92c7f7', font=(None, 18, 'bold'))
title.grid(row=0, column=0, columnspan=4)
title.grid(sticky='nsew')

# top corner frame
top_corner = tk.LabelFrame(root, relief='solid', bg='white')
top_corner.grid(row=0, column=0)
top_corner.grid(padx=1, pady=1)
top_corner.grid(sticky='nwse')

# middle frame
middle_frame = tk.LabelFrame(root, relief='solid', highlightthickness=1, borderwidth=2, bg='#92c7f7')
middle_frame.grid(row=1, column=0, columnspan=4)
middle_frame.grid(padx=20, pady=20)
middle_frame.grid(sticky='nwes')


# top corner label and inputs
ticker_label = tk.Label(top_corner, text='Stock Ticker')
ticker_label.config(bg='white', font=(None, 14, 'bold'))
ticker_label.grid(row=0, column=0)

ticker_input = tk.Entry(top_corner, relief='solid')
ticker_input.config(bg='white', font=(None, 14, 'bold'), width=10, highlightthickness=1, highlightbackground="black")
ticker_input.grid(row=0, column=1)
ticker_input.grid(padx=20, pady=5)

price_results_label = tk.Label(top_corner, relief='solid')
price_results_label.config(bg='white', font=(None, 14, 'bold'), width=9)
price_results_label.grid(row=1, column=1)
price_results_label.grid(padx=1, pady=1)

# middle frame labels and inputs
# known values
known_values = tk.Label(middle_frame, text='Known Values', relief='solid', font=14, width=15, height=1)
known_values.grid(row=0, column=0)
known_values.grid(padx=5, pady=20)

# revenue
revenue_label = tk.Label(middle_frame, text='Revenues', relief='solid', font=14, width=15, height=1)
revenue_label.grid(row=1, column=0)
revenue_label.grid(padx=5, pady=20)

# net incomes
net_incomes = tk.Label(middle_frame, text='Net Incomes', relief='solid', font=14, width=15, height=1)
net_incomes.grid(row=2, column=0)
net_incomes.grid(padx=5, pady=20)

# free cash flow
free_cash_flow = tk.Label(middle_frame, text='Free Cash Flow', relief='solid', font=14, width=15, height=1)
free_cash_flow.grid(row=3, column=0)
free_cash_flow.grid(padx=5, pady=20)

# period 1
create_period_1 = tk.Label(middle_frame, text='Year 1', relief='solid', font=14, width=20, height=1)
create_period_1.grid(row=0, column=1)
create_period_1.grid(padx=5, pady=20)

# period 2
create_period_2 = tk.Label(middle_frame, text='Year 2', relief='solid', font=14, width=20, height=1)
create_period_2.grid(row=0, column=2)
create_period_2.grid(padx=5, pady=20)


# period 3
create_period_3 = tk.Label(middle_frame, text='Year 3', relief='solid', font=14, width=20, height=1)
create_period_3.grid(row=0, column=3)
create_period_3.grid(padx=5, pady=20)

# period 4
create_period_4 = tk.Label(middle_frame, text='Year 4', relief='solid', font=14, width=20, height=1)
create_period_4.grid(row=0, column=4)
create_period_4.grid(padx=5, pady=20)

# revenue input 1
rev_input_period_1 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
rev_input_period_1.config(highlightthickness=1, highlightbackground="black")
rev_input_period_1.grid(row=1, column=1)
rev_input_period_1.grid(padx=5, pady=20)

# revenue input 2
rev_input_period_2 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
rev_input_period_2.config(highlightthickness=1, highlightbackground="black")
rev_input_period_2.grid(row=1, column=2)
rev_input_period_2.grid(padx=5, pady=20)

# revenue input 3
rev_input_period_3 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
rev_input_period_3.config(highlightthickness=1, highlightbackground="black")
rev_input_period_3.grid(row=1, column=3)
rev_input_period_3.grid(padx=5, pady=20)

# # revenue input 4
rev_input_period_4 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
rev_input_period_4.config(highlightthickness=1, highlightbackground="black")
rev_input_period_4.grid(row=1, column=4)
rev_input_period_4.grid(padx=5, pady=20)

# net incomes input 1
net_incomes_input1 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
net_incomes_input1.config(highlightthickness=1, highlightbackground="black")
net_incomes_input1.grid(row=2, column=1)
net_incomes_input1.grid(padx=5, pady=20)

net_incomes_input2 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
net_incomes_input2.config(highlightthickness=1, highlightbackground="black")
net_incomes_input2.grid(row=2, column=2)
net_incomes_input2.grid(padx=5, pady=20)

net_incomes_input3 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
net_incomes_input3.config(highlightthickness=1, highlightbackground="black")
net_incomes_input3.grid(row=2, column=3)
net_incomes_input3.grid(padx=5, pady=20)

net_incomes_input4 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
net_incomes_input4.config(highlightthickness=1, highlightbackground="black")
net_incomes_input4.grid(row=2, column=4)
net_incomes_input4.grid(padx=5, pady=20)

free_cash_flows_input1 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
free_cash_flows_input1.config(highlightthickness=1, highlightbackground="black")
free_cash_flows_input1.grid(row=3, column=1)
free_cash_flows_input1.grid(padx=5, pady=20)

free_cash_flows_input2 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
free_cash_flows_input2.config(highlightthickness=1, highlightbackground="black")
free_cash_flows_input2.grid(row=3, column=2)
free_cash_flows_input2.grid(padx=5, pady=20)

free_cash_flows_input3 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
free_cash_flows_input3.config(highlightthickness=1, highlightbackground="black")
free_cash_flows_input3.grid(row=3, column=3)
free_cash_flows_input3.grid(padx=5, pady=20)

free_cash_flows_input4 = tk.Entry(middle_frame, relief='solid', font=14, width=20)
free_cash_flows_input4.config(highlightthickness=1, highlightbackground="black")
free_cash_flows_input4.grid(row=3, column=4)
free_cash_flows_input4.grid(padx=5, pady=20)

# bottom left frame
bottom_left_frame = tk.LabelFrame(root, relief='solid', highlightthickness=1, borderwidth=2, bg='#92c7f7')
bottom_left_frame.grid(row=2, column=0)
bottom_left_frame.grid(padx=20, pady=20)
bottom_left_frame.grid(sticky='nws')

# create labels and inputs for bottom left frame

years_to_project = tk.Label(bottom_left_frame, text='Years to Project', relief='solid',
                            font=14, width=20, height=1)

years_to_project.grid(row=0, column=0)
years_to_project.grid(padx=5, pady=20)


required_return = tk.Label(bottom_left_frame, text='Required Return', relief='solid',
                            font=14, width=20, height=1)
required_return.grid(row=1, column=0)
required_return.grid(padx=5, pady=20)


perpetual_growth_rate = tk.Label(bottom_left_frame, text='Perpetual Growth Rate', relief='solid',
                                 font=14, width=20, height=1)
perpetual_growth_rate.grid(row=2, column=0)
perpetual_growth_rate.grid(padx=5, pady=20)

shares_outstanding = tk.Label(bottom_left_frame, text='Shares Outstanding', relief='solid',
                              font=14, width=20, height=1)
shares_outstanding.grid(row=3, column=0)
shares_outstanding.grid(padx=5, pady=20)

todays_value = tk.Label(bottom_left_frame, text='Todays Value', relief='solid',
                        font=14, width=20, height=1)
todays_value.grid(row=4, column=0)
todays_value.grid(padx=5, pady=20)

years_to_project_input = tk.Entry(bottom_left_frame, relief='solid', font=14, width=18)
years_to_project_input.config(highlightthickness=1, highlightbackground="black")
years_to_project_input.grid(row=0, column=1)
years_to_project_input.grid(padx=5, pady=20)

required_return_input = tk.Entry(bottom_left_frame, relief='solid', font=14, width=18)
required_return_input.config(highlightthickness=1, highlightbackground="black")
required_return_input.grid(row=1, column=1)
required_return_input.grid(padx=5, pady=20)

perpetual_growth_rate_input = tk.Label(bottom_left_frame, relief='solid', text=f'{(calc.perpetual_growth_rate * 100)}%',
                                       font=14, width=18, bg='white')
perpetual_growth_rate_input.config(highlightthickness=1, highlightbackground="black")
perpetual_growth_rate_input.grid(row=2, column=1)
perpetual_growth_rate_input.grid(padx=5, pady=20)

shares_outstanding_input = tk.Entry(bottom_left_frame, relief='solid', font=14, width=18)
shares_outstanding_input.config(highlightthickness=1, highlightbackground="black")
shares_outstanding_input.grid(row=3, column=1)
shares_outstanding_input.grid(padx=5, pady=20)

todays_value_input = tk.Entry(bottom_left_frame, relief='solid', font=14, width=18)
todays_value_input.config(highlightthickness=1, highlightbackground="black")
todays_value_input.grid(row=4, column=1)
todays_value_input.grid(padx=5, pady=20)

# bottom right frame
bottom_right_frame = tk.LabelFrame(root, relief='solid', highlightthickness=1, borderwidth=2, bg='#92c7f7')
bottom_right_frame.grid(row=2, column=1, columnspan=1)
bottom_right_frame.grid(padx=0, pady=20)
bottom_right_frame.grid(sticky='nws')

# set bottom right frame grid
bottom_right_frame.columnconfigure(0, weight=1)
bottom_right_frame.rowconfigure(0, weight=0)
bottom_right_frame.columnconfigure(1, weight=1)
bottom_right_frame.rowconfigure(1, weight=0)
bottom_right_frame.rowconfigure(2, weight=0)
bottom_right_frame.rowconfigure(3, weight=0)
bottom_right_frame.rowconfigure(4, weight=0)

# create labels and inputs for bottom right frame

share_prices = tk.Label(bottom_right_frame, text='Share Prices', relief='solid',
                        font=18, width=37, height=2)
share_prices.grid(row=0, column=0, columnspan=2)
share_prices.grid(padx=5, pady=5)

fair_value_equity = tk.Label(bottom_right_frame, text='Fair Value of Equity', relief='solid',
                        font=14, width=20, height=1)
fair_value_equity.grid(row=1, column=0)
fair_value_equity.grid(padx=5, pady=20)
fair_value_equity.grid(sticky='nw')

margin_safety_label_25 = tk.Label(bottom_right_frame, text='25% Margin of Safety', relief='solid',
                        font=14, width=20, height=1)
margin_safety_label_25.grid(row=2, column=0)
margin_safety_label_25.grid(padx=5, pady=20)
margin_safety_label_25.grid(sticky='nw')

margin_safety_label_15 = tk.Label(bottom_right_frame, text='15% Margin of Safety', relief='solid',
                        font=14, width=20, height=1)
margin_safety_label_15.grid(row=3, column=0)
margin_safety_label_15.grid(padx=5, pady=20)
margin_safety_label_15.grid(sticky='nw')

margin_safety_label_10 = tk.Label(bottom_right_frame, text='10% Margin of Safety', relief='solid',
                        font=14, width=20, height=1)
margin_safety_label_10.grid(row=4, column=0)
margin_safety_label_10.grid(padx=5, pady=20)
margin_safety_label_10.grid(sticky='nw')

fair_value_equity_input = tk.Entry(bottom_right_frame, relief='solid', font=14, width=15)
fair_value_equity_input.config(highlightthickness=1, highlightbackground="black")
fair_value_equity_input.grid(row=1, column=1)
fair_value_equity_input.grid(padx=5, pady=20)

margin_safety_label_25_input = tk.Entry(bottom_right_frame, relief='solid', font=14, width=15)
margin_safety_label_25_input.config(highlightthickness=1, highlightbackground="black")
margin_safety_label_25_input.grid(row=2, column=1)
margin_safety_label_25_input.grid(padx=5, pady=20)

margin_safety_label_15_input = tk.Entry(bottom_right_frame, relief='solid', font=14, width=15)
margin_safety_label_15_input.config(highlightthickness=1, highlightbackground="black")
margin_safety_label_15_input.grid(row=3, column=1)
margin_safety_label_15_input.grid(padx=5, pady=20)

margin_safety_label_10_input = tk.Entry(bottom_right_frame, relief='solid', font=14, width=15)
margin_safety_label_10_input.config(highlightthickness=1, highlightbackground="black")
margin_safety_label_10_input.grid(row=4, column=1)
margin_safety_label_10_input.grid(padx=5, pady=20)

# frame bottom button frame
bottom_button_frame = tk.LabelFrame(root, relief='solid', bg='white')
bottom_button_frame.grid(row=2, column=2)
bottom_button_frame.grid(padx=10, pady=21)
bottom_button_frame.grid(sticky='ws')


# bottom_button_frame.grid(sticky='n')


# bottom button labels
save_record = tk.Button(bottom_button_frame, relief='solid', text='SAVE RECORD', font=14, width=13, height=1,
                        borderwidth=2, command=lambda: dcf.insert_record_into_db(get_stock_ticker(), get_stock_ticker_label(),
                                              calc.previous_revenues[0], calc.previous_revenues[1],
                                              calc.previous_revenues[2], calc.previous_revenues[3],
                                              calc.previous_net_incomes[0], calc.previous_net_incomes[1],
                                              calc.previous_net_incomes[2], calc.previous_net_incomes[3],
                                              calc.previous_free_cash_flows[0], calc.previous_free_cash_flows[1],
                                              calc.previous_free_cash_flows[2], calc.previous_free_cash_flows[3],
                                              calc.years_to_project, calc.required_return, calc.shares_outstanding,
                                              calc.todays_value, calc.fair_value_of_equity,
                                              calc.margins_of_safety['percent_25'], calc.margins_of_safety['percent_15'],
                                              calc.margins_of_safety['percent_10']))
save_record.config(font=(None, 14, 'bold'), bg='yellow')
save_record.grid(row=2, column=0)
save_record.grid(padx=5, pady=10)

# buttons

button_calculate = tk.Button(bottom_button_frame, text='CALCULATE', relief='solid', width=13, height=1, borderwidth=2,
                             command=lambda: [calc.set_required_rate_return(get_required_rate_return()),
                                              calc.set_years_to_project(get_years_to_project()),
                                              calc.set_previous_revenues(get_revenue_inputs()),
                                              calc.set_previous_net_incomes(get_net_income_inputs()),
                                              calc.set_previous_free_cash_flows(get_free_cash_flow_inputs()),
                                              calc.set_average_free_cash_flow_net_income(),
                                              calc.set_annual_average_growth_rate(),
                                              calc.set_projected_revenues(),
                                              calc.set_projected_net_incomes(),
                                              calc.set_projected_free_cash_flows(),
                                              calc.set_terminal_value(),
                                              calc.set_discount_factors(),
                                              calc.set_pv_future_cash_flows(),
                                              calc.set_discounted_terminal_value(),
                                              calc.set_todays_value(),
                                              calc.set_shares_outstanding(get_shares_outstanding()),
                                              calc.set_fair_value_of_equity(),
                                              calc.set_margins_of_safety(),
                                              insert_todays_value(calc.todays_value),
                                              insert_fair_value_of_equity(calc.fair_value_of_equity),
                                              insert_margin_of_safety_25(calc.margins_of_safety['percent_25']),
                                              insert_margin_of_safety_15(calc.margins_of_safety['percent_15']),
                                              insert_margin_of_safety_10(calc.margins_of_safety['percent_10'])])
button_calculate.config(font=(None, 14, 'bold'), bg='lightgreen')
button_calculate.grid(row=0, column=0)
button_calculate.grid(padx=5, pady=15)
# button_calculate.grid(sticky='nwe')

button_clear = tk.Button(bottom_button_frame, text='CLEAR', relief='solid', width=13, height=1, borderwidth=2,
                         command=lambda: clear_all_inputs())
button_clear.config(font=(None, 14, 'bold'), bg='red')
button_clear.grid(row=3, column=0)
button_clear.grid(padx=5, pady=15)
# button_clear.grid(sticky='swe')

# visualize button
visualize_button = tk.Button(bottom_button_frame, text='VISUALIZE', relief='solid', width=13, height=1, borderwidth=2,
                             command=lambda: calc.run_visualizations())
visualize_button.config(font=(None, 14, 'bold'), bg='lightblue')
visualize_button.grid(row=1, column=0)
visualize_button.grid(padx=5, pady=15)


# button top left
button_get_price = tk.Button(top_corner, text='Get Price Now', relief='solid', width=12,
                             command=lambda: insert_price_now(calc.get_current_stock_price(get_stock_ticker())))
button_get_price.config(font=(None, 12, 'bold'), bg='lightgreen')
button_get_price.grid(row=1, column=0)
button_get_price.grid(padx=2, pady=0)
button_get_price.grid(sticky='nw')


# disable window resize
root.resizable(False, False)


# run
root.mainloop()

dcf.conn.close()
