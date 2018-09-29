from flask import url_for


def test_query_count_5(client):
    # Given I have a running app

    # When I ask for the top 5 results for apple
    response = client.get("{}?count={}".format(url_for('query', model_name="moscow_times_1200_fasttext", word="apple"), 5))

    # Then it will return an OK status
    assert response.status_code == 200
    # And the top 5 results

    assert response.json == [{"label": "family", "value": 0.9689775705337524},
                             {"label": "divide", "value": 0.9656867980957031},
                             {"label": "applicable", "value": 0.9607474207878113},
                             {"label": "downturn", "value": 0.9604483842849731},
                             {"label": "revert", "value": 0.9601423144340515}]


def test_query_count_2(client):
    # Given I have a running app

    # When I ask for the top 2 results for apple
    response = client.get("{}?count={}".format(url_for('query', model_name="moscow_times_1200_fasttext", word="apple"), 2))

    # Then it will return an OK status
    assert response.status_code == 200
    # And the top 2 results
    assert response.json == [{"label": "family", "value": 0.9689775705337524},
                             {"label": "divide", "value": 0.9656867980957031}]


def test_query_another_model(client):
    # Given I have a running app

    # When I ask for the top 5 results for apple
    response = client.get("{}?count={}".format(url_for('query', model_name="moscow_times_1200_word2vec", word="apple"), 5))

    # Then it will return an OK status
    assert response.status_code == 200
    # And the top 5 results

    assert response.json == [{
        "label": "swedish",
        "value": 0.7846378087997437
    }, {
        "label": "furniture",
        "value": 0.7715908288955688
    }, {
        "label": "frank",
        "value": 0.771047830581665
    }, {
        "label": "mercedes",
        "value": 0.7708911299705505
    }, {
        "label": "auctions",
        "value": 0.7658798694610596
    }]
