# high-stakes-bot-plugins

Documentação para desenvolvimento de um novo plugin:  
https://errbot.readthedocs.io/en/latest/user_guide/plugin_development/basics.html

--------------------------------

Para testar local utilizando docker:  
> docker build -t errbot .  
> docker run -it -v $(pwd):/errbot/plugins errbot

--------------------------------

Para atualizar o bot após merge/commit, enviar para o bot:
> atualizar  
> restart