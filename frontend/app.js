fetch("http://127.0.0.1:8000/auth/register", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(data)
})
.then(async response => {
  const resData = await response.json().catch(() => ({})); // por si no hay JSON
  if (!response.ok) {
    throw new Error(resData.detail || JSON.stringify(resData));
  }
  return resData;
})
.then(data => {
  alert("✅ Usuario registrado con éxito!");
  console.log("Respuesta del servidor:", data);
})
.catch(error => {
  alert("❌ Error al registrar: " + error.message);
  console.error("Detalles del error:", error);
});
