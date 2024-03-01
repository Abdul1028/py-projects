import csv
import pyfpgrowth



def load_data(file_path):
    with open(file_path, encoding="utf8", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for i in range(len(data)):
        if '' in data[i]:
            data[i] = [x for x in data[i] if x]

    data.pop(0)
    return data

def mine_fp_tree_and_associations(data, min_support, min_confidence):
    patterns = pyfpgrowth.find_frequent_patterns(data, min_support)
    print("Frequent Patterns:")
    print(patterns)

    rules = pyfpgrowth.generate_association_rules(patterns, min_confidence)
    print("\nAssociation Rules:")
    print(rules)

def main():
    file_path = 'movies1.csv'
    min_support = 2
    min_confidence = 0.7

    # transactions = load_data(file_path)

    # print("Some records:", transactions[0:10])

    transactions = [['B','A'],
                    ['B','D'],
                    ['B','C'],
                    ['B','A','D'],
                    ['A','C'],
                    ['B','C'],
                    ['A','C'],
                    ['B','A','C'],
                    ['B','A','C']]


    a = mine_fp_tree_and_associations(transactions, min_support, min_confidence)
    print(a)

if __name__ == "__main__":
    main()