num_of_steps = 12
log_file = 'analytics.log'

def report_template(heads, tails, headf, tailf):
    return f"Report\nWe have made {num_of_steps} observations from tossing a coin: {tails} of them were tails and {heads} of\
them were heads. The probabilities are {round(tailf, 3)}% and {round(headf, 3)}%, respectively. Our\
forecast is that in the next 3 observations we will have: {1 if tails > heads else 2} tail and {1 if tails <= heads else 2} heads.\n"
