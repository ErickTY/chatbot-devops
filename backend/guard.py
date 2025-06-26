from flask import request

AUTHORIZED_TOKENS = {"seutoken123"}

def is_authorized():
    token = request.headers.get("Authorization", "")
    return token in AUTHORIZED_TOKENS
