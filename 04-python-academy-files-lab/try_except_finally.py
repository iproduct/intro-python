import sys
from io import UnsupportedOperation

if __name__ == '__main__':
    FILENAME = "demofile.txt"
    try:
        f = open(FILENAME, "rt")
        try:
            f.write("Lorum Ipsum" + 12)
        except UnsupportedOperation as ex:
            print("The file is not open for writing")
            print(f"Error: {ex}, {type(ex)=}")
            # raise ex
        except Exception as ex:
            print("Something went wrong when writing to the file:", ex)
            raise ex
        else:
            print("Data wtritten to file successfully.")
        finally:
            print("Closing file:", FILENAME)
            f.close()
    except:
        print("Something went wrong with the file")
        # raise ex

    print("More work to do ...")