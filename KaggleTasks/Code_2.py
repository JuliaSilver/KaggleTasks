candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
mae_list = [] #ошибка
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
for node in candidate_max_leaf_nodes:
    mae = get_mae(node, train_X, val_X, train_y, val_y) #функция высчитывает ошибку с текущими значениями х, у из трен и валид датасетов и некоторого количества узлов дерева
    mae_list.append(mae)
smallest_error = min(mae_list)
inx = mae_list.index(smallest_error)
# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = candidate_max_leaf_nodes[inx]
print(best_tree_size)
