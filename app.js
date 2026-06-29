(function () {
  const form = document.getElementById('prediction-form');
  const button = document.getElementById('predict-btn');
  const errorEl = document.getElementById('error');
  const resultEl = document.getElementById('result');

  async function handleSubmit(event) {
    event.preventDefault();
    errorEl.textContent = '';
    resultEl.style.display = 'none';
    resultEl.innerHTML = '';

    const teamA = document.getElementById('teamA').value.trim();
    const teamB = document.getElementById('teamB').value.trim();
    const stage = document.getElementById('stage').value.trim();

    if (!teamA || !teamB) {
      errorEl.textContent = 'Please provide both teams.';
      return;
    }

    button.disabled = true;
    button.textContent = 'Predicting…';

    try {
      const response = await fetch('http://localhost:8080/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ team_a: teamA, team_b: teamB, stage }),
      });

      if (!response.ok) {
        throw new Error('API error: ' + response.status + ' ' + response.statusText);
      }

      const data = await response.json();

      resultEl.innerHTML =
        '<h2>Prediction</h2>' +
        '<ul>' +
        '<li>Team A win probability: ' + (data.team_a_win_prob * 100).toFixed(1) + '%</li>' +
        '<li>Team B win probability: ' + (data.team_b_win_prob * 100).toFixed(1) + '%</li>' +
        '<li>Draw probability: ' + (data.draw_prob * 100).toFixed(1) + '%</li>' +
        '</ul>' +
        '<p>' + (data.explanation || 'No explanation provided.') + '</p>';

      resultEl.style.display = 'block';
    } catch (err) {
      console.error(err);
      errorEl.textContent = err.message || 'Failed to fetch prediction.';
    } finally {
      button.disabled = false;
      button.textContent = 'Predict Match';
    }
  }

  form.addEventListener('submit', handleSubmit);
})();
