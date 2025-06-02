async function cancelarReserva(id) {
  if (!confirm("Tem certeza que deseja cancelar esta reserva?")) {
    return;
  }

  try {
    const resposta = await fetch(`/api/reservas/${id}/cancelar`, {
      method: "POST"
    });

    const resultado = await resposta.json();
    
    if (resposta.ok) {
      alert(resultado.mensagem);
      location.reload();  // Recarrega pra atualizar
    } else {
      alert("❌ Erro: " + resultado.erro);
    }
  } catch (erro) {
    alert("❌ Erro de conexão: " + erro.message);
  }
}
