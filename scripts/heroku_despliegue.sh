git init
heroku git:remote -a heroku-prueba-servidor
git add .
git commit -am "Despliegue a Heroku"
git push heroku master