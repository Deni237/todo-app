const API = "http://localhost:8000";

// Charger les tâches au démarrage
window.onload = loadTasks;

// --------------------
// Ajouter une tâche
// --------------------
async function addTask() {
  const input = document.getElementById("taskInput");
  const title = input.value.trim();

  if (!title) return;

  try {
    await fetch(`${API}/tasks`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title }),
    });

    input.value = "";
    loadTasks();
  } catch (error) {
    console.error("Erreur ajout:", error);
  }
}

// --------------------
// Charger les tâches
// --------------------
async function loadTasks() {
  try {
    const res = await fetch(`${API}/tasks`);
    const data = await res.json();

    const list = document.getElementById("list");
    list.innerHTML = "";

    data.forEach((t) => {
      const li = document.createElement("li");

      const span = document.createElement("span");
      span.textContent = t.title;

      const btn = document.createElement("button");
      btn.textContent = "Supprimer";
      btn.className = "delete-btn";
      btn.onclick = () => deleteTask(t.id);

      li.appendChild(span);
      li.appendChild(btn);

      list.appendChild(li);
    });
  } catch (error) {
    console.error("Erreur chargement:", error);
  }
}

// --------------------
// Supprimer une tâche
// --------------------
async function deleteTask(id) {
  try {
    await fetch(`${API}/tasks/${id}`, {
      method: "DELETE",
    });

    loadTasks();
  } catch (error) {
    console.error("Erreur suppression:", error);
  }
}
