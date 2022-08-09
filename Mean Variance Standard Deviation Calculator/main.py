import numpy as np 

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers." )

    newNpList = np.array(list).reshape(3,3)
    
    mean_row = [newNpList[0, :].mean(), newNpList[1, :].mean(), newNpList[2, :].mean()]
    mean_col = [newNpList[:, 0].mean(), newNpList[:, 1].mean(), newNpList[:, 2].mean()]

    var_row = [newNpList[0, :].var(), newNpList[1, :].var(), newNpList[2, :].var()]
    var_col = [newNpList[:, 0].var(), newNpList[:, 1].var(), newNpList[:, 2].var()]

    std_row = [newNpList[0, :].std(), newNpList[1, :].std(), newNpList[2, :].std()]
    std_col = [newNpList[:, 0].std(), newNpList[:, 1].std(), newNpList[:, 2].std()]
    
    max_row = [newNpList[0, :].max(), newNpList[1, :].max(), newNpList[2, :].max()]
    max_col = [newNpList[:, 0].max(), newNpList[:, 1].max(), newNpList[:, 2].max()]
    
    min_row = [newNpList[0, :].min(), newNpList[1, :].min(), newNpList[2, :].min()]
    min_col = [newNpList[:, 0].min(), newNpList[:, 1].min(), newNpList[:, 2].min()]

    sum_row = [newNpList[0, :].sum(), newNpList[1, :].sum(), newNpList[2, :].sum()]
    sum_col = [newNpList[:, 0].sum(), newNpList[:, 1].sum(), newNpList[:, 2].sum()]


    calculations ={
        "mean": [mean_col, mean_row, newNpList.mean()],
        "variance": [var_col, var_row, newNpList.var()],
        "standard deviation": [std_col, std_row, newNpList.std()],
        "max": [max_col, max_row, newNpList.max()],
        "min": [min_col, min_row, newNpList.min()],
        "sum": [sum_col, sum_col, newNpList.sum()]
    }


    return calculations
    
print(calculate([0,1,2,3,4,5,6,7,8,9]))
