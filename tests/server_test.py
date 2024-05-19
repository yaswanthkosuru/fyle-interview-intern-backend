import pytest
from flask import Flask
from core import app



def test_ready_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'status' in response.json
    assert response.json['status'] == 'ready'


def test_error_handling_fyle_error(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert 'error' in response.json
    assert response.json['error'] == 'NotFound'


def test_error_handling_http_exception(client):
    # Send a request that triggers an HTTP exception
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert 'error' in response.json
    assert response.json['error'] == 'NotFound'
