from pandas import read_csv
def transactions_info():
    dataset = read_csv('creditcard.csv')
    transactions = len(dataset)
    notfraud = len(dataset[dataset.Class == 0])
    fraud = len(dataset[dataset.Class == 1])
    percentage = round(fraud / transactions * 100, 2)
    print('total: '+str(transactions)+'\nfraud: '+str(fraud)+'\npercentage fraud: '+str(percentage)+'%')



if __name__ == '__main__':
    transactions_info() #gives stats on the dataset
    import Train_models
    import predict

