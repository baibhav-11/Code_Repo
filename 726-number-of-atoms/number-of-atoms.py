class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(formula, i):
            count_dict = {}
            while i < len(formula):
                if formula[i] == '(':
                    i += 1
                    sub_count_dict, i = parse_formula(formula, i)
                    count = 0
                    while i < len(formula) and formula[i].isdigit():
                        count = count * 10 + int(formula[i])
                        i += 1
                    count = max(count, 1)
                    for element, element_count in sub_count_dict.items():
                        count_dict[element] = count_dict.get(element, 0) + element_count * count
                elif formula[i] == ')':
                    i += 1
                    return count_dict, i
                else:
                    element = formula[i]
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        element += formula[i]
                        i += 1
                    count = 0
                    while i < len(formula) and formula[i].isdigit():
                        count = count * 10 + int(formula[i])
                        i += 1
                    count = max(count, 1)
                    count_dict[element] = count_dict.get(element, 0) + count
            return count_dict, i
        
        count_dict, _ = parse_formula(formula, 0)
        elements = list(count_dict.keys())
        elements.sort()
        result = ""
        for element in elements:
            result += element
            if count_dict[element] > 1:
                result += str(count_dict[element])
        return result