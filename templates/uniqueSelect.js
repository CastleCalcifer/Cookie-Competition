const selectedOptions = Array(3).fill('');
document.querySelector(".rankDropdown").addEventListener('change', e => {
  const selects = document.querySelectorAll('select');
  selectedOptions[e.target.id] = e.target.value;
  [...selects].forEach(select => {
    if(e.target.id !== select.id) {
      const options = select.getElementsByClassName('ranking');
      [...options].forEach((option) => {
        option.disabled = selectedOptions.includes(option.value);
      });
    }
  });
});