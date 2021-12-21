class Operations(object):
    
    @staticmethod
    def compute_result(value, currencies):
        result_currencies = []
        for key in currencies:
            result_currencies.append(value * currencies[key])
        return result_currencies