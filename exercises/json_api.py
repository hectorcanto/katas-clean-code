
# https://jsonapi.org/format/
# https://jsonapi.org/recommendations/
# https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module

LAST_VERSION = "0.2.2-alpha.1"
CHANGELOG = """
## [0.2.2] - Unreleased

### Added
- Optional versioning in generic events

### Changed
- Remove relationships from PaymentRequest and Location

### Fix
- Fix event models and factories with Null body
"""

ROUTE = "/users?filter[location]=Vigo&fields[user]=first_name&sort=-age&page[number]=3&page[size]=2&page[limit]=1"
# more pagination: after, before, cursor, limit,


JSON_API_GET = {
    "links": {
        "next": "/users/?page[number]=4",  # NOTE should be the full query part
        "current": "/users/?&page[number]=3",
        "first": "users/?&page[number]=1",
        "last": "users/?&page[number]=10",
    },
    "data": [
        {"type": "user", "id": "5", "attributes": {"first_name": "Manuel"}},
        {"type": "user", "id": "6", "attributes": {"first_name": "Pepe"}},
    ],
    "meta": {
        "total": 2
    }
}

JSON_API_ERROR = {
    "status": "401",
    "code": 215,
    "title": "Bad Authentication data",
    "detail": "Authentication headers are missing",
    "source": {"pointer": "/headers/Authorization"},
    "links": {
        "type": ["https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline"]
    },
    "meta": {"apiVersion": 1.1},
}
