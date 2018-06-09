from flask import url_for


def test_query_count_5(client):
    # Given I have a running app

    # When I ask for the top 5 results for apple
    response = client.get("{}?count={}".format(url_for('query', word="apple"), 5))

    # Then it will return an OK status
    assert response.status_code == 200
    # And the top 5 results
    assert response.json == [
        {'label': 'apply', 'value': 0.9990808963775635},
        {'label': 'example', 'value': 0.9988269805908203},
        {'label': 'single', 'value': 0.998824417591095},
        {'label': 'issued', 'value': 0.998813271522522},
        {'label': 'agriculture', 'value': 0.9988113045692444}
    ]


def test_query_count_2(client):
    # Given I have a running app

    # When I ask for the top 2 results for apple
    response = client.get("{}?count={}".format(url_for('query', word="apple"), 2))

    # Then it will return an OK status
    assert response.status_code == 200
    # And the top 2 results
    assert response.json == [
        {'label': 'apply', 'value': 0.9990808963775635},
        {'label': 'example', 'value': 0.9988269805908203}
    ]
