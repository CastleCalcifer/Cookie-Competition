function reset() {
    const selects = document.querySelectorAll('select');
    [...selects].forEach(select => {
        select.selectedIndex = 0;
        const options = select.getElementsByTagName('option');
        [...options].forEach((option) => {
            option.style.display = "block";
        });
    });
}