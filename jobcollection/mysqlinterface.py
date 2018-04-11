#-*- coding: UTF-8 -*-
import MySQLdb
import usersetting


class SqlInterface(object):
    def __init__(self):
        self._host = usersetting.HOST if "HOST" in dir(usersetting) else "localhost"
        self._user = usersetting.USER if "USER" in dir(usersetting) else "root"
        self._port = usersetting.PORT if "PORT" in dir(usersetting) else 3306
        try:
            self._password = usersetting.PASSWD
            self._init_db = usersetting.DATABASE
        except Exception:
            raise ValueError("PASSWD or database is not set, please set it in usersetting.py")
        self._cursor = None
        self._db = None

    def __enter__(self):
        self.connect()
        return self.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        self._db = MySQLdb.connect(host=self._host, user=self._user, passwd=self._password,
                                   db=self._init_db, port=self._port, charset='utf8')
        if self._db:
            self._cursor = self._db.cursor()
            return self._db
        else:
            return None

    def cursor(self):
        return self._cursor

    def close(self):
        if self._db:
            self._db.close()

    @property
    def initial_db(self):
        return self._init_db

    @property
    def initial_port(self):
        return self._port

    @property
    def initial_host(self):
        return self._local_host

    @property
    def initial_user(self):
        return self._user

    @property
    def current_database(self):
        if self._cursor:
            self._cursor.execute("""select database()""")
            temp_result = self._cursor.fetchone()
            if len(temp_result) > 0:
                return temp_result[0]
            else:
                return None