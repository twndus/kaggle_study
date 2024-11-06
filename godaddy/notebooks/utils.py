# define evaluation metric, SMAPE
def SMAPE(actuals, preds):
	smape = 0
	for actual, pred in zip(actuals, preds):
		if (actual==0) and (pred==0): continue
		smape += abs(actual-pred) / (abs(actual) + abs(pred)) * 2 * 100
	return smape / len(actuals)