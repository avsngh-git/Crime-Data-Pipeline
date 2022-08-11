import nasdaqdatalink

if __name__ == "__main__":
    data = nasdaqdatalink.get_table("WB/DATA", paginate=True)
    print(data)