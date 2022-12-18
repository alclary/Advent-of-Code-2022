class Monkey:
    def __init__(self, identity, items, operation, test):
        self.identity = identity
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def inspect_items(self, monkey_list):
        print(f"Monkey {self.identity}:")
        while len(self.items) > 0:
            # Inspect item & adjust worry level
            print(f"\tMonkey inspects an item with a worry level of {self.items[0]}.")
            self.items[0] = self.operation(self.items[0])
            self.inspections += 1
            print(f"\t\tWorry level is multiplied to {self.items[0]}")

            # Decrease worry level
            #self.items[0] = self.items[0] // 3
            print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {self.items[0]}")

            # Test worry level and throw item
            test_item = self.test(self.items[0])
            if test_item[0]:
                print(f"\t\tCurrent worry level is divisible.")
                print(f"\t\tItem with worry level {self.items[0]} is thrown to monkey {test_item[1]}")
            else:
                print(f"\t\tCurrent worry level is not divisible.")
                print(f"\t\tItem with worry level {self.items[0]} is thrown to monkey {test_item[1]}")
            self.throw(self.items[0], monkey_list[test_item[1]])
        return

    def throw(self, item, recipient_monkey):
        self.items.remove(item)
        recipient_monkey.items.append(item)
        return

def gen_monkey_list(file_name):
    # seperate monkeys by line breaks
    with open(file_name, 'r') as infile:
        body = infile.read()
        raw_monkey_list = body.split("\n\n")

    monkey_list =  []

    # seperate individual monkey lines by new lines
    for raw_monkey in raw_monkey_list:
        monkey = raw_monkey.split("\n")
        monkey_list.append(monkey)
    return monkey_list

def gen_list_monkey_objs(monkey_list):
    monkey_objs = []
    # parse monkey attributes and functions from str input
    for monkey in monkey_list:
        identity = int(monkey[0].strip(':').split()[1])
        items = monkey[1].lstrip('Starting items: ').strip().split(', ')
        items = list(map(int, items))
        operation_str = monkey[2].strip().split(' = ')[1]
        operation = gen_operation_func(operation_str)
        test_func = gen_test_func(monkey[3:])
        # create Monkey obj and append to list
        monkey_objs.append(Monkey(identity, items, operation, test_func))
    return(monkey_objs)

def gen_operation_func(operation_str):
    # generate operation function via lambda eval
    operation_str = "lambda old: " + operation_str
    operation = eval(operation_str)
    return operation

def gen_test_func(test_lines):
    # parse 3 lines describing test function for variables
    divisor = test_lines[0].strip().split(' by ')[1]
    true_throw = test_lines[1].strip().split('monkey ')[1]
    false_throw = test_lines[2].strip().split('monkey ')[1]

    # template definition for test function
    def test_func(x):
        if x % int(divisor) == 0:
            return (True, int(true_throw))
        else: return (False, int(false_throw))

    return test_func

def run_monkey_round(monkey_obj_list):
    for monkey in monkey_objs:
        monkey.inspect_items(monkey_obj_list)

    print()
    for monkey in monkey_objs:
        print(f"Monkey {monkey.identity}: {monkey.items}")

if __name__ == '__main__':
    monkey_list = gen_monkey_list('input\d11_test.txt')
    monkey_objs = gen_list_monkey_objs(monkey_list)
    rounds = 10000
    for _ in range(rounds):
        run_monkey_round(monkey_objs)

    print()

    for monkey in monkey_objs:
        print(f"Monkey {monkey.identity} inspected items {monkey.inspections} times.")