# Ubuntu上安裝Heroku_CLI
sudo snap install heroku --classic

# requirements.txt 是要叫Heroku透過pip install 安裝的套件名稱
flask
gunicorn
line-bot-sdk

# runtime.txt 是要運行的環境
python-3.7.8

# Procfile 是告訴 Heroku 我的程式該怎麼跑起來 
web: gunicorn linechatbot:app

# 登入heroku
heroku login

# 在project目錄下執行, 我這邊是以 terry-chatbot 命名, 跟我在Heroku建立的Application是一樣的名字
git init
heroku git:remote -a terry-chatbot
git add -A
git status
git rm --cached .vscode/settings.json
git commit -am "terry-chatbot v2"
git push heroku master

# 看目前機器狀況
heroku ps

# 遠端關機
heroku ps:scale web=0

# 遠端開機
heroku ps:scale web=1

# 在Chrome開啟網址連結
heroku open

# 查看後台即時log
heroku logs --tail
> Press Control+C to stop streaming the logs.