#!/opt/allot/clearsee/python/bin/python2.7

USERS = {'placeholder': 'placeholder'}


class ResourceWarning(Exception):
    pass


def display():
    print("Dummy function.")


def insert():
    print("Dummy function.")


def work():
    """Starts the mini DB program."""
    if len(USERS) > 5:
        raise ResourceWarning("User DB is full.")

    action = raw_input("a or b? ").lower()
    if action == 'a':
        insert()
    elif action == 'b':
        display()


def main():
    """Starting point."""
    try:
        while True:
            work()
    except KeyboardInterrupt:
        print("Quitting mini DB explorer.")
    except ResourceWarning as err:
        print("{err}")


if __name__ == "__main__":
    main()