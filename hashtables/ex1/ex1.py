#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# #Brute Force
# def get_indices_of_item_weights(weights, length, limit):
#     ht = HashTable(16)

#     """
#     YOUR CODE HERE
#     """
#     if len(weights) is 1:
#         return None
#     winners = []
#     for i in range(len(weights)):
#         for j in range(i+1, len(weights)):
#             if weights[i] + weights[j] == limit:
#                 if j > i:
#                     good = [j,i]
#                 else:
#                     good = [i,j]
                
#                 # print(good)
#                 winners.append(good)

#     best_winner_index = 0
#     best_winner_number = 0
#     for i in range(len(winners)):
#         if weights[winners[i][0]] > best_winner_number:
#             best_winner_number = weights[winners[i][0]]
#             best_winner_index = i

#     return winners[best_winner_index]


def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    if len(weights) == 1:
        return None
    ht = HashTable(16)
    winner = []
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    for i in weights:
        search = limit - i
        search_ht = hash_table_retrieve(ht, search)
        if search_ht:
            # print("GOOD", search_ht)
            winner.append(search_ht)
            hash_table_remove(ht, search)
            winner.append(hash_table_retrieve(ht, i))
            return winner
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
