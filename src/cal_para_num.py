import numpy as np

num_layers = 12
layer = [[3],
         [1],
         [3],
         [0],
         [4],
         [4],
         [3],
         [1],
         [4],
         [1],
         [3],
         [3]]

parameters_matrix_as_body = np.array([36 * 36 + 3 * 3 * 36 * 36,
                                      36 * 36 + 3 * 3 * 36 + 36 * 36,
                                      36 * 36 + 5 * 5 * 36 * 36,
                                      36 * 36 + 5 * 5 * 36 + 36 * 36,
                                      36 * 36,
                                      36 * 36])


param = []
# cal parameters num
for layer_id in range(num_layers):
    param.append(parameters_matrix_as_body[layer[layer_id][0]])

print('para list %s' % param, 'para num %s' % np.sum(param))
