ip_blacklist = ["192.168.1.1", "10.0.0.5", "192.168.1.1"]

clr_ip_blacklist = set(ip_blacklist)

print(clr_ip_blacklist)

admins = ["mohamed", "hossam", "ziad", "ahmad"]

def attack_log_simulator():

    ip_counter = 1

    while True:
        yield f"192.0.2.14.{ip_counter}"

        ip_counter += 1

def check_clearance(func):

    def check(*args, **kwargs):
        x = input("enter the admin")

        if x in admins:

            print("log succece")

            func(*args, **kwargs)

        else:
            print("wong admin")

    return check

@check_clearance
def log_port():

    print("welcome to the community")

    g = attack_log_simulator()

    with open("cyber_report.txt", "w") as my_file:

        ips_arrangment = [next(g), next(g), next(g), next(g), next(g)]

        for count, ip in enumerate(ips_arrangment, start=1):

            my_file.write(f"line {count}: arrengment detect from ip {ip}\n")


log_port()
