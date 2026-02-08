# PyVault 🔒

O **PyVault** é um gerenciador de senhas local desenvolvido em Python. Ele utiliza uma interface gráfica amigável para ajudar você a armazenar e gerenciar suas credenciais de sites e aplicativos de forma organizada e segura em um arquivo JSON.

## ✨ Funcionalidades

- **Armazenamento Seguro:** Salve nome do website, e-mail/usuário e senha.
- **Persistência em JSON:** Seus dados são salvos localmente em um arquivo `data.json`.
- **Busca Rápida:** Digite o nome do site e clique em "Search" para recuperar seus dados.
- **Gerador de Senhas:** Cria senhas aleatórias e complexas com um clique.
- **Auto-Copy:** Ao gerar uma senha, ela é automaticamente copiada para a sua área de transferência (Ctrl+V).
- **Interface Intuitiva:** Desenvolvido com Tkinter para uma experiência de usuário simples.

## 🛠️ Tecnologias Utilizadas
Python: Linguagem principal.

Tkinter: Interface gráfica (GUI).

JSON: Armazenamento e manipulação de dados.

Pyperclip: Interação com a área de transferência do sistema.

## 📝 Notas de Versão
O programa verifica automaticamente se o arquivo data.json existe; caso contrário, ele cria um novo.

Ao adicionar um site que já existe, o programa atualizará os dados daquele cadastro.
