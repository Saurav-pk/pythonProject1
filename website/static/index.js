function deleteNote(noteId) {
  console.log("Deleting note with ID:", noteId);
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}