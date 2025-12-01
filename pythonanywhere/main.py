#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

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

# アプリ起動時にDB初期化
init_db()

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
