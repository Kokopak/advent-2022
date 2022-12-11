import operator
import re
from copy import deepcopy

MAP_SIGN = {
    "+": operator.add,
    "*": operator.mul,
    "/": operator.truediv,
    "-": operator.sub,
}


def parse_monkey(s):
    regex = (
        r"Monkey (\d+):\n"
        r"  Starting items:([ \d+,]*)\n"
        r"  Operation: new = old (.) (.+)\n"
        r"  Test: divisible by (\d+)\n"
        r"    If true: throw to monkey (\d+)\n"
        r"    If false: throw to monkey (\d+)"
    )
    (
        monkey,
        items,
        operator,
        operator_value,
        divisible_by,
        true_monkey,
        false_monkey,
    ) = re.findall(regex, s)[0]

    return monkey, {
        "items": list(map(int, items.split(","))),
        "operator": MAP_SIGN[operator],
        "operator_value": operator_value,
        "divisible_by": divisible_by,
        "if_true": true_monkey,
        "if_false": false_monkey,
        "inspected_items": 0,
    }


def get_monkey_business(n, monkeys, small_number=False):
    total_modulo = 1
    for modulo in [int(monkeys[monkey]["divisible_by"]) for monkey in monkeys]:
        total_modulo *= modulo

    for _ in range(n):
        for monkey in monkeys:
            for i in range(len(monkeys[monkey]["items"])):
                item = monkeys[monkey]["items"].pop(0)

                operator_value = monkeys[monkey]["operator_value"]
                operator_value = (
                    int(operator_value) if operator_value != "old" else item
                )

                divisible_by = int(monkeys[monkey]["divisible_by"])

                worry_level = monkeys[monkey]["operator"](item, operator_value)
                worry_level //= 3 if small_number else 1

                monkeys[monkey]["inspected_items"] += 1

                if worry_level % divisible_by == 0:
                    monkeys[monkeys[monkey]["if_true"]]["items"].append(
                        worry_level % total_modulo
                    )
                else:
                    monkeys[monkeys[monkey]["if_false"]]["items"].append(
                        worry_level % total_modulo
                    )

    inspected_items = [monkeys[monkey]["inspected_items"] for monkey in monkeys]

    return operator.mul(*sorted(inspected_items, reverse=True)[:2])


monkeys = {}

with open("input.txt") as f:
    s = ""
    for l in f.readlines():
        if l == "\n":
            monkey, monkey_def = parse_monkey(s)
            monkeys[monkey] = monkey_def

            s = ""
        else:
            s += l

    monkey, monkey_def = parse_monkey(s)
    monkeys[monkey] = monkey_def


p1 = get_monkey_business(20, deepcopy(monkeys), small_number=True)
print(p1)
p2 = get_monkey_business(10000, deepcopy(monkeys))
print(p2)
