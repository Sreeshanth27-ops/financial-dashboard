document.getElementById('portfolioForm').addEventListener('submit', async function (e) {
    e. preventDefault();

    const tickers = document.getElementById('tickers').value.split(',').map(t => t.trim());
    const weights = document.getElementById('weights').value.split(',').map(w => parseFloat(w.trim()));

    const response = await fetch('/portfolio-metrics', {
        method: 'POST';
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({tickers, weights})
    });

    const result = await response.json();
    document.getElementById('result').textContent =JSON.stringify(result, null, 2);
});