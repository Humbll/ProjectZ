
from flask import *
from flask import Blueprint, request, redirect, url_for, render_template, jsonify, session
from flask_oauthlib.client import OAuth


oauth = OAuth(app)

riotloginblueprint = Blueprint('riotlogin', __name__, template_folder='templates')

riotapikey = 'RGAPI-6fcd2047-a50f-40ab-a2a1-7c18d2adcad2'
riot_client_id = 'your_riot_client_id'
riot_client_secret = 'your_riot_client_secret'
riot_redirect_uri = 'your_redirect_uri'

riot = oauth.remote_app(
    'riot',
    consumer_key=riot_client_id,
    consumer_secret=riot_client_secret,
    request_token_params={'scope': 'openid'},
    base_url='https://api.riotgames.com/',
    authorize_url='https://example.com/oauth/authorize',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://example.com/oauth/token',
    redirect_uri=riot_redirect_uri,
)


@riotloginblueprint.route('/riotlogin')
def riotlogin():
    return riot.authorize(callback=url_for('riot_authorized', _external=True))


@riotloginblueprint.route('/riot_authorized')
def riot_authorized():
    response = riot.authorized_response()

    if response is None or response.get('access_token') is None:
        flash('Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        ))
        return redirect(url_for('index'))


    session['riot_token'] = (response['access_token'], '')

    user_info = riot.get('me')

    return jsonify(user_info.data)

@riotloginblueprint.route('/logout')
def logout():
    session.pop('riot_token', None)
    return redirect(url_for('index'))
