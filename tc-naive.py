import csv
import pandas as pd
import matplotlib.pyplot as plt



# keeps the size of each set

# takes a csv path. returns a list of tests to mutants
def csv_reader(csv_filename):
    with open(filename, newline='') as File:
        completeness_in_reader = {}
        reader = csv.reader(File)

        # skipping the header
        next(reader)
        for k, y in reader:
            # converting to integers
            k = int(k)
            y = int(y)
            s = completeness_in_reader.get(k, set())
            s.add(y)
            completeness_in_reader[k] = s
        return completeness_in_reader

    # try to count the mutants


# takes the list of tests and tells us how many mutants are in that test
def mutant_weight_counter(completeness):
    mutants_unsorted_weight_keeper = {}
    for size in completeness:
        s = len(completeness.get(size))
        mutants_unsorted_weight_keeper[size] = s
    return mutants_unsorted_weight_keeper


def mutant_sorter(mutants_unsorted_weight_keeper):
    return sorted(mutants_unsorted_weight_keeper.items(), key=lambda w: w[1], reverse=True)


mutants_explored = set()
test_sorted_weight_non_duplicate = []


def duplicate_mutant_remover(test_sorted_weight, completeness):
    global test_sorted_weight_non_duplicate
    global mutants_explored
    for x in test_sorted_weight:

        test_name = x[0]
        failing_mutants = completeness.get(test_name)

        if failing_mutants:
            # remove mutants that are already detected
            failing_mutants = failing_mutants - mutants_explored
            if failing_mutants:
                test_sorted_weight_non_duplicate.append((test_name, len(failing_mutants)))
                mutants_explored = mutants_explored | failing_mutants

    test_sorted_weight_non_duplicate_again = sorted(test_sorted_weight_non_duplicate, key=lambda u: -u[1])
    mutants_explored = sorted(mutants_explored)
    total_mutant_sum = len(mutants_explored)

    current_test_completeness_achieved = [[0, 0]]
    summer = 0

    for i, test in zip(range(len(test_sorted_weight_non_duplicate_again)), test_sorted_weight_non_duplicate_again):
        summer += test[1]
        current_test_completeness_achieved.append([i + 1, summer])
    return current_test_completeness_achieved


def plotter_function(current_test_completeness_achieved, test_sorted_weight_non_duplicate, mutants_explored):
    plotter = pd.DataFrame(
        data=current_test_completeness_achieved,
        columns=["Work", "Test Completeness"]
    )
    ax = plotter.plot(x='Work', y='Test Completeness', xticks=range(len(test_sorted_weight_non_duplicate)),
                      yticks=range(0, len(mutants_explored), 100), legend=False)
    ax.set_ylabel("Test Completeness")
    plt.show()


# putting it altogether
filename = 'test-data/killMap.csv'
completeness_main = csv_reader(filename)
print("final array list is", completeness_main)
mutants_unsorted_weight_keeper_main = mutant_weight_counter(completeness_main)
test_sorted_weight_main = mutant_sorter(mutants_unsorted_weight_keeper_main)
current_test_completeness_achieved_main = duplicate_mutant_remover(test_sorted_weight_main, completeness_main)

print(mutants_unsorted_weight_keeper_main)
print("printing values", test_sorted_weight_main)
plotter_function(current_test_completeness_achieved_main, test_sorted_weight_non_duplicate, mutants_explored)
