const selectedOptions = Array()
document.querySelector(".row").addEventListener('change', e => {
  const selects = document.querySelectorAll('select');

  if(e.target.value !== "---"){
    selectedOptions.push(e.target.value);
  }
  [...selects].forEach(select => {
  console.log(selectedOptions);
    if(e.target.id !== select.id) {
      const options = select.getElementsByTagName('option');
      [...options].forEach((option) => {
        option.disabled = selectedOptions.includes(option.value);
      });
    }
  });
});