const selectedOptions = [];
document.querySelector('form').addEventListener('change', e => { //waits for change in the form
  const selects = Array.from(document.querySelectorAll('select')); //grabs all drop downs
  selectedOptions[e.target.id] = e.target.value; //puts the current ranking in a selected list
  [...selects].forEach(select => { //iterates over the 5 drop down menus
    if(e.target.id !== select.id) { // targets the other 4 drop down menus
      const options = Array.from(select.getElementsByTagName('option')); // grabs the options from each drop down
      [...options].forEach((option) => { //iterates over each option in the select field
        if(selectedOptions.includes(option.value) && option.value !== "---"){ //if the select field is the just select option, but not the default "---" hide it
          option.style.display = "none";
        }
        else if(!selectedOptions.includes(option.value)){ //if not, restore it
          option.style.display = "block";
        }
      });
    }
  });
});