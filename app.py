from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3
import joblib
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'bca_final_project_2026'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FERT_NAMES = {
    "14-35-14": "NPK (Standard)", "28-28": "Urea/DAP Mix",
    "17-17-17": "NPK (Balanced)", "20-20": "Ammonium Phosphate",
    "10-26-26": "Potash Mix", "Urea": "Urea", "DAP": "DAP"
}

# Load Models Safely
try:
    fert_model = joblib.load(os.path.join(BASE_DIR, "fertilizer_model.pkl"))
    soil_enc = joblib.load(os.path.join(BASE_DIR, "soil_encoder.pkl"))
    crop_enc = joblib.load(os.path.join(BASE_DIR, "crop_encoder.pkl"))
    fert_enc = joblib.load(os.path.join(BASE_DIR, "fertilizer_encoder.pkl"))
    market_df = pd.read_csv(os.path.join(BASE_DIR, "clean_market_prices.csv"))
    print("✅ Models and Data Loaded Successfully")
except Exception as e:
    print(f"❌ Error Loading Data: {e}")

def init_db():
    conn = sqlite3.connect('farmers.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html')

@app.route('/auth', methods=['POST'])
def auth():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "msg": "No JSON payload received."})
            
        user = data.get('user', '').strip()
        pwd = data.get('pass', '').strip()
        action = data.get('type')
        
        if not user or not pwd:
            return jsonify({"success": False, "msg": "Username and password cannot be empty!"})
        
        conn = sqlite3.connect('farmers.db')
        cursor = conn.cursor()
        
        if action == 'register':
            try:
                cursor.execute('INSERT INTO users VALUES (?,?)', (user, pwd))
                conn.commit()
                conn.close()
                return jsonify({"success": True, "msg": "Registration Successful! You can now Login."})
            except sqlite3.IntegrityError:
                conn.close()
                return jsonify({"success": False, "msg": "User already exists!"})
        
        # Login Verification
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (user, pwd))
        user_record = cursor.fetchone()
        conn.close()
        
        if user_record:
            session['user'] = user
            return jsonify({"success": True, "redirect": url_for('dashboard')})
        else:
            return jsonify({"success": False, "msg": "Invalid Login! Please Register first."})
    except Exception as e:
        return jsonify({"success": False, "msg": f"Backend Error: {str(e)}"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        temp = float(data.get('temp'))
        rain = float(data.get('rain'))
        soil_raw = data.get('soil').lower().replace(" soil", "").strip()

        if soil_raw == "black":
            crops = ["cotton", "sugarcane", "soyabean"] if rain > 100 else ["maize", "cotton", "millet"]
        elif soil_raw == "clayey":
            crops = ["rice", "paddy", "wheat"] if rain > 120 else ["gram", "lentil", "wheat"]
        elif soil_raw == "sandy":
            crops = ["groundnut", "millet", "maize"]
        elif soil_raw == "red":
            crops = ["ragi", "groundnut", "tobacco"] if rain < 100 else ["rice", "paddy", "maize"]
        else:
            crops = ["maize", "tobacco", "wheat"]

        s_map = soil_enc.transform([soil_raw])[0]
        results = []

        for c in crops:
            try:
                c_map = crop_enc.transform([c.lower()])[0]
                input_vec = [[temp, 65, 45, s_map, c_map, 40, 40, 40]]
                fert_code = str(fert_enc.inverse_transform(fert_model.predict(input_vec))[0])
                
                price = "₹2,500/qt"
                if market_df is not None:
                    p_row = market_df[market_df['crop'].str.lower() == c.lower()]
                    if not p_row.empty: price = f"₹{p_row.iloc[0]['price_per_quintal']}/qt"
                
                results.append({"crop": c.capitalize(), "fert": FERT_NAMES.get(fert_code, fert_code), "price": price})
            except: continue

        return jsonify({"success": True, "results": results})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Switched to port 8000 to resolve local server blocks
    app.run(debug=True, port=8000)