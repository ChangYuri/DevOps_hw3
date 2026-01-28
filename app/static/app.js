document.addEventListener("DOMContentLoaded", () => {
  const byId = (id) => document.getElementById(id);

  byId("btn-daily").addEventListener("click", async () => {
    const res = await fetch("/daily");
    const data = await res.json();
    byId("daily-result").textContent = JSON.stringify(data, null, 2);
  });

  byId("btn-recommend").addEventListener("click", async () => {
    const raw = byId("ingredients").value.trim();
    const list = raw
      ? raw
          .split(",")
          .map((s) => s.trim())
          .filter(Boolean)
      : [];
    const res = await fetch("/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ingredients: list }),
    });
    const data = await res.json();
    byId("recommend-result").textContent = JSON.stringify(data, null, 2);
  });

  byId("btn-get-recipe").addEventListener("click", async () => {
    const id = byId("recipe-id").value.trim();
    if (!id) return;
    const res = await fetch(`/recipe/${encodeURIComponent(id)}`);
    const data = await (res.status === 404 ? res.json() : res.json());
    byId("recipe-result").textContent =
      `status: ${res.status}\n` + JSON.stringify(data, null, 2);
  });
});
