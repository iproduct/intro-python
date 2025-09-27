# genlog.py
#
# Sum up the bytes transferred in an Apache server log using
# generator expressions
from decorators.profile_decorator import profile


@profile
def get_total():
    with open("access-log") as wwwlog:
        bytecolumn = (line.rsplit(None, 1)[1] for line in wwwlog)
        bytes_sent = (int(x) for x in bytecolumn if x != '-')
        return sum(bytes_sent)


@profile
def get_total_iter():
    with open("access-log") as wwwlog:
        total = 0
        for line in wwwlog:
            bytes_sent = line.rsplit(None, 1)[1]
            if bytes_sent != '-':
                total += int(bytes_sent)
        return total


if __name__ == "__main__":
    print("Total", get_total())
    print("Total", get_total_iter())
