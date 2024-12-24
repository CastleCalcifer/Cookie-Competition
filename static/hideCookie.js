const options = Array.from(document.querySelectorAll('option'));
bakerCookie = document.getElementById("bakerCookie").textContent;
console.log(bakerCookie);
[...options].forEach(option => {
    console.log(option.value);
      if (option.value == bakerCookie){
        option.style.display = "none"
      }}
    );