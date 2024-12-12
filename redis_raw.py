import redis

# key-value

redis_conn = redis.Redis()  # default: localhost, 6379, db=0
redis_conn.set("hello", "world5")

value = redis_conn.get("hello").decode("utf-8")
print(value)

redis_conn.delete("hello")

# hash

redis_conn.hset("my-hash", "name", "john")
redis_conn.hset("my-hash", "age", "30")
redis_conn.hset("my-hash", "city", "sao paulo")


value = redis_conn.hget("my-hash", "name").decode("utf-8")
print(value)

redis_conn.hdel("my-hash", "city")

# search if exists

response = redis_conn.exists("hello")
print("exists(hello)", response)

response = redis_conn.hexists("my-hash", "name")
print("hexists(my-hash, name)", response)

redis_conn.set("hello_30", "12s", 30)
redis_conn.expire("my-hash", 30)
