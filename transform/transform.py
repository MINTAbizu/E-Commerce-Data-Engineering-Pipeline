def  transform_data(df):
    print("Transformation data")







    #  clean  column names
    df.columns= df.columns.str.lower()

    #  create  total amount
    df['total_amount'] = df['quantity'] * df['unit_price']

    # remove  rows  with invalid  price

    df = df[df['price'] > 0]


    return df
    # str.replace(' ', '_')


    


