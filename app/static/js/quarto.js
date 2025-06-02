document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(form); 

    try {
      const resposta = await fetch("/api/quartos", {
        method: "POST",
        body: formData
      });

      const resultado = await resposta.json();

      if (resposta.ok) {
        // Mensagem na tela
        const mensagemDiv = document.getElementById("mensagem");
        mensagemDiv.innerText = `✅ Quarto ${resultado.numero} cadastrado com sucesso!`;
        mensagemDiv.style.color = "green";

        form.reset(); 

        
      } else {
        alert("❌ Erro: " + resultado.erro);
      }
    } catch (erro) {
      alert("❌ Erro na requisição: " + erro.message);
    }
  });
});
