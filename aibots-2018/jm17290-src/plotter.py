import matplotlib.pyplot as plt
import numpy as np

# Plotting fitness of resistance genes with spy genes with subsequent generations.
# resistance_genes, = plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
#                              [0.191564147627417, 0.20855614973262, 0.207513416815742, 0.225303292894281, 0.220430107526882, 0.222222222222222, 0.218487394957983, 0.224416517055655, 0.202578268876611, 0.217857142857143, 0.224168126094571, 0.216318785578748, 0.210431654676259, 0.223931623931624, 0.229323308270677, 0.217616580310881, 0.217537942664418, 0.234234234234234, 0.218694885361552, 0.213780918727915, 0.227443609022556, 0.23963963963964, 0.212435233160622, 0.228621291448517, 0.221837088388215, 0.228828828828829, 0.228426395939086, 0.24031007751938, 0.217314487632509, 0.225303292894281, 0.211908931698774, 0.254054054054054, 0.25414364640884, 0.271719038817006, 0.272893772893773, 0.261460101867572, 0.260714285714286, 0.289855072463768, 0.281138790035587, 0.283609576427256, 0.267504488330341, 0.276338514680484, 0.272727272727273, 0.264, 0.278084714548803, 0.28219696969697, 0.271959459459459, 0.28842504743833, 0.273921200750469, 0.257042253521127, 0.290843806104129, 0.280405405405405, 0.259124087591241, 0.285470085470085, 0.283216783216783, 0.261648745519713, 0.31214953271028, 0.293402777777778, 0.280148423005566, 0.274956217162872, 0.27447216890595],
#                              label='Resistance Genes')
#
# spy_genes, = plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
#                       [0.329446064139942, 0.345744680851064, 0.383908045977011, 0.369620253164557, 0.376923076923077, 0.368146214099217, 0.371900826446281, 0.373655913978495, 0.366748166259169, 0.409090909090909, 0.38961038961039, 0.393700787401575, 0.440594059405941, 0.454545454545455, 0.457219251336898, 0.417553191489362, 0.450520833333333, 0.481894150417827, 0.434447300771208, 0.450980392156863, 0.462915601023018, 0.455555555555556, 0.436314363143631, 0.4343163538874, 0.430051813471503, 0.462365591397849, 0.450980392156863, 0.45983379501385, 0.454773869346734, 0.493540051679587, 0.488888888888889, 0.526041666666667, 0.497252747252747, 0.50379746835443, 0.485714285714286, 0.490666666666667, 0.528, 0.513715710723192, 0.51063829787234, 0.520435967302452, 0.5, 0.501222493887531, 0.526315789473684, 0.518229166666667, 0.521390374331551, 0.541025641025641, 0.511363636363636, 0.510752688172043, 0.520618556701031, 0.531746031746032, 0.554896142433234, 0.530026109660574, 0.526760563380282, 0.555269922879177, 0.54957507082153, 0.538647342995169, 0.537396121883656, 0.531486146095718, 0.542234332425068, 0.528, 0.559278350515464],
#                       label='Spy Genes')
#
# plt.title('Fitness Improvement with Subsequent Generations')
# plt.ylabel('Fitness (Games Won %)')
# plt.xlabel('Generation')
# plt.legend(handles=[resistance_genes, spy_genes])

# Plotting Fittest - Resistance
plt.bar(list(range(0, 15)),
        [0.41031111191729, 0.810704837654553, 0.474840040694015, 0.504913723311206, 0.597685887348422, 0.700203627857123, 0.19680430271345, 0.501056713172492, 0.427299008118781, 0.600031738188556, 1.13744031828526, 0.640319560559956, 0.431370171233806, 0.403174965131434, 0.290316333016446])
plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
plt.title('Expert Rule Weights of Fittest Resistance Gene')
plt.ylabel('Weight')

#Plotting Fittest - Spy
# plt.bar(list(range(0, 25)),
#         [0.489024372889951, 0.510615719894065, 0.771726947747221, 0.222090167727367, 0.495011888873639, 0.417658784557995, 0.334915321750891, 0.517161991732565, 0.300158590014646, 0.584157504635239, 0.152770707589673, 0.248524564627197, 0.544632134112408, 0.532148087453266, 0.677482389993213, 0.48931296791924, 0.749656915089866, 1.09220018078465, 0.522465249683372, 0.484299026192786, 0.276346752429635, 0.704610263859575, 0.147403499928082, 0.290752533323706, 0.43702446482557],
#         color='r')
# plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# plt.title('Expert Rule Weights of Fittest Spy Gene')
# plt.ylabel('Weight')

plt.show()
