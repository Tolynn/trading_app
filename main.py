from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='Trading app'
)


@app.get('/')
def hello():
    return 'Hello world'


fake_users = [
    {'id': 1, 'name': 'Bob'},
    {'id': 2, 'name': 'Kate'},
    {'id': 3, 'name': 'Fill'},
    {'id': 4, 'name': 'Tolyn'},
]


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]


@app.post('/users/{user_id}')
def change_name(user_id: int, name: str):
    current_user = list(filter(lambda user: user_id == user.get('id'), fake_users))[0]
    current_user['name'] = name
    return {'status': 200, 'data': current_user}


fake_trades = [
    {'id': 1, 'user_id': 1, 'side': 'sell', 'amount': 100},
    {'id': 2, 'user_id': 1, 'side': 'buy', 'amount': 80},
    {'id': 3, 'user_id': 2, 'side': 'sell', 'amount': 110},
]


class Trade(BaseModel):
    id: int
    user_id: int
    side: str
    amount: int


@app.post('/trades')
def add_trade(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
