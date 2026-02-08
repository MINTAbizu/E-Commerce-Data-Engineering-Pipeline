from  Extract import  extract
from transform import  transform
from load import load


file_path="../raw_orders.csv"


def  run_etl():
    df= extract(file_path)
    df=transform(df)
    load(df)


if __name__ == " __main__":
    run_etl()
