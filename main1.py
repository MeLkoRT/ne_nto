import db_session
from tables import Temp_hum_sens

def main():
    db_session.global_init("base.sqlite")


if __name__ == '__main__':
    main()
