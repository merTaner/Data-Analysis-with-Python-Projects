import numpy as np 

list = [0,1,2,3,4,5,6,7,8]
npList = np.array(list).reshape(3,3)
print(npList)

mean_row = [npList[0, :].mean(), npList[1, :].mean(), npList[2, :].mean()]
mean_col = [npList[:, 0].mean(), npList[:, 1].mean(), npList[:, 2].mean()]

var_row = [npList[0, :].var(), npList[1, :].var(), npList[2, :].var()]
var_col = [npList[:, 0].var(), npList[:, 1].var(), npList[:, 2].var()]

std_row = [npList[0, :].std(), npList[1, :].std(), npList[2, :].std()]
std_col = [npList[:, 0].std(), npList[:, 1].std(), npList[:, 2].std()]


print(var_col)
print(std_col)


"""
mean_row2 = []
for i in range(npList.shape[0]):
    i = npList[i, :].mean()
    mean_row2.append(i)

print(mean_row2)

"""