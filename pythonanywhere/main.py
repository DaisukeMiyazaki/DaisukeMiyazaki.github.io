#!/usr/bin/env python
from flask import Flask, redirect, request, url_for, jsonify
from flask_cors import CORS
import logging, io, base64, os, datetime, time
from datetime import datetime
import sqlite3

app = Flask(__name__)
# 本番ドメインとローカル開発環境の両方を許可
CORS(app, resources={r"/api/*": {"origins": ["https://mdaisuke.net", "http://localhost:4000", "http://127.0.0.1:4000"]}})

DB_PATH = 'blog.db'

def init_db():
    """データベースとテーブルの初期化"""
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        # いいねログ用テーブル: どのページが、いついいねされたか
        c.execute('''
            CREATE TABLE IF NOT EXISTS likes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                page_id TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# アプリ起動時にDB初期化（簡易的な方法）
init_db()

@app.route("/signup", methods=['POST', 'GET'])
def signup_page():
    if request.method == 'POST':
        email_param = request.form['email_address']
        signup_page_param = request.form['signup_page']
        url = "https://mdaisuke.net/" + signup_page_param
        if email_param is not None and signup_page_param is not None:
            st = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            # save to file and send thank you note
            with open("email_repo.txt","a") as myfile:
                myfile.write('Timestamp: ' + st + ' email:' + email_param + ' source:' + signup_page_param + '\n')
        if "/en/" in signup_page_param:
            return redirect(url_for('static', filename='thanks_en.html', to_url=url))
    return redirect(url_for('static', filename='thanks.html', to_url=url))

# --- 新しい いいね機能 ---

@app.route("/api/likes", methods=['GET'])
def get_likes():
    """指定されたページのいいね数を取得"""
    page_id = request.args.get('page_id')
    if not page_id:
        return jsonify({'error': 'page_id is required'}), 400
    
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM likes WHERE page_id = ?', (page_id,))
        count = c.fetchone()[0]
    
    return jsonify({'page_id': page_id, 'count': count})

@app.route("/api/likes", methods=['POST'])
def add_like():
    """いいねを追加"""
    # JSONデータとして受け取る想定
    data = request.get_json()
    if not data or 'page_id' not in data:
        return jsonify({'error': 'page_id is required'}), 400
    
    page_id = data['page_id']
    
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO likes (page_id) VALUES (?)', (page_id,))
        conn.commit()
        
        # 最新のカウントを返す
        c.execute('SELECT COUNT(*) FROM likes WHERE page_id = ?', (page_id,))
        count = c.fetchone()[0]
        
    return jsonify({'status': 'success', 'page_id': page_id, 'count': count})
