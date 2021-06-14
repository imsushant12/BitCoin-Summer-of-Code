import csv

# a global list to contain the final ids of the transactions.
parent = []

def read_id(weight):
    """
    This function will read the csv file in a greedy approach and store the transaction ids
    of the transactions which do not have a parent. It also follows the two mentioned
    conditions:
        1. the weight should be less than 4000000.
        2. the current fee should be greater than the previous fee.
    """
    currentWeight = 0
    # reading the input from the csv file.
    with open('mempool.csv', 'r') as file:
        reader = csv.reader(file, delimiter = '\t')
        currentfee = 0
        # iterating over each row of ids, fee, weight and parent.
        for row in reader:
            newlist = row[0].split(',')
            # iterating the list splitted by comma.
            for i in newlist:
                if currentfee <= int(newlist[1]) and currentWeight < weight:
                    if newlist[3]:
                        pass
                    else:
                        currentfee = int(newlist[1])
                        currentWeight += int(newlist[2])
                        parent.append(newlist[0])
                    break
    return currentWeight, currentfee

def read_parent(weight , fee):
    """
    This function will read the csv file in a greedy approach and store the transaction ids
    of the transactions which do have a parent. It also follows the three mentioned conditions:
        1. the weight should be less than 4000000.
        2. the current fee should be greater than the previous fee.
        3. no transaction should appear before one of its parents.
    """
    currentWeight = 0
    with open('mempool.csv', 'r') as file:
        reader = csv.reader(file, delimiter = '\t')
        currentfee = fee
        for row in reader:
            newlist = row[0].split(',')
            for i in newlist:
                if currentfee <= int(newlist[1]) and currentWeight < weight:
                    if newlist[3] and newlist[3] in parent:
                        currentfee = int(newlist[1])
                        currentWeight += int(newlist[2])
                        parent.append(newlist[0])
                break

def result():
    with open('block.txt' , 'w') as f:
        for item in parent:
            f.write("%s\n" % item)


if __name__ == "__main__":
    currentWeight, currentfee = read_id(4000000)
    if currentWeight < 4000000:
        read_parent(currentWeight, currentfee)
    result()


