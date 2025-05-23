document.getElementById('btnAlugar').addEventListener('click', async (e) => {
  e.preventDefault(); 

  const cpf = document.getElementById('cpf').value.trim();
  const cpfNumerico = cpf.replace(/\D/g, ''); 

  if (cpfNumerico.length !== 11) {
    alert('CPF inválido. Insira os 11 dígitos corretamente.');
    return;
  }

  try {
    const response = await fetch(`/api/verificar-cpf/${cpfNumerico}`);
    const resultado = await response.json();

    if (resultado.existe) {
      window.location.href = '/alugar?quarto=101&cpf=' + encodeURIComponent(cpfNumerico);
    } else {
      alert('CPF não encontrado. Redirecionando para cadastro...');
      window.location.href = '/cadastro';
    }
  } catch (err) {
    console.error('Erro ao verificar CPF:', err);
  }
});
