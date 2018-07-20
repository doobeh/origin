# Origin

A starter project that doesn't really do all too much.

- It doesn't save the world.
- It doesn't morally correct the corrupt.
- It doesn't provide donuts.

However, if *you* want to build an app to deliver donuts while saving the
world, Origin should help you get up and running a little quicker--
meaning you can spend more time adding the special sauce that makes your
project stand out and less time juggling boilerplate code.

Only thing that's required is creating an `instance` folder alongside
the tests folder, that has your `settings.cfg` and optionally
`test_settings.cfg`.  Here's what I use as a starting point:

#### settings.cfg:

```
SECRET_KEY='ABCDEFG'
SQLALCHEMY_DATABASE_URI='postgresql://localhost/project'
SQLALCHEMY_TRACK_NOTIFICATIONS=False
SECURITY_PASSWORD_SALT='hash_browns'
SITE_TITLE = 'EXAMPLE'

```

#### test_settings.cfg

````
SQLALCHEMY_DATABASE_URI='postgresql://localhost/test_project'
````