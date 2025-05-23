document.getElementById('formCadastro').addEventListener('submit', async function (e) {
    e.preventDefault();
  
    const formData = new FormData(this);
    const data = {
      nome: formData.get('nome'),
      cpf: formData.get('cpf'),
      rg: formData.get('rg'),
      telefone: formData.get('telefone'),
      email: formData.get('email'),
      nascimento: formData.get('nascimento'),
    };
  
    try {
      const resposta = await fetch('/api/cadastro/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
  
      const resultado = await resposta.json();
  
      const mensagemEl = document.createElement('div');
      mensagemEl.classList.add('mensagem');
      mensagemEl.classList.add(resultado.status === 'sucesso' ? 'sucesso' : 'erro');
      mensagemEl.innerText = resultado.mensagem;
  
      const container = document.querySelector('.container');
      const form = document.getElementById('formCadastro');
  
      const antigas = document.querySelectorAll('.mensagem');
      antigas.forEach(m => m.remove());
  
      container.insertBefore(mensagemEl, form);
  
      if (resultado.status === 'sucesso') {
        form.reset();
      }
  
    } catch (error) {
      console.error('Erro ao enviar requisição:', error);
    }
  });
  