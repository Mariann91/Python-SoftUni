class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):

        if isinstance(float_value, float):
            return Integer(int(float_value))

        return "value is not a float"

    @classmethod
    def from_roman(cls, value):

        romans_as_integers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0

        for i in range(len(value)):

            if i != 0 and romans_as_integers[value[i]] > romans_as_integers[value[i - 1]]:
                result += romans_as_integers[value[i]] - 2 * romans_as_integers[value[i - 1]]
            else:
                result += romans_as_integers[value[i]]

        return Integer(result)

    @classmethod
    def from_string(cls, value):

        if not isinstance(value, str):
            return "wrong type"

        return Integer(int(value))
