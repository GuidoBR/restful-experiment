# restful-experiment
Restful API for user registration and login. Python, DRF, JWT.

https://restful-experiment.herokuapp.com/

## Getting Started

### Getting a token (Username: concrete, password: solutions)

#### Request
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"concrete","password":"solutions"}' http://restful-experiment.herokuapp.com/api-token-auth/
```
#### Response

```
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IiIsInVzZXJuYW1lIjoiY29uY3JldGUiLCJ1c2VyX2lkIjoyLCJleHAiOjE0NzU4OTE4OTh9.HcqA0TB7yEaMv1oeTtwvRuoSq5jAPjM3ycmntuxlr9Q"}
```

## Contributing

## Installing

```
$ git clone git@github.com:GuidoBR/restful-experiment.git
$ virtualenv venv && source venv/bin/activate
$ pip install -r requirements.txt
```

To run locally, use django command:

```
$ python manage.py runserver
```

### Tests

Run the project's tests.

```
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
