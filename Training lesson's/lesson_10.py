def calculate(amount, years, rate):
   for year in range(0, years):
       amount *= 1+rate
   return amount

total = calculate(2000, 10, 0.1)
print(total)

def do_it(param_1: int, param_2: str, param_3: float) -> list:
		"""
				Эта функция берет первые два параметра, складывает их и делит на третий.
				Результат печатается в консоль.
				Параметры должны быть в консоли.
				int — 19;
                float — 2.6;
                bool — True/False;
                str — “Test”;
                dict — {};
                list — [].
		"""
        result = (param_1 + param_2) * param_3
    return [param_1, param_2, param_3, result]
lst = do_it(1, 2, 3)