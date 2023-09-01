function openModal() {
    document.getElementById("registration-modal").style.display = "block";
  }

  function closeModal() {
    document.getElementById("registration-modal").style.display = "none";
  }
  
  document.getElementById("create-account").addEventListener("click", openModal);
  
  document.getElementById("close-modal").addEventListener("click", closeModal);

 