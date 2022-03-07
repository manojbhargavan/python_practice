import pandas as pd

sales_df = pd.read_csv('SalesData.csv')
print(sales_df)
print('loaded')

file_type_analysis: dict = {}
average_user_price: dict = {}

for order in sales_df.iterrows():
    file_type = order[1]['File_Type']
    SKU_number = order[1]['SKU_number']
    ItemCount = order[1]['ItemCount']
    LowNetPrice = order[1]['LowNetPrice']

    if file_type in file_type_analysis:
        file_type_analysis[file_type] += 1
    else:
        file_type_analysis[file_type] = 1

    if ItemCount != 0:
        if SKU_number in average_user_price:
            average_user_price[SKU_number] = (average_user_price[SKU_number] + (LowNetPrice / ItemCount)) / 2
        else:
            average_user_price[SKU_number] = LowNetPrice / ItemCount


print(average_user_price)
print(file_type_analysis)
