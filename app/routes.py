from flask import Blueprint, request, jsonify, render_template
from .utils import get_portfolio_metrics

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/portfolio-metrics', methods=['POST'])
def portfolio_metrics():
    data = request.get_json()
    tickers = data.get('tickers', [])
    weights = data.get('weights', [])

    if not tickers or not weights or len(tickers) != len(weights):
        return jsonify({"error": "Tickers and weights must be the same length"}), 400
    
    metrics = get_portfolio_metrics(tickers, weights)
    return jsonify(metrics)

