document.getElementById('matchBtn').addEventListener('click', async () => {
  const groupesText = document.getElementById('groupes').value;
  const tablesText = document.getElementById('tables').value;

  let groupes, tables;
  try {
    groupes = JSON.parse(groupesText);
    tables = JSON.parse(tablesText);
  } catch (e) {
    document.getElementById('result').textContent = 'JSON invalide: ' + e.message;
    return;
  }

  const payload = { groupes, tables };

  try {
    const resp = await fetch('/match', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const json = await resp.json();
    document.getElementById('result').textContent = JSON.stringify(json, null, 2);
  } catch (err) {
    document.getElementById('result').textContent = 'Erreur requête: ' + err.message;
  }
});