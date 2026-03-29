# サロンレビュー返信ジェネレーター

ホットペッパービューティーの口コミを自動取得し、Claude AIで返信文を生成するツールです。

## 機能
- ホットペッパービューティーから口コミを自動取得
- Claude APIで自然な返信文を自動生成
- React UIで簡単操作
- 複数ページ対応

## 技術スタック
- Python / Selenium
- Anthropic Claude API
- Flask
- React

## 使い方

### 1. バックエンド起動
```bash
pip install -r requirements.txt
python api.py
```

### 2. フロントエンド起動
```bash
cd salon-review-ui
npm install
npm start
```

### 3. ブラウザで操作
`http://localhost:3000` を開いてホットペッパーのURLを入力して「取得する」を押す。
