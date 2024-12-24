
const cookieImages = new Map();
cookieImages.set("---", "https://www.jocooks.com/wp-content/uploads/2021/12/sugar-cookies-1-17.jpg")
cookieImages.set("Chocolate Grocery Store", "https://assets.bonappetit.com/photos/5ca534485e96521ff23b382b/1:1/w_2560%2Cc_limit/chocolate-chip-cookie.jpg")
cookieImages.set("Gingerbread Royal Cream", "https://www.thepkpway.com/wp-content/uploads/2017/12/gingerbread-cookies-3f.jpg")
cookieImages.set("Tiramisu Cookie", "https://thelittlevintagebakingcompany.com/wp-content/uploads/2023/03/Sprinkle-Sugar-Cookies-15.jpg")
cookieImages.set("Italian Ricotta", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh4k251xFF_9ijySYa4PoRBwdRDOixcZmkhw&s")
document.querySelector('form').addEventListener('change', e =>{
        selectedDivID = e.target.parentElement.id;
        console.log(document.getElementById("awardDropdown" + selectedDivID).value)
        document.getElementById("awardImage" + selectedDivID).src = cookieImages.get(document.getElementById("awardDropdown" + selectedDivID).value)
});