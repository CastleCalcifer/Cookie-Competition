const selectedOptions = [];
document.querySelector('form').addEventListener('change', e => { //waits for change in the form
  const selects = document.querySelectorAll('select'); //grabs all drop downs
  selectedOptions[e.target.id] = e.target.value; //puts the current ranking in a selected list
  [...selects].forEach(select => { //iterates over the 5 drop down menus
    if(e.target.id !== select.id) { // targets the other 4 drop down menus
      const options = select.getElementsByTagName('option'); // grabs the options from each drop down
      [...options].forEach((option) => { //iterates over each option
        if(selectedOptions.includes(option.value)){ //if the currently
          option.style.display = "none";
        }
        else if(!selectedOptions.includes(option.value)){
          option.style.display = "block"
          for(var i = 0; i < selectedOptions.length; i++){
            if(selectedOptions[i] === option.value){
              selectedOptions.splice(i, 1);
            }
          }
          console.log(selectedOptions);
        }
      });
    }
  });
});