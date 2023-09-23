import redis
r = redis.Redis(host='localhost', port=6379)

r.set('Utilisateur', 'IUT-3A')
print(r.get('foo'))