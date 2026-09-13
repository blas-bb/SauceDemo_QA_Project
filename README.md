# SauceDemo QA Automation projekat

Kompletan početnički Selenium + pytest projekat sa Page Object Model strukturom.

## Šta sadrži

- 5 login testova (3 prolaze, 2 namerno padaju)
- 5 testova korpe
- 5 checkout testova
- automatski screenshot svakog palog testa
- screenshot ugrađen direktno u HTML report
- automatsko pravljenje `reports/report.html`

Očekivani konačni rezultat je: **13 passed, 2 failed**. Dva testa su namerno
napisana sa pogrešnim očekivanim porukama kako bi se videli FAIL, screenshot i
detalji greške u HTML reportu.

## Prvo pokretanje u VS Code-u (Windows PowerShell)

Otvori ovaj folder u VS Code-u, pa u terminal upiši redom:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Chrome će se automatski otvoriti za svaki test. Kada se izvršavanje završi,
otvori `reports/report.html`. Screenshotovi palih testova nalaze se i u
`screenshots` folderu.

Za brže pokretanje bez prikazivanja Chrome prozora upiši:

```powershell
pytest --headless
```

Za pokretanje samo jedne grupe:

```powershell
pytest tests/test_login.py
pytest tests/test_cart.py
pytest tests/test_checkout.py
```
Git practice
Testing Git branch