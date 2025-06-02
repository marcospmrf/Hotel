document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = {
      nome: form.nome.value,
      email: form.email.value,
      telefone: form.telefone.value,
      cpf: form.cpf.value,
      numero_quarto: form.numero_quarto.value,
      checkin: form.checkin.value,
      checkout: form.checkout.value,
      pagamento: form.pagamento.value
    };

    try {
      const resposta = await fetch("/api/reservas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
      });

      const resultado = await resposta.json();
      const mensagem = document.getElementById("mensagem");

      if (resposta.ok) {
        mensagem.innerText = `✅ Reserva realizada para o quarto ${resultado.quarto} | Valor: R$ ${resultado.valor}`;
        mensagem.style.color = "green";
        form.reset();
      } else {
        mensagem.innerText = "❌ Erro: " + resultado.erro;
        mensagem.style.color = "red";
      }
    } catch (erro) {
      alert("❌ Erro de conexão: " + erro.message);
    }
  });
});

