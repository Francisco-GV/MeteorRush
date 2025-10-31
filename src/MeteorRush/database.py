import pyodbc

from MeteorRush import settings


class Database:
    def __init__(self):
        self.server = settings.DB_SERVER
        self.database = settings.DB_DATABASE
        self.user = settings.DB_USER
        self.password = settings.DB_PASSWORD
        self.cnxn = None
        self.cursor = None

    def __enter__(self):
        self.cnxn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.server};"
            f"UID={self.user};"
            f"PWD={self.password};"
            f"DATABASE={self.database};"
            f"TrustServerCertificate=yes;"
        )
        self.cursor = self.cnxn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cnxn:
            self.cnxn.close()

    def upload_player_data(
        self, player_name, score, duration, destroyed_asteroid_counts
    ):
        self.cursor.execute(
            (
                "INSERT INTO player ("
                "name,"
                "score,"
                "duration,"
                "tiny_asteroids_destroyed,"
                "small_asteroids_destroyed,"
                "medium_asteroids_destroyed,"
                "large_asteroids_destroyed"
                ") VALUES (?, ?, ?, ?, ?, ?, ?)"
            ),
            player_name,
            score,
            duration,
            destroyed_asteroid_counts["tiny"],
            destroyed_asteroid_counts["small"],
            destroyed_asteroid_counts["medium"],
            destroyed_asteroid_counts["large"],
        )
        self.cnxn.commit()
