document.getElementById('btnAlugar').addEventListener('click', async (e) => {
  e.preventDefault(); 

  const cpf = document.getElementById('cpf').value.trim();
  const cpfNumerico = cpf.replace(/\D/g, ''); // Remove caracteres não numéricos

  if (cpfNumerico.length !== 11) {
    alert('CPF inválido. Insira os 11 dígitos corretamente.');
    return;
  }

  // Pegando o número do quarto do botão
  const numeroQuarto = document.getElementById('btnAlugar').getAttribute('data-quarto');

  try {
    const response = await fetch(`/api/verificar-cpf/${cpfNumerico}`);
    const resultado = await response.json();

    if (resultado.existe) {
      // Redireciona para a reserva do quarto certo
      window.location.href = `/alugar?quarto=${encodeURIComponent(numeroQuarto)}&cpf=${encodeURIComponent(cpfNumerico)}`;
    } else {
      alert('CPF não encontrado. Redirecionando para cadastro...');
      window.location.href = '/cadastro';
    }
  } catch (err) {
    console.error('Erro ao verificar CPF:', err);
  }
});
