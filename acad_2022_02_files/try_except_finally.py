from io import UnsupportedOperation

if __name__ == '__main__':
    FILENAME = "temp.txt"
    try:
        f = open(FILENAME, "wt")
        try:
            f.write("Lorum Ipsum" + '12')
        except UnsupportedOperation as ex:
            print("The file is not open for writing")
            print(f"Error: {ex}, {type(ex)}")
            raise
        except Exception as ex:
            print("Something went wrong when writing to file:", ex, type(ex))
            raise
        else:
            print("Data written to file successfully.")
        finally:
            print("Closing file:", FILENAME)
            f.close()
    except FileNotFoundError:
        print("File not found:", FILENAME)
    except Exception as ex:
        print("Error writing to file:", FILENAME,"-", ex, type(ex))

    print("More work to do ...")