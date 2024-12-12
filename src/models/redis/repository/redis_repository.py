from redis import Redis


class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conns

    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value)

    def get_key(self, key: str) -> str:
        value = self.__redis_conn.get(key)
        if value:
            return value.decode("utf-8")
        return None

    def insert_hash(self, key: str, field: str, value; any) -> None:
        self.__redis_conn.hset(key, field, value)

    def get_hash(self, key: str, field: str) -> any:
        value = self.__redis_conn.hget(key, field)
        if value:
            return value.decode("utf-8")
        return None

    def insert(self, key: str, value: any, seconds_ttl: int) -> None:
        self.__redis_conn.set(key, value, seconds_ttl)

    def insert_hash(self, key: str, field: str, value: any, seconds_ttl: int) -> None:
        self.__redis_conn.hset(key, field, value, seconds_ttl)