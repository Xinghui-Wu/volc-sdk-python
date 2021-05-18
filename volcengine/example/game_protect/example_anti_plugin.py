
from volcengine.game_protect.GameProtectService import GameProtectService

if __name__ == '__main__':
    gameProtector = GameProtectService()

    # call below method if you dont set ak and sk in $HOME/.volc/config
    gameProtector.set_ak('AKLTMWRiNDFiYWVmZjkyNGI1ZmE3YmIxNTQxOTdjODU1ZTE')
    gameProtector.set_sk('TUdFeU0ySmtZek0zWWpZek5EYzJNVGxrWlRkbU56TmhaV1JoTjJFeU1EQQ==')

    params = {
        'AppId': 218745,
        'StartTime': 1618502400,
        'EndTime': 1618545491,
        'PageSize': 10,
        'PageNum': 1
    }
    req = dict()

    resp = gameProtector.risk_result(params, req)
    print resp